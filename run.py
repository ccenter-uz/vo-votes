from app import create_app
from app.core.updater import background_refresher
import threading
import os
from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv("PORT", 5000))
HOST = os.getenv("HOST", "0.0.0.0")

app = create_app()

if __name__ == "__main__":
    threading.Thread(target=background_refresher, daemon=True).start()
    app.run(host=HOST, port=PORT)
