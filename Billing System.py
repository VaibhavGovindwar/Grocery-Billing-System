from prettytable import PrettyTable

print("------ Welcome to V Grocery Store ------")
table = PrettyTable(["Item Name: ", "Item Price: "])
total1 = 0
while (1):
    name = input("Enter Item Name: ")
    if (name != "q"):
        price = int(input("Enter the price: "))
        total1 += price
        discount = total1 * 5 / 100
        table.add_row([name, price])
        continue
    elif (name == "q"):
        break

total = total1-discount
table.add_row(["Discount", discount])
table.add_row(["Total", total])
print(table)
print("\n Your Total Amount is: ",total)
print("\nThank you for Shopping\n Have a Nice Day")