"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer
  💡 Making things beautiful
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""
import textwrap

def get_data():
    data = {}
    data["name"] = input("Name: ").strip()
    data["proffession"] = input("Profession: ").strip()
    data["passion"] = input("Passion: ").strip()
    data["emoji"] = input("An emoji you can relate to: ")
    data["website"] = input("Website: ")

    return data

def bio_choice():
    data = get_data()
    print("\nEnter your Choice for Bio")
    print("1. Normal Vertical Lines")
    print("2. Vertical Flair lines")
    print("3. Emoji Sandwich")

    style = int(input("Enter 1, 2 or 3: ").strip())
    result = get_bio(data, style)
    return result

def get_bio(data, style):
    if style == 1:
        return f"{data["emoji"]} {data["name"]} | {data["proffession"]}\n{data["passion"]}\n{data["website"]}"
    elif style == 2:
        return f"{data["emoji"]} {data["name"]}\n{data["proffession"]}🔥\n{data["passion"]}\n{data["website"]}🔥"
    elif style == 3:
        return f"{data["emoji"]*3}\n{data["name"]} - {data["proffession"]}\n{data["passion"]}\n{data["website"]}\n{data["emoji"]*3}"
    else:
        print("Invalid Choice, Go Again (^C to Exit)")
        return bio_choice()

def main():
    bio = bio_choice()
    print("\nYour Stylish Bio:\n")
    print("*" * 50)
    print(textwrap.dedent(bio))
    print("*" * 50)

    save = input("Do you want to save the Bio(y/n): ").strip().lower()
    name = input("Enter your name: ").lower().replace(" ","_")
    if save == "y":
        filename = f"{name}_bio.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(bio)
        print("File Saved")

if __name__ == "__main__":
    main()
