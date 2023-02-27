import os
import time

import openai
import pyttsx3
import speech_recognition as sr
from colorama import Fore
from rich import print
from rich.console import Console
from rich.traceback import install

import art
import imagegen
from art import mainart

install()

console = Console(record=True)

Voice = False
voicemodel = 2
voicespeed = 2
openai.api_key = ("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")

def assistant():

    art.art1()
    def menu1():
        while True:
            choice = input("Response: ")
            if choice == "1":
                os.system("cls||clear")
                program()
                break
            elif choice == "3":
                os.system("cls||clear")
                print("[bold red]_______Settings_______[/bold red]")
                print(r'''[bold purple]
                [A] Change Assistant Voice.
                [B] Change Assistant Voice Speed.
                [C] Change API(May cause errors!)
                (//) Back!
                [/bold purple]
                ''')
                menu2()
            elif choice == "2":
                imagegen.imagegen()
                menu2()
            elif choice == "4":
                print("Exit")
                break
            else:
                print("Invalid Selection!")

    def menu2():
        while True:
            choice = input("\nResponse: ")
            if choice == "A" or choice == "a":
                print("[bold blue]\nAi Voice Settings.[/bold blue]")
                ai_voice()
            elif choice == "B" or choice == "b":
                print("[bold blue]\nAi voice speed Settings.[/bold blue]")
                ai_voice_speed()
            elif choice == "C" or choice == "c":
                print("[bold blue]Api key Settings![/bold blue]")
            elif choice == "//":
                os.system("cls||clear")
                master()
            else:
                print("[bold red]Invalid Response![/bold red]")

    def master():
        print(r'''[bold blue]
        [1] AI ChatBot.
        [2] Text To Image AI.
        [3] Settings.
        [4] Exit.
        [/bold blue]
        ''')
        menu1()

    def ai_voice_speed():
        global voicespeed
        print("[bold green]Default speed set to 150! You may change from here![/bold green]\n")
        while True:
            print("--Options--")
            print("[1]Slow speaking rate")
            print("[2]Default speaking rate")
            print("[3]Fast speaking rate")
            choice = input("\nResponse: ")
            if choice == "1":
                voicespeed = 1
                print("Ai voice set to Slow speaking rate!")
                os.system("clear||cls")
                print("Press 3 for Settings or 1 to continue to ChatBot or 2 to ImageBot!")
                menu1()
                print("[bold red]_______Settings_______[/bold red]")
                print(r'''[bold purple]
                                            [A] Change Assistant Voice.
                                            [B] Change Assistant Voice Speed.
                                            [C] Change API(May cause errors!)
                                            (//) Back!
                                            [/bold purple]
                                            ''')
                break
            if choice == "2":
                voicespeed = 2
                print("Ai voice set to Default speaking rate!")
                os.system("clear||cls")
                print("Press 3 for Settings or 1 to continue to ChatBot or 2 to ImageBot!")
                menu1()
                print("[bold red]_______Settings_______[/bold red]")
                print(r'''[bold purple]
                                            [A] Change Assistant Voice.
                                            [B] Change Assistant Voice Speed.
                                            [C] Change API(May cause errors!)
                                            (//) Back!
                                            [/bold purple]
                                            ''')
                break
            if choice == "3":
                voicespeed = 3
                print("Ai voice set to Fast speaking rate!")
                os.system("clear||cls")
                print("Press 3 for Settings or 1 to continue to ChatBot or 2 to ImageBot!")
                menu1()
                print("[bold red]_______Settings_______[/bold red]")
                print(r'''[bold purple]
                                            [A] Change Assistant Voice.
                                            [B] Change Assistant Voice Speed.
                                            [C] Change API(May cause errors!)
                                            (//) Back!
                                            [/bold purple]
                                            ''')
                break

    def ai_api():
        print("--Options--")
        print("[bold red]Changing Api key may cause program failures.[/bold red]")
        choice = input("\nNew Api Key: ")
        openai.api_key = (choice)

    def ai_voice():
        global voicemodel
        while True:
            print("--Options--")
            print("[1] Male voice")
            print("[2] Female voice")
            choice = input("\nResponse: ")
            if choice == "1":
                voicemodel = 1
                os.system("cls||clear")
                print("AI Voice changed to Male Voice!")
                print("Press 3 for Settings or 1 to continue to ChatBot or 2 to ImageBot!")
                menu1()
                print("[bold red]_______Settings_______[/bold red]")
                print(r'''[bold purple]
                            [A] Change Assistant Voice.
                            [B] Change Assistant Voice Speed.
                            [C] Change API(May cause errors!)
                            (//) Back!
                            [/bold purple]
                            ''')
                break
            elif choice == "2":
                voicemodel = 2
                os.system("cls||clear")
                print("AI Voice Changed to Female Voice!")
                print("Press 3 for Settings or 1 to continue to ChatBot or 2 to ImageBot!")
                menu1()
                print("[bold red]_______Settings_______[/bold red]")
                print(r'''[bold purple]
                                        [A] Change Assistant Voice.
                                        [B] Change Assistant Voice Speed.
                                        [C] Change API(May cause errors!)
                                        (//) Back!
                                        [/bold purple]
                                        ''')
                break
            else:
                print("Invalid Response!")

    master()

def program():
    mainart()

    ai_voice = input(f"{Fore.RED} Do you want to turn on the AI's voice response (y/n)?: ")
    ai_voice = ai_voice.lower()
    if ai_voice == "y":
        print("AI may talk now!")


    r = sr.Recognizer()

    while True:

        ask = input(f'\n {Fore.GREEN}Question: {Fore.CYAN}')
        if ask == "voice off":
            ai_voice == "f"
            print("Voice Turned off!")
            break
        else:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=ask,
                temperature=0.9,
                max_tokens=1000,
                top_p = 1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " Ai:"]
              )
            text = response['choices'][0]['text']
            print('Reply: ')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.03)
            print("")
            


        if ai_voice == "y":
            engine = pyttsx3.init()
            if voicespeed == "1":
                engine.setProperty('rate', 110)
            elif voicespeed == "2":
                engine.setProperty('rate', 150)
            elif voicespeed == "3":
                engine.setProperty('rate', 170)
            eng = pyttsx3.init()
            voice = eng.getProperty('voices')
            if voicemodel == "1":
                eng.setProperty('voice', voice[0].id)
            elif voicemodel == "2":
                eng.setProperty('voice', voice[1].id)
            engine.say(text)
            engine.runAndWait()

# console.save_html("log\\log_ai.html")