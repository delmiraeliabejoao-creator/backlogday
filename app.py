# ==================================================
# 🔹 SISTEMA BACKLOGDAY — VERSÃO COMPLETA FUTURISTA
# ✅ TEMA: Preto + Ciano/Azul/Verde Neon
# ✅ ITENS DE INSPEÇÃO: Máquina Base / Cabeçote (automático)
# ✅ Permissões por cargo + Relatório PDF
# ✅ Ilustrações: Máquinas florestais no cabeçalho
# ==================================================

import json
import os
from datetime import datetime
from fpdf import FPDF  # 📦 Instale com: pip install fpdf

# ==================================================
# 🎨 TEMA FUTURISTA — PALETA DE CORES
# ==================================================
class Cores:
    CIANO_TITULO   = "\033[38;5;51m"
    AZUL_DESTAQUE  = "\033[38;5;75m"
    VERDE_SUCESSO  = "\033[38;5;46m"
    AMARELO_ALERTA = "\033[38;5;226m"
    VERMELHO_ERRO  = "\033[38;5;196m"
    BRANCO_TEXTO   = "\033[38;5;255m"
    CINZA_SUAVE    = "\033[38;5;245m"
    RESET          = "\033[0m"

Co = Cores

# ==================================================
# 🖼️ CABEÇALHO VISUAL DO SISTEMA
# ==================================================
def exibir_cabecalho_sistema():
    print(f"\n{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")
    print(f"{Co.AZUL_DESTAQUE}    🚜  BACKLOGDAY — SISTEMA DE GESTÃO DE MANUTENÇÃO  🪓{Co.RESET}")
    print(f"{Co.CINZA_SUAVE}    Máquinas Florestais · Cabeçotes · Unidades de Corte{Co.RESET}")
    print(f"{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")
    print(f"{Co.VERDE_SUCESSO}    🌲 Representação visual: Colhedora + Cabeçote Processador 🌲{Co.RESET}")
    print(f"{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")

# ==================================================
# 🏭 MÁQUINAS CADASTRADAS
# ==================================================
MAQUINAS = [
    "HV-10105", "HV-10110", "HV-10111", "HV-10114", "HV-10116",
    "HV-10117", "HV-10119", "HV-10120", "HV-10121", "HV-10122",
    "HV-10123", "HV-10080", "HV-10089", "HV-19029", "HV-10164",
    "HV-10134"
]

# ==================================================
# 🏷️ CABEÇOTES CADASTRADOS
# ==================================================
CABECOTES = [
    "CB-12153", "CB-12158", "CB-10159", "CB-12163", "CB-12165",
    "CB-12166", "CB-12168", "CB-12169", "CB-12170", "CB-12171",
    "CB-12172", "CB-12144", "CB-12149", "CB-12214", "CB-12106",
    "CB-12173"
]

# ==================================================
# 🔧 ITENS DE INSPEÇÃO — MÁQUINA BASE (sem cabeçote)
# ==================================================
SISTEMAS_MAQUINA_BASE = {
    "MÁQUINA BASE": [
        "MOTOR", "RADIADOR DE ÁGUA", "RADIADOR DE ÓLEO", "CONDENSADOR",
        "PROTEÇÃO ANTICHAMAS MANG DIESEL", "BATERIAS", "MANGUEIRAS TANQUE DIESEL",
        "MANGUEIRAS LINHA SUCÇÃO AR", "ABRAÇADEIRA MANG FIL AR", "PROTEÇÃO MANG SUCÇÃO AR",
        "MANTA DO SILENCIOSO", "PROTEÇÃO DA TURBINA", "TURBINA", "VAZAMENTO MOTOR",
        "VAZAMENTO BOMBA DE ÁGUA", "BICO INJETOR", "CHICOTE ELÉTRICO", "ALTERNADOR",
        "MOTOR DE PARTIDA", "COXINS E PARAFUSOS", "TAMPA DO TANQUE"
    ],
    "GIRO": ["VAZAMENTO REDUTOR", "MANGUEIRAS", "SWIVEL"],
    "COMANDO HIDRÁULICO": [
        "PROTEÇÃO DO BRAÇO", "VAZAMENTO", "MANGUEIRAS",
        "CHICOTE ELÉTRICO", "CONECTORES", "VÁLVULAS/SOLENÓIDES"
    ],
    "SISTEMA DE LUBRIFICAÇÃO": ["CONEXÕES E MANGUEIRAS", "SISTEMA LINCOLN"],
    "TRANSMISSÃO": [
        "BOMBA HIDRÁULICA", "MANGUEIRAS", "MOTOR DE TRAÇÃO",
        "MANGUEIRAS MOTOR DE TRAÇÃO"
    ],
    "MATERIAL RODANTE": [
        "ROLETES SUP", "ROLETES INF", "PROTEÇÃO DOS ROLETES", "LINK/ SAPATA"
    ],
    "PROTEÇÕES": [
        "GRADES DA MÁQUINA", "FARÓIS", "ESCADA", "CABINE", "MOTOR",
        "CORRIMÃO", "GRUA", "EXTINTOR", "TAMPÃO INFERIOR DO H"
    ],
    "GRUA/BRAÇO/LANÇA": [
        "CILINDRO", "FOLGAS", "MANGUEIRAS", "TUBULAÇÃO",
        "DISTRIBUIÇÃO DE GRAXA", "PONTEIRA"
    ],
    "CABINE": [
        "CHAVE GERAL", "CHAVE DE PARTIDA", "FARÓIS DA CABINE",
        "LIMPADOR DO LEXAN", "CABOS/CONECTORES"
    ]
}

# ==================================================
# 🔧 ITENS DE INSPEÇÃO — CABEÇOTE
# ==================================================
SISTEMAS_CABECOTE = {
    "CABEÇOTE": ["ROTATOR", "MOTOR DO ROTATOR", "BIELA", "MANGUEIRAS"],
    "UNIDADE DE CORTE": [
        "SENSORES", "PROTEÇÃO DO SENSOR", "PLACA DO SABRE", "CILINDRO DO SABRE",
        "MOTOR DE SERRA", "TUBOS", "MANGUEIRAS", "CAIXA DE SERRA"
    ],
    "CHASSIS": [
        "CHASSIS", "CILINDRO DO TILT", "BATENTE DO TILT", "LINK",
        "MANGUEIRA LANÇA LINK", "SWIVEL MANG LANÇA LINK", "SUPORTE DO LINK", "CAPÔ"
    ],
    "ROLOS": [
        "MOTORES", "SUPORTE DO ROLO", "TAMPA PROTEÇÃO DO MOTOR", "MANGUEIRAS DO ROLO",
        "BRAÇADEIRA MANG ROLO", "SWIVEL MANG DO ROLO", "CAPA DOS ROLOS", "CAMES",
        "ROLAMENTO", "ARTICULADORES", "CILINDRO", "ROLO DO DORSO"
    ],
    "FACAS": [
        "CILINDROS", "FACA SUP ESQ", "FACA SUP DIR", "FACA INF ESQ",
        "FACA INF DIR", "FACA FIXAS", "MANGUEIRAS"
    ],
    "COMANDO": [
        "SUPORTE", "CHICOTE", "CONECTORES", "VÁLVULAS/SOLENÓIDES",
        "VAZAMENTO", "MANG LINK AO COMANDO", "MÓDULO ELETRÔNICO (MHC)"
    ]
}

# 📁 ARQUIVOS E PASTAS
ARQUIVO_USUARIOS = "backlogday_usuarios.json"
ARQUIVO_DADOS = "backlogday_ordens.json"
PASTA_ANEXOS = "anexos_ordens"
PASTA_RELATORIOS = "relatorios_pdf"

# 🔐 NÍVEIS DE ACESSO
NIVEIS = {
    1: "Operador",
    2: "Mecânico",
    3: "Almoxarifado",
    4: "Inspetor",
    5: "Supervisor de Manutenção",
    6: "Supervisor de Operação",
    7: "Coordenador",
    8: "Gerente",
    9: "ADMINISTRADOR"
}

# 📊 STATUS DAS ORDENS
STATUS = {
    1: "⏳ AGUARDANDO SERVIÇO",
    2: "🔧 EM MANUTENÇÃO",
    3: "⏳ AGUARDANDO PEÇA",
    4: "📦 PEÇA PARA RETIRADA",
    5: "⏳ AGUARDANDO FINALIZAÇÃO",
    6: "✅ ORDEM CONCLUÍDA",
    7: "🚧 MÁQUINA PARADA",
    8: "✅ MÁQUINA LIBERADA"
}

# ==================================================
# 💾 FUNÇÕES DE DADOS
# ==================================================
def carregar_arquivo(arquivo, padrao):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return padrao

def salvar_arquivo(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def criar_pastas():
    if not os.path.exists(PASTA_ANEXOS): os.makedirs(PASTA_ANEXOS)
    if not os.path.exists(PASTA_RELATORIOS): os.makedirs(PASTA_RELATORIOS)

# ==================================================
# 📋 ESCOLHA DE MÁQUINA / CABEÇOTE / SISTEMA / ITEM
# ==================================================
def escolher_maquina():
    print(f"\n{Co.AZUL_DESTAQUE}🏭 MÁQUINAS CADASTRADAS:{Co.RESET}")
    for i, maq in enumerate(MAQUINAS, 1):
        print(f"   {Co.CIANO_TITULO}{i:2d}{Co.RESET} → {Co.BRANCO_TEXTO}{maq}{Co.RESET}")
    print(f"{Co.AZUL_DESTAQUE}─"*35 + Co.RESET)
    while True:
        try:
            op = int(input(f"{Co.CIANO_TITULO}▸ Escolha o NÚMERO da máquina: {Co.RESET}"))
            if 1 <= op <= len(MAQUINAS): return MAQUINAS[op - 1]
            print(f"{Co.AMARELO_ALERTA}⚠️ Digite entre 1 e {len(MAQUINAS)}!{Co.RESET}")
        except ValueError:
            print(f"{Co.VERMELHO_ERRO}⚠️ Apenas números!{Co.RESET}")

def escolher_cabecote():
    print(f"\n{Co.AZUL_DESTAQUE}🏷️ CABEÇOTES CADASTRADOS:{Co.RESET}")
    print(f"   {Co.CIANO_TITULO} 0{Co.RESET} → {Co.BRANCO_TEXTO}Nenhum (Máquina Base){Co.RESET}")
    for i, cab in enumerate(CABECOTES, 1):
        print(f"   {Co.CIANO_TITULO}{i:2d}{Co.RESET} → {Co.BRANCO_TEXTO}{cab}{Co.RESET}")
    print(f"{Co.AZUL_DESTAQUE}─"*35 + Co.RESET)
    while True:
        try:
            op = int(input(f"{Co.CIANO_TITULO}▸ Escolha o NÚMERO do cabeçote: {Co.RESET}"))
            if op == 0: return "Nenhum"
            if 1 <= op <= len(CABECOTES): return CABECOTES[op - 1]
            print(f"{Co.AMARELO_ALERTA}⚠️ Digite entre 0 e {len(CABECOTES)}!{Co.RESET}")
        except ValueError:
            print(f"{Co.VERMELHO_ERRO}⚠️ Apenas números!{Co.RESET}")

def escolher_sistema_e_item(tem_cabecote):
    sistemas = SISTEMAS_CABECOTE if tem_cabecote else SISTEMAS_MAQUINA_BASE
    titulo = "🔧 SISTEMAS DO CABEÇOTE" if tem_cabecote else "🔧 SISTEMAS DA MÁQUINA BASE"
    lista = list(sistemas.keys())

    print(f"\n{Co.AZUL_DESTAQUE}{titulo}:{Co.RESET}")
    for i, s in enumerate(lista, 1):
        print(f"   {Co.CIANO_TITULO}{i:2d}{Co.RESET} → {Co.BRANCO_TEXTO}{s}{Co.RESET}")
    print(f"{Co.AZUL_DESTAQUE}─"*35 + Co.RESET)

    while True:
        try:
            op_s = int(input(f"{Co.CIANO_TITULO}▸ Escolha o NÚMERO do SISTEMA: {Co.RESET}"))
            if 1 <= op_s <= len(lista):
                sistema = lista[op_s - 1]
                break
            print(f"{Co.AMARELO_ALERTA}⚠️ Digite entre 1 e {len(lista)}!{Co.RESET}")
        except ValueError:
            print(f"{Co.VERMELHO_ERRO}⚠️ Apenas números!{Co.RESET}")

    itens = sistemas[sistema]
    print(f"\n{Co.AZUL_DESTAQUE}🔧 ITENS — {sistema}:{Co.RESET}")
    for i, item in enumerate(itens, 1):
        print(f"   {Co.CIANO_TITULO}{i:2d}{Co.RESET} → {Co.BRANCO_TEXTO}{item}{Co.RESET}")
    print(f"{Co.AZUL_DESTAQUE}─"*35 + Co.RESET)

    while True:
        try:
            op_i = int(input(f"{Co.CIANO_TITULO}▸ Escolha o NÚMERO do ITEM: {Co.RESET}"))
            if 1 <= op_i <= len(itens):
                return sistema, itens[op_i - 1]
            print(f"{Co.AMARELO_ALERTA}⚠️ Digite entre 1 e {len(itens)}!{Co.RESET}")
        except ValueError:
            print(f"{Co.VERMELHO_ERRO}⚠️ Apenas números!{Co.RESET}")

# ==================================================
# 🔐 LOGIN E CADASTRO DE USUÁRIOS
# ==================================================
def cadastrar_usuario(usuarios, nome, senha, nivel):
    for u in usuarios:
        if u["nome"].strip().lower() == nome.strip().lower():
            print(f"{Co.AMARELO_ALERTA}⚠️ Usuário '{nome}' já existe!{Co.RESET}")
            return False
    usuarios.append({"id": len(usuarios)+1, "nome": nome.strip(), "senha": senha, "nivel": nivel})
    salvar_arquivo(ARQUIVO_USUARIOS, usuarios)
    print(f"{Co.VERDE_SUCESSO}✅ Usuário '{nome}' cadastrado como {NIVEIS[nivel]}!{Co.RESET}")
    return True

def login(usuarios):
    exibir_cabecalho_sistema()
    print(f"{Co.CIANO_TITULO}   🔐  TELA DE ACESSO{Co.RESET}")
    print(f"{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")
    nome = input(f"{Co.BRANCO_TEXTO}▸ Usuário: {Co.RESET}")
    senha = input(f"{Co.BRANCO_TEXTO}▸ Senha:   {Co.RESET}")
    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print(f"\n{Co.VERDE_SUCESSO}   ✅ ACESSO CONCEDIDO → {nome}{Co.RESET}")
            print(f"   {Co.CIANO_TITULO}▸ Perfil: {NIVEIS[u['nivel']]}{Co.RESET}")
            return u
    print(f"{Co.VERMELHO_ERRO}   ❌ Usuário ou senha inválidos!{Co.RESET}")
    return None

# ==================================================
# 📦 RELATÓRIO DE PEÇAS — PDF
# ==================================================
def gerar_relatorio_pecas(ordens, usuario):
    data_relatorio = datetime.now().strftime("%d/%m/%Y %H:%M")
    data_arquivo = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"{PASTA_RELATORIOS}/relatorio_pecas_{data_arquivo}.pdf"
    solicitacoes = [o for o in ordens if o.get("solicitacao_pecas")]

    if not solicitacoes:
        print(f"{Co.CINZA_SUAVE}📭 Nenhuma solicitação de peças encontrada.{Co.RESET}")
        return

    try:
        pdf = FPDF("P", "mm", "A4")
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "RELATÓRIO DE SOLICITAÇÕES DE PEÇAS", ln=True, align="C")
        pdf.set_font("Arial", "", 10)
        pdf.cell(0, 6, f"Data: {data_relatorio} | Por: {usuario['nome']} ({NIVEIS[usuario['nivel']]})", ln=True, align="C")
        pdf.ln(8)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(25, 7, "Ordem", border=1)
        pdf.cell(30, 7, "Máquina", border=1)
        pdf.cell(30, 7, "Cabeçote", border=1)
        pdf.cell(45, 7, "Sistema/Item", border=1)
        pdf.cell(55, 7, "Peças Solicitadas", border=1)
        pdf.cell(25, 7, "Status", border=1, ln=True)
        pdf.set_font("Arial", "", 9)
        for o in solicitacoes:
            status_texto = STATUS[o["status"]].split(" ", 1)[-1] if " " in STATUS[o["status"]] else STATUS[o["status"]]
            pdf.cell(25, 7, f"#{o['id']}", border=1)
            pdf.cell(30, 7, o["maquina"], border=1)
            pdf.cell(30, 7, o.get("cabecote", "---"), border=1)
            pdf.cell(45, 7, f"{o.get('sistema','---')[:15]} / {o.get('item','---')[:15]}", border=1)
            pecas_resumo = o["solicitacao_pecas"][:45] + ("..." if len(o["solicitacao_pecas"])>45 else "")
            pdf.cell(55, 7, pecas_resumo, border=1)
            pdf.cell(25, 7, status_texto, border=1, ln=True)
        pdf.output(nome_arquivo)
        print(f"{Co.VERDE_SUCESSO}✅ Relatório gerado: {nome_arquivo}{Co.RESET}")
    except Exception as e:
        print(f"{Co.VERMELHO_ERRO}❌ Erro ao gerar PDF: {e}{Co.RESET}")

# ==================================================
# 📝 FUNÇÕES DE ORDENS
# ==================================================
def abrir_ordem(ordens, operador, titulo, descricao, maquina, cabecote, sistema, item, anexos=""):
    nova = {
        "id": len(ordens)+1, "titulo": titulo, "descricao": descricao,
        "maquina": maquina, "cabecote": cabecote, "sistema": sistema, "item": item,
        "status": 1, "solicitante_id": operador["id"], "solicitante_nome": operador["nome"],
        "data_abertura": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "anexos_abertura": anexos, "responsavel_nome": None, "data_inicio": None,
        "solicitacao_pecas": "", "data_solicitacao_pecas": "", "data_recebimento_pecas": "",
        "data_finalizacao_mecanico": None, "observacao_execucao": "", "anexos_execucao": "",
        "materiais_utilizados": "", "data_registro_materiais": "",
        "data_conclusao_supervisor": None, "observacao_conclusao_supervisor": "",
        "data_parada_maquina": "", "motivo_parada": "", "data_liberacao_maquina": "",
        "observacao_liberacao": "", "liberado_por": ""
    }
    ordens.append(nova)
    salvar_arquivo(ARQUIVO_DADOS, ordens)
    print(f"\n{Co.VERDE_SUCESSO}══════════════════════════════════════════════{Co.RESET}")
    print(f"{Co.VERDE_SUCESSO}✅ ORDEM #{nova['id']} ABERTA COM SUCESSO{Co.RESET}")
    print(f"{Co.CIANO_TITULO}▸ Máquina: {Co.BRANCO_TEXTO}{maquina}{Co.RESET}  |  {Co.CIANO_TITULO}Cabeçote: {Co.BRANCO_TEXTO}{cabecote}{Co.RESET}")
    print(f"{Co.CIANO_TITULO}▸ Sistema: {Co.BRANCO_TEXTO}{sistema}{Co.RESET}  ·  Item: {Co.BRANCO_TEXTO}{item}{Co.RESET}")
    print(f"{Co.CIANO_TITULO}▸ Status: {Co.BRANCO_TEXTO}{STATUS[1]}{Co.RESET}")
    print(f"{Co.VERDE_SUCESSO}══════════════════════════════════════════════{Co.RESET}")

def assumir_ordem(ordens, mecanico, id_o):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] != 1:
                print(f"{Co.AMARELO_ALERTA}⚠️ Ordem #{id_o} não está disponível!{Co.RESET}"); return
            o["status"] = 2; o["responsavel_nome"] = mecanico["nome"]
            o["data_inicio"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            salvar_arquivo(ARQUIVO_DADOS, ordens)
            print(f"{Co.VERDE_SUCESSO}✅ Ordem #{id_o} assumida → {STATUS[2]}{Co.RESET}")
            return
    print(f"{Co.VERMELHO_ERRO}❌ Ordem #{id_o} não encontrada!{Co.RESET}")

def solicitar_pecas(ordens, mecanico, id_o, pecas):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] != 2:
                print(f"{Co.AMARELO_ALERTA}⚠️ Ordem #{id_o} não está em manutenção!{Co.RESET}"); return
            o["solicitacao_pecas"] = pecas
            o["data_solicitacao_pecas"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["status"] = 3
            salvar_arquivo(ARQUIVO_DADOS, ordens)
            print(f"{Co.VERDE_SUCESSO}✅ Peças solicitadas → {STATUS[3]}{Co.RESET}")
            return
    print(f"{Co.VERMELHO_ERRO}❌ Ordem #{id_o} não encontrada!{Co.RESET}")

def confirmar_recebimento_pecas(ordens, almoxarifado, id_o):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] != 3:
                print(f"{Co.AMARELO_ALERTA}⚠️ Ordem #{id_o} não aguardando peça!{Co.RESET}"); return
            o["status"] = 4; o["data_recebimento_pecas"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            salvar_arquivo(ARQUIVO_DADOS, ordens)
            print(f"{Co.VERDE_SUCESSO}✅ Peças recebidas → {STATUS[4]}{Co.RESET}")
            return
    print(f"{Co.VERMELHO_ERRO}❌ Ordem #{id_o} não encontrada!{Co.RESET}")

def registrar_materiais(ordens, almoxarifado, id_o, materiais):
    for o in ordens:
        if o["id"] == id_o:
            o["materiais_utilizados"] = materiais
            o["data_registro_materiais"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            salvar_arquivo(ARQUIVO_DADOS, ordens)
            print(f"{Co.VERDE_SUCESSO}✅ Materiais registrados na Ordem #{id_o}{Co.RESET}")
            return
    print(f"{Co.VERMELHO_ERRO}❌ Ordem #{id_o} não encontrada!{Co.RESET}")

def registrar_parada_maquina(ordens, mecanico, id_o, motivo):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] in [6,7,8]:
                print(f"{Co.AMARELO_ALERTA}⚠️ Ordem já fechada/parada!{Co.RESET}"); return
            o["status"] = 7; o["data_parada_maquina"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["motivo_parada"] = motivo
            salvar_arquivo(ARQUIVO_DADOS, ordens)
            print(f"{Co.AMARELO_ALERTA}🚧 MÁQUINA PARADA registrada!{Co.RESET}")
            return
    print(f"{Co.VERMELHO_ERRO}❌ Ordem #{id_o} não encontrada!{Co.RESET}")

def liberar_maquina_para_operacao(ordens, usuario, id_o, observacao=""):
    if usuario["nivel"] not in [7,8,9]:
        print(f"{Co.VERMELHO_ERRO}❌ Sem permissão! Apenas Coordenador/Gerente/ADM.{Co.RESET}"); return
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] != 7:
                print(f"{Co.AMARELO_ALERTA}⚠️ Máquina não está parada!{Co.RESET}"); return
            o["status"] = 8; o["data_liberacao_maquina"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["observacao_liberacao"] = observacao; o["liberado_por"] = usuario["nome"]
            salvar_arquivo(ARQUIVO_DADOS, ordens)
            print(f"{Co.VERDE_SUCESSO}✅ MÁQUINA LIBERADA por {usuario['nome']}{Co.RESET}")
            return
    print(f"{Co.VERMELHO_ERRO}❌ Ordem #{id_o} não encontrada!{Co.RESET}")

def finalizar_ordem_mecanico(ordens, mecanico, id_o, observacao, anexos_execucao):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] == 7:
                print(f"{Co.AMARELO_ALERTA}⚠️ Ordem parada — aguarde liberação!{Co.RESET}"); return
            if o["status"] < 4:
                print(f"{Co.AMARELO_ALERTA}⚠️ Peças pendentes!{Co.RESET}"); return
            o["status"] = 5; o["data_finalizacao_mecanico"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["observacao_execucao"] = observacao; o["anexos_execucao"] = anexos_execucao
            salvar_arquivo(ARQUIVO_DADOS, ordens)
            print(f"{Co.VERDE_SUCESSO}✅ Enviada para conferência → {STATUS[5]}{Co.RESET}")
            return
    print(f"{Co.VERMELHO_ERRO}❌ Ordem #{id_o} não encontrada!{Co.RESET}")

def concluir_ordem_supervisor(ordens, usuario, id_o, observacao=""):
    pode_todos = usuario["nivel"] in [8,9]
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] == 7:
                print(f"{Co.AMARELO_ALERTA}⚠️ Ordem parada — liberação primeiro!{Co.RESET}"); return
            if not pode_todos and o["status"] != 5:
                print(f"{Co.AMARELO_ALERTA}⚠️ Apenas GERENTE/ADM fecham em qualquer status!{Co.RESET}"); return
            o["status"] = 6; o["data_conclusao_supervisor"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["observacao_conclusao_supervisor"] = observacao
            salvar_arquivo(ARQUIVO_DADOS, ordens)
            print(f"{Co.VERDE_SUCESSO}✅ ORDEM CONCLUÍDA por {usuario['nome']} ({NIVEIS[usuario['nivel']]}){Co.RESET}")
            return
    print(f"{Co.VERMELHO_ERRO}❌ Ordem #{id_o} não encontrada!{Co.RESET}")

def listar_ordens(ordens, usuario):
    print(f"\n{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")
    print(f"{Co.CIANO_TITULO}   📋 LISTA DE ORDENS — {NIVEIS[usuario['nivel']].upper()}{Co.RESET}")
    print(f"{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")
    if not ordens:
        print(f"{Co.CINZA_SUAVE}   📭 Nenhuma ordem cadastrada.{Co.RESET}"); return
    encontrou = False
    for o in ordens:
        exibir = False
        if usuario["nivel"] == 1: exibir = o["solicitante_id"] == usuario["id"]
        elif usuario["nivel"] == 2: exibir = o["status"] == 1 or o["responsavel_nome"] == usuario["nome"]
        elif usuario["nivel"] == 3: exibir = o["status"] in (1,3)
        else: exibir = True
        if not exibir: continue
        encontrou = True
        icones = {1:"⏳",2:"🔧",3:"⏳",4:"📦",5:"⏳",6:"✅",7:"🚧",8:"✅"}[o["status"]]
        print(f"\n{Co.AZUL_DESTAQUE}{icones} ORDEM #{o['id']}{Co.RESET}  {Co.BRANCO_TEXTO}{STATUS[o['status']]}{Co.RESET}")
        print(f"   {Co.CIANO_TITULO}▸ Máquina:{Co.RESET} {o['maquina']}  |  {Co.CIANO_TITULO}Cabeçote:{Co.RESET} {o.get('cabecote','---')}")
        print(f"   {Co.CIANO_TITULO}▸ Sistema:{Co.RESET} {o.get('sistema','---')}  ·  Item: {o.get('item','---')}")
        print(f"   {Co.CIANO_TITULO}▸ Solicitante:{Co.RESET} {o['solicitante_nome']}  ·  {Co.CIANO_TITULO}Abertura:{Co.RESET} {o['data_abertura']}")
        if o.get("solicitacao_pecas"): print(f"   {Co.CIANO_TITULO}▸ Peças:{Co.RESET} {o['solicitacao_pecas']}")
        if o["status"] == 7: print(f"   {Co.AMARELO_ALERTA}▸ Motivo Parada:{Co.RESET} {o.get('motivo_parada','---')}")
        if o["status"] == 8: print(f"   {Co.VERDE_SUCESSO}▸ Liberado por:{Co.RESET} {o.get('liberado_por','---')}")
        if o["status"] == 6: print(f"   {Co.VERDE_SUCESSO}▸ Concluído:{Co.RESET} {o.get('data_conclusao_supervisor','---')}")
    if not encontrou:
        print(f"{Co.CINZA_SUAVE}   📭 Nenhuma ordem disponível.{Co.RESET}")

def remover_ordem(ordens, usuario, id_o):
    if usuario["nivel"] != 9:
        print(f"{Co.VERMELHO_ERRO}❌ Apenas ADM exclui ordens!{Co.RESET}"); return
    for i, o in enumerate(ordens):
        if o["id"] == id_o:
            ordens.pop(i); salvar_arquivo(ARQUIVO_DADOS, ordens)
            print(f"{Co.VERDE_SUCESSO}🗑️ Ordem #{id_o} REMOVIDA!{Co.RESET}"); return
    print(f"{Co.VERMELHO_ERRO}❌ Ordem #{id_o} não encontrada!{Co.RESET}")

# ==================================================
# 🚀 MENU PRINCIPAL
# ==================================================
def menu():
    criar_pastas()
    usuarios = carregar_arquivo(ARQUIVO_USUARIOS, [])
    ordens = carregar_arquivo(ARQUIVO_DADOS, [])

    # Criar ADM padrão se não houver usuários
    if not usuarios:
        print(f"{Co.AMARELO_ALERTA}⚙️ Criando conta ADMINISTRADOR padrão...{Co.RESET}")
        usuarios.append({"id":1,"nome":"adm","senha":"adm123","nivel":9})
        salvar_arquivo(ARQUIVO_USUARIOS, usuarios)
        print(f"{Co.VERDE_SUCESSO}✅ Usuário: adm  |  Senha: adm123  |  Nível: ADMINISTRADOR{Co.RESET}")

    # Tela de Login
    usuario_logado = None
    while not usuario_logado:
        usuario_logado = login(usuarios)
        if not usuario_logado:
            input(f"\n{Co.CINZA_SUAVE}Pressione ENTER para tentar novamente...{Co.RESET}")

    # Loop Principal
    while True:
        cargo = NIVEIS[usuario_logado["nivel"]]
        print(f"\n{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")
        print(f"{Co.CIANO_TITULO}   🚀 PAINEL PRINCIPAL · {usuario_logado['nome']} · {cargo}{Co.RESET}")
        print(f"{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")

        n = usuario_logado["nivel"]
        opcoes = []
        if n == 1:
            opcoes = ["📝 Abrir Ordem de Manutenção", "📄 Minhas Ordens"]
        elif n == 2:
            opcoes = ["🔧 Assumir Ordem", "📋 Solicitar Peças", "🚧 Registrar Parada de Máquina", "⏳ Finalizar Ordem", "📄 Listar Ordens"]
        elif n == 3:
            opcoes = ["✅ Confirmar Recebimento de Peças", "📦 Registrar Materiais", "📊 Gerar Relatório de Peças (PDF)", "📄 Listar Ordens"]
        elif n == 5:
            opcoes = ["✅ Concluir Ordem", "📄 Listar Ordens"]
        elif n == 7:
            opcoes = ["✅ Concluir Ordem", "🔓 Liberar Máquina", "📄 Listar Ordens"]
        elif n == 8:
            opcoes = ["✅ Concluir QUALQUER Ordem", "🔓 Liberar Máquina", "📄 Listar Ordens"]
        elif n == 9:
            opcoes = ["✅ Concluir QUALQUER Ordem", "🔓 Liberar Máquina", "📄 Listar Ordens", "🗑️ Excluir Ordem", "👤 Cadastrar Novo Usuário", "📊 Relatório Geral"]

        for i, txt in enumerate(opcoes, 1):
            print(f"   {Co.AZUL_DESTAQUE}{i}.{Co.RESET} {txt}")
        print(f"   {Co.AZUL_DESTAQUE}0.{Co.RESET} 🚪 Sair do Sistema")
        escolha = input(f"\n{Co.CIANO_TITULO}▸ Selecione uma opção: {Co.RESET}")

        def pedir_id():
            try: return int(input(f"{Co.CIANO_TITULO}▸ Número da Ordem: {Co.RESET}"))
            except: print(f"{Co.VERMELHO_ERRO}⚠️ Digite um número válido!{Co.RESET}"); return None

        # ══════════════ OPÇÃO 1 ══════════════
        if escolha == "1":
            if n == 1:
                print(f"\n{Co.AZUL_DESTAQUE}📝 ABRIR NOVA ORDEM DE MANUTENÇÃO{Co.RESET}")
                titulo = input(f"{Co.BRANCO_TEXTO}▸ Título / Assunto: {Co.RESET}")
                descricao = input(f"{Co.BRANCO_TEXTO}▸ Descreva o problema: {Co.RESET}")
                maquina = escolher_maquina()
                cabecote = escolher_cabecote()
                tem_cab = (cabecote != "Nenhum")
                sistema, item = escolher_sistema_e_item(tem_cab)
                anexos = input(f"{Co.BRANCO_TEXTO}▸ Anexos / Observações (opcional): {Co.RESET}")
                abrir_ordem(ordens, usuario_logado, titulo, descricao, maquina, cabecote, sistema, item, anexos)

            elif n == 2:
                id_o = pedir_id()
                if id_o: assumir_ordem(ordens, usuario_logado, id_o)

            elif n in (3,5,7,8,9):
                id_o = pedir_id()
                if id_o:
                    obs = input(f"{Co.BRANCO_TEXTO}▸ Observações de conclusão (opcional): {Co.RESET}")
                    concluir_ordem_supervisor(ordens, usuario_logado, id_o, obs)

        # ══════════════ OPÇÃO 2 ══════════════
        elif escolha == "2":
            if n == 2:
                id_o = pedir_id()
                if id_o:
                    pecas = input(f"{Co.BRANCO_TEXTO}▸ Peças e quantidades: {Co.RESET}")
                    solicitar_pecas(ordens, usuario_logado, id_o, pecas)

            elif n == 3:
                id_o = pedir_id()
                if id_o: confirmar_recebimento_pecas(ordens, usuario_logado, id_o)

            elif n in (7,8,9):
                id_o = pedir_id()
                if id_o:
                    obs = input(f"{Co.BRANCO_TEXTO}▸ Observações de liberação (opcional): {Co.RESET}")
                    liberar_maquina_para_operacao(ordens, usuario_logado, id_o, obs)

        # ══════════════ OPÇÃO 3 ══════════════
        elif escolha == "3":
            if n == 2:
                id_o = pedir_id()
                if id_o:
                    motivo = input(f"{Co.BRANCO_TEXTO}▸ Motivo da parada: {Co.RESET}")
                    registrar_parada_maquina(ordens, usuario_logado, id_o, motivo)

            elif n == 3:
                id_o = pedir_id()
                if id_o:
                    mat = input(f"{Co.BRANCO_TEXTO}▸ Materiais utilizados: {Co.RESET}")
                    registrar_materiais(ordens, usuario_logado, id_o, mat)

            elif n in (5,7,8,9):
                listar_ordens(ordens, usuario_logado)

        # ══════════════ OPÇÃO 4 ══════════════
        elif escolha == "4":
            if n == 2:
                id_o = pedir_id()
                if id_o:
                    obs = input(f"{Co.BRANCO_TEXTO}▸ Observações de execução: {Co.RESET}")
                    anex = input(f"{Co.BRANCO_TEXTO}▸ Anexos (opcional): {Co.RESET}")
                    finalizar_ordem_mecanico(ordens, usuario_logado, id_o, obs, anex)

            elif n == 3:
                gerar_relatorio_pecas(ordens, usuario_logado)

            elif n == 9:
                id_o = pedir_id()
                if id_o: remover_ordem(ordens, usuario_logado, id_o)

        # ══════════════ OPÇÃO 5 ══════════════
        elif escolha == "5":
            if n == 2:
                listar_ordens(ordens, usuario_logado)

            elif n == 9:
                print(f"\n{Co.CIANO_TITULO}👤 CADASTRAR NOVO USUÁRIO{Co.RESET}")
                nome = input(f"{Co.BRANCO_TEXTO}▸ Nome do usuário: {Co.RESET}")
                senha = input(f"{Co.BRANCO_TEXTO}▸ Senha: {Co.RESET}")
                print(f"{Co.CINZA_SUAVE}Níveis: 1=Op 2=Mec 3=Alm 4=Insp 5=SupMan 6=SupOp 7=Coord 8=Ger 9=ADM{Co.RESET}")
                try:
                    nivel = int(input(f"{Co.BRANCO_TEXTO}▸ Nível de acesso: {Co.RESET}"))
                    cadastrar_usuario(usuarios, nome, senha, nivel)
                except:
                    print(f"{Co.VERMELHO_ERRO}⚠️ Nível inválido!{Co.RESET}")

        # ══════════════ OPÇÃO 6 ══════════════
        elif escolha == "6" and n == 9:
            total = len(ordens)
            print(f"\n{Co.CIANO_TITULO}📊 RELATÓRIO GERAL{Co.RESET}")
            print(f"   {Co.CIANO_TITULO}Total de Ordens:{Co.RESET} {Co.BRANCO_TEXTO}{total}{Co.RESET}")
            for s in STATUS:
                qtd = sum(1 for o in ordens if o["status"] == s)
                if qtd > 0:
                    print(f"   {Co.AZUL_DESTAQUE}{STATUS[s]}{Co.RESET}: {Co.BRANCO_TEXTO}{qtd}{Co.RESET}")

        # ══════════════ OPÇÃO 0 ══════════════
        elif escolha == "0":
            print(f"\n{Co.VERDE_SUCESSO}👋 Encerrando sessão... Até logo!{Co.RESET}"); break

        # ══════════════ LISTAR ORDENS (demais opções) ══════════════
        elif escolha in ("2","3","4","5") and n in (1,3,5):
            listar_ordens(ordens, usuario_logado)

        else:
            print(f"{Co.VERMELHO_ERRO}⚠️ Opção inválida! Tente novamente.{Co.RESET}")

# ==================================================
# ▶️ INICIAR SISTEMA
# ==================================================
if __name__ == "__main__":
    os.system("")  # Habilita cores ANSI no Windows
    menu()
