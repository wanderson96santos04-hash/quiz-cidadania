import csv
from datetime import datetime
from app.config import LEADS_FILE
import requests


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


def enviar_telegram(lead: dict) -> None:
    TOKEN = "8791868047:AAH3WKdxpHFARA4icaHhksSHBM8xtuIdVck"
    CHAT_ID = "8321287889"

    mensagem = f"""
🚨 NOVO LEAD 🚨

👤 Nome: {lead['nome']}
📞 WhatsApp: {lead['whatsapp']}
📍 Interesse: {lead['interesse']}
⚡ Urgência: {lead['urgencia']}
""".strip()

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    resposta = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": mensagem
        },
        timeout=15,
    )

    print("TELEGRAM STATUS:", resposta.status_code)
    print("TELEGRAM RESPOSTA:", resposta.text)
    resposta.raise_for_status()


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

    try:
        enviar_telegram(lead)
    except Exception as e:
        print("ERRO AO ENVIAR TELEGRAM:", str(e))