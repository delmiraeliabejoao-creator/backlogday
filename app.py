import streamlit as st
from datetime import datetime
from fpdf import FPDF
from dados import *
from banco import *

# Configuração da página
st.set_page_config(
    page_title="BACKLOGDAY",
    layout="wide",
    initial_sidebar_state="expanded"
)
# 🔹 ESTILOS PERSONALIZADOS
st.markdown("""
<style>
    * { font-family: 'Segoe UI', sans-serif; }
    .stApp {
        background: linear-gradient(135deg, #050814 0%, #0F172A 50%, #050814 100%);
        color: #E0F7FF;
    }
    h1, h2, h3 {
        color: #00D4FF;
        font-weight: 600;
        text-shadow: 0 0 8px rgba(0, 212, 255, 0.5);
    }
    .stButton>button {
        background: linear-gradient(90deg, #0077B6, #00B4D8);
        color: white;
        border: 1px solid rgba(0, 212, 255, 0.4);
        border-radius: 8px;
        box-shadow: 0 0 12px rgba(0, 180, 216, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #00B4D8, #00D4FF);
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.6);
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea, .stSelectbox>div>div>div {
        background: rgba(10, 20, 40, 0.8);
        border: 1px solid rgba(0, 212, 255, 0.3);
        color: #E0F7FF;
        border-radius: 6px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(5, 10, 25, 0.6);
        border-radius: 8px;
        padding: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: #8FBBDB;
        border-radius: 6px;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(0, 180, 216, 0.2);
        color: #00D4FF;
        border: 1px solid #00D4FF;
    }
    .card-ordem {
        background: rgba(8, 15, 35, 0.9);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border: 1px solid rgba(0, 212, 255, 0.2);
    }
    .stSidebar {
        background: rgba(5, 8, 20, 0.95);
        border-right: 1px solid rgba(0, 212, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# 🔹 INICIA BANCO DE DADOS
iniciar_banco()

# ------------------- TELA DE LOGIN -------------------
if "logado" not in st.session_state:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div style="text-align:center; padding:30px; border:1px solid rgba(0,212,255,0.4); border-radius:15px; background:rgba(8,15,35,0.9);">
            <h1 style="font-size:42px;">BACKLOGDAY</h1>
            <p style="color:#8FBBDB;">Sistema Inteligente de Gestão de Manutenção</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        with st.form("login"):
            email = st.text_input("E-mail", placeholder="digite seu e-mail")
            senha = st.text_input("Senha", type="password", placeholder="digite sua senha")
            entrar = st.form_submit_button("ACESSAR SISTEMA")

            if entrar:
                user = consultar("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
                if user:
                    st.session_state.logado = True
                    st.session_state.id_user = user[0][0]
                    st.session_state.email = user[0][1]
                    st.session_state.perfil = user[0][3]
                    st.rerun()
                else:
                    st.error("⚠️ Credenciais inválidas")

# ------------------- SISTEMA PRINCIPAL -------------------
else:
    perfil = st.session_state.perfil
    st.sidebar.markdown(f"""
    <div style="text-align:center; padding:15px; border-bottom:1px solid rgba(0,212,255,0.3);">
        <h3 style="margin:0;">👤 {perfil}</h3>
        <p style="color:#8FBBDB; font-size:13px;">{st.session_state.email}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.sidebar.button("🚪 Sair do Sistema"):
        st.session_state.clear()
        st.rerun()

    # ✅ MONTAGEM CORRETA DAS ABAS
    abas = []
    if perfil in ["Administrador", "Operador", "Inspetor de Manutenção"]:
        abas.append("📝 Abrir Ordem")
    abas.append("📋 Ordens de Serviço")
    if perfil in ["Administrador", "Mecânico", "Almoxarifado"]:
        abas.append("📦 Pedidos de Peças")
    if perfil in ["Administrador", "Supervisor de Manutenção"]:
        abas.append("⚙️ Gerenciar")
    if perfil in ["Administrador", "Almoxarifado"]:
        abas.append("📄 Relatórios")
    if perfil == "Administrador":
        abas.append("👥 Usuários")

    menu = st.tabs(abas)

            # 1. ABRIR ORDEM
    if "📝 Abrir Ordem" in abas:
        with menu[abas.index("📝 Abrir Ordem")]:
            st.header("📝 Nova Ordem de Manutenção")
            tipo = st.radio("Tipo de Equipamento", ["Maquina Base", "Cabeçote"], horizontal=True)
            lista = MAQUINA_BASE if tipo == "Maquina Base" else CABECOTE
            cod = st.selectbox("Código do Equipamento", lista)

            if tipo == "Maquina Base":
                grupos = [
                    ("CABINE", ITENS_MAQUINA_BASE.get("CABINE", [])),
                    ("BRAÇO", ITENS_MAQUINA_BASE.get("BRAÇO", [])),
                    ("LANÇA", ITENS_MAQUINA_BASE.get("LANÇA", [])),
                    ("MAQUINA BASE", ITENS_MAQUINA_BASE.get("MAQUINA BASE", []))
                ]
            else:
                grupos = [
                    ("DESGALHAMENTO", ITENS_CABECOTE.get("DESGALHAMENTO", [])),
                    ("ROLO", ITENS_CABECOTE.get("ROLO", [])),
                    ("TILT", ITENS_CABECOTE.get("TILT", [])),
                    ("ROTATOR", ITENS_CABECOTE.get("ROTATOR", []) + ITENS_CABECOTE.get("MOTOR DE SERRA", []) + ITENS_CABECOTE.get("CHASSIS", []))
                ]

            pendentes = []
            for nome_grupo, lista_itens in grupos:
                st.subheader(f"🔹 {nome_grupo}")
                sel = st.multiselect(f"Selecione os itens com problema", lista_itens)
                pendentes.extend(sel)

            desc = st.text_area("📝 Descrição Detalhada do Problema", height=120)
            midia = st.file_uploader("📷 Anexar fotos / vídeos", accept_multiple_files=True)

            if st.button("🚀 GERAR ORDEM"):
                arquivos = ", ".join([arq.name for arq in midia]) if midia else "Sem arquivos anexados"
                executar('''INSERT INTO ordens
                    (data, tipo_equipamento, codigo_equipamento, itens_pendentes, descricao, status, mecanico, solicitante, midia)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (
                        datetime.now().strftime("%d/%m/%Y %H:%M"),
                        tipo,
                        cod,
                        str(pendentes),
                        desc,
                        "Aguardando Serviço",
                        "",
                        st.session_state.email,
                        arquivos
                    ))
                st.success("✅ Ordem gerada com sucesso!")

    # 2. ORDENS DE SERVIÇO
    with menu[abas.index("📋 Ordens de Serviço")]:
        st.header("📋 Ordens de Serviço")
        if st.button("🔄 Atualizar"):
            st.rerun()

        ordens = consultar("SELECT * FROM ordens ORDER BY data DESC")
        if not ordens:
            st.info("📭 Nenhuma ordem registrada ainda")
        for o in ordens:
            cor = STATUS.get(o[6], "#888888")
            st.markdown(f'''
            <div class="card-ordem">
                <strong>#{o[0]} | {o[2]} | <span style="color:{cor};">{o[6] if o[6] else "Aguardando Serviço"}</span></strong><br>
                <span style="color:#8FBBDB;">Data: {o[1]} | Solicitante: {o[8]}</span><br>
                Itens: {o[3]}
            </div>
            ''', unsafe_allow_html=True)

            with st.expander(f"📝 Ver detalhes completos da Ordem #{o[0]}"):
                st.write("**Descrição do Problema:**")
                st.info(o[4] if o[4] else "Nenhuma descrição informada")
                st.write("**Arquivos Anexados:**")
                st.info(o[9] if len(o) > 9 and o[9] else "Nenhum arquivo enviado")

            if perfil == "Mecânico" and (o[6] in ["Aguardando Serviço", "Aguardando Peça"] or o[6] is None):
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"✅ Concluir #{o[0]}"):
                        executar("UPDATE ordens SET status = 'Concluída', mecanico = ? WHERE id = ?", (st.session_state.email, o[0]))
                        st.rerun()
                with col2:
                    if st.button(f"📦 Pedir Peças #{o[0]}"):
                        with st.form(f"pedido_{o[0]}"):
                            qtd = st.number_input("Quantidade", min_value=1, value=1)
                            cod_p = st.text_input("Código da Peça")
                            nome_p = st.text_input("Nome da Peça")
                            if st.form_submit_button("Confirmar"):
                                executar('''INSERT INTO pedidos_pecas
                                    (id_ordem, quantidade, codigo_peca, nome_peca, solicitante, tipo_equipamento)
                                    VALUES (?, ?, ?, ?, ?, ?)''',
                                    (o[0], qtd, cod_p, nome_p, st.session_state.email, o[2]))
                                executar("UPDATE ordens SET status = 'Aguardando Peça' WHERE id = ?", (o[0],))
                                st.rerun()

            if perfil == "Almoxarifado" and o[6] == "Aguardando Peça":
                if st.button(f"🔵 Confirmar Pedido #{o[0]}"):
                    executar("UPDATE ordens SET status = 'Peça Solicitada' WHERE id = ?", (o[0],))
                    st.rerun()
                if st.button(f"🔔 Notificar Chegada #{o[0]}"):
                    st.success("📤 Notificação enviada!")

            if perfil == "Supervisor de Manutenção" and o[6] == "Concluída":
                if st.button(f"⚫ Finalizar Ordem #{o[0]}"):
                    executar("UPDATE ordens SET status = 'Finalizada' WHERE id = ?", (o[0],))
                    st.rerun()
            st.markdown("---")

    # 3. PEDIDOS DE PEÇAS
    if "📦 Pedidos de Peças" in abas:
        with menu[abas.index("📦 Pedidos de Peças")]:
            st.header("📦 Pedidos de Peças")
            ped = consultar("SELECT * FROM pedidos_pecas ORDER BY id DESC")
            if not ped:
                st.info("📭 Nenhum pedido registrado")
            for p in ped:
                st.markdown(f'''
                <div class="card-ordem">
                    <strong>Ordem #{p[1]}</strong> | Qtd: {p[2]}<br>
                    Peça: {p[3]} - {p[4]}<br>
                    Solicitante: {p[5]} | Equipamento: {p[6]}
                </div>
                ''', unsafe_allow_html=True)

    # 4. GERENCIAR
    if "⚙️ Gerenciar" in abas:
        with menu[abas.index("⚙️ Gerenciar")]:
            st.header("⚙️ Alterar Status")
            ordens = consultar("SELECT id, codigo_equipamento, status FROM ordens")
            if ordens:
                ids = [f"#{o[0]} - {o[1]} ({o[2]})" for o in ordens]
                sel = st.selectbox("Selecione a Ordem", ids)
                id_sel = sel.split(" - ")[0].replace("#","")
                novo_status = st.selectbox("Novo Status", list(STATUS.keys()))
                if st.button("🔄 Atualizar Status"):
                    executar("UPDATE ordens SET status = ? WHERE id = ?", (novo_status, id_sel))
                    st.success("✅ Atualizado!")

    # 5. RELATÓRIOS
    if "📄 Relatórios" in abas:
        with menu[abas.index("📄 Relatórios")]:
            st.header("📄 Relatórios")
            filtro = st.selectbox("Filtrar por Status", ["Todos"] + list(STATUS.keys()))
            if st.button("📥 Gerar Relatório PDF"):
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", "B", 18)
                pdf.cell(0, 12, "RELATÓRIO BACKLOGDAY", ln=True, align="C")
                pdf.ln(8)
                pdf.set_font("Arial", size=11)
                dados = consultar("SELECT * FROM ordens") if filtro == "Todos" else consultar("SELECT * FROM ordens WHERE status = ?", (filtro,))
                for o in dados:
                    pdf.cell(0, 8, f"#{o[0]} | {o[2]} | {o[6] if o[6] else 'Aguardando Serviço'} | {o[1]}", ln=True)
                nome_arq = f"relatorio_{datetime.now().strftime('%d%m%Y_%H%M')}.pdf"
                pdf.output(nome_arq)
                with open(nome_arq, "rb") as f:
                    st.download_button("⬇️ Baixar", f, file_name=nome_arq)

    # 6. USUÁRIOS (SÓ ADM)
    if "👥 Usuários" in abas:
        with menu[abas.index("👥 Usuários")]:
            st.header("👤 Gerenciar Usuários")
            st.subheader("📋 Usuários Cadastrados")
            lista_usuarios = consultar("SELECT id, email, perfil FROM usuarios ORDER BY id")
            if lista_usuarios:
                for u in lista_usuarios:
                    id_user, email, perfil_user = u
                    st.markdown(f"""
                    <div class="card-ordem">
                        <strong>ID: {id_user}</strong><br>
                        E-mail: {email}<br>
                        Perfil: {perfil_user}
                    </div>
                    """, unsafe_allow_html=True)
                    if email != st.session_state.email:
                        if st.button(f"🗑️ Excluir {email}", key=f"del_{id_user}"):
                            executar("DELETE FROM usuarios WHERE id = ?", (id_user,))
                            st.success(f"✅ {email} excluído!")
                            st.rerun()
                    else:
                        st.info("🔒 Não pode excluir seu próprio acesso")
                    st.markdown("---")
            else:
                st.info("📭 Nenhum usuário cadastrado")

            st.subheader("➕ Cadastrar Novo")
            with st.form("cad_user"):
                em = st.text_input("E-mail")
                se = st.text_input("Senha", type="password")
                pe = st.selectbox("Perfil", PERFIS)
                if st.form_submit_button("✅ Cadastrar"):
                    try:
                        executar("INSERT INTO usuarios (email, senha, perfil) VALUES (?, ?, ?)", (em, se, pe))
                        st.success("✅ Cadastrado!")
                        st.rerun()
                    except:
                        st.error("⚠️ E-mail já existe")
