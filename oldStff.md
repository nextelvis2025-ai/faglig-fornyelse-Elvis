import tkinter as tk
import pyttsx3

engine = pyttsx3.init()


def speak() -> None:
    text = text_box.get("1.0", "end").strip()
    if text:
        engine.say(text)
        engine.runAndWait()


window = tk.Tk()
window.title("Text to Speech yo")


text_box = tk.Text(window, height=10, width=40)
text_box.pack(padx=10, pady=10)

speak_button = tk.Button(window, text="Speak", command=speak)
speak_button.pack(pady=(0, 10))


window.mainloop()




*

import tkinter as tk
from tkinter import messagebox, ttk

import pyttsx3


class SpeechApp:

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Offline Text to Speech")
        self.root.geometry("620x460")
        self.root.minsize(480, 360)

        self.engine = pyttsx3.init()
        self.engine.connect("finished-utterance", self._on_speech_finished)
        self.engine.startLoop(False)

        self._voice_ids: dict[str, str] = {}
        self.status = tk.StringVar(value="Ready")
        self.rate = tk.IntVar(value=175)

        self._build_window()
        self._iterate_id = self.root.after(10, self._iterate_engine)
        self.root.protocol("WM_DELETE_WINDOW", self._close)

    def _build_window(self) -> None:
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        ttk.Label(
            self.root,
            text="Enter text to hear it spoken aloud.",
            padding=(16, 16, 16, 8),
        ).grid(row=0, column=0, sticky="w")

        text_frame = ttk.Frame(self.root, padding=(16, 0, 16, 12))
        text_frame.grid(row=1, column=0, sticky="nsew")
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)

        self.text_input = tk.Text(text_frame, wrap="word", height=10)
        self.text_input.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(
            text_frame, orient="vertical", command=self.text_input.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.text_input.configure(yscrollcommand=scrollbar.set)

        options = ttk.Frame(self.root, padding=(16, 0, 16, 12))
        options.grid(row=2, column=0, sticky="ew")
        options.columnconfigure(1, weight=1)

        ttk.Label(options, text="Voice").grid(row=0, column=0, sticky="w", padx=(0, 12))
        voices = self.engine.getProperty("voices")
        voice_labels: list[str] = []
        for index, voice in enumerate(voices, start=1):
            label = voice.name or f"Voice {index}"
            if label in self._voice_ids:
                label = f"{label} ({index})"
            self._voice_ids[label] = voice.id
            voice_labels.append(label)

        self.voice_choice = ttk.Combobox(
            options,
            values=voice_labels,
            state="readonly" if voice_labels else "disabled",
        )
        self.voice_choice.grid(row=0, column=1, sticky="ew")
        if voice_labels:
            self.voice_choice.current(0)
        else:
            self.voice_choice.set("No voices found")

        ttk.Label(options, text="Speed").grid(
            row=1, column=0, sticky="w", padx=(0, 12), pady=(12, 0)
        )
        tk.Scale(
            options,
            from_=100,
            to=250,
            resolution=10,
            orient="horizontal",
            variable=self.rate,
            showvalue=True,
            length=220,
        ).grid(row=1, column=1, sticky="w", pady=(8, 0))

        buttons = ttk.Frame(self.root, padding=(16, 0, 16, 8))
        buttons.grid(row=3, column=0, sticky="ew")
        self.speak_button = ttk.Button(buttons, text="Speak", command=self._speak)
        self.speak_button.pack(side="left")
        ttk.Button(buttons, text="Stop", command=self._stop).pack(
            side="left", padx=(8, 0)
        )

        ttk.Label(self.root, textvariable=self.status, padding=(16, 0, 16, 12)).grid(
            row=4, column=0, sticky="w"
        )

    def _speak(self) -> None:
        text = self.text_input.get("1.0", "end-1c").strip()
        if not text:
            self.status.set("Type something first.")
            return

        self.engine.stop()
        self.engine.setProperty("rate", self.rate.get())
        selected_voice = self.voice_choice.get()
        if selected_voice in self._voice_ids:
            self.engine.setProperty("voice", self._voice_ids[selected_voice])
        self.engine.say(text)
        self.status.set("Speaking...")

    def _stop(self) -> None:
        self.engine.stop()
        self.status.set("Stopped")

    def _on_speech_finished(self, _: str, completed: bool) -> None:
        if completed:
            self.status.set("Finished")

    def _iterate_engine(self) -> None:
        self.engine.iterate()
        self._iterate_id = self.root.after(10, self._iterate_engine)

    def _close(self) -> None:
        self.root.after_cancel(self._iterate_id)
        self.engine.stop()
        self.engine.endLoop()
        self.root.destroy()


def main() -> None:
    root = tk.Tk()
    try:
        SpeechApp(root)
    except (OSError, RuntimeError) as error:
        messagebox.showerror("Text to Speech", f"Could not start speech: {error}")
        root.destroy()
        raise SystemExit(1) from error
    root.mainloop()


if __name__ == "__main__":
    main()
    