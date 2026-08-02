# PERFIS DE USUÁRIO
PERFIS = [
    "Administrador",
    "Operador",
    "Inspetor de Manutenção",
    "Mecânico",
    "Almoxarifado",
    "Supervisor de Manutenção",
    "Supervisor de Operação"
]

# STATUS E CORES
STATUS = {
    "Aguardando Serviço": "#FF9800",
    "Aguardando Peça": "#2196F3",
    "Peça Solicitada": "#9C27B0",
    "Concluída": "#4CAF50",
    "Finalizada": "#607D8B"
}

# EQUIPAMENTOS
MAQUINA_BASE = [
    "HV-10105", "HV-10110", "HV-10111", "HV-10114", "HV-10116",
    "HV-10117", "HV-10119", "HV-10120", "HV-10121", "HV-10122",
    "HV-10123", "HV-10134", "HV-19029", "HV-10080", "HV-10089", "HV-10164"
]
# EQUIPAMENTOS
CABECOTE = [
    "CB-12153", "CB-12158", "CB-12159", "CB-12163", "CB-12165",
    "CB-12166", "CB-12168", "CB-12239", "CB-12170", "CB-12171",
    "CB-12172", "CB-12173", "CB-12214", "CB-12136", "CB-12149", "CB-12106"
]

# ITENS - MAQUINA BASE (CORRIGIDO: CABINE)
ITENS_MAQUINA_BASE = {
    "CABINE": ["Acento", "Cortina", "Porta", "Lexan frontal", "Lexan Lateral", "Radio musica", "Farol Cabine", "Farol Lateral", "Farol traseiro", "Monitor", "Tela"],
    "BRAÇO": ["Proteção", "Mangueira", "Cilindro", "Lubrificação", "Registro", "Tubo", "Pino", "Abraçadeira"],
    "LANÇA": ["Abraçadeira", "Pino", "Ponteira", "Mancal", "Cilindro", "Tubo", "Lubrificação"],
    "MAQUINA BASE": ["Proteção", "Tampa lateral Bomba", "Tampa lateral Radiador", "Comando", "Proteção Bateria", "Dog. Houser", "Borracha de proteção", "Tampa do Motor", "Motor", "Bomba Hidráulica", "Radiador", "Esteira", "Roda Guia", "Roda Motriz", "Rolete", "Ar-Condicionado", "Estribo", "Corrimão", "Escada"]
}

# ITENS - CABEÇOTE
ITENS_CABECOTE = {
    "DESGALHAMENTO": ["Faca Fixa", "Parafuso", "Faca Superior LE", "Faca Superior LD", "Biela", "Pino", "Mangueira"],
    "ROLO": ["Suporte do Rolo", "Proteção do Cilindro", "Articulado", "Motor do Rolo", "Cilindro do Rolo", "Rolo do Dorso", "Pista do Cames", "Rolamento Cames", "Capa do Rolo", "Prisioneiro", "Mangueira", "Pino"],
    "TILT": ["Cilindro", "Mangueira", "Pino", "Link", "Batente"],
    "ROTATOR": ["Motor Hidráulico", "Mangueira", "Parafuso", "Rolamento", "Cremalheira", "Pino", "Biela"],
    "MOTOR DE SERRA": ["Mangueira", "Chicote", "Sensor Indutivo", "Sensor Led", "Cabo y", "Tampa do Motor", "Cilindro", "Pino", "Placa do Sabre", "Grampo", "Batente", "Bomba de Lubrificação", "Caixa da serra", "Espaçador"],
    "CHASSIS": ["Capô Grande", "Capô pequeno", "Trava do Capô", "Eixo Central"]
}
