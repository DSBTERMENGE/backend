# BackEnd_Teste - Framework Genérico Reutilizável

**Data de Criação:** 09 de Agosto de 2025
**Origem:** Extraído e simplificado do projeto FinCtlByDSB
**Objetivo:** Framework base para múltiplos projetos web

##  CONCEITO FUNDAMENTAL

### **BackEnd_Teste + FrontEnd_Teste = FRAMEWORK GENÉRICO REUTILIZÁVEL**

**ESPECIALIZAÇÃO ÚNICA:**
- Receber requisições HTTP
- Acessar banco de dados SQLite  
- Retornar dados (sucesso) ou mensagem de erro (falha)
- **NADA MAIS QUE ISSO!**

### **Filosofia do Framework:**

```
FORNECE (Base Genérica):
 Estrutura de API REST básica (CRUD)
 Acesso genérico ao banco de dados SQLite
 Sistema de logging configurável
 Sistema de configurações flexível
 Estrutura de pastas organizada
 Documentação de uso

NÃO FORNECE (Cada projeto implementa conforme necessário):
 Funcionalidades específicas de domínio
 Validações específicas de negócio  
 Processamento de arquivos específicos
 Orquestradores complexos
 Regras de negócio particulares
```

### **Casos de Uso do Framework:**

- **Projeto A:** Framework base + leitura de PDF
- **Projeto B:** Framework base + integração com APIs externas
- **Projeto C:** Framework base + sistema de classificação personalizado
- **Projeto D:** Framework base + processamento de imagens
- **Projeto N:** Framework base + funcionalidades específicas

##  Estrutura do Framework

```
BackEnd_Teste/                    # FRAMEWORK BASE REUTILIZÁVEL
 docs/
    README.md                # Esta documentação
 tests/                       # Testes da infraestrutura base
 requirements.txt             # Dependências mínimas
 src/                        # Código fonte genérico
     infrastructure/         # Infraestrutura genérica
        config/
           config.py       # Sistema de configurações
        logging/
           logger_setup.py # Sistema de logging
        database/
            data_manager.py # CRUD genérico SQLite
            example.db      # Banco de exemplo
     presentation/           # Interface genérica
         api/
             api.py          # API REST básica
```

##  Como Usar o Framework

### **1. Para Desenvolvedores (Início de Projeto):**

```bash
# 1. Copie a estrutura do BackEnd_Teste
cp -r BackEnd_Teste MeuProjeto

# 2. Adapte as configurações em src/infrastructure/config/
# 3. Adicione suas funcionalidades específicas em:
#    - src/domain/ (regras de negócio)
#    - src/application/ (casos de uso)
#    - src/extensions/ (funcionalidades extras)

# 4. Mantenha compatibilidade com os imports básicos:
from infrastructure.config import config
from infrastructure.database import data_manager
from infrastructure.logging import logger_setup
```

### **2. Funcionalidades Garantidas:**

```python
# CRUD Básico (sempre disponível)
data_manager.create_record(table, data)
data_manager.read_records(table, filters)
data_manager.update_record(table, id, data) 
data_manager.delete_record(table, id)

# Configurações (sempre disponível)
config.DATABASE_PATH
config.LOG_LEVEL
config.API_PORT

# Logging (sempre disponível)
logger_setup.setup_logging()
```

##  Componentes Genéricos

### **Infrastructure Layer:**
- **config.py:** Sistema de configurações flexível
- **logger_setup.py:** Logging configurável 
- **data_manager.py:** CRUD genérico para SQLite

### **Presentation Layer:**
- **api.py:** Endpoints básicos (GET, POST, PUT, DELETE)

##  O que NÃO está no Framework

- Validações específicas de negócio
- Processamento de arquivos específicos  
- Orquestradores complexos
- Regras de domínio particulares
- Integrações específicas

##  Status de Implementação

### Framework Base:
- [ ] config.py - Sistema de configurações genérico
- [ ] logger_setup.py - Sistema de logging genérico
- [ ] data_manager.py - CRUD genérico SQLite
- [ ] api.py - API REST básica
- [ ] Testes da infraestrutura
- [ ] Documentação completa

---
**Última atualização:** 09 de Agosto de 2025
**Versão:** 1.0 (Framework Base)
