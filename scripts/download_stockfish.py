import os
import requests
import zipfile
import platform

def download_stockfish():
    url = "https://stockfishchess.org/files/stockfish_14.1_win_x64.zip"
    if platform.system() == "Linux":
        url = "https://stockfishchess.org/files/stockfish_14.1_linux_x64.zip"
    elif platform.system() == "Darwin":
        url = "https://stockfishchess.org/files/stockfish_14.1_mac.zip"

    response = requests.get(url)
    os.makedirs("bin", exist_ok=True)
    zip_path = os.path.join("bin", "stockfish.zip")
    with open(zip_path, "wb") as f:
        f.write(response.content)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall("bin")

    os.remove(zip_path)

if __name__ == "__main__":
    download_stockfish()
