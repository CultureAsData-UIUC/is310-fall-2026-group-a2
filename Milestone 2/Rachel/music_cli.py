import csv

with open("music_collaborations.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    songs = list(reader)

while True:
    print("\n===== Music Collaboration Explorer =====")
    print("1. View All Collaborations")
    print("2. Search Collaborations by Artist")
    print("3. Explore Collaboration Credits")
    print("4. Explore Record Labels")
    print("5. Explore Song Versions")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")


    if choice == "1":
        for song in songs:
            print(song["Song Title"], "-", song["Pop Artist"],
                  "ft.", song["Collaborating Artist"],
                  "(", song["Release Year"], ")")


    elif choice == "2":
        while True:
            artist_name = input("Enter the artist name to search for collaborations: ").strip()

            if not artist_name:
                print("Please enter an artist name.")
                continue

            found = False

            for song in songs:
                if (artist_name.lower() in song["Pop Artist"].lower() or
                    artist_name.lower() in song["Collaborating Artist"].lower()):

                    print(song["Song Title"], "-", song["Pop Artist"],
                          "ft.", song["Collaborating Artist"],
                          "(", song["Release Year"], ")")
                    found = True

            if found:
                break

            print("No collaborations found.")
            retry = input("Retry? (Y/N): ").strip().lower()

            if retry != "y":
                break

    elif choice == "3":
        for song in songs:
            print(song["Song Title"], "-", song["Pop Artist"], song["Collaboration Credit"])
    
    elif choice == "4":
        print("\n===== Record Labels =====")

        for song in songs:
            print("\n" + "-" * 45)
            print(song["ID"] + ". " + song["Song Title"],
                "(" + song["Release Year"] + ")")

            print("Artists:", song["Pop Artist"],
                "ft.", song["Collaborating Artist"])

            label = song["Song/ Release Label"].strip()

            if label:
                print("Label:", label)
            else:
                print("Label: Unknown")

        print("\n" + "-" * 45)

        view_notes = input(
            "\nWould you like to view dataset notes? (Y/N): "
        ).strip().lower()

        if view_notes == "y":
            print("\n===== Dataset Notes =====")

            notes_found = False

            for song in songs:
                note = song["Notes"].strip()

                if note:
                    print("\n" + "-" * 45)
                    print(song["Song Title"],
                        "(" + song["Release Year"] + ")")
                    print("Label:",
                        song["Song/ Release Label"] or "Unknown")
                    print("Note:", note)

                    notes_found = True

            if not notes_found:
                print("No dataset notes available.")

    elif choice == "5":
        for song in songs:
            print(song["Song Title"], "-", song["Song Version"])

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
