def create_anki_file(input_path, output_path):

    # Importing from file

    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    cards = []

    for i in range(0, len(lines), 3):
        eng = lines[i]
        pol = lines[i+2]
        cards.append((eng, pol))  # english -> polish
        cards.append((pol, eng))  # other way

    # Writing into a file, separated by \t - tabulator
    with open(output_path, "w", encoding="utf-8") as out:
        for front, back in cards:
            out.write(f"{front}\t{back}\n")
    print(f"All success")

# Use how you like:
create_anki_file("flashcards.txt", "output_cards.txt")
