# Configurações do Backend - Framework DSB

## 🚀 Como iniciar o Backend

### 1. **Servidor Genérico (Para qualquer aplicação)**
```bash
cd c:\Applications_DSB\framework_dsb\backend
python server.py
```

### 2. **Servidor Específico do FinCtl**
```bash
cd c:\Applications_DSB\framework_dsb\backend
python server_finctl.py
```

## ⚙️ Variáveis de Ambiente (Opcional)

Para o servidor genérico, você pode configurar via variáveis de ambiente:

```bash
# Windows PowerShell
$env:APP_NAME="MeuApp"
$env:APP_VERSION="2.0.0"
$env:HOST="localhost"
$env:PORT="5001"
$env:DEBUG="True"
$env:DATABASE_PATH="meuapp.db"
python server.py
```

## 📋 Instâncias Criadas

### **Servidor Genérico (server.py)**
```python
# Instância da API Backend
api_backend = api_be()

# Configuração automática via ambiente ou padrões
api_backend.aplicacao = "Framework_DSB"  # ou $APP_NAME
api_backend.host = "localhost"           # ou $HOST
api_backend.porta = 5000                 # ou $PORT
api_backend.debug = True                 # ou $DEBUG
```

### **Servidor FinCtl (server_finctl.py)**
```python
# Instância específica para FinCtl
api_finctl_backend = api_be()

# Configuração específica do FinCtl
api_finctl_backend.aplicacao = "FinCtl"
api_finctl_backend.host = "localhost"
api_finctl_backend.porta = 5000
api_finctl_backend.debug = True
api_finctl_backend.database_path = "finctl_database.db"

# Gerenciador de banco específico
db_finctl = db_manager("finctl_database.db")
api_finctl_backend.db_manager = db_finctl
```

## 🗃️ Estrutura do Banco (FinCtl)

O servidor específico do FinCtl cria automaticamente:

### **Tabelas:**
- `tb_grupos_finctl` - Grupos de classificação
- `tb_subgrupos_finctl` - Subgrupos de classificação  
- `tb_lancamentos_finctl` - Lançamentos financeiros

### **Views:**
- `vw_grupos_finctl` - Visão completa dos grupos
- `vw_subgrupos_finctl` - Visão completa dos subgrupos
- `vw_lancamentos_finctl` - Visão completa dos lançamentos

### **Dados de Exemplo:**
- Grupos: Alimentação, Transporte, Moradia, Saúde, etc.
- Subgrupos: Supermercado, Combustível, Aluguel, etc.

## 🔗 Endpoints Disponíveis

Ambos os servidores expõem os mesmos endpoints:

- `POST /inserir` - Inserir dados
- `PUT /atualizar` - Atualizar dados
- `DELETE /excluir` - Excluir dados
- `GET /obter_view` - Obter dados de views

## 🎯 Resumo das Instanciações

| Componente | Arquivo | Instância | Configuração |
|------------|---------|-----------|--------------|
| **Backend Genérico** | `server.py` | `api_backend = api_be()` | Via ambiente ou padrão |
| **Backend FinCtl** | `server_finctl.py` | `api_finctl_backend = api_be()` | Específica FinCtl |
| **Frontend FinCtl** | `FinCtl/main.js` | `window.api_finctl = new api_fe()` | Global frontend |

## ✅ Para usar no FinCtl:

1. **Inicie o backend:**
   ```bash
   python server_finctl.py
   ```

2. **Abra o frontend:**
   ```bash
   # Sirva os arquivos do FinCtl via servidor web
   # Ou abra index.html no navegador
   ```

3. **A comunicação funcionará:**
   - Frontend: `window.api_finctl` → HTTP requests
   - Backend: `api_finctl_backend` → Database operations
