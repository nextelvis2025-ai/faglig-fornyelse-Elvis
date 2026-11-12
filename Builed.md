## Hvordan er programmet bygget?

### 1. Importer biblioteker

I starten af `speech.py` importeres Tkinter til vinduet og kontrollerne.
`pyttsx3` importeres som tale-motoren. `messagebox` bruges til at vise en
fejlbesked, hvis tale-motoren ikke kan startes.

### 2. Opret vinduet og tale-motoren

Klassen `SpeechApp` samler appens brugerflade og funktioner. Når klassen
oprettes, starter den tale-motoren, læser de tilgængelige stemmer og opretter
status og hastighed. Derefter kalder den `_configure_style` og `_build_window`.

### 3. Byg brugerfladen

`_configure_style` definerer farver og udseendet af Tkinter-kontrollerne.
`_build_window` opretter tekstfeltet, scrollbar, stemmelisten, hastighedsskyderen,
knapperne og statuslinjen. Tkinter bruger layoutværktøjet `grid` til at
placere de fleste dele i rækker og kolonner.

Stemmelisten viser et læsbart navn, mens programmet gemmer stemmens interne ID
i `_voice_ids`. Når brugeren starter oplæsningen, kan programmet derfor sende
det korrekte ID til tale-motoren.

### 4. Start oplæsningen

Metoden `_speak` henter tekst fra tekstfeltet. Den kontrollerer først, om
teksten er tom. Hvis den ikke er tom, stopper den eventuel tidligere tale,
indstiller hastighed og stemme og sender teksten til `pyttsx3`.

`_stop` stopper tale-motoren. `_clear_text` tømmer feltet og nulstiller
teksttælleren. `_update_text_count` beregner tegn og ord ud fra indholdet i
tekstfeltet.

### 5. Lad vinduet og tale-motoren arbejde sammen

Tkinter skal kunne reagere på klik og tegne vinduet, samtidig med at
tale-motoren behandler oplæsningen. Derfor starter appen `pyttsx3` med sin egen
event loop slået fra og kalder i stedet `engine.iterate()` regelmæssigt gennem
Tkinter-metoden `after`.

`_iterate_engine` udfører et kort stykke arbejde for tale-motoren og planlægger
det næste kald. Når vinduet lukkes, kalder `_close` `after_cancel`, stopper
talen og afslutter motorens loop. Det forhindrer, at appen fortsætter med at
planlægge opdateringer efter vinduets lukning.

### 6. Start kun appen ved direkte kørsel

Funktionen `main` opretter Tkinter-vinduet, starter `SpeechApp` og starter
Tkinter's hoved-loop. Tjekket `if __name__ == "__main__":` sørger for, at appen
starter, når `speech.py` køres direkte.