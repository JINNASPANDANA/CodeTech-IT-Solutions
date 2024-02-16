
print("Welcome to Mirrors of Immortality!")
print("In Mirrors of Immortality, you find yourself drawn into a mystical world where mirrors hold the key to eternal life. As you navigate through this realm, you discover that each mirror represents a different aspect of existence, offering both blessings and curses to those who dare to peer into their depths. Your choices will determine whether you unlock the secrets of immortality or fall victim to the dark forces that lurk within.")

print("\nCHAPTER 1: The Mirror's Call")

print("You stumble upon a hidden chamber adorned with ornate mirrors of various shapes and sizes. A mysterious voice beckons you to choose a mirror and gaze into its surface. As you approach, you sense both intrigue and trepidation coursing through your veins.")
print("What will you do?")

print("1. Choose a mirror and gaze into its depths.")
print("2. Ignore the voice and leave the chamber, seeking answers elsewhere.")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("\nYou choose a mirror and gaze into its depths.")

    print("CHAPTER 2: Reflections of Power")
    print("Gazing into the mirror, you are transported to a realm of boundless energy and raw power.")
    print("You discover that this mirror grants the ability to wield formidable magic, but at a cost.")

    print("What will you do?")

    print("1. Embrace the power of the mirror and become a master of magic, using your abilities to protect the realm.")
    print("2. Reject the allure of power and seek a different path to immortality, wary of the consequences it may bring.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nYou embrace the power of the mirror and become a master of magic..")
        print("\nCHAPTER 3: Echoes of Wisdom")
        print("Congrats you entered into the chapter3,lets begins the journey!")
        print("In another mirror, you find yourself immersed in a realm of ancient knowledge and wisdom.")
        print("Here, the mirror offers enlightenment and insight, guiding those who seek to understand the mysteries of existence.")

        print("What will you do?")

        print("1. Delve deeper into the mirror's wisdom, seeking answers to life's greatest mysteries and unlocking the secrets of immortality.")
        print("2. Shun the knowledge offered by the mirror, fearing the truths it may reveal and opting for a simpler existence.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nYou delve deeper into the mirror's wisdom, seeking answers...")
            print("CHAPTER 4: Shadows of Despair")
            print("As you journey deeper into the realm of mirrors, you encounter one that reflects the darkest recesses of the soul.")
            print("This mirror holds the key to eternal life, but at a grave cost.")

            print("What will you do?")

            print("1. Embrace the darkness within and accept the mirror's offer of immortality, regardless of the consequences.")
            print("2. Reject the mirror's temptations and seek a path that preserves your humanity, even if it means facing mortality.")
            choice = input("Enter your choice (1 or 2): ")

            if choice == "1":
                print("\nYou embrace the darkness within and accept the mirror's offer of immortality...")
                print("\nCHAPTER 5: The Reflections Merge")
                print("In the final chapter, your choices converge as you confront the ultimate mirror, which holds the power to shape your destiny.")
                print("The reflection it offers will determine whether you achieve immortality or fade into obscurity, forever bound by the choices you have made.") 

                print("\nWhat will you do?")
                print("1. Embrace the reflection and accept your fate, whether it leads to eternal life or mortal demise.")
                print("2. Reject the reflection and forge your own path, determined to defy fate and carve out a destiny of your own making.")
                choice = input("Enter your choice (1 or 2): ")

                if choice == "1":
                    print("\nYou embrace the reflection and accept your fate...")
                    print("Congratulations! You Won the Game!!!")

                elif choice == "2":
                    print("\nYou reject the reflection and forge your own path...")

                else:
                    print("Invalid choice. Please enter 1 or 2.")

            elif choice == "2":
                print("\nYou reject the mirror's temptations and seek a path that preserves your humanity...")

            else:
                print("Invalid choice. Please enter 1 or 2.")

        elif choice == "2":
            print("\nYou shun the knowledge offered by the mirror and opt for a simpler existence...")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    elif choice == "2":
        print("\nYou reject the allure of power and seek a different path...")

    else:
        print("Invalid choice. Please enter 1 or 2.")

elif choice == "2":
    print("\nYou ignore the voice and decide to leave the chamber.")
    print("\nYou leave the chamber and get hunted by the ghost.")

else:
    print("Invalid choice. Please enter 1 or 2.")
