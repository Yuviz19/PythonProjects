"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""
import datetime

def main():
    journal = input("What did you learn today?\n>> ")
    try:
        rate = int(input("\nHow well do you think you did today?(1-5)"))
        if rate not in range(1,6):
            raise ValueError
    except ValueError:
        print("There was a Value Error Sir..\nExiting Program")
        return

    timestamp = datetime.datetime.now()
    date_str = timestamp.strftime("%Y-%m-%d %H:%M")

    journal_entry = f"\n{'*' * 30}\n[{date_str}]\n{journal}\nProductivity Rating: {rate}/5\n" 
    with open("daily_journal.txt","a",encoding="utf-8") as f:
        f.write(journal_entry)

if __name__ == "__main__":
    main()
