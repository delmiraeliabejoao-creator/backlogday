# ==================================================
# 🔹 DADOS.PY — DADOS ESTÁTICOS E CONFIGURAÇÕES
# ✅ Máquinas, Cabeçotes, Itens de Inspeção
# ✅ Níveis de Acesso, Status, Permissões
# ✅ Paleta de Cores do Tema Futurista
# ==================================================

# ==================================================
# 🎨 TEMA FUTURISTA — PALETA DE CORES ANSI
# ==================================================
class Cores:
    """Paleta de cores para terminal — Tema Preto Futurista"""
    PRETO_FUNDO    = "\033[48;5;234m"
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
# 🔧 ITENS DE INSPEÇÃO — MÁQUINA BASE
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

# ==================================================
# 🔐 NÍVEIS DE ACESSO / CARGOS
# ==================================================
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

# ==================================================
# 📊 STATUS DAS ORDENS
# ==================================================
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
# 📋 PERMISSÕES POR NÍVEL
# ==================================================
PERMISSOES = {
    1: ["abrir_ordem", "ver_suas_ordens"],
    2: ["ver_aguardando_servico", "assumir_ordem", "solicitar_pecas", 
        "finalizar_ordem", "registrar_parada_maquina"],
    3: ["ver_aguardando_servico", "ver_solicitacoes_pecas", 
        "confirmar_recebimento_pecas", "registrar_materiais", "gerar_relatorio_pecas"],
    5: ["ver_todas_abertas_e_solicitacoes", "concluir_ordem_restrita", 
        "ver_todas_ordens", "ver_relatorios_pecas"],
    7: ["ver_todas_abertas_e_solicitacoes", "concluir_ordem_restrita", 
        "ver_todas_ordens", "ver_relatorios_pecas", "liberar_maquina"],
    8: ["ver_todas_abertas_e_solicitacoes", "concluir_ordem_TODOS_STATUS", 
        "liberar_maquina", "ver_todas_ordens", "ver_relatorios_pecas", "relatorios"],
    9: ["controle_total", "remover_ordem", "cadastrar_usuario", 
        "concluir_ordem_TODOS_STATUS", "liberar_maquina", "ver_todas_ordens", 
        "ver_relatorios_pecas", "relatorios"]
}

# ==================================================
# 🖼️ CABEÇALHO VISUAL
# ==================================================
def exibir_cabecalho_sistema():
    """Exibe o cabeçalho estilizado do sistema"""
    print(f"\n{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")
    print(f"{Co.AZUL_DESTAQUE}    🚜  BACKLOGDAY — SISTEMA DE GESTÃO DE MANUTENÇÃO  🪓{Co.RESET}")
    print(f"{Co.CINZA_SUAVE}    Máquinas Florestais · Cabeçotes · Unidades de Corte{Co.RESET}")
    print(f"{Co.VERDE_SUCESSO}    🌲 Colhedora Processadora · Cabeçote de Corte 🌲{Co.RESET}")
    print(f"{Co.CIANO_TITULO}{'═'*70}{Co.RESET}")

# ==================================================
# 📋 FUNÇÕES AUXILIARES DE ESCOLHA
# ==================================================
def escolher_maquina():
    """Exibe lista e retorna a máquina escolhida"""
    print(f"\n{Co.AZUL_DESTAQUE}🏭 MÁQUINAS CADASTRADAS:{Co.RESET}")
    for i, maq in enumerate(MAQUINAS, 1):
        print(f"   {Co.CIANO_TITULO}{i:2d}{Co.RESET} → {Co.BRANCO_TEXTO}{maq}{Co.RESET}")
    print(f"{Co.AZUL_DESTAQUE}─"*35 + Co.RESET)
    while True:
        try:
            op = int(input(f"{Co.CIANO_TITULO}▸ Escolha o NÚMERO da máquina: {Co.RESET}"))
            if 1 <= op <= len(MAQUINAS):
                return MAQUINAS[op - 1]
            print(f"{Co.AMARELO_ALERTA}⚠️ Digite entre 1 e {len(MAQUINAS)}!{Co.RESET}")
        except ValueError:
            print(f"{Co.VERMELHO_ERRO}⚠️ Apenas números!{Co.RESET}")

def escolher_cabecote():
    """Exibe lista e retorna o cabeçote escolhido ou 'Nenhum'"""
    print(f"\n{Co.AZUL_DESTAQUE}🏷️ CABEÇOTES CADASTRADOS:{Co.RESET}")
    print(f"   {Co.CIANO_TITULO} 0{Co.RESET} → {Co.BRANCO_TEXTO}Nenhum (Máquina Base){Co.RESET}")
    for i, cab in enumerate(CABECOTES, 1):
        print(f"   {Co.CIANO_TITULO}{i:2d}{Co.RESET} → {Co.BRANCO_TEXTO}{cab}{Co.RESET}")
    print(f"{Co.AZUL_DESTAQUE}─"*35 + Co.RESET)
    while True:
        try:
            op = int(input(f"{Co.CIANO_TITULO}▸ Escolha o NÚMERO do cabeçote: {Co.RESET}"))
            if op == 0:
                return "Nenhum"
            if 1 <= op <= len(CABECOTES):
                return CABECOTES[op - 1]
            print(f"{Co.AMARELO_ALERTA}⚠️ Digite entre 0 e {len(CABECOTES)}!{Co.RESET}")
        except ValueError:
            print(f"{Co.VERMELHO_ERRO}⚠️ Apenas números!{Co.RESET}")

def escolher_sistema_e_item(tem_cabecote):
    """Escolhe sistema e item conforme tipo de equipamento"""
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
# ▶️ TESTE DO MÓDULO
# ==================================================
if __name__ == "__main__":
    exibir_cabecalho_sistema()
    print(f"{Co.VERDE_SUCESSO}✅ Módulo dados carregado com sucesso!{Co.RESET}")
    print(f"{Co.CIANO_TITULO}   → {len(MAQUINAS)} Máquinas cadastradas{Co.RESET}")
    print(f"{Co.CIANO_TITULO}   → {len(CABECOTES)} Cabeçotes cadastrados{Co.RESET}")
    print(f"{Co.CIANO_TITULO}   → {len(NIVEIS)} Níveis de acesso{Co.RESET}")
    print(f"{Co.CIANO_TITULO}   → {len(STATUS)} Status de ordem{Co.RESET}")
