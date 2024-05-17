import tempfile, customtkinter, ctypes
import tkinter as tk
import soundfile as sf
import sounddevice as sd
from gtts import gTTS, lang
from tkinter import filedialog


# Base window
class Root(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.title("Text to speech")
        self.resizable(False, False)

        # Label
        self.label = customtkinter.CTkLabel(self, text="Text To Speech")
        self.label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Type menu
        self.type_menu = customtkinter.CTkOptionMenu(
            self,
            values=[".wav", ",mp3"],
            width=90,
            height=20,
        )

        # Language Menu
        self.language_menu = customtkinter.CTkOptionMenu(
            self,
            values=[
                "Greek",
                "English",
                "Afrikaans",
                "Czech",
                "Danish",
                "German",
                "Hindi",
                "Hungarian",
                "Italian",
                "Japanese",
                "Korean",
                "Norwegian",
                "Polish",
                "Portuguese",
                "Russian",
                "Spanish",
                "Swedish",
                "Turkish",
            ],
            width=90,
            height=20,
        )
        self.language_menu.place(relx=0.12, rely=0.4, anchor=tk.CENTER)

        # URL Input
        self.text_input = customtkinter.CTkEntry(
            self, width=200, height=40, placeholder_text="Enter a text"
        )
        self.text_input.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Play Button
        self.play_button = customtkinter.CTkButton(
            self, width=70, height=30, text="Play", state="normal", command=playSound
        )
        self.play_button.place(relx=0.87, rely=0.4, anchor=tk.CENTER)

        # Save Button
        self.save_button = customtkinter.CTkButton(
            self, width=100, height=30, text="Save", command=saveSound
        )
        self.save_button.place(relx=0.35, rely=0.7, anchor=tk.CENTER)

        # Reset Button
        self.reset_button = customtkinter.CTkButton(
            self, width=100, height=30, text="Reset", command=reset
        )
        self.reset_button.place(relx=0.65, rely=0.7, anchor=tk.CENTER)

        self.toplevel_window = None


# Convert text to speech
def getSound():

    text = root.text_input.get()

    if text == "":
        ctypes.windll.user32.MessageBoxW(0, "Insert a text", "Error", 0)
        return

    language = root.language_menu.get()

    match language:
        case "Greek":
            speech = gTTS(text=text, lang="el", slow=False)
        case "English":
            speech = gTTS(text=text, lang="en", slow=False)
        case "Afrikaans":
            speech = gTTS(text=text, lang="af", slow=False)
        case "Czech":
            speech = gTTS(text=text, lang="cs", slow=False)
        case "Danish":
            speech = gTTS(text=text, lang="da", slow=False)
        case "German":
            speech = gTTS(text=text, lang="de", slow=False)
        case "Hindi":
            speech = gTTS(text=text, lang="hi", slow=False)
        case "Hungarian":
            speech = gTTS(text=text, lang="hu", slow=False)
        case "Italian":
            speech = gTTS(text=text, lang="it", slow=False)
        case "Japanese":
            speech = gTTS(text=text, lang="ja", slow=False)
        case "Korean":
            speech = gTTS(text=text, lang="ko", slow=False)
        case "Norwegian":
            speech = gTTS(text=text, lang="no", slow=False)
        case "Polish":
            speech = gTTS(text=text, lang="pl", slow=False)
        case "Portuguese":
            speech = gTTS(text=text, lang="pt", slow=False)
        case "Russian":
            speech = gTTS(text=text, lang="ru", slow=False)
        case "Spanish":
            speech = gTTS(text=text, lang="es", slow=False)
        case "Swedish":
            speech = gTTS(text=text, lang="sv", slow=False)
        case "Turkish":
            speech = gTTS(text=text, lang="tr", slow=False)

    return speech


# Play sound
def playSound():

    sound = getSound()

    # Open temp file, save and play sound
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        sound.save(f.name)
        data, fs = sf.read(f.name)
        sd.play(data, fs)
        sd.wait()


# Save sound
def saveSound():

    sound = getSound()

    if sound is not None:
        output_file_path = filedialog.asksaveasfilename(
            defaultextension=".mp3", filetypes=[("wav", "*.wav"), ("mp3", "*.mp3")]
        )
        if output_file_path:
            sound.save(output_file_path)


# Reset
def reset():

    global speech
    root.text_input.delete(0, tk.END)
    root.language_menu.set("Greek")


# Start main loop
root = Root()
root.mainloop()
