from dotenv import load_dotenv
import os

load_dotenv()
DEVICE = os.getenv("DEVICE")

print(f"Using device: {DEVICE}")