import csv

def add_payment(payment_list):
    """
    Add a new payment to the payment list.
    """
    name = input("Enter the name of the payment: ")
    amount = float(input("Enter the amount of the payment: "))
    payment = {'name': name, 'amount': amount}
    payment_list.append(payment)
    print("Payment added successfully!")

def show_payments(payment_list):
    """
    Show all payments in the payment list.
    """
    print("Payment History:")
    for payment in payment_list:
        print(f"{payment['name']}: ${payment['amount']}")

def save_payments(payment_list):
    """
    Save the payment list to a CSV file.
    """
    with open('payments.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "amount"])
        for payment in payment_list:
            writer.writerow([payment['name'], payment['amount']])
    print("Payments saved successfully!")

def load_payments():
    """
    Load the payment list from the CSV file.
    """
    payment_list = []
    try:
        with open('payments.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                payment = {'name': row['name'], 'amount': float(row['amount'])}
                payment_list.append(payment)
    except FileNotFoundError:
        pass
    return payment_list

def main():
    """
    Main function that runs the payment tracker program.
    """
    payment_list = load_payments()

    while True:
        print("\nPayment Tracker Menu:")
        print("1. Add a payment")
        print("2. Show all payments")
        print("3. Save payments to file")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_payment(payment_list)
        elif choice == "2":
            show_payments(payment_list)
        elif choice == "3":
            save_payments(payment_list)
        elif choice == "4":
            save_payments(payment_list)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
