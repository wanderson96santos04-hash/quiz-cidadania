def classificar_lead(lead):
    score = 0

    if "imediatamente" in lead["prazo"].lower():
        score += 3
    elif "3 meses" in lead["prazo"].lower():
        score += 2
    else:
        score += 1

    if "sim" in lead["documentos"].lower():
        score += 2

    if "investir" in lead["investimento"].lower():
        score += 3

    if "sim" in lead["antepassado"].lower():
        score += 2

    if score >= 8:
        return "QUENTE 🔥"
    elif score >= 5:
        return "MORNO ⚡"
    else:
        return "FRIO ❄️"


def formatar_lead(lead):
    classificacao = classificar_lead(lead)

    mensagem = f"""
🔥 LEAD QUALIFICADO - CIDADANIA ITALIANA

👤 Nome: {lead['nome']}
📞 Telefone: {lead['telefone']}

📊 Classificação: {classificacao}

📅 Prazo: {lead['prazo']}
🇮🇹 Antepassado: {lead['antepassado']}
📄 Documentos: {lead['documentos']}
💰 Investimento: {lead['investimento']}

📆 Data: {lead['data']}
"""
    return mensagem