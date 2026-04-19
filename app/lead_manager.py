import csv
from datetime import datetime
from app.config import LEADS_FILE


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