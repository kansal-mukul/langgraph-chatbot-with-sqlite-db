from pathlib import Path

CHATBOT_DATABASE_PATH = (
    Path(__file__).resolve().parents[1] / "database" / "chatbot.db"
)
