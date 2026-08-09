import streamlit as st
from banco import carregar_usuarios, salvar_usuarios, carregar_ordens, salvar_ordens
from dados import MAQUINAS, CABECOTES, SISTEMAS_MAQUINA_BASE, SISTEMAS_CABECOTE, NIVEIS, STATUS
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="BACKLOGDAY - Gestão de Manutenção", layout="wide")

# Inicializar sessão
if "usuario" not in st.session_state:
    st.session_state.usuario = None
if "pagina" not in st.session_state:
    st.session_state.pagina = "login"

usuarios = carregar_usuarios()
ordens = carregar_ordens()

# ------------------- TELA DE LOGIN -------------------
if st.session_state.pagina == "login":
    st.title("🔐 BACKLOGDAY — Sistema de Gestão de Manutenção")
    st.subheader("Máquinas Florestais · Cabeçotes · Unidades de Corte")
    st.divider()

    nome = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Entrar", type="primary"):
            for u in usuarios:
                if u["nome"] == nome and u["senha"] == senha:
                    st.session_state.usuario = u
                    st.session_state.pagina = "principal"
                    st.success(f"Bem-vindo, {u['nome']}! Perfil: {NIVEIS[u['nivel']]}")
                    st.rerun()
                    break
            else:
                st.error("Usuário ou senha inválidos!")

    st.divider()
    st.info("🔑 Acesso padrão: Usuário: adm | Senha: adm123")

# ------------------- PAINEL PRINCIPAL -------------------
elif st.session_state.pagina == "principal" and st.session_state.usuario:
    u = st.session_state.usuario
    st.title(f"🚜 BACKLOGDAY — Olá, {u['nome']} ({NIVEIS[u['nivel']]})")
    st.divider()

    menu = st.sidebar.radio("Menu", [
        "📋 Listar Ordens",
        "➕ Abrir Ordem",
        "🔧 Assumir Ordem",
        "📦 Solicitar Peças",
        "✅ Finalizar Ordem",
        "⚙️ Cadastrar Usuário",
        "📊 Relatórios",
        "🚪 Sair"
    ])

    # Sair
    if menu == "🚪 Sair":
        st.session_state.usuario = None
        st.session_state.pagina = "login"
        st.rerun()

    # Listar Ordens
    elif menu == "📋 Listar Ordens":
        st.subheader("Lista de Ordens de Manutenção")
        if not ordens:
            st.info("Nenhuma ordem cadastrada.")
        else:
            for o in ordens:
                st.markdown(f"""
                **Ordem #{o['id']} — {STATUS[o['status']]}**
                - 📌 Máquina: {o['maquina']} | Cabeçote: {o.get('cabecote', '---')}
                - 🔧 Sistema/Item: {o.get('sistema', '---')} / {o.get('item', '---')}
                - 👤 Solicitante: {o['solicitante_nome']} | 📅 Abertura: {o['data_abertura']}
                """)
                st.divider()

    # Abrir Ordem
    elif menu == "➕ Abrir Ordem":
        if u["nivel"] not in [1, 2, 4, 5, 7, 8, 9]:
            st.error("Sem permissão!")
        else:
            st.subheader("Abrir Nova Ordem")
            titulo = st.text_input("Título / Assunto")
            descricao = st.text_area("Descrição do Problema")
            maquina = st.selectbox("Máquina", MAQUINAS)
            cabecote = st.selectbox("Cabeçote", ["Nenhum"] + CABECOTES)
            tem_cab = cabecote != "Nenhum"
            sistemas = list(SISTEMAS_CABECOTE.keys()) if tem_cab else list(SISTEMAS_MAQUINA_BASE.keys())
            sistema = st.selectbox("Sistema", sistemas)
            itens = SISTEMAS_CABECOTE[sistema] if tem_cab else SISTEMAS_MAQUINA_BASE[sistema]
            item = st.selectbox("Item", itens)

            if st.button("Abrir Ordem", type="primary"):
                novo_id = max([x["id"] for x in ordens], default=0) + 1
                ordens.append({
                    "id": novo_id, "titulo": titulo, "descricao": descricao,
                    "maquina": maquina, "cabecote": cabecote, "sistema": sistema, "item": item,
                    "status": 1, "solicitante_id": u["id"], "solicitante_nome": u["nome"],
                    "data_abertura": datetime.now().strftime("%d/%m/%Y %H:%M")
                })
                salvar_ordens(ordens)
                st.success(f"✅ Ordem #{novo_id} aberta com sucesso!")
                st.rerun()

    # Assumir Ordem
    elif menu == "🔧 Assumir Ordem":
        if u["nivel"] != 2:
            st.error("Apenas Mecânicos podem assumir ordens!")
        else:
            st.subheader("Assumir Ordem")
            ordens_abertas = [o for o in ordens if o["status"] == 1]
            if not ordens_abertas:
                st.info("Nenhuma ordem disponível.")
            else:
                id_escolhida = st.selectbox("Escolha a Ordem", [f"#{o['id']} - {o['maquina']}" for o in ordens_abertas])
                id_num = int(id_escolhida.split("#")[1].split(" ")[0])
                if st.button("Assumir", type="primary"):
                    for o in ordens:
                        if o["id"] == id_num:
                            o["status"] = 2
                            o["responsavel_nome"] = u["nome"]
                            o["data_inicio"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                            salvar_ordens(ordens)
                            st.success(f"✅ Ordem #{id_num} assumida!")
                            st.rerun()

    # Solicitar Peças
    elif menu == "📦 Solicitar Peças":
        if u["nivel"] != 2:
            st.error("Apenas Mecânicos podem solicitar peças!")
        else:
            st.subheader("Solicitar Peças")
            ordens_em_andamento = [o for o in ordens if o["status"] == 2 and o.get("responsavel_nome") == u["nome"]]
            if not ordens_em_andamento:
                st.info("Nenhuma ordem em manutenção.")
            else:
                id_escolhida = st.selectbox("Escolha a Ordem", [f"#{o['id']} - {o['maquina']}" for o in ordens_em_andamento])
                id_num = int(id_escolhida.split("#")[1].split(" ")[0])
                pecas = st.text_area("Peças e Quantidades")
                if st.button("Solicitar", type="primary"):
                    for o in ordens:
                        if o["id"] == id_num:
                            o["solicitacao_pecas"] = pecas
                            o["status"] = 3
                            salvar_ordens(ordens)
                            st.success(f"✅ Peças solicitadas na Ordem #{id_num}!")
                            st.rerun()

    # Finalizar Ordem
    elif menu == "✅ Finalizar Ordem":
        st.subheader("Finalizar Ordem")
        pode_todas = u["nivel"] in [8, 9]
        if pode_todas:
            ordens_finalizaveis = [o for o in ordens if o["status"] in [4, 5]]
        else:
            ordens_finalizaveis = [o for o in ordens if o["status"] == 5 and o.get("responsavel_nome") == u["nome"]]
        if not ordens_finalizaveis:
            st.info("Nenhuma ordem para finalizar.")
        else:
            id_escolhida = st.selectbox("Escolha a Ordem", [f"#{o['id']} - {o['maquina']}" for o in ordens_finalizaveis])
            id_num = int(id_escolhida.split("#")[1].split(" ")[0])
            obs = st.text_area("Observações de Conclusão")
            if st.button("Concluir", type="primary"):
                for o in ordens:
                    if o["id"] == id_num:
                        o["status"] = 6
                        o["observacao_conclusao_supervisor"] = obs
                        o["data_conclusao_supervisor"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                        salvar_ordens(ordens)
                        st.success(f"✅ Ordem #{id_num} CONCLUÍDA!")
                        st.rerun()

    # Cadastrar Usuário
    elif menu == "⚙️ Cadastrar Usuário":
        if u["nivel"] != 9:
            st.error("Apenas ADMINISTRADOR pode cadastrar usuários!")
        else:
            st.subheader("Cadastrar Novo Usuário")
            nome_novo = st.text_input("Nome do Usuário")
            senha_nova = st.text_input("Senha", type="password")
            nivel_novo = st.selectbox("Nível de Acesso", list(NIVEIS.keys()), format_func=lambda x: f"{x} - {NIVEIS[x]}")
            if st.button("Cadastrar", type="primary"):
                for x in usuarios:
                    if x["nome"] == nome_novo:
                        st.error("Usuário já existe!")
                        break
                else:
                    novo_id = max([x["id"] for x in usuarios], default=0) + 1
                    usuarios.append({"id": novo_id, "nome": nome_novo, "senha": senha_nova, "nivel": nivel_novo})
                    salvar_usuarios(usuarios)
                    st.success(f"✅ Usuário '{nome_novo}' cadastrado como {NIVEIS[nivel_novo]}!")
                    st.rerun()

    # Relatórios
    elif menu == "📊 Relatórios":
        st.subheader("Relatório Geral")
        st.write(f"**Total de Ordens:** {len(ordens)}")
        for s in STATUS:
            qtd = sum(1 for o in ordens if o["status"] == s)
            if qtd > 0:
                st.write(f"{STATUS[s]}: **{qtd}**")

else:
    st.session_state.pagina = "login"
    st.rerun()
