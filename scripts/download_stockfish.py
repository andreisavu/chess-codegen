import os
import requests
import tarfile
import platform

def download_stockfish():
    url = ""
    if platform.system() == "Linux":
        url = "https://github.com/official-stockfish/Stockfish/releases/latest/download/stockfish-ubuntu-x86-64-avx2.tar"
    elif platform.system() == "Darwin":
        url = "https://github.com/official-stockfish/Stockfish/releases/latest/download/stockfish-macos-m1-apple-silicon.tar"

    response = requests.get(url)
    os.makedirs("bin", exist_ok=True)
    tar_path = os.path.join("bin", "stockfish.tar")
    with open(tar_path, "wb") as f:
        f.write(response.content)

    with tarfile.open(tar_path, "r") as tar_ref:
        tar_ref.extractall("bin")

    os.chmod(os.path.join("bin", "stockfish"), 0o755)
    os.remove(tar_path)

if __name__ == "__main__":
    download_stockfish()
