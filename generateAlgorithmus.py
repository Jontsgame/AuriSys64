import json

# Beispiel-Fragen und Antworten
fragen_antworten = {
    "wie geht es dir": "Mir geht es gut, danke!",
    "was ist dein name": "Ich bin dein virtueller Assistent iLexa.",
    "was kannst du tun": "Ich kann dir bei verschiedenen Aufgaben helfen.",
    "wie ist das wetter": "Ich kann dir die aktuelle Wettervorhersage sagen."
}

# Anzahl der gewünschten Fragen
anzahl = 1500

# Fragen generieren (indem vorhandene Fragen variiert oder erweitert werden)
fragen_dict = {}
for i in range(anzahl):
    frage, antwort = list(fragen_antworten.items())[i % len(fragen_antworten)]
    fragen_dict[f"{frage} {i}"] = antwort  # Variation der Fragen

# JSON speichern
with open("fragen.json", "w", encoding="utf-8") as file:
    json.dump(fragen_dict, file, indent=4, ensure_ascii=False)

print("1500 Fragen wurden erfolgreich generiert und gespeichert.")
