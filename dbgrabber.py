import os
import shutil

import requests
from rich import print
from rich.console import Console
from rich.traceback import install
from tqdm import tqdm

install()


console = Console(record=True)

def dbgrab():
    print("[bold red]Downloading Databases![/bold red]")
    #Database
    db_path = r"Userdata.db"
    dst_path = r"Database\\"
    file_path = "Database\\Userdata.db"

    chunk_size = 1024
    url = "https://projectevedb.000webhostapp.com/Userinfo.db"

    r = requests.get(url, stream = True)
    total_size = int(r.headers['content-length'])

    if os.path.isfile(file_path):
        os.remove(file_path)
        with open ("Userdata.db", 'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size = chunk_size), total= total_size/chunk_size, unit= 'KB'):
                f.write(data)
    else:
        with open ("Userdata.db", 'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size = chunk_size), total= total_size/chunk_size, unit= 'KB'):
                f.write(data)

    print("\n[bold yellow]Success[/bold yellow]")
    shutil.move(db_path, dst_path)

# console.save_html("log\\log_dbgrabber.html")