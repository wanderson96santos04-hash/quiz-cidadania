import csv
from datetime import datetime
from app.config import LEADS_FILE
import requests  # 👈 NOVO


HEADERS = [
    "data",
    "nome",
    "whatsapp",
    "sobrenome_italiano",
    "familia_cidadania",
    "documentos",
    "interesse",
    "urgencia",
    "consentimento",
]


def ensure_csv_exists() -> None:
    if not LEADS_FILE.exists():
        with open(LEADS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)


def enviar_telegram(lead: dict):  # 👈 NOVO
    TOKEN = "8791868047:AAFpr3DkLAvWLE_o5KNmPdyB9rJJ2JwROTA"
    CHAT_ID = "8321287889"

    mensagem = f"""
🚨 NOVO LEAD 🚨

👤 Nome: {lead['nome']}
📞 WhatsApp: {lead['whatsapp']}
📍 Interesse: {lead['interesse']}
⚡ Urgência: {lead['urgencia']}
    """

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    try:
        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": mensagem
        })
    except:
        pass  # 👈 não quebra nada se der erro


def save_lead(lead: dict) -> None:
    ensure_csv_exists()

    with open(LEADS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                lead["nome"],
                lead["whatsapp"],
                lead["sobrenome_italiano"],
                lead["familia_cidadania"],
                lead["documentos"],
                lead["interesse"],
                lead["urgencia"],
                "Sim" if lead["consentimento"] else "Não",
            ]
        )

    enviar_telegram(lead)  # 👈 SÓ ADICIONAMOS ISSO