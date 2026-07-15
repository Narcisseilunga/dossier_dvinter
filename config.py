"""import os
class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SUPABASE_URL = os.getenv("SUPABASE_URL")

    SUPABASE_KEY = os.getenv("SUPABASE_KEY")"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "UneCleTresLongueEtSecretePourLeDeveloppement123456789!"
    )

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 500 Mo