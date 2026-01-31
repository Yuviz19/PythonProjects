"""
Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.
"""

def bill(n):
    total_amount = float(input("Total Bill: "))
    share = round(total_amount / n, 2)
    return share

def main():
    num_people = int(input("How many people are there in your group? "))
    names = []

    for i in range(num_people):
        name = input(f"Enter the name of person {i+1}: ")
        names.append(name)

    share = bill(num_people)
    print("*" * 50)    
    for name in names:
        print(f"Each person owes {share} rupees")
    print("*" * 50)

if __name__ == "__main__":
    main()
