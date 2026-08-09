# ==================================================
# 🔹 app.py — PRINCIPAL · SEM CORES · SEM TELA ESCURA
# ==================================================

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from banco import (
    criar_pastas, carregar_usuarios, salvar_usuarios,
    carregar_ordens, salvar_ordens
)
from dados import (
    NIVEIS, STATUS, exibir_cabecalho_sistema,
    escolher_maquina, escolher_cabecote, escolher_sistema_e_item
)

import os
from datetime import datetime
from fpdf import FPDF

# RELATORIO PDF
def gerar_relatorio_pecas(ordens, usuario):
    data_relatorio = datetime.now().strftime("%d/%m/%Y %H:%M")
    data_arquivo = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"relatorios_pdf/relatorio_pecas_{data_arquivo}.pdf"
    solicitacoes = [o for o in ordens if o.get("solicitacao_pecas")]
    if not solicitacoes:
        print("  Nenhuma solicitacao de pecas.")
        return
    try:
        pdf = FPDF("P", "mm", "A4")
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "RELATORIO DE SOLICITACOES DE PECAS", ln=True, align="C")
        pdf.set_font("Arial", "", 10)
        pdf.cell(0, 6, f"Data: {data_relatorio} | Por: {usuario['nome']} ({NIVEIS[usuario['nivel']]})", ln=True, align="C")
        pdf.ln(8)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(25, 7, "Ordem", border=1)
        pdf.cell(30, 7, "Maquina", border=1)
        pdf.cell(30, 7, "Cabecote", border=1)
        pdf.cell(45, 7, "Sistema/Item", border=1)
        pdf.cell(55, 7, "Pecas Solicitadas", border=1)
        pdf.cell(25, 7, "Status", border=1, ln=True)
        pdf.set_font("Arial", "", 9)
        for o in solicitacoes:
            status_texto = STATUS[o["status"]].split(" ", 1)[-1] if " " in STATUS[o["status"]] else STATUS[o["status"]]
            pdf.cell(25, 7, f"#{o['id']}", border=1)
            pdf.cell(30, 7, o["maquina"], border=1)
            pdf.cell(30, 7, o.get("cabecote", "---"), border=1)
            pdf.cell(45, 7, f"{o.get('sistema','---')[:15]} / {o.get('item','---')[:15]}", border=1)
            resumo = o["solicitacao_pecas"][:45] + ("..." if len(o["solicitacao_pecas"])>45 else "")
            pdf.cell(55, 7, resumo, border=1)
            pdf.cell(25, 7, status_texto, border=1, ln=True)
        pdf.output(nome_arquivo)
        print(f"  Relatorio gerado: {nome_arquivo}")
    except Exception as e:
        print(f"  Erro ao gerar PDF: {e}")

# LOGIN E CADASTRO
def cadastrar_usuario(usuarios, nome, senha, nivel):
    for u in usuarios:
        if u["nome"].strip().lower() == nome.strip().lower():
            print(f"  Usuario '{nome}' ja existe!")
            return False
    novo_id = max([u["id"] for u in usuarios], default=0) + 1
    usuarios.append({"id": novo_id, "nome": nome.strip(), "senha": senha, "nivel": nivel})
    salvar_usuarios(usuarios)
    print(f"  Usuario '{nome}' cadastrado como {NIVEIS[nivel]}!")
    return True

def login(usuarios):
    exibir_cabecalho_sistema()
    print("   TELA DE ACESSO")
    print("-"*60)
    nome = input("  Usuario: ")
    senha = input("  Senha:   ")
    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print(f"\n  ACESSO CONCEDIDO → {nome}")
            print(f"  Perfil: {NIVEIS[u['nivel']]}")
            return u
    print("  Usuario ou senha invalidos!")
    return None

# FUNCOES DE ORDENS
def abrir_ordem(ordens, operador, titulo, descricao, maquina, cabecote, sistema, item, anexos=""):
    novo_id = max([o["id"] for o in ordens], default=0) + 1
    nova = {
        "id": novo_id, "titulo": titulo, "descricao": descricao,
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
    salvar_ordens(ordens)
    print("\n" + "="*60)
    print(f"  ORDEM #{nova['id']} ABERTA COM SUCESSO")
    print(f"  Maquina: {maquina}  |  Cabecote: {cabecote}")
    print(f"  Sistema: {sistema}  /  Item: {item}")
    print(f"  Status: {STATUS[1]}")
    print("="*60)

def assumir_ordem(ordens, mecanico, id_o):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] != 1:
                print(f"  Ordem #{id_o} nao esta disponivel!"); return
            o["status"] = 2; o["responsavel_nome"] = mecanico["nome"]
            o["data_inicio"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            salvar_ordens(ordens)
            print(f"  Ordem #{id_o} assumida → {STATUS[2]}")
            return
    print(f"  Ordem #{id_o} nao encontrada!")

def solicitar_pecas(ordens, mecanico, id_o, pecas):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] != 2:
                print(f"  Ordem #{id_o} nao esta em manutencao!"); return
            o["solicitacao_pecas"] = pecas
            o["data_solicitacao_pecas"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["status"] = 3
            salvar_ordens(ordens)
            print(f"  Pecas solicitadas → {STATUS[3]}")
            return
    print(f"  Ordem #{id_o} nao encontrada!")

def confirmar_recebimento_pecas(ordens, almoxarifado, id_o):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] != 3:
                print(f"  Ordem #{id_o} nao aguardando peca!"); return
            o["status"] = 4; o["data_recebimento_pecas"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            salvar_ordens(ordens)
            print(f"  Pecas recebidas → {STATUS[4]}")
            return
    print(f"  Ordem #{id_o} nao encontrada!")

def registrar_materiais(ordens, almoxarifado, id_o, materiais):
    for o in ordens:
        if o["id"] == id_o:
            o["materiais_utilizados"] = materiais
            o["data_registro_materiais"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            salvar_ordens(ordens)
            print(f"  Materiais registrados na Ordem #{id_o}")
            return
    print(f"  Ordem #{id_o} nao encontrada!")

def registrar_parada_maquina(ordens, mecanico, id_o, motivo):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] in [6,7,8]:
                print("  Ordem ja fechada/parada!"); return
            o["status"] = 7; o["data_parada_maquina"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["motivo_parada"] = motivo
            salvar_ordens(ordens)
            print("  MAQUINA PARADA registrada!")
            return
    print(f"  Ordem #{id_o} nao encontrada!")

def liberar_maquina_para_operacao(ordens, usuario, id_o, observacao=""):
    if usuario["nivel"] not in [7,8,9]:
        print("  Sem permissao! Apenas Coordenador/Gerente/ADM."); return
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] != 7:
                print("  Maquina nao esta parada!"); return
            o["status"] = 8; o["data_liberacao_maquina"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["observacao_liberacao"] = observacao; o["liberado_por"] = usuario["nome"]
            salvar_ordens(ordens)
            print(f"  MAQUINA LIBERADA por {usuario['nome']}")
            return
    print(f"  Ordem #{id_o} nao encontrada!")

def finalizar_ordem_mecanico(ordens, mecanico, id_o, observacao, anexos_execucao):
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] == 7:
                print("  Ordem parada — aguarde liberacao!"); return
            if o["status"] < 4:
                print("  Pecas pendentes!"); return
            o["status"] = 5; o["data_finalizacao_mecanico"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["observacao_execucao"] = observacao; o["anexos_execucao"] = anexos_execucao
            salvar_ordens(ordens)
            print(f"  Enviada para conferencia → {STATUS[5]}")
            return
    print(f"  Ordem #{id_o} nao encontrada!")

def concluir_ordem_supervisor(ordens, usuario, id_o, observacao=""):
    pode_todos = usuario["nivel"] in [8,9]
    for o in ordens:
        if o["id"] == id_o:
            if o["status"] == 7:
                print("  Ordem parada — libere primeiro!"); return
            if not pode_todos and o["status"] != 5:
                print("  Apenas GERENTE/ADM fecham em qualquer status!"); return
            o["status"] = 6; o["data_conclusao_supervisor"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            o["observacao_conclusao_supervisor"] = observacao
            salvar_ordens(ordens)
            print(f"  ORDEM CONCLUIDA por {usuario['nome']} ({NIVEIS[usuario['nivel']]})")
            return
    print(f"  Ordem #{id_o} nao encontrada!")

def listar_ordens(ordens, usuario):
    print("\n" + "="*60)
    print(f"  LISTA DE ORDENS — {NIVEIS[usuario['nivel']].upper()}")
    print("="*60)
    if not ordens:
        print("  Nenhuma ordem cadastrada."); return
    encontrou = False
    for o in ordens:
        exibir = False
        if usuario["nivel"] == 1: exibir = o["solicitante_id"] == usuario["id"]
        elif usuario["nivel"] == 2: exibir = o["status"] == 1 or o["responsavel_nome"] == usuario["nome"]
        elif usuario["nivel"] == 3: exibir = o["status"] in (1,3)
        else: exibir = True
        if not exibir: continue
        encontrou = True
        print(f"\n  ORDEM #{o['id']} — {STATUS[o['status']]}")
        print(f"   Maquina: {o['maquina']}  |  Cabecote: {o.get('cabecote','---')}")
        print(f"   Sistema: {o.get('sistema','---')}  /  Item: {o.get('item','---')}")
        print(f"   Solicitante: {o['solicitante_nome']}  |  Abertura: {o['data_abertura']}")
        if o.get("solicitacao_pecas"): print(f"   Pecas: {o['solicitacao_pecas']}")
        if o["status"] == 7: print(f"   Motivo Parada: {o.get('motivo_parada','---')}")
        if o["status"] == 8: print(f"   Liberado por: {o.get('liberado_por','---')}")
        if o["status"] == 6: print(f"   Concluido: {o.get('data_conclusao_supervisor','---')}")
    if not encontrou:
        print("  Nenhuma ordem disponivel.")

def remover_ordem(ordens, usuario, id_o):
    if usuario["nivel"] != 9:
        print("  Apenas ADM exclui ordens!"); return
    for i, o in enumerate(ordens):
        if o["id"] == id_o:
            ordens.pop(i); salvar_ordens(ordens)
            print(f"  Ordem #{id_o} REMOVIDA!"); return
    print(f"  Ordem #{id_o} nao encontrada!")

# MENU PRINCIPAL
def menu():
    criar_pastas()
    usuarios = carregar_usuarios()
    ordens = carregar_ordens()

    usuario_logado = None
    while not usuario_logado:
        usuario_logado = login(usuarios)
        if not usuario_logado:
            input("\nPressione ENTER para tentar novamente...")

    while True:
        cargo = NIVEIS[usuario_logado["nivel"]]
        print("\n" + "="*60)
        print(f"  PAINEL PRINCIPAL · {usuario_logado['nome']} · {cargo}")
        print("="*60)

        n = usuario_logado["nivel"]
        opcoes = []
        if n == 1:
            opcoes = ["1. Abrir Ordem de Manutencao", "2. Minhas Ordens"]
        elif n == 2:
            opcoes = ["1. Assumir Ordem", "2. Solicitar Pecas", "3. Registrar Parada de Maquina", "4. Finalizar Ordem", "5. Listar Ordens"]
        elif n == 3:
            opcoes = ["1. Confirmar Recebimento de Pecas", "2. Registrar Materiais", "3. Gerar Relatorio de Pecas (PDF)", "4. Listar Ordens"]
        elif n == 5:
            opcoes = ["1. Concluir Ordem", "2. Listar Ordens"]
        elif n == 7:
            opcoes = ["1. Concluir Ordem", "2. Liberar Maquina", "3. Listar Ordens"]
        elif n == 8:
            opcoes = ["1. Concluir QUALQUER Ordem", "2. Liberar Maquina", "3. Listar Ordens"]
        elif n == 9:
            opcoes = ["1. Concluir QUALQUER Ordem", "2. Liberar Maquina", "3. Listar Ordens", "4. Excluir Ordem", "5. Cadastrar Usuario", "6. Relatorio Geral"]

        for txt in opcoes: print(f"  {txt}")
        print("  0. Sair do Sistema")
        escolha = input("\n  Escolha uma opcao: ")

        def pedir_id():
            try: return int(input("  Numero da Ordem: "))
            except: print("  Digite um numero valido!"); return None

        if escolha == "1":
            if n == 1:
                print("\n  ABRIR NOVA ORDEM")
                titulo = input("  Titulo / Assunto: ")
                descricao = input("  Descreva o problema: ")
                maquina = escolher_maquina()
                cabecote = escolher_cabecote()
                tem_cab = (cabecote != "Nenhum")
                sistema, item = escolher_sistema_e_item(tem_cab)
                anexos = input("  Anexos / Observacoes (opcional): ")
                abrir_ordem(ordens, usuario_logado, titulo, descricao, maquina, cabecote, sistema, item, anexos)
            elif n == 2:
                id_o = pedir_id()
                if id_o: assumir_ordem(ordens, usuario_logado, id_o)
            elif n in (3,5,7,8,9):
                id_o = pedir_id()
                if id_o:
                    obs = input("  Observacoes de conclusao (opcional): ")
                    concluir_ordem_supervisor(ordens, usuario_logado, id_o, obs)

        elif escolha == "2":
            if n == 2:
                id_o = pedir_id()
                if id_o:
                    pecas = input("  Pecas e quantidades: ")
                    solicitar_pecas(ordens, usuario_logado, id_o, pecas)
            elif n == 3:
                id_o = pedir_id()
                if id_o: confirmar_recebimento_pecas(ordens, usuario_logado, id_o)
            elif n in (7,8,9):
                id_o = pedir_id()
                if id_o:
                    obs = input("  Observacoes de liberacao (opcional): ")
                    liberar_maquina_para_operacao(ordens, usuario_logado, id_o, obs)
            elif n in (1,3,5):
                listar_ordens(ordens, usuario_logado)

        elif escolha == "3":
            if n == 2:
                id_o = pedir_id()
                if id_o:
                    motivo = input("  Motivo da parada: ")
                    registrar_parada_maquina(ordens, usuario_logado, id_o, motivo)
            elif n == 3:
                id_o = pedir_id()
                if id_o:
                    mat = input("  Materiais utilizados: ")
                    registrar_materiais(ordens, usuario_logado, id_o, mat)
            elif n in (5,7,8,9):
                listar_ordens(ordens, usuario_logado)

        elif escolha == "4":
            if n == 2:
                id_o = pedir_id()
                if id_o:
                    obs = input("  Observacoes de execucao: ")
                    anex = input("  Anexos (opcional): ")
                    finalizar_ordem_mecanico(ordens, usuario_logado, id_o, obs, anex)
            elif n == 3:
                gerar_relatorio_pecas(ordens, usuario_logado)
            elif n == 9:
                id_o = pedir_id()
                if id_o: remover_ordem(ordens, usuario_logado, id_o)
            elif n in (1,5):
                listar_ordens(ordens, usuario_logado)

        elif escolha == "5":
            if n == 2:
                listar_ordens(ordens, usuario_logado)
            elif n == 9:
                print("\n  CADASTRAR NOVO USUARIO")
                nome = input("  Nome do usuario: ")
                senha = input("  Senha: ")
                print("  Niveis: 1=Op 2=Mec 3=Alm 4=Insp 5=SupMan 6=SupOp 7=Coord 8=Ger 9=ADM")
                try:
                    nivel = int(input("  Nivel de acesso: "))
                    cadastrar_usuario(usuarios, nome, senha, nivel)
                except:
                    print("  Nivel invalido!")
            elif n in (1,3,5):
                listar_ordens(ordens, usuario_logado)

        elif escolha == "6" and n == 9:
            total = len(ordens)
            print("\n  RELATORIO GERAL")
            print(f"  Total de Ordens: {total}")
            for s in STATUS:
                qtd = sum(1 for o in ordens if o["status"] == s)
                if qtd > 0:
                    print(f"  {STATUS[s]}: {qtd}")

        elif escolha == "0":
            print("\n  Encerrando... Até logo!"); break

        else:
            print("  Opcao invalida! Tente novamente.")

if __name__ == "__main__":
    menu()
