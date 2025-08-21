#!/usr/bin/env python3
"""
Servidor Backend para FinCtl
Instancia e inicializa a API backend para o sistema FinCtl
"""

import sys
import os

# Adiciona o diretório src ao path para importações
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.infrastructure.database.backend_api import api_be
from src.infrastructure.database.data_manager import db_manager

def main():
    """
    Função principal para inicializar o servidor backend do FinCtl
    """
    print("🚀 Iniciando Servidor Backend FinCtl...")
    
    # ========== INSTANCIAÇÃO DA API BACKEND ==========
    
    # Instanciando a API backend para FinCtl
    api_finctl_backend = api_be()
    
    # Configurando propriedades específicas do FinCtl
    api_finctl_backend.aplicacao = "FinCtl"
    api_finctl_backend.versao = "1.0.0"
    api_finctl_backend.host = "localhost"
    api_finctl_backend.porta = 5000
    api_finctl_backend.debug = True
    
    # Configurando banco de dados do FinCtl
    api_finctl_backend.database_path = "finctl_database.db"
    
    print(f"✅ API Backend FinCtl configurada:")
    print(f"   📱 Aplicação: {api_finctl_backend.aplicacao}")
    print(f"   📍 Host: {api_finctl_backend.host}:{api_finctl_backend.porta}")
    print(f"   💾 Database: {api_finctl_backend.database_path}")
    
    # ========== CONFIGURAÇÃO DO BANCO DE DADOS ==========
    
    # Instanciando o gerenciador de banco para FinCtl
    db_finctl = db_manager(api_finctl_backend.database_path)
    
    # Criando tabelas específicas do FinCtl se não existirem
    criar_estrutura_finctl(db_finctl)
    
    # Associando o db_manager à API
    api_finctl_backend.db_manager = db_finctl
    
    # ========== INICIALIZAÇÃO DO SERVIDOR ==========
    
    try:
        print("🌐 Iniciando servidor Flask...")
        api_finctl_backend.iniciar_servidor()
        
    except KeyboardInterrupt:
        print("\n⏹️ Servidor interrompido pelo usuário")
        
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        
    finally:
        print("🔒 Encerrando servidor backend FinCtl")


def criar_estrutura_finctl(db_manager_instance):
    """
    Cria a estrutura de tabelas específicas do FinCtl
    
    Args:
        db_manager_instance: Instância do gerenciador de banco
    """
    print("🗃️ Criando estrutura de tabelas do FinCtl...")
    
    try:
        # Tabela de grupos financeiros
        sql_grupos = """
        CREATE TABLE IF NOT EXISTS tb_grupos_finctl (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grupo TEXT NOT NULL UNIQUE,
            descricao TEXT NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        # Tabela de subgrupos financeiros
        sql_subgrupos = """
        CREATE TABLE IF NOT EXISTS tb_subgrupos_finctl (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subgrupo TEXT NOT NULL,
            grupo_pai TEXT NOT NULL,
            descricao TEXT NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (grupo_pai) REFERENCES tb_grupos_finctl(grupo),
            UNIQUE(subgrupo, grupo_pai)
        )
        """
        
        # Tabela de lançamentos financeiros
        sql_lancamentos = """
        CREATE TABLE IF NOT EXISTS tb_lancamentos_finctl (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor DECIMAL(10,2) NOT NULL,
            data_lancamento DATE NOT NULL,
            tipo TEXT CHECK(tipo IN ('RECEITA', 'DESPESA')) NOT NULL,
            grupo TEXT NOT NULL,
            subgrupo TEXT,
            observacoes TEXT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (grupo) REFERENCES tb_grupos_finctl(grupo),
            FOREIGN KEY (subgrupo) REFERENCES tb_subgrupos_finctl(subgrupo)
        )
        """
        
        # Views para facilitar consultas
        sql_view_grupos = """
        CREATE VIEW IF NOT EXISTS vw_grupos_finctl AS
        SELECT 
            grupo,
            descricao,
            (SELECT COUNT(*) FROM tb_subgrupos_finctl s WHERE s.grupo_pai = g.grupo) as qtd_subgrupos,
            (SELECT COUNT(*) FROM tb_lancamentos_finctl l WHERE l.grupo = g.grupo) as qtd_lancamentos,
            data_criacao,
            data_atualizacao
        FROM tb_grupos_finctl g
        ORDER BY grupo
        """
        
        sql_view_subgrupos = """
        CREATE VIEW IF NOT EXISTS vw_subgrupos_finctl AS
        SELECT 
            s.subgrupo,
            s.grupo_pai,
            s.descricao,
            g.descricao as descricao_grupo_pai,
            (SELECT COUNT(*) FROM tb_lancamentos_finctl l WHERE l.subgrupo = s.subgrupo) as qtd_lancamentos,
            s.data_criacao,
            s.data_atualizacao
        FROM tb_subgrupos_finctl s
        INNER JOIN tb_grupos_finctl g ON s.grupo_pai = g.grupo
        ORDER BY s.grupo_pai, s.subgrupo
        """
        
        sql_view_lancamentos = """
        CREATE VIEW IF NOT EXISTS vw_lancamentos_finctl AS
        SELECT 
            l.id,
            l.descricao,
            l.valor,
            l.data_lancamento,
            l.tipo,
            l.grupo,
            l.subgrupo,
            g.descricao as descricao_grupo,
            COALESCE(s.descricao, '') as descricao_subgrupo,
            l.observacoes,
            l.data_criacao,
            l.data_atualizacao
        FROM tb_lancamentos_finctl l
        INNER JOIN tb_grupos_finctl g ON l.grupo = g.grupo
        LEFT JOIN tb_subgrupos_finctl s ON l.subgrupo = s.subgrupo
        ORDER BY l.data_lancamento DESC, l.id DESC
        """
        
        # Executando as criações
        tabelas = [
            ("Grupos", sql_grupos),
            ("Subgrupos", sql_subgrupos), 
            ("Lançamentos", sql_lancamentos),
            ("View Grupos", sql_view_grupos),
            ("View Subgrupos", sql_view_subgrupos),
            ("View Lançamentos", sql_view_lancamentos)
        ]
        
        for nome, sql in tabelas:
            db_manager_instance.executar_sql_direto(sql)
            print(f"   ✅ {nome} criada/verificada")
            
        # Inserindo dados de exemplo se não existirem
        inserir_dados_exemplo(db_manager_instance)
        
        print("✅ Estrutura do banco FinCtl criada com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao criar estrutura do banco: {e}")
        raise


def inserir_dados_exemplo(db_manager_instance):
    """
    Insere dados de exemplo no banco se estiver vazio
    
    Args:
        db_manager_instance: Instância do gerenciador de banco
    """
    try:
        # Verifica se já existem grupos
        resultado = db_manager_instance.executar_sql_direto(
            "SELECT COUNT(*) as total FROM tb_grupos_finctl"
        )
        
        if resultado and resultado[0]['total'] == 0:
            print("📝 Inserindo dados de exemplo...")
            
            # Grupos de exemplo
            grupos_exemplo = [
                ("Alimentação", "Despesas com alimentação e bebidas"),
                ("Transporte", "Gastos com locomoção e veículos"),
                ("Moradia", "Custos relacionados à habitação"),
                ("Saúde", "Despesas médicas e de bem-estar"),
                ("Educação", "Investimentos em aprendizado"),
                ("Lazer", "Entretenimento e diversão"),
                ("Receitas", "Fontes de renda")
            ]
            
            for grupo, descricao in grupos_exemplo:
                sql_insert = "INSERT INTO tb_grupos_finctl (grupo, descricao) VALUES (?, ?)"
                db_manager_instance.executar_sql_direto(sql_insert, (grupo, descricao))
                
            print("   ✅ Grupos de exemplo inseridos")
            
            # Subgrupos de exemplo
            subgrupos_exemplo = [
                ("Supermercado", "Alimentação", "Compras em supermercados"),
                ("Restaurantes", "Alimentação", "Refeições fora de casa"),
                ("Combustível", "Transporte", "Gasolina e álcool"),
                ("Transporte Público", "Transporte", "Ônibus, metrô, táxi"),
                ("Aluguel", "Moradia", "Valor do aluguel mensal"),
                ("Contas", "Moradia", "Água, luz, gás, internet"),
                ("Salário", "Receitas", "Salário principal"),
                ("Freelances", "Receitas", "Trabalhos extras")
            ]
            
            for subgrupo, grupo_pai, descricao in subgrupos_exemplo:
                sql_insert = "INSERT INTO tb_subgrupos_finctl (subgrupo, grupo_pai, descricao) VALUES (?, ?, ?)"
                db_manager_instance.executar_sql_direto(sql_insert, (subgrupo, grupo_pai, descricao))
                
            print("   ✅ Subgrupos de exemplo inseridos")
            
    except Exception as e:
        print(f"⚠️ Aviso ao inserir dados de exemplo: {e}")


if __name__ == "__main__":
    main()
