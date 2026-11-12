## Lidt om Python

Python er et fortolket, objektorienteret programmeringssprog på højt niveau med dynamisk semantik. Dets indbyggede datastrukturer på højt niveau, kombineret med dynamisk typning og dynamisk binding, gør det særdeles velegnet til hurtig applikationsudvikling (Rapid Application Development) samt til brug som scriptsprog eller "limsprog" til at forbinde eksisterende komponenter. Pythons enkle syntaks, der er let at lære, vægter readability højt, hvilket reducerer omkostningerne ved vedligeholdelse af programmer siger de. 

Python understøtter modules og packages, hvilket fremmer genbrug af kode. Python's standardbibliotek er tilgængelige – enten som kildekode eller i binær form – uden beregning til alle gængse platforme og må distribueres frit.

Programmører bliver ofte begejstrede for Python på grund af den øgede produktivitet, sproget giver. Da der ikke er noget kompileringsskrin, er cyklussen med at redigere, teste og fejlfinde ekstremt hurtig. Det er nemt at fejlfinde Python-programmer: En fejl eller ugyldig input vil aldrig føre til en "segmentation fault" (hukommelsesfejl). I stedet udløser fortolkeren en undtagelse (exception), når den støder på en fejl. Hvis programmet ikke håndterer denne undtagelse, udskriver fortolkeren en "stack trace" (en oversigt over kaldstakken). En debugger på kildekodeniveau gør det muligt at inspicere lokale og globale variabler, evaluere vilkårlige udtryk, sætte "breakpoints" (afbrydelsespunkter), gennemgå koden linje for linje osv. Selve debuggeren er skrevet i Python, hvilket vidner om sprogets evne til selvinspektion (introspektion). På den anden side er den hurtigste måde at fejlfinde et program ofte blot at tilføje et par "print"-instruktioner i kildekoden; den hurtige cyklus med redigering, test og fejlfinding gør denne simple metode yderst effektiv.


## Dowload pyttsx3

pip install pyttsx3

## Start tekst-til-tale-programmet

Programmet bruger `pyttsx3` til at tale med stemmer, der allerede er installeret på computeren. Teksten sendes ikke til en online tjeneste.


# Kom godt i gang: SpeakEasy

## Hvad er SpeakEasy?

SpeakEasy er et lille tekst-til-tale-program til Windows. Du skriver eller
indsætter tekst i programmet, vælger en stemme og en hastighed, og programmet
læser teksten højt. Programmet er lavet i Python med Tkinter til vinduet og
`pyttsx3` til tale.

SpeakEasy bruger stemmer, der allerede findes på computeren. Det betyder, at
teksten ikke sendes til en online tale-tjeneste. Det betyder også, at de
tilgængelige stemmer og deres kvalitet afhænger af computeren.

## Problem og formål

Det kan være lettere at lytte til en tekst end at læse den på en skærm. Et
tekst-til-tale-program kan for eksempel bruges til at lytte til egne noter,
korrekturlæse en tekst ved at høre den læst op eller gøre tekst mere
tilgængelig for personer, der foretrækker lyd.

Projektet
viser blandt andet, hvordan et program kan modtage tekst, give brugeren nogle
valg og sende en handling videre til et eksternt bibliotek.

## Funktioner

- Tekstfelt: Skriv eller indsæt teksten, der skal læses op.
  
- Stemmevalg: Du kan vælg mellem de stemmer, som kan findes på
  computeren.

- Hastighed: Ryk på knapen til at ændre taletempoet.

- Stop: Stop den tale, der er i gang.

- Clear text: Tøm tekstfeltet og nulstil tælleren.

- Teksttæller: Vis antal tegn og ord, mens teksten ændres.


## Det skal du bruge

- En computer med Python installeret. og mine projektets filer, `speech.py` og `requirements.txt`. Du skal også dowloded `pyttsx3` og have nogen stemme på din computer.

Note. Projektet er udviklet og testet på Windows.


## Sådan bruger du programmet

1. Start programmet med den fulde `.venv`-sti som vist sener.

2. Skriv eller indsæt tekst i det store tekstfelt.

3. Vælg en stemme i listen. Listen viser de stemmer, som programmet finder på
   computeren.

4. Flyt hastighedsskyderen, hvis du vil have teksten læst langsommere eller
   hurtigere.

5. Klik på **Speak** for at starte oplæsningen.

6. Klik på **Stop**, hvis du vil afbryde oplæsningen.

7. Klik på **Clear text** for at tømme tekstfeltet.


## Stemmer

SpeakEasy bruger computerens installerede stemmer og forsøger ikke at hente
andre stemmer. Kontrollér computerens tale- eller tilgængelighedsindstillinger
for at se, hvilke stemmer der er installeret. Stemmerne kan variere mellem
computere.



## Kort opsummering

SpeakEasy forbinder en grafisk brugerflade lavet med Tkinter med en lokal
tale-motor via `pyttsx3`.


## Kør

Åbn en terminal i projektmappen, og kør:


```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python speech.py
```



.\.venv\Scripts\python.exe .\Produtype.py



.\.venv\Scripts\python.exe speech.py



1. Åbn en terminal i projektmappen.
2. Kør `node serve_web.js`.
3. Åbn `http://localhost:8000` i browseren.
4. Skriv “In the end”, og klik på “Play background music”, hvis browseren
   blokerer automatisk afspilning.







```py

consol.log()


``` 











## Første skridt til at lave dit egen text to specch program.

- Python skal saføling værert installeret og pyttsx3 skal også dowlodeds.

## Så skal vi impoter nogen ting

```python
import tkinter as tk
from tkinter import messagebox, ttk

import pyttsx3
```

## derefter skal vi programer et vindue med egenskaberne.

```python
class SpeechApp:
   
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Offline Text to Speech")
        self.root.geometry("620x460")
        self.root.minsize(480, 360)

        # Start pyttsx3 uden dens egen blocking loop så Tkinter kan lave button clicks og vindu updates på samme tid.
        self.engine = pyttsx3.init()
        self.engine.connect("finished-utterance", self._on_speech_finished)
        self.engine.startLoop(False)

        # Dette sørgr for, at de viste stemmenavne er knyttet til de IDs, der anvendes af pyttsx3.
        self._voice_ids: dict[str, str] = {}
        self.status = tk.StringVar(value="Ready")
        self.rate = tk.IntVar(value=175)

        self._build_window()
        # Bed Tkinter om at lade tale-motoren udføre lidt arbejde hvert 10 ms.
        self._iterate_id = self.root.after(10, self._iterate_engine)
        self.root.protocol("WM_DELETE_WINDOW", self._close)

    def _build_window(self) -> None:
        """Add the text box, voice and speed controls, buttons, and status."""
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Tekstfeltet udvider sig sammen med vinduet og får en rullebjælke, hvis teksten er lang.
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

        # Læs op med stemmer fra computeren.
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

        # Her biver funstion der styer hvor hurtig det få lavet.
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
```




 ## opstartsfunktionen ser sådan ud:

```python

def main() -> None:
    root = tk.Tk()
    try:
        SpeechApp(root)
    except (OSError, RuntimeError) as error:
        messagebox.showerror("Text to Speech", f"Could not start speech: {error}")
        root.destroy()
        raise SystemExit(1) from error
    root.mainloop()
```





## Hvad der sker når man trykker på Speak

Knappen kalder `_speak()`. Først henter metoden teksten fra tekstfeltet:

```python
text = self.text_input.get("1.0", "end-1c").strip()
if not text:
    self.status.set("Type something first.")
    return
```

I Tkinter betyder `"1.0"` starten af tekstfeltet. `"end-1c"` betyder slutningen
minus det ekstra linjeskift, som Tkinter holder sidst i feltet. `strip()`
fjerner mellemrum og linjeskift i starten og slutningen.

Hvis teksten er tom, viser `if not text` en besked. `return` afslutter metoden,
så programmet ikke prøver at læse tom tekst op.

Derefter vælges hastighed og stemme, og oplæsningen sættes i gang:

```python
self.engine.stop()
self.engine.setProperty("rate", self.rate.get())

selected_voice = self.voice_choice.get()
if selected_voice in self._voice_ids:
    self.engine.setProperty("voice", self._voice_ids[selected_voice])

self.engine.say(text)
self.status.set("Speaking...")
```

`self.rate.get()` henter værdien fra hastighedsskyderen. 

`voice_choice.get()`
henter det valgte navn fra listen. Programmet slår navnet op i
`_voice_ids` for at finde det ID, som tale-motoren bruger.

`say(text)` giver teksten til tale-motoren, og status ændres til
“Speaking...”. Det forrige opkald til `stop()` afbryder eventuel tidligere
oplæsning, inden den nye begynder.

## og her laver du Stop-knappen

```python
def _stop(self) -> None:
    self.engine.stop()
    self.status.set("Stopped")

def _on_speech_finished(self, _: str, completed: bool) -> None:
    if completed:
        self.status.set("Finished")

def _iterate_engine(self) -> None:
    self.engine.iterate()
    self._iterate_id = self.root.after(10, self_iterate_engine)
```

## Luk tale-motoren ned

```python
def _close(self) -> None:
    self.root.after_cancel(self._iterate_id)
    self.engine.stop()
    self.engine.endLoop()
    self.root.destroy()
```