import sys
import os

# Adiciona o diretorio src ao path para permitir imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

def teste_imports():
    print("=== TESTANDO IMPORTS ===")
    
    try:
        print("Testando infrastructure.config...")
        from infrastructure.config import config
        print(f"  - Banco de dados: {config.CAMINHO_BANCO_DE_DADOS}")
        
        print("Testando infrastructure.logging...")
        from infrastructure.logging import logger_setup
        
        print("Testando infrastructure.database...")
        from infrastructure.database import data_manager
        
        print("Testando domain.services...")
        from domain.services import classificacao
        
        print("Testando application.orchestrators...")
        from application.orchestrators import orquestrador_consultas
        from application.orchestrators import orquestrador_reclassificacao
        
        print("Todos os imports principais funcionaram!")
        return True
        
    except Exception as e:
        print(f"Erro no import: {e}")
        return False

def teste_banco_dados():
    print("\n=== TESTANDO BANCO DE DADOS ===")
    
    try:
        from infrastructure.database import data_manager
        
        classificacoes = data_manager.obter_todas_classificacoes()
        print(f"Conexao com banco OK - {len(classificacoes)} classificacoes encontradas")
        
        if classificacoes:
            print("  Primeiras classificacoes:")
            for i, c in enumerate(classificacoes[:3]):
                print(f"    {i+1}. {c['grupo']} - {c['subgrupo']}")
        
        return True
        
    except Exception as e:
        print(f"Erro no banco: {e}")
        return False

def main():
    print("TESTE DO BACKEND_TESTE")
    print("=" * 50)
    
    imports_ok = teste_imports()
    
    if imports_ok:
        banco_ok = teste_banco_dados()
    else:
        banco_ok = False
    
    print("\n" + "=" * 50)
    if imports_ok and banco_ok:
        print("SUCESSO! O sistema esta funcionando!")
    else:
        print("FALHA! Ha problemas que precisam ser corrigidos.")
    
    return imports_ok and banco_ok

if __name__ == "__main__":
    main()
