import requests
import json
import time
import os
import platform
import progressbar
from pathlib import Path
from rich import print
from rich.prompt import Prompt
from rich.traceback import install
from rich.console import Console
import art
install()

console = Console()

def imagegen():
    url = "https://api.openai.com/v1/images/generations"


    api_key = "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"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    os.system("cls||clear")
    art.art3()
    while True:
        path = os.path.expanduser("~/Documents/ProjectEve/GeneratedImages")
        if not os.path.exists(path):
            os.makedirs(path)

        print("")
        print("")
        console.print("Prompt to be generated to an Image: ", style="bold blue")
        prompt = Prompt.ask("")
        print("")

        num_images = 1

        size = "512x512"


        widgets = [progressbar.AnimatedMarker(), 'Generating images: ', progressbar.Percentage(), ' ', progressbar.Bar(marker='=', left='[', right=']'), ' ', progressbar.ETA()]
        bar = progressbar.ProgressBar(widgets=widgets, maxval=num_images).start()

        output_dir = Path.home() / "Documents" / "ProjectEve" / "GeneratedImages"
        output_dir.mkdir(parents=True, exist_ok=True)

        for i in range(num_images):

            timestamp = int(time.time())
            filename = f"generated_image_{timestamp}_{i}.png"

            data = {
                "model": "image-alpha-001",
                "prompt": prompt,
                "num_images": 1,
                "size": size
            }

            response = requests.post(url, headers=headers, data=json.dumps(data))

            try:
                image_url = response.json()["data"][0]["url"]
            except KeyError:
                print(response.text)
                break

            response = requests.get(image_url)

            output_file = output_dir / filename
            with open(output_file, "wb") as f:
                f.write(response.content)

            if platform.system() == 'Darwin':    # macOS
                os.system('open {}'.format(output_file))
            elif platform.system() == 'Windows': # Windows
                os.system('start {}'.format(output_file))
            else:                                # Linux
                os.system('xdg-open {}'.format(output_file))

            bar.update(i+1)

        bar.finish()

# console.save_html("log\\log_imagegen.html")