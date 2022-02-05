
accountAhmet = {
    "name" : "Ahmet",
    "accountNo" : "123456",
    "balance" : 3000,
    "extra" : 1000
}


accountSevil = {
    "name" : "Sevil",
    "accountNo" : "654321",
    "balance" : 5000,
    "extra" : 3000
}

def getMoney(account, money):
    print(f'Hi! {account["name"]}')
    askBalance(accountAhmet)

    if (account["balance"] >= money):
        account["balance"] -= money
        print("You can take your money.")
        askBalance(accountAhmet)
    else:
        total = account["balance"] + account["extra"]

        if total >= money:
            useExtra = input("Do you wanna use extra in your account? (y/n) :")

            if useExtra == "y":
                howmanyExtra = money - account["balance"]
                account["balance"] = 0
                account["extra"] -= howmanyExtra               
                print("You can take your money")
                askBalance(accountAhmet)
            else : 
                print(f"You have {account['balance']} in your account number {account['accountNo']}") 
        else :
            print("Sorry! Your balance is not enough")
            askBalance(accountAhmet)


def askBalance(account):
    print(f"You have a {account['balance']}$ in your account number {account['accountNo']}. Your extra limit is {account['extra']}$")

# askBalance(accountSevil)

getMoney(accountAhmet,2000)

print("".center(73,"*"))

getMoney(accountAhmet,3000)

