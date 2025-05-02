import json

# JSON-Datei einlesen
with open("datas.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Funktion zum Bearbeiten der "question"-Felder
def lowercase_questions(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "question" and isinstance(value, str):
                obj[key] = value.lower().replace("?", "")  # Kleinschreibung + Fragezeichen entfernen
            else:
                lowercase_questions(value)
    elif isinstance(obj, list):
        for item in obj:
            lowercase_questions(item)

# JSON-Daten bearbeiten
lowercase_questions(data)

# Neue JSON-Datei speichern
with open("bereinigte_daten.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Alle 'question'-Felder wurden in Kleinbuchstaben umgewandelt und Fragezeichen entfernt.")
