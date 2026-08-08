# ==================================================
# 🔹 BANCO.PY — CAMADA DE PERSISTÊNCIA
# ✅ Carrega / Salva Usuários e Ordens em JSON
# ✅ Cria pastas e arquivos padrão automaticamente
# ==================================================

import json
import os
from datetime import datetime

# 📁 CAMINHOS DOS ARQUIVOS
ARQUIVO_USUARIOS = "backlogday_usuarios.json"
ARQUIVO_DADOS = "backlogday_ordens.json"
PASTA_ANEXOS = "anexos_ordens"
PASTA_RELATORIOS = "relatorios_pdf"

# 🎨 Cores para mensagens
class Cores:
    CIANO = "\033[38;5;51m"
    VERDE = "\033[38;5;46m"
    AMARELO = "\033[38;5;226m"
    VERMELHO = "\033[38;5;196m"
    RESET = "\033[0m"

Co = Cores

# ==================================================
# 📂 CRIAR PASTAS NECESSÁRIAS
# ==================================================
def criar_pastas():
    """Cria as pastas de anexos e relatórios se não existirem"""
    try:
        if not os.path.exists(PASTA_ANEXOS):
            os.makedirs(PASTA_ANEXOS)
            print(f"{Co.VERDE}📂 Pasta '{PASTA_ANEXOS}' criada!{Co.RESET}")
        if not os.path.exists(PASTA_RELATORIOS):
            os.makedirs(PASTA_RELATORIOS)
            print(f"{Co.VERDE}📂 Pasta '{PASTA_RELATORIOS}' criada!{Co.RESET}")
        return True
    except Exception as e:
        print(f"{Co.VERMELHO_ERRO}❌ Erro ao criar pastas: {e}{Co.RESET}")
        return False

# ==================================================
# 💾 CARREGAR ARQUIVO JSON
# ==================================================
def carregar_arquivo(caminho_arquivo, valor_padrao=None):
    """
    Carrega um arquivo JSON. Retorna 'valor_padrao' se o arquivo não existir.
    """
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{Co.AMARELO}📭 Arquivo '{caminho_arquivo}' não encontrado. Usando padrão...{Co.RESET}")
        return valor_padrao if valor_padrao is not None else []
    except json.JSONDecodeError as e:
        print(f"{Co.VERMELHO}⚠️ Arquivo '{caminho_arquivo}' corrompido! Erro: {e}{Co.RESET}")
        return valor_padrao if valor_padrao is not None else []
    except Exception as e:
        print(f"{Co.VERMELHO}❌ Erro ao ler '{caminho_arquivo}': {e}{Co.RESET}")
        return valor_padrao if valor_padrao is not None else []

# ==================================================
# 💾 SALVAR ARQUIVO JSON
# ==================================================
def salvar_arquivo(caminho_arquivo, dados):
    """Salva dados em formato JSON com indentação legível"""
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4, default=str)
        return True
    except Exception as e:
        print(f"{Co.VERMELHO}❌ Erro ao salvar '{caminho_arquivo}': {e}{Co.RESET}")
        return False

# ==================================================
# 👤 USUÁRIOS — CARREGAR / SALVAR
# ==================================================
def carregar_usuarios():
    """Carrega a lista de usuários. Cria ADM padrão se vazio."""
    usuarios = carregar_arquivo(ARQUIVO_USUARIOS, [])
    
    # Cria ADM padrão se não houver usuários
    if not usuarios:
        print(f"{Co.AMARELO}⚙️ Nenhum usuário encontrado. Criando conta ADMINISTRADOR...{Co.RESET}")
        usuarios = [{"id": 1, "nome": "adm", "senha": "adm123", "nivel": 9}]
        if salvar_arquivo(ARQUIVO_USUARIOS, usuarios):
            print(f"{Co.VERDE}✅ Usuário padrão criado → adm / adm123{Co.RESET}")
    return usuarios

def salvar_usuarios(usuarios):
    """Salva a lista de usuários"""
    return salvar_arquivo(ARQUIVO_USUARIOS, usuarios)

# ==================================================
# 📋 ORDENS — CARREGAR / SALVAR
# ==================================================
def carregar_ordens():
    """Carrega a lista de ordens de manutenção"""
    return carregar_arquivo(ARQUIVO_DADOS, [])

def salvar_ordens(ordens):
    """Salva a lista de ordens de manutenção"""
    return salvar_arquivo(ARQUIVO_DADOS, ordens)

# ==================================================
# 🔍 BUSCAR FUNÇÕES AUXILIARES
# ==================================================
def proximo_id(lista):
    """Retorna o próximo ID disponível para cadastro"""
    if not lista:
        return 1
    return max(item.get("id", 0) for item in lista) + 1

# ==================================================
# ▶️ TESTE DO MÓDULO
# ==================================================
if __name__ == "__main__":
    print(f"{Co.CIANO}{'═'*50}{Co.RESET}")
    print(f"{Co.CIANO}   🧪 TESTE DO MÓDULO BANCO.PY{Co.RESET}")
    print(f"{Co.CIANO}{'═'*50}{Co.RESET}")
    
    criar_pastas()
    
    usuarios = carregar_usuarios()
    print(f"\n{Co.VERDE}✅ {len(usuarios)} usuário(s) carregado(s){Co.RESET}")
    
    ordens = carregar_ordens()
    print(f"{Co.VERDE}✅ {len(ordens)} ordem(ns) carregada(s){Co.RESET}")
    
    print(f"\n{Co.CIANO}🏁 Módulo funcionando corretamente!{Co.RESET}")
