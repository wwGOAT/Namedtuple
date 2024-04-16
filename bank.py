

user = int(input("Enter money: "))

bank_money = {
    '200': 10,
    '100': 20,
    '50': 30,
    '20': 15,
    '10': 25,
    '5': 50,
}

bank = CalculateMoney(user, bank_money)
bank.calculate_num_of_sum()
