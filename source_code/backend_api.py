"""
BACKEND API - FRAMEWORK DSB
==========================
API Backend simplificada com funções Flask para comunicação frontend ↔ backend
Versão refatorada: Classes → Funções simples para melhor performance e manutenibilidade
"""

# =============================================================================
# IMPORTS E DEPENDÊNCIAS
# =============================================================================

from flask import Flask, request, jsonify, send_from_directory, send_from_directory, send_from_directory
import logging
import sys
import os
from datetime import datetime, date
from decimal import Decimal
import bcrypt
import sqlite3
import data_manager
from data_manager import consultar_bd, get_view, inserir_dados, atualizar_dados, atualizar_dados_lote, excluir_dados
from debugger import flow_marker, error_catcher

# Importa debugger personalizado
from debugger import flow_marker, error_catcher, unexpected_error_catcher, _inicializar_log

# =============================================================================
# CONVERSÃO DE TIPOS PARA JSON (PostgreSQL)
# =============================================================================

def converter_tipos_postgresql(obj):
    """
    Converte tipos específicos do PostgreSQL para tipos compatíveis com JSON
    
    - Decimal → float (valores monetários)
    - date/datetime → string ISO YYYY-MM-DD (para <input type="date">)
    
    IMPORTANTE: Campos HTML5 <input type="date"> esperam formato ISO.
    O navegador exibe automaticamente no formato local do usuário (dd/mm/yyyy no Brasil).
    """
    if isinstance(obj, Decimal):
        return float(obj)  # Decimal('3125.50') → 3125.5
    if isinstance(obj, (date, datetime)):
        # Retorna formato ISO para compatibilidade com <input type="date">
        return obj.isoformat()  # datetime.date(2025, 10, 30) → "2025-10-30"
    if isinstance(obj, dict):
        return {k: converter_tipos_postgresql(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [converter_tipos_postgresql(item) for item in obj]
    return obj

# =============================================================================
# VALIDAÇÃO CENTRALIZADA DE PARÂMETROS
# =============================================================================

def validar_database_config(database_path, database_name):
    """
    Valida configurações de banco de dados de forma centralizada
    
    ⚠️ IMPORTANTE: Para PostgreSQL, database_path é string vazia ("")
    PostgreSQL não usa path de arquivo - conexão configurada no backend (db_config.py)
    
    @param database_path: Path do banco (pode ser string vazia para PostgreSQL)
    @param database_name: Nome do banco
    @raises ValueError: Se algum parâmetro for None (não configurado)
    
    Exemplos:
        # SQLite - precisa de path
        validar_database_config("c:\\apps\\data", "financas.db")
        
        # PostgreSQL - path vazio
        validar_database_config("", "financas")
    """
    # Aceita string vazia, apenas rejeita None (não configurado)
    if database_path is None:
        raise ValueError("Parâmetro 'database_path' é obrigatório")
    
    if not database_name:
        raise ValueError("Parâmetro 'database_name' é obrigatório")

# =============================================================================
# FUNÇÃO PARA CONFIGURAR ENDPOINTS EM QUALQUER INSTÂNCIA FLASK
# =============================================================================

def configurar_endpoints(app):
    """
    Configura todos os endpoints da API em uma instância Flask fornecida
    
    @param {Flask} app - Instância Flask onde os endpoints serão registrados
    """
    
    # Configuração de logging
    logger = logging.getLogger(__name__)
    
    @app.route('/')
    def index():
        """
        Serve o arquivo index.html na rota raiz
        """
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.route('/framework_dsb/<path:filename>')
    def serve_framework(filename):
        """
        Serve arquivos do framework DSB
        """
        # Caminho absoluto para a pasta framework_dsb
        framework_base = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        return send_from_directory(framework_base, filename)
    
    @app.route('/health', methods=['GET'])
    def health_check():
        """
        Endpoint de health check - verifica se API está funcionando
        
        @return {dict} - Status da API e informações básicas
        """
        return jsonify({
            "status": "ok", 
            "app": "Framework DSB API",
            "message": "API Backend funcionando",
            "timestamp": datetime.now().isoformat()
        })
    
    @app.route('/api/login', methods=['POST'])
    def login():
        """
        Endpoint de autenticação de usuários
        Redireciona para data_manager.autoriza_login()
        """
        try:
            data = request.json
            username = data.get('username', '').strip()
            password = data.get('password', '')
            
            if not username or not password:
                return jsonify({'success': False, 'message': 'Usuário e senha são obrigatórios'}), 400
            
            path_name = _processar_db_path_name(data)
            
            resultado = data_manager.autoriza_login(
                username=username,
                password=password,
                database_path=path_name.get('database_path'),
                database_name=path_name.get('database_name')
            )
            
            if resultado['sucesso']:
                return jsonify({'success': True, 'message': resultado['message']}), 200
            else:
                return jsonify({'success': False, 'message': resultado['message']}), 401
                
        except Exception as e:
            error_catcher("Erro no endpoint /api/login", e)
            return jsonify({'success': False, 'message': 'Erro interno no servidor'}), 500
    
    # =========================================================================
    # 💾 SISTEMA DE BACKUP AUTOMÁTICO
    # =========================================================================
    # 
    # 📍 IMPLEMENTAÇÃO ATUAL:
    # - Backup salvo no PythonAnywhere: /home/davidbit/backups/
    # - Mantém 4 últimas cópias
    # - Chamado automaticamente por cron-job.org (grátis)
    # 
    # 🔄 FUTURA IMPLEMENTAÇÃO - GOOGLE DRIVE (quando necessário):
    # 
    # MUDANÇAS NECESSÁRIAS:
    # 
    # 1. Instalar dependências no requirements.txt:
    #    google-auth
    #    google-auth-oauthlib
    #    google-auth-httplib2
    #    google-api-python-client
    # 
    # 2. Criar endpoint adicional para enviar ao Google Drive:
    #    @app.route('/api/backup/sync-to-drive', methods=['POST'])
    #    def sincronizar_drive():
    #        # Autentica com Google Drive API
    #        # Upload do último backup para Drive
    #        # Mantém 4 últimas cópias no Drive também
    # 
    # 3. Ou modificar este endpoint para fazer backup duplo:
    #    - Salva no servidor (rápido, local)
    #    - Envia cópia para Google Drive (segurança off-site)
    # 
    # 4. Configurar credenciais Google:
    #    - Criar projeto no Google Cloud Console
    #    - Habilitar Google Drive API
    #    - Baixar credentials.json
    #    - Upload para PythonAnywhere
    # 
    # CÓDIGO EXEMPLO (descomente quando implementar):
    # 
    # from google.oauth2 import service_account
    # from googleapiclient.discovery import build
    # from googleapiclient.http import MediaFileUpload
    # 
    # def enviar_para_google_drive(arquivo_local):
    #     """Envia backup para Google Drive"""
    #     SCOPES = ['https://www.googleapis.com/auth/drive.file']
    #     SERVICE_ACCOUNT_FILE = '/home/davidbit/credentials.json'
    #     
    #     credentials = service_account.Credentials.from_service_account_file(
    #         SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    #     
    #     service = build('drive', 'v3', credentials=credentials)
    #     
    #     # ID da pasta no Drive (criar pasta "Backups FinCtl" e pegar ID da URL)
    #     folder_id = 'COLE_AQUI_O_ID_DA_PASTA_DO_DRIVE'
    #     
    #     file_metadata = {
    #         'name': os.path.basename(arquivo_local),
    #         'parents': [folder_id]
    #     }
    #     
    #     media = MediaFileUpload(arquivo_local, resumable=True)
    #     
    #     file = service.files().create(
    #         body=file_metadata,
    #         media_body=media,
    #         fields='id'
    #     ).execute()
    #     
    #     return file.get('id')
    # 
    # =========================================================================
    
    @app.route('/api/backup/create', methods=['GET', 'POST'])
    def criar_backup():
        """
        Cria backup do banco de dados PostgreSQL usando pg_dump
        Endpoint chamado automaticamente por task agendada no PythonAnywhere ou manualmente
        
        Segurança: Requer token de autenticação
        
        IMPLEMENTAÇÃO ATUAL: Salva no PythonAnywhere (/home/davidbit/backups/)
        Mantém os 4 backups mais recentes
        
        FUTURA: Descomentar código acima para sincronizar com Google Drive
        """
        try:
            # Validar token de segurança
            token = request.args.get('token') or (request.json or {}).get('token')
            token_esperado = os.getenv('BACKUP_TOKEN', 'finctl_backup_2025_secure')
            
            if token != token_esperado:
                return jsonify({'success': False, 'message': 'Token inválido'}), 401
            
            # Obter configurações do banco
            data = request.json if request.method == 'POST' else {}
            path_name = _processar_db_path_name(data)
            
            database_name = path_name.get('database_name', 'financas')
            db_user = os.getenv('PGUSER', 'davidbit')
            
            # Criar diretório de backups no servidor
            backup_dir = '/home/davidbit/backups' if os.path.exists('/home/davidbit') else os.path.join(os.getcwd(), 'backups')
            os.makedirs(backup_dir, exist_ok=True)
            
            # Nome do arquivo de backup com timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_filename = f'financas_backup_{timestamp}.sql'
            backup_path = os.path.join(backup_dir, backup_filename)
            
            # Criar backup usando pg_dump
            import subprocess
            cmd = f'pg_dump -U {db_user} -d {database_name} -f {backup_path}'
            resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if resultado.returncode == 0 and os.path.exists(backup_path):
                tamanho = os.path.getsize(backup_path) / 1024  # KB
                
                # Comprimir o backup para economizar espaço
                import gzip
                with open(backup_path, 'rb') as f_in:
                    with gzip.open(f'{backup_path}.gz', 'wb') as f_out:
                        f_out.writelines(f_in)
                os.remove(backup_path)  # Remove arquivo SQL não comprimido
                backup_path = f'{backup_path}.gz'
                backup_filename = f'{backup_filename}.gz'
                tamanho_comprimido = os.path.getsize(backup_path) / 1024  # KB
                
                # Limpar backups antigos (manter últimos 4)
                # FUTURO: Quando implementar Google Drive, aumentar para manter=30 no servidor
                # e manter=4 no Google Drive (backups semanais)
                _limpar_backups_antigos(backup_dir, manter=4)
                
                # FUTURO: Descomentar quando implementar Google Drive
                # try:
                #     drive_file_id = enviar_para_google_drive(backup_path)
                #     flow_marker(f"✅ Backup enviado para Google Drive: {drive_file_id}")
                # except Exception as e:
                #     error_catcher("Erro ao enviar para Google Drive (backup local OK)", e)
                
                return jsonify({
                    'success': True,
                    'arquivo': backup_filename,
                    'tamanho_original_kb': round(tamanho, 2),
                    'tamanho_comprimido_kb': round(tamanho_comprimido, 2),
                    'caminho': backup_path,
                    'timestamp': timestamp,
                    'tipo': 'PostgreSQL dump (gzip)'
                    # FUTURO: Adicionar quando implementar Drive
                    # 'google_drive_id': drive_file_id,
                    # 'google_drive_url': f'https://drive.google.com/file/d/{drive_file_id}/view'
                }), 200
            else:
                return jsonify({
                    'success': False,
                    'message': 'Erro ao criar backup',
                    'erro': resultado.stderr
                }), 500
                
        except Exception as e:
            error_catcher("Erro no endpoint /api/backup/create", e)
            return jsonify({'success': False, 'message': str(e)}), 500
    
    @app.route('/api/backup/list', methods=['GET'])
    def listar_backups():
        """Lista todos os backups disponíveis"""
        try:
            # Obter diretório de backups
            data = request.args.to_dict()
            path_name = _processar_db_path_name(data)
            db_path = os.path.join(path_name.get('database_path', ''), path_name.get('database_name', 'financas.db'))
            backup_dir = os.path.join(os.path.dirname(db_path), '..', 'backups')
            
            if not os.path.exists(backup_dir):
                return jsonify({'success': True, 'backups': []}), 200
            
            # Listar arquivos de backup
            backups = []
            for arquivo in os.listdir(backup_dir):
                if arquivo.startswith('financas_backup_') and arquivo.endswith('.db'):
                    caminho_completo = os.path.join(backup_dir, arquivo)
                    stat = os.stat(caminho_completo)
                    backups.append({
                        'nome': arquivo,
                        'tamanho_kb': round(stat.st_size / 1024, 2),
                        'data_criacao': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                        'timestamp': stat.st_mtime
                    })
            
            # Ordenar por data (mais recente primeiro)
            backups.sort(key=lambda x: x['timestamp'], reverse=True)
            
            return jsonify({'success': True, 'backups': backups, 'total': len(backups)}), 200
            
        except Exception as e:
            error_catcher("Erro no endpoint /api/backup/list", e)
            return jsonify({'success': False, 'message': str(e)}), 500
    
    @app.route('/api/backup/download/latest', methods=['GET'])
    def baixar_ultimo_backup():
        """Download do backup mais recente"""
        try:
            from flask import send_file
            
            # Obter diretório de backups
            data = request.args.to_dict()
            path_name = _processar_db_path_name(data)
            db_path = os.path.join(path_name.get('database_path', ''), path_name.get('database_name', 'financas.db'))
            backup_dir = os.path.join(os.path.dirname(db_path), '..', 'backups')
            
            if not os.path.exists(backup_dir):
                return jsonify({'success': False, 'message': 'Nenhum backup encontrado'}), 404
            
            # Encontrar backup mais recente
            backups = [f for f in os.listdir(backup_dir) if f.startswith('financas_backup_') and f.endswith('.db')]
            
            if not backups:
                return jsonify({'success': False, 'message': 'Nenhum backup encontrado'}), 404
            
            backups.sort(reverse=True)  # Ordem alfabética = ordem cronológica
            ultimo_backup = os.path.join(backup_dir, backups[0])
            
            return send_file(
                ultimo_backup,
                mimetype='application/x-sqlite3',
                as_attachment=True,
                download_name=backups[0]
            )
            
        except Exception as e:
            error_catcher("Erro no endpoint /api/backup/download/latest", e)
            return jsonify({'success': False, 'message': str(e)}), 500
    
    @app.route('/api/backup/download/<filename>', methods=['GET'])
    def baixar_backup_especifico(filename):
        """Download de backup específico"""
        try:
            from flask import send_file
            
            # Validar nome do arquivo (segurança)
            if not filename.startswith('financas_backup_') or not filename.endswith('.db'):
                return jsonify({'success': False, 'message': 'Nome de arquivo inválido'}), 400
            
            # Obter diretório de backups
            data = request.args.to_dict()
            path_name = _processar_db_path_name(data)
            db_path = os.path.join(path_name.get('database_path', ''), path_name.get('database_name', 'financas.db'))
            backup_dir = os.path.join(os.path.dirname(db_path), '..', 'backups')
            backup_path = os.path.join(backup_dir, filename)
            
            if not os.path.exists(backup_path):
                return jsonify({'success': False, 'message': 'Backup não encontrado'}), 404
            
            return send_file(
                backup_path,
                mimetype='application/x-sqlite3',
                as_attachment=True,
                download_name=filename
            )
            
        except Exception as e:
            error_catcher("Erro no endpoint /api/backup/download", e)
            return jsonify({'success': False, 'message': str(e)}), 500

    @app.route('/processar_extratos_pdf', methods=['POST'])
    def processar_extratos_pdf():
        """
        Endpoint para processar extratos PDF e extrair despesas
        Delega toda validação para o orquestrador de validação
        
        Executa o processo completo:
        1. Validação de arquivos e banco de dados (orquestrador)
        2. Extração de dados dos PDFs
        3. Classificação das despesas
        4. Salvamento no banco de dados
        
        @return {dict} - Resultado do processamento com status e mensagem
        """
        flow_marker("INÍCIO endpoint /processar_extratos_pdf")
        _inicializar_log()  # Limpa o log anterior
        
        try:
            # Adicionar o path do extrator ao sys.path
            extrator_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'extratorDePDF')
            if extrator_path not in sys.path:
                sys.path.append(extrator_path)
            
            # Imports diretos com path absoluto
            try:
                import importlib.util
                
                # Carregar orquestrador_validacao
                spec_validacao = importlib.util.spec_from_file_location(
                    "orquestrador_validacao", 
                    os.path.join(extrator_path, "orquestrador_validacao.py")
                )
                orquestrador_validacao = importlib.util.module_from_spec(spec_validacao)
                spec_validacao.loader.exec_module(orquestrador_validacao)
                
                # Carregar orquestrador_extracao  
                spec_extracao = importlib.util.spec_from_file_location(
                    "orquestrador_extracao",
                    os.path.join(extrator_path, "orquestrador_extracao.py")
                )
                orquestrador_extracao = importlib.util.module_from_spec(spec_extracao)
                spec_extracao.loader.exec_module(orquestrador_extracao)
                
                # Extrair as funções necessárias
                executar_validacao_completa = orquestrador_validacao.executar_validacao_completa
                processar_e_salvar_extratos = orquestrador_extracao.processar_e_salvar_extratos
                
            except (ImportError, AttributeError, FileNotFoundError) as e:
                flow_marker(f"Erro ao importar módulos do extrator: {str(e)}")
                return jsonify({
                    "sucesso": False,
                    "msg": f"Módulo extrator não encontrado: {str(e)}"
                }), 500
            
            # FASE 1: Validação completa (orquestrador faz todas as verificações)
            sucesso_validacao, dados_validados = executar_validacao_completa()
            
            if not sucesso_validacao:
                flow_marker(f"Validação falhou: {dados_validados}")
                return jsonify({
                    "sucesso": False,
                    "msg": f"Erro na validação: {dados_validados}. Verifique o arquivo log_de_erros.md para detalhes."
                }), 400
            
            flow_marker(f"Validação bem-sucedida. Dados validados: {dados_validados}")
            
            # FASE 2: Processamento e salvamento
            flow_marker("Iniciando extração e salvamento dos extratos")
            sucesso_extracao, mensagem_extracao = processar_e_salvar_extratos(dados_validados)
            
            if sucesso_extracao:
                flow_marker(f"Processo concluído com sucesso: {mensagem_extracao}")
                return jsonify({
                    "sucesso": True,
                    "mensagem": mensagem_extracao
                })
            else:
                flow_marker(f"Erro na extração: {mensagem_extracao}")
                return jsonify({
                    "sucesso": False,
                    "mensagem": f"{mensagem_extracao}\n\nVerifique o arquivo log_de_erros.md para detalhes."
                }), 500
                
        except ImportError as e:
            error_msg = f"Erro ao importar módulos de extração: {str(e)}"
            error_catcher(error_msg, e)
            return jsonify({
                "sucesso": False,
                "msg": "Erro nos módulos de extração. Verifique o arquivo log_de_erros.md para detalhes."
            }), 500
            
        except Exception as e:
            error_msg = f"Erro inesperado durante processamento: {str(e)}"
            error_catcher(error_msg, e)
            return jsonify({
                "sucesso": False,
                "msg": "Erro inesperado no processamento. Verifique o arquivo log_de_erros.md para detalhes."
            }), 500

    @app.route('/consultar_dados_db', methods=['POST'])
    def consultar_dados_db():
        """
        Endpoint para consultar dados de views prontas para popular formulários
        
        REGRA IMPORTANTE: Este endpoint deve ser usado APENAS com views prontas
        que foram criadas especificamente para uso em determinados formulários.
        
        NÃO usar consultas diretas em tabelas - sempre usar views dedicadas.
        
        @param {string} view - Nome da view pronta (ex: vw_grupos, vw_lancamentos)
        @param {string} database_path - Caminho do banco de dados
        @param {string} database_name - Nome do arquivo do banco
        @param {string} database_host - Host do banco (se remoto)
        @return {dict} - Dicionário de dados para popular formulário
        """
        flow_marker("INÍCIO endpoint /consultar_dados_db")
        
        try:
            # Validação de request usando função auxiliar
            dados_request, erro = _validar_request_json()
            if erro:
                return erro
            
            flow_marker("Dados recebidos no endpoint", dados_request)
            
            # Valida se view foi fornecida
            nome_view = dados_request.get('view', '')
            if not nome_view:
                return jsonify({
                    "dados": [],
                    "mensagem": "Nome da view não fornecido"
                }), 400
            
            # Valida campos solicitados
            campos_solicitados = dados_request.get('campos', ['Todos'])
            if not campos_solicitados or campos_solicitados == []:
                return jsonify({
                    "dados": [],
                    "mensagem": "Nenhum campo informado"
                }), 400
            
            flow_marker(f"Consultando view: {nome_view} com campos: {campos_solicitados}")
            
            # Processa configurações
            path_name = _processar_db_path_name(dados_request)
            
            # Extrai filtros da requisição
            filtros = dados_request.get('filtros', '')
            
            # Executa consulta na view usando função direta
            resultado = consultar_bd(nome_view, campos_solicitados, database_path=path_name.get('database_path'), database_name=path_name.get('database_name'), filtros=filtros)
            
            # ✅ CONVERTE Decimal → float, date → ISO (YYYY-MM-DD) para <input type="date">
            resultado_convertido = converter_tipos_postgresql(resultado)
            
            # Prepara resposta padronizada
            resposta = {
                "dados": resultado_convertido if resultado_convertido else [],
                "mensagem": "sucesso"
            }
            
            flow_marker(f"Consulta executada - View: {nome_view}, Registros: {len(resultado) if resultado else 0}")
            
            # Rastreamento do envio da resposta
            flow_marker(f"✅ ENVIANDO RESPOSTA AO FRONTEND: {len(resultado) if resultado else 0} registros")
            flow_marker(f"📤 ESTRUTURA DA RESPOSTA: {resposta}")
            
            return jsonify(resposta)
            
        except Exception as e:
            return _erro_padronizado("/consultar_dados_db", e)

    @app.route('/update_data_db', methods=['POST'])
    def update_data_db():
        """
        Endpoint para atualizar dados existentes
        
        @param {dict} dados_para_update - Dados para atualização contendo:
            - tabela: nome da tabela
            - campos: lista de campos  
            - dados_a_atualizar: dados atuais do registro
            - dados_form_out: novos dados para atualização
            - database_path: caminho do banco
            - database_name: nome do banco
        @return {dict} - Resultado da operação de atualização
        """
        flow_marker("INÍCIO endpoint /update_data_db")
        
        try:
            # Validação de request usando função auxiliar
            dados_request, erro = _validar_request_json()
            if erro:
                return erro
            
            flow_marker("Dados recebidos no endpoint", dados_request)
            
            # Valida se tabela_alvo foi fornecida
            tabela = dados_request.get('tabela_alvo', '')
            if not tabela:
                return jsonify({
                    "dados": [],
                    "mensagem": "Nome da tabela_alvo não fornecido"
                }), 400
            
            flow_marker(f"Atualizando tabela: {tabela}")
            
            # Processa configurações
            path_name = _processar_db_path_name(dados_request)
            
            # Extrai parâmetros adicionais do payload
            tabela_alvo = dados_request.get('tabela_alvo')
            campos_obrigatorios = dados_request.get('campos_obrigatorios')
            filtros = dados_request.get('filtros', '')
            
            # Executa operação de update usando função direta
            dados_a_atualizar = dados_request.get('dados', {})
            resultado = atualizar_dados(tabela, dados_a_atualizar, path_name.get('database_path'), path_name.get('database_name'), tabela_alvo, campos_obrigatorios)
            
            flow_marker(f"Update executado - Tabela: {tabela}")
            flow_marker("🔍 RESULTADO da função atualizar_dados", resultado)
            
            # ===============================================================
            # ESTRATÉGIA DE SINCRONIZAÇÃO INTELIGENTE (UPDATE):
            # Após atualização bem-sucedida, consultamos novamente a view para
            # retornar o array completo atualizado e ordenado.
            # Isso evita "tremor" na interface e mantém navegação fluida,
            # especialmente quando campos ordenados são alterados.
            # ===============================================================
            
            if resultado.get('sucesso'):
                flow_marker('🔄 Consultando dados atualizados após update')
                
                # Consulta dados atualizados aplicando filtros (se houver)
                consulta_atualizada = consultar_bd(
                    f"{tabela_alvo}_view", 
                    ['Todos'], 
                    database_path=path_name.get('database_path'), 
                    database_name=path_name.get('database_name'),
                    filtros=filtros if filtros else None
                )
                
                flow_marker('📊 Dados atualizados consultados', {
                    'view': f"{tabela_alvo}_view",
                    'filtros_aplicados': filtros if filtros else 'Nenhum',
                    'total_registros': len(consulta_atualizada.get('dados', [])) if consulta_atualizada and consulta_atualizada.get('dados') else 0
                })
                
                # ✅ CONVERTE Decimal → float, date → dd/mm/yyyy ANTES de enviar JSON
                dados_convertidos = converter_tipos_postgresql(consulta_atualizada.get('dados', [])) if consulta_atualizada else []
                
                # Resposta enriquecida com dados atualizados
                resultado_final = {
                    "sucesso": True,
                    "mensagem": resultado.get('mensagem', 'Registro atualizado com sucesso'),
                    "dados_atualizados": dados_convertidos,
                    "total_registros": len(dados_convertidos)
                }
                
                flow_marker('✅ Resposta completa com dados atualizados (UPDATE)', {
                    'total_registros': resultado_final['total_registros']
                })
                
                return jsonify(resultado_final)
            
            return jsonify(resultado)
            
        except Exception as e:
            return _erro_padronizado("/update_data_db", e)

    @app.route('/verificar_dependencias_delete', methods=['POST'])
    def verificar_dependencias_delete_endpoint():
        """
        Endpoint para verificar se há registros dependentes antes de deletar
        
        @param {dict} payload - Dados da requisição contendo:
            - tabela_alvo (str): Nome da tabela onde está o registro
            - id_campo (str): Nome do campo chave primária
            - id_valor (int|str): Valor da chave primária
            - database_name (str): Nome do banco
        
        @return {dict} - {'tem_dependencias': bool, 'quantidade': int, 'detalhes': list}
        """
        try:
            dados = request.get_json()
            
            tabela_alvo = dados.get('tabela_alvo')
            id_campo = dados.get('id_campo')
            id_valor = dados.get('id_valor')
            database_name = dados.get('database_name')
            
            # Validações
            if not all([tabela_alvo, id_campo, id_valor, database_name]):
                return jsonify({
                    'erro': 'Parâmetros obrigatórios: tabela_alvo, id_campo, id_valor, database_name'
                }), 400
            
            # Chama função de verificação
            resultado = verificar_dependencias_delete(
                tabela_alvo=tabela_alvo,
                id_campo=id_campo,
                id_valor=id_valor,
                database_name=database_name
            )
            
            return jsonify(resultado)
            
        except Exception as e:
            return _erro_padronizado("/verificar_dependencias_delete", e)

    @app.route('/atualizar_lote', methods=['POST'])
    def atualizar_lote():
        """
        Endpoint para atualizar múltiplos registros em lote (operação em massa)
        FUNÇÃO GENÉRICA: Pode ser usada para qualquer tabela do sistema
        
        Performance: 1 requisição HTTP + loop interno de UPDATEs + 1 COMMIT
        Muito mais rápido que N requisições individuais
        
        @param {dict} payload - Dados da requisição contendo:
            - tabela_alvo (str): Nome da tabela para UPDATE (ex: 'despesas', 'produtos')
            - dados_lote (list[dict]): Array de objetos com dados para atualizar
                                       Ex: [{'iddespesa': 1234, 'idgrupo': 3, 'idsubgrupo': 5}, ...]
            - pk_field (str): Nome do campo chave primária (ex: 'iddespesa', 'idproduto')
            - campos_permitidos (list): Lista de campos permitidos para atualização (segurança)
                                       Ex: ['idgrupo', 'idsubgrupo']
            - database_path (str): Caminho do banco (opcional, usa config padrão)
            - database_name (str): Nome do banco (opcional, usa config padrão)
        
        @return {dict} - Resultado com estatísticas:
                        {
                            "sucesso": True/False,
                            "total_processados": 1000,
                            "atualizados": 950,
                            "erros": 50,
                            "erros_detalhes": [{...}]
                        }
        
        @example Requisição:
            POST /atualizar_lote
            {
                "tabela_alvo": "despesas",
                "dados_lote": [
                    {"iddespesa": 1234, "idgrupo": 3, "idsubgrupo": 5},
                    {"iddespesa": 1235, "idgrupo": 2, "idsubgrupo": 8}
                ],
                "pk_field": "iddespesa",
                "campos_permitidos": ["idgrupo", "idsubgrupo"],
                "database_path": "C:/Apps/data",
                "database_name": "financas.db"
            }
        """
        flow_marker("INÍCIO endpoint /atualizar_lote")
        
        try:
            # Validação de request usando função auxiliar
            dados_request, erro = _validar_request_json()
            if erro:
                return erro
            
            flow_marker("Dados recebidos no endpoint /atualizar_lote", {
                "tabela_alvo": dados_request.get('tabela_alvo'),
                "total_registros": len(dados_request.get('dados_lote', [])),
                "pk_field": dados_request.get('pk_field')
            })
            
            # =================================================================
            # VALIDAÇÃO DE PARÂMETROS OBRIGATÓRIOS
            # =================================================================
            
            tabela_alvo = dados_request.get('tabela_alvo')
            if not tabela_alvo:
                flow_marker("❌ Erro: tabela_alvo não fornecida")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'tabela_alvo' não fornecido"
                }), 400
            
            dados_lote = dados_request.get('dados_lote')
            if not dados_lote or not isinstance(dados_lote, list) or len(dados_lote) == 0:
                flow_marker("❌ Erro: dados_lote inválido")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'dados_lote' deve ser um array não vazio"
                }), 400
            
            pk_field = dados_request.get('pk_field')
            if not pk_field:
                flow_marker("❌ Erro: pk_field não fornecido")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'pk_field' não fornecido"
                }), 400
            
            # Parâmetros opcionais
            campos_permitidos = dados_request.get('campos_permitidos')  # Pode ser None
            
            # Processa configurações de banco de dados
            path_name = _processar_db_path_name(dados_request)
            database_path = path_name.get('database_path')
            database_name = path_name.get('database_name')
            
            flow_marker(f"Parâmetros validados - Tabela: {tabela_alvo}, PK: {pk_field}, Registros: {len(dados_lote)}")
            
            # =================================================================
            # EXECUTA ATUALIZAÇÃO EM LOTE
            # =================================================================
            
            resultado = atualizar_dados_lote(
                tabela_alvo=tabela_alvo,
                dados_lote=dados_lote,
                pk_field=pk_field,
                database_path=database_path,
                database_name=database_name,
                campos_permitidos=campos_permitidos
            )
            
            flow_marker("Atualização em lote concluída", {
                "sucesso": resultado.get('sucesso'),
                "total_processados": resultado.get('total_processados', 0),
                "atualizados": resultado.get('atualizados', 0),
                "erros": resultado.get('erros', 0)
            })
            
            # =================================================================
            # RETORNA RESULTADO
            # =================================================================
            
            if resultado.get('sucesso'):
                flow_marker("✅ Atualização em lote bem-sucedida")
                return jsonify(resultado), 200
            else:
                flow_marker("❌ Atualização em lote com erro")
                return jsonify(resultado), 500
            
        except Exception as e:
            flow_marker(f"❌ EXCEÇÃO no endpoint /atualizar_lote: {str(e)}")
            return _erro_padronizado("/atualizar_lote", e)

    @app.route('/incluir_reg_novo_db', methods=['POST'])
    def incluir_reg_novo_db():
        """
        Endpoint para incluir novos registros
        
        @param {dict} dados_novo_registro - Dados do novo registro
        @return {dict} - Resultado da operação de inclusão
        """
        try:
            flow_marker('🔄 INÍCIO endpoint /incluir_reg_novo_db')
            
            dados_request = request.get_json()
            flow_marker('📋 Dados recebidos no endpoint', dados_request)
            
            # Extrai parâmetros da requisição
            tabela_alvo = dados_request.get('tabela_alvo')
            dados_form_in = dados_request.get('dados', {})
            database_path = dados_request.get('database_path')
            database_name = dados_request.get('database_name')
            campos_obrigatorios = dados_request.get('campos_obrigatorios', [])
            filtros = dados_request.get('filtros', '')
            
            # Constrói caminho completo do banco
            database_file = os.path.join(database_path, database_name)
            
            flow_marker('🔧 Parâmetros extraídos', {
                'tabela_alvo': tabela_alvo,
                'database_file': database_file,
                'campos_para_inserir': list(dados_form_in.keys()),
                'filtros': filtros
            })
            
            # Chama data_manager para inserir dados
            resultado = data_manager.inserir_dados(
                tabela=tabela_alvo,
                dados_form_in=dados_form_in,
                database_path=database_path,
                database_name=database_name,
                tabela_alvo=tabela_alvo,
                campos_obrigatorios=campos_obrigatorios
            )
            
            flow_marker('📤 Resultado da inserção', resultado)
            
            if resultado.get('sucesso'):
                # ===============================================================
                # ESTRATÉGIA DE SINCRONIZAÇÃO INTELIGENTE:
                # Após inserção bem-sucedida, consultamos novamente a view para
                # retornar o array completo atualizado e ordenado.
                # Isso evita "tremor" na interface e mantém navegação fluida,
                # pois o frontend substitui dadosDisponiveis e recalcula reg_num
                # automaticamente através de find() da nova PK.
                # ===============================================================
                
                flow_marker('🔄 Consultando dados atualizados após inserção')
                
                # Consulta dados atualizados aplicando filtros (se houver)
                consulta_atualizada = consultar_bd(
                    f"{tabela_alvo}_view", 
                    ['Todos'], 
                    database_path=database_path, 
                    database_name=database_name,
                    filtros=filtros if filtros else None
                )
            
                flow_marker('📊 Dados atualizados consultados', {
                    'view': f"{tabela_alvo}_view",
                    'filtros_aplicados': filtros if filtros else 'Nenhum',
                    'total_registros': len(consulta_atualizada.get('dados', [])) if consulta_atualizada and consulta_atualizada.get('dados') else 0
                })
                
                # ✅ CONVERTE Decimal → float, date → dd/mm/yyyy ANTES de enviar JSON
                dados_convertidos = converter_tipos_postgresql(consulta_atualizada.get('dados', [])) if consulta_atualizada else []
                
                resposta = {
                    "sucesso": True,
                    "mensagem": resultado.get('mensagem', 'Registro inserido com sucesso'),
                    "dados_atualizados": dados_convertidos,
                    "total_registros": len(dados_convertidos)
                }
                flow_marker('✅ Resposta completa com dados atualizados', {
                    'total_registros': resposta['total_registros']
                })
                return jsonify(resposta)
            else:
                resposta = {
                    "sucesso": False,
                    "mensagem": resultado.get('mensagem', 'Erro na inserção')
                }
                flow_marker('❌ Resposta de erro', resposta)
                return jsonify(resposta), 400
            
        except Exception as e:
            logger.error(f"Erro em incluir_reg_novo_db: {e}")
            flow_marker('💥 Erro crítico no endpoint', str(e))
            return jsonify({"sucesso": False, "mensagem": f"Erro: {str(e)}"}), 500

    @app.route('/delete_reg', methods=['POST'])
    def delete_reg():
        """
        Endpoint para excluir registros existentes
        
        @param {dict} dados_para_delete - Dados para exclusão contendo:
            - tabela_alvo: nome da tabela
            - pk_para_excluir: chave primária do registro a excluir
            - database_path: caminho do banco
            - database_name: nome do banco
            - forcar: (opcional) True para forçar exclusão ignorando dependências
        @return {dict} - Resultado da operação de exclusão com dados atualizados
        """
        flow_marker('🔄 INÍCIO endpoint /delete_reg')
        
        try:
            # Validação de request usando função auxiliar
            dados_request, erro = _validar_request_json()
            if erro:
                return erro
            
            flow_marker('📋 Dados recebidos no endpoint', dados_request)
            
            # Valida se tabela_alvo foi fornecida
            tabela_alvo = dados_request.get('tabela_alvo', '')
            if not tabela_alvo:
                return jsonify({
                    "sucesso": False,
                    "mensagem": "Nome da tabela_alvo não fornecido"
                }), 400
            
            # Valida se pk_para_excluir foi fornecida
            pk_para_excluir = dados_request.get('pk_para_excluir')
            if not pk_para_excluir:
                return jsonify({
                    "sucesso": False,
                    "mensagem": "Chave primária para exclusão não fornecida"
                }), 400
            
            # Extrai flag forcar (default: False)
            forcar = dados_request.get('forcar', False)
            
            flow_marker(f'🗑️ Excluindo registro da tabela: {tabela_alvo}, PK: {pk_para_excluir}, Forçar: {forcar}')
            
            # Processa configurações
            database_path = dados_request.get('database_path', '')
            database_name = dados_request.get('database_name', '')
            
            # Monta caminho completo do banco
            database_file = os.path.join(database_path, database_name)
            flow_marker('🔧 Parâmetros extraídos', {
                'tabela_alvo': tabela_alvo,
                'database_file': database_file,
                'pk_para_excluir': pk_para_excluir,
                'forcar': forcar
            })
            
            # Executa operação de exclusão usando função direta (COM PARÂMETRO FORCAR)
            resultado = excluir_dados(tabela_alvo, pk_para_excluir, database_path, database_name, tabela_alvo, forcar)
            
            flow_marker('📤 Resultado da exclusão', resultado)
            
            # ===============================================================
            # ESTRATÉGIA DE SINCRONIZAÇÃO INTELIGENTE (DELETE):
            # Após exclusão bem-sucedida, consultamos novamente a view para
            # retornar o array completo atualizado e ordenado.
            # Isso evita "tremor" na interface e mantém navegação fluida,
            # reposicionando automaticamente após remoção do registro.
            # ===============================================================
            
            if resultado.get('sucesso'):
                flow_marker('🔄 Consultando dados atualizados após exclusão')
                
                # Consulta dados atualizados com parâmetros corretos
                consulta_atualizada = consultar_bd(f"{tabela_alvo}_view", ['Todos'], database_path=database_path, database_name=database_name)
                
                flow_marker('📊 Dados atualizados consultados', {
                    'view': f"{tabela_alvo}_view",
                    'total_registros': len(consulta_atualizada.get('dados', [])) if consulta_atualizada and consulta_atualizada.get('dados') else 0
                })
                
                # ✅ CONVERTE Decimal → float, date → dd/mm/yyyy ANTES de enviar JSON
                dados_convertidos = converter_tipos_postgresql(consulta_atualizada.get('dados', [])) if consulta_atualizada else []
                
                resposta = {
                    "sucesso": True,
                    "mensagem": resultado.get('mensagem', 'Registro excluído com sucesso'),
                    "dados_atualizados": dados_convertidos,
                    "total_registros": len(dados_convertidos)
                }
                flow_marker('✅ Resposta completa com dados atualizados (DELETE)', {
                    'total_registros': resposta['total_registros']
                })
                return jsonify(resposta)
            else:
                resposta = {
                    "sucesso": False,
                    "mensagem": resultado.get('mensagem', 'Erro na exclusão')
                }
                flow_marker('❌ Resposta de erro', resposta)
                return jsonify(resposta), 400
            
        except Exception as e:
            logger.error(f"Erro em delete_reg: {e}")
            flow_marker('💥 Erro crítico no endpoint', str(e))
            return jsonify({"sucesso": False, "mensagem": f"Erro: {str(e)}"}), 500

    @app.route('/executar_sql', methods=['POST'])
    def executar_sql_endpoint():
        """
        Endpoint para executar SQL direto no banco de dados
        
        Permite envio de consultas SQL personalizadas do frontend.
        Retorna dados estruturados para SELECT ou resultado de operação para DDL/DML.
        
        @param {dict} request_data - Dados da requisição
        @param {str} request_data.sql - Comando SQL a executar
        @param {str} request_data.database_path - Caminho do banco
        @param {str} request_data.database_name - Nome do banco
        
        @return {dict} - Resultado estruturado:
        Para SELECT: {"sucesso": True, "dados": [{"campo": "valor"}], "mensagem": "..."}
        Para DDL/DML: {"sucesso": True, "registros_afetados": N, "mensagem": "..."}
        Para erro: {"sucesso": False, "erro": "..."}
        """
        flow_marker("INÍCIO endpoint /executar_sql")
        
        try:
            # Validação do request JSON
            dados_request, erro_response = _validar_request_json()
            if erro_response:
                return erro_response
            
            # Validação de campos obrigatórios
            sql = dados_request.get('sql', '').strip()
            if not sql:
                flow_marker('❌ SQL não fornecido')
                return jsonify({
                    "sucesso": False,
                    "erro": "SQL não fornecido"
                }), 400
            
            # Extração de parâmetros obrigatórios
            database_path = dados_request.get('database_path')
            database_name = dados_request.get('database_name')
            
            # Validação centralizada
            try:
                validar_database_config(database_path, database_name)
            except ValueError as e:
                flow_marker(f'❌ {str(e)}')
                return jsonify({
                    "sucesso": False,
                    "erro": str(e)
                }), 400
            
            flow_marker(f"📝 SQL recebido: {sql[:100]}...")
            flow_marker(f"💾 Database: {database_name} em {database_path}")
            
            # Importa e executa a função do data_manager
            from data_manager import executar_sql
            resultado = executar_sql(sql, database_path, database_name)
            
            # ✅ CONVERTE Decimal → float ANTES de enviar JSON
            if resultado.get('sucesso') and resultado.get('dados'):
                resultado['dados'] = converter_tipos_postgresql(resultado['dados'])
            
            # Loga o resultado para diagnóstico
            flow_marker(f"📊 RESULTADO da query SQL: {resultado}")
            
            # Retorna resultado estruturado
            if resultado.get('sucesso'):
                flow_marker('✅ SQL executado com sucesso')
                return jsonify(resultado)
            else:
                flow_marker(f'❌ Erro na execução SQL: {resultado.get("erro")}')
                return jsonify(resultado), 400
                
        except Exception as e:
            logger.error(f"Erro em executar_sql_endpoint: {e}")
            flow_marker('💥 Erro crítico no endpoint executar_sql', str(e))
            return jsonify({
                "sucesso": False,
                "erro": f"Erro interno: {str(e)}"
            }), 500

    @app.route('/analise_abc', methods=['POST'])
    def analise_abc_endpoint():
        """
        Endpoint para análise ABC de despesas
        
        Retorna curva ABC de despesas individuais, por grupos e dados para gráfico pizza
        conforme filtros fornecidos (ano, mês, instituição)
        
        @param {dict} request_data - Dados da requisição:
            - tipo_analise: 'despesas_individuais' | 'por_grupos' | 'grafico_pizza'
            - ano: Ano para filtro (ex: '2025')
            - mes: Mês para filtro (ex: 'MAR')
            - instituicao: Instituição financeira (ex: 'MASTERCARD') ou null para todas
            - database_path: Caminho do banco (opcional)
            - database_name: Nome do banco (opcional)
        
        @return {dict} - Resultado da análise ABC estruturado
        """
        flow_marker("INÍCIO endpoint /analise_abc")
        
        try:
            # Validação do request JSON
            dados_request, erro_response = _validar_request_json()
            if erro_response:
                return erro_response
            
            # Extração de parâmetros
            tipo_analise = dados_request.get('tipo_analise', '').lower()
            ano = dados_request.get('ano')
            mes = dados_request.get('mes')
            instituicao = dados_request.get('instituicao')
            database_path = dados_request.get('database_path')
            database_name = dados_request.get('database_name')
            
            # Validações
            if not tipo_analise:
                flow_marker('❌ tipo_analise não fornecido')
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'tipo_analise' é obrigatório"
                }), 400
            
            if tipo_analise not in ['despesas_individuais', 'por_grupos', 'grafico_pizza']:
                flow_marker(f'❌ tipo_analise inválido: {tipo_analise}')
                return jsonify({
                    "sucesso": False,
                    "erro": "tipo_analise deve ser: 'despesas_individuais', 'por_grupos' ou 'grafico_pizza'"
                }), 400
            
            if not ano or not mes:
                flow_marker('❌ Filtros ano/mes não fornecidos')
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetros 'ano' e 'mes' são obrigatórios"
                }), 400
            
            flow_marker(f"📊 Análise ABC solicitada: {tipo_analise}")
            flow_marker(f"📅 Filtros: {ano}/{mes}, Instituição: {instituicao or 'TODAS'}")
            
            # Importar funções do data_analysis
            import data_analysis
            
            # Montar filtro data_extrato
            data_extrato = f"{mes}_{ano}"
            
            # Construir filtros
            filtros = {'data_extrato': data_extrato}
            if instituicao:
                filtros['instituicao'] = instituicao
            
            # =============================================================
            # ANÁLISE 1: CURVA ABC - DESPESAS INDIVIDUAIS
            # =============================================================
            if tipo_analise == 'despesas_individuais':
                flow_marker("Calculando Curva ABC - Despesas Individuais")
                
                resultado = data_analysis.calcular_curva_abc(
                    view_name='despesas_view',
                    campo_descricao='descricao',
                    campo_valor='valor',
                    filtros=filtros,
                    database_path=database_path,
                    database_name=database_name,
                    limite_a=80.0,
                    limite_b=95.0
                )
                
                if resultado['sucesso']:
                    flow_marker(f"✅ Curva ABC calculada: {len(resultado['dados'])} despesas")
                    return jsonify(resultado)
                else:
                    flow_marker(f"❌ Erro ao calcular curva ABC: {resultado.get('erro')}")
                    return jsonify(resultado), 400
            
            # =============================================================
            # ANÁLISE 2: CURVA ABC - POR GRUPOS
            # =============================================================
            elif tipo_analise == 'por_grupos':
                flow_marker("Calculando Curva ABC - Por Grupos")
                
                resultado = data_analysis.calcular_curva_abc(
                    view_name='despesas_view_01',
                    campo_descricao='grupo',
                    campo_valor='valor',
                    filtros=filtros,
                    database_path=database_path,
                    database_name=database_name,
                    limite_a=80.0,
                    limite_b=95.0
                )
                
                if resultado['sucesso']:
                    flow_marker(f"✅ Curva ABC por grupos calculada: {len(resultado['dados'])} grupos")
                    return jsonify(resultado)
                else:
                    flow_marker(f"❌ Erro ao calcular curva ABC por grupos: {resultado.get('erro')}")
                    return jsonify(resultado), 400
            
            # =============================================================
            # ANÁLISE 3: DADOS PARA GRÁFICO PIZZA
            # =============================================================
            elif tipo_analise == 'grafico_pizza':
                flow_marker("Preparando dados para gráfico pizza")
                
                # Primeiro calcular curva ABC por grupos
                curva_grupos = data_analysis.calcular_curva_abc(
                    view_name='despesas_view_01',
                    campo_descricao='grupo',
                    campo_valor='valor',
                    filtros=filtros,
                    database_path=database_path,
                    database_name=database_name,
                    limite_a=80.0,
                    limite_b=95.0
                )
                
                if not curva_grupos['sucesso']:
                    flow_marker(f"❌ Erro ao calcular curva ABC para pizza: {curva_grupos.get('erro')}")
                    return jsonify(curva_grupos), 400
                
                # Preparar dados para pizza (threshold 2%)
                resultado = data_analysis.preparar_dados_grafico_pizza(
                    dados_curva_abc=curva_grupos['dados'],
                    campo_label='descricao',  # calcular_curva_abc renomeia para 'descricao'
                    campo_valor='valor_total',
                    campo_percentual='percentual',
                    threshold=2.0
                )
                
                if resultado['sucesso']:
                    flow_marker(f"✅ Dados pizza preparados: {len(resultado['labels'])} fatias")
                    return jsonify(resultado)
                else:
                    flow_marker(f"❌ Erro ao preparar dados pizza: {resultado.get('erro')}")
                    return jsonify(resultado), 400
                
        except ImportError as e:
            logger.error(f"Erro ao importar data_analysis: {e}")
            flow_marker('💥 Módulo data_analysis não encontrado', str(e))
            return jsonify({
                "sucesso": False,
                "erro": f"Módulo de análise não disponível: {str(e)}"
            }), 500
            
        except Exception as e:
            logger.error(f"Erro em analise_abc_endpoint: {e}")
            flow_marker('💥 Erro crítico no endpoint analise_abc', str(e))
            return jsonify({
                "sucesso": False,
                "erro": f"Erro interno: {str(e)}"
            }), 500

    # =============================================================================
    #                    ENDPOINT: EVOLUÇÃO MENSAL DE DESPESAS (12M)
    # =============================================================================
    
    @app.route('/despesas_12m', methods=['POST'])
    def despesas_12m_endpoint():
        """
        ✅ ENDPOINT GENÉRICO - Retorna evolução mensal em formato de matriz pivotada
        
        FILOSOFIA: Backend NÃO decide view, campos ou filtros - apenas EXECUTA o que recebe
        
        REQUEST JSON (TUDO vem do RELATÓRIO):
        {
            "ano_referencia": 2024,           // OBRIGATÓRIO - Ano para análise
            "view_name": "despesas_view",     // OBRIGATÓRIO - View a consultar
            "campo_descricao": "grupo",       // OBRIGATÓRIO - Campo para linhas
            "campo_valor": "valor",           // OBRIGATÓRIO - Campo para agregação
            "campo_ano": "ano",               // OPCIONAL - Nome do campo ano (padrão: 'ano')
            "campo_mes": "mes",               // OPCIONAL - Nome do campo mês (padrão: 'mes')
            "filtros": {                      // OPCIONAL - Filtros dinâmicos
                "instituicao": "Itau",
                "tipo": "Despesa"
            },
            "database_path": "c:\\...",       // OBRIGATÓRIO - Caminho do banco
            "database_name": "financas.db"    // OBRIGATÓRIO - Nome do arquivo .db
        }
        
        RESPONSE JSON:
        {
            "sucesso": true,
            "colunas": ["JAN", "FEV", "MAR", ..., "TOTAL"],
            "linhas": [
                {
                    "descricao": "Alimentação",
                    "JAN": 1200.00,
                    "FEV": 1350.00,
                    ...
                    "TOTAL": 15000.00
                },
                ...
            ],
            "resumo": {
                "ano": 2024,
                "meses_com_dados": 12,
                "total_descricoes": 5,
                "total_geral": 27500.00,
                "ano_corrente": false
            },
            "criterios": {...}
        }
        """
        try:
            flow_marker("INÍCIO endpoint /despesas_12m")
            
            # =============================================================
            # VALIDAÇÃO DE REQUEST
            # =============================================================
            
            if not request.is_json:
                flow_marker("❌ Request não é JSON")
                return jsonify({
                    "sucesso": False,
                    "erro": "Content-Type deve ser application/json"
                }), 400
            
            dados = request.get_json()
            flow_marker(f"📦 Dados recebidos: {dados}")
            
            # ✅ EXTRAIR TODOS OS PARÂMETROS DO PAYLOAD (frontend define tudo)
            view_name = dados.get('view_name')
            campo_Agrupamento = dados.get('campo_Agrupamento')
            campo_Pivot = dados.get('campo_Pivot')
            campo_valor = dados.get('campo_valor')
            numColunasPivot = dados.get('numColunasPivot', 12)
            database_path = dados.get('database_path')
            database_name = dados.get('database_name')
            
            # Validar parâmetros obrigatórios
            if not view_name:
                flow_marker("❌ Parâmetro 'view_name' não fornecido")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'view_name' é obrigatório"
                }), 400
            
            if not campo_Agrupamento:
                flow_marker("❌ Parâmetro 'campo_Agrupamento' não fornecido")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'campo_Agrupamento' é obrigatório"
                }), 400
            
            if not campo_Pivot:
                flow_marker("❌ Parâmetro 'campo_Pivot' não fornecido")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'campo_Pivot' é obrigatório"
                }), 400
            
            if not campo_valor:
                flow_marker("❌ Parâmetro 'campo_valor' não fornecido")
                return jsonify({
                    "sucesso": False,
                    "erro": "Parâmetro 'campo_valor' é obrigatório"
                }), 400
            
            # Validação centralizada de database_path e database_name
            try:
                validar_database_config(database_path, database_name)
            except ValueError as e:
                flow_marker(f"❌ {str(e)}")
                return jsonify({
                    "sucesso": False,
                    "erro": str(e)
                }), 400
            
            # =============================================================
            # CHAMAR FUNÇÃO DE ANÁLISE COM PARÂMETROS DO PAYLOAD
            # =============================================================
            
            flow_marker(f"📊 Calculando tabela pivot:")
            flow_marker(f"   - View: {view_name}")
            flow_marker(f"   - Campo agrupamento: {campo_Agrupamento}")
            flow_marker(f"   - Campo pivot: {campo_Pivot}")
            flow_marker(f"   - Campo valor: {campo_valor}")
            flow_marker(f"   - Num colunas pivot: {numColunasPivot}")
            
            import data_analysis
            
            resultado = data_analysis.calcular_tabela_pivot(
                view_name=view_name,
                campo_Agrupamento=campo_Agrupamento,
                campo_Pivot=campo_Pivot,
                campo_valor=campo_valor,
                numColunasPivot=numColunasPivot,
                database_path=database_path,
                database_name=database_name
            )
            
            # =============================================================
            # RETORNAR RESULTADO
            # =============================================================
            
            if resultado['success']:
                num_grupos = len(resultado['labels']) - 1  # -1 para excluir TOTAL GERAL
                num_colunas = len(resultado['colunas'])
                flow_marker(f"✅ Tabela pivot calculada: {num_grupos} grupos × {num_colunas} colunas")
                return jsonify(resultado)
            else:
                flow_marker(f"❌ Erro ao calcular tabela pivot: {resultado.get('erro')}")
                return jsonify(resultado), 400
        
        except ImportError as e:
            logger.error(f"Erro ao importar módulo de análise: {e}")
            flow_marker('💥 Módulo data_analysis não encontrado', str(e))
            return jsonify({
                "success": False,
                "erro": f"Módulo de análise não disponível: {str(e)}"
            }), 500
            
        except Exception as e:
            logger.error(f"Erro em despesas_12m_endpoint: {e}")
            flow_marker('💥 Erro crítico no endpoint despesas_12m', str(e))
            return jsonify({
                "success": False,
                "erro": f"Erro interno: {str(e)}"
            }), 500

   
# =============================================================================
#                           VALIDAÇÕES
# =============================================================================

def _validar_request_json():
    """
    Valida se o request contém JSON válido
    
    @return {tuple} - (dados_request, erro_response) 
    """
    dados_request = request.get_json()

    if not dados_request:
        flow_marker("ERRO: Dados não fornecidos")
        erro = jsonify({
            "dados": [],
            "mensagem": "Dados não fornecidos"
        }), 400
        return None, erro
    
    # Retorna dados válidos sem erro
    return dados_request, None

# =============================================================================
#                         FUNÇÕES AUXILIARES
# =============================================================================

def _processar_db_path_name(dados_request):
    """
    Organiza os dados de configuração do database em um dicionário
    @param {dict} dados_request - Dados da requisição
    @return {dict} - Configurações do database processadas
    """
    return {
        'database_path': dados_request.get('database_path', ''),
        'database_name': dados_request.get('database_name', ''),
        'database_host': dados_request.get('database_host', '')
    }

def _limpar_backups_antigos(backup_dir, manter=4):
    """
    Remove backups antigos, mantendo apenas os N mais recentes
    
    @param {str} backup_dir - Diretório com os backups
    @param {int} manter - Quantidade de backups a manter
    """
    try:
        # Listar todos os backups (PostgreSQL dumps comprimidos)
        backups = []
        for arquivo in os.listdir(backup_dir):
            if arquivo.startswith('financas_backup_') and arquivo.endswith('.sql.gz'):
                caminho = os.path.join(backup_dir, arquivo)
                backups.append((arquivo, os.path.getmtime(caminho)))
        
        # Ordenar por data (mais recente primeiro)
        backups.sort(key=lambda x: x[1], reverse=True)
        
        # Deletar excedentes
        if len(backups) > manter:
            for arquivo, _ in backups[manter:]:
                caminho = os.path.join(backup_dir, arquivo)
                os.remove(caminho)
                flow_marker(f"🗑️ Backup antigo removido: {arquivo}")
                
    except Exception as e:
        error_catcher("Erro ao limpar backups antigos", e)

def _erro_padronizado(endpoint_nome, erro):
    """
    Gera resposta de erro padronizada
    
    @param {string} endpoint_nome - Nome do endpoint
    @param {Exception} erro - Objeto de erro
    @return {tuple} - Response JSON e código HTTP
    """
    error_catcher(f"Erro no endpoint {endpoint_nome}", erro)
    return jsonify({
        "dados": [],
        "mensagem": f"Erro interno: {str(erro)}"
    }), 500

