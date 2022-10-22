from ast import main
from datetime import date, datetime
from operator import truediv
import os
from pickle import TRUE
from time import sleep
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import math
import random

class Bank:
    money = open("bank_balance.txt","r")
    balanceA = money.read()
    balance = int(balanceA)
    money.close()
    def update(self):
        f1= open("bank_balance.txt","w")
        f1.write(str(Bank.balance))
        f1.close()

bankobject = Bank()
    
class wallet:
    money1 = open("wallet_balance.txt","r")
    balanceB = money1.read()
    balance = int(balanceB)
    money1.close()
    blk_mom = "U"
    blk_lucy = "U"
    blk_simba = "U"
    blk_jack = "U"
    blk_alex = "U"
    blk_maria= "U"
    blk_maggie= "U"
    blk_john= "U"
    blk_sandra="U"
    blk_kratos="U"
    blk_alan="U"
    def update_wallet(self):
        f2= open("wallet_balance.txt","w")
        f2.write(str(wallet.balance))
        f2.close()
    def transfer_wallet(self):
        print('Transfer Money from Bank to Wallet')
        print('Available balance in Bank is', Bank.balance )
        trans_amount = int(input('Enter the amount to be transferred from the bank to Wallet'))
        if trans_amount< Bank.balance :
            wallet.balance = wallet.balance + trans_amount
            Bank.balance = Bank.balance - trans_amount
            print('bank balance',Bank.balance)
            print('Wallet Balance is ', wallet.balance)
            bankobject.update()
            walletobject.update_wallet()
            admin_obj.admin_menu()
        else:
            print('Insufficient Balance in Bank account')
            return wallet.balance
walletobject = wallet()

def generateOTP() :             # function to generate OTP
    digits = "0123456789"
    OTP = ""
    # length of password can be changed
    for i in range(4) :# by changing value in range
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

class Admin(wallet):
    def admin_login(self):
        print('\n\t ----------------Admin Login Menu------------------ \n')
        print('\n')
        admin_id = input('\nEnter the User ID\n')
        admin_pass = input('\nEnter the Password\n')
        admin_file = open("Admin_db.txt","r")
        for line in admin_file:
            login_admin = line.strip().split(",")
            if admin_id == login_admin[0] and admin_pass == login_admin[2] :
                print('\n------------Welcome', login_admin[1],'------------' )
                self.admin_menu()
                return True
            elif admin_id == 'mom' and admin_pass == login_admin[2] and wallet.blk_mom == "U":
                self.admin_menu()
            elif admin_id == "mom" and admin_pass == login_admin[2] and wallet.blk_mom == "B":    
                main_m.main_menu(self)
                print('You entered the wrong Password or username')
                main_m.main_menu(self)
        
    def withdraw(self):
        amount_withdraw = int(input('Enter the amount to be withdrawn from the wallet and transferred to the bank'))
        if amount_withdraw > wallet.balance or amount_withdraw <= 0 or wallet.balance ==0:
            print('Invalid input please check the amount entered')
        else:
            wallet.balance = wallet.balance - amount_withdraw
            Bank.balance = Bank.balance + amount_withdraw
            bankobject.update()
            walletobject.update_wallet()
            print('\n\tUpdated Wallet Balance is   \t' , wallet.balance)  
            self.admin_menu()
    def pay(self) :
        name = input('Enter the name of the Vendor/shop')
        amount = int(input('Enter the amount to be Paid'))
        dt = datetime.now()
        if amount > wallet.balance or wallet.balance==0 :
            print('TRANSACTION DECLINED ! Insufficient Balance, please add money to your wallet')
            main_m.main_menu(self)
            dt = datetime.now()
            main_m.main_menu(self)
        else:
            Payee = input("Enter your Name ")
            print('Payment successful to '+ name + ' at ', dt)
            wallet.balance = wallet.balance - amount
            walletobject.update_wallet()
            print('Available Wallet balance :', wallet.balance)
            transact_file = open("transact.txt","a")
            transact_file.write('\n')
            transact_file.write('\n Paid By : '+ Payee + '    Vendor Name : '+str(name) + '    Amount Paid :' + str(amount) + '   Time : '+ str(dt) )
            transact_file.write('\n')
            transact_file.close()
            main_m.main_menu(self)
            
    def blocking(self):
        blkk =input("Select the correct choice for blocking \n 1. Lucy \n 2. Simba \n 3. Jack \n 4. Alex \n 5.Maria \n 6.Maggie \n7. John \n8.Sandra .\n9. Jenny (mom)")
        if blkk == "1":
            wallet.blk_lucy= "B"                                   
            main_m.main_menu(self)
        elif blkk == "2":
            wallet.blk_simba = "B"
            main_m.main_menu(self)
        elif blkk == "3":
            wallet.blk_jack = "B"
            main_m.main_menu(self)
        elif blkk =="4":
            wallet.blk_alex = "B"
            main_m.main_menu(self)
        elif blkk =="5":
            wallet.blk_maria = "B"
            main_m.main_menu(self)
        elif blkk =="6":
            wallet.blk_maggie = "B"
            main_m.main_menu(self)
        elif blkk =="7":
            wallet.blk_john = "B"
            main_m.main_menu(self)
        elif blkk =="8":
            wallet.blk_sandra = "B"
            main_m.main_menu(self)
        elif blkk =="9":
            wallet.blk_mom = "B"
            main_m.main_menu(self)
    

    def unblocking(self):
        bk = input("Select the correct choice for Unblocking \n 1. Lucy \n 2. Simba \n 3. Jack \n 4. Alex \n 5.Maria \n 6.Maggie \n7. John \n8.Sandra .")
        if bk == "1":
            wallet.blk_lucy = "U"                                   
            main_m.main_menu(self)
        elif bk == "2":
            wallet.blk_simba = "U"
            main_m.main_menu(self)
        elif bk == "3":
            wallet.blk_jack = "U"
            main_m.main_menu(self)
        elif bk =="4":
            wallet.blk_alex = "U"
            main_m.main_menu(self)
        elif bk =="5":
            wallet.blk_maria = "U"
            main_m.main_menu(self)
        elif bk =="6":
            wallet.blk_maggie = "U"
            main_m.main_menu(self)
        elif bk =="7":
            wallet.blk_john = "U"
            main_m.main_menu(self)
        elif bk =="8":
            wallet.blk_sandra = "U"
            main_m.main_menu(self)
        elif bk =="9":
            wallet.blk_mom = "U"
            main_m.main_menu(self)
        
    def view_trans(self):
        transact = open("transact.txt","r")
        transaction =transact.read()
        transact.close()
        print(transaction)
        main_m.main_menu(self)


    def admin_menu(self):
        print("\n\nWallet Balance is----- ",wallet.balance)
        print('1.Transfer Money from the Bank')
        print('2.Pay')
        print('3. Withdraw')
        print('4.View Transaction')
        print('5. Block Or Unblock a person')
        print('6. Go back to Main Menu ')
        print('7. Quit')
        sub_menu = input('Please select the operation you want to perform(1/2/3/4/5/6)')
   
        if sub_menu == '1': 
            walletobject.transfer_wallet()
        elif sub_menu == '2':
            self.pay()
        elif sub_menu =='3':
            self.withdraw()
        elif sub_menu =='4':
            print("\n")
            self.view_trans()
        elif sub_menu == '5' :
            i1 = input("1. Block a user \n 2. Unblock a person")
            if i1== "1":
                self.blocking()
            elif i1=="2":
                self.unblocking()
        elif sub_menu == '6' :
            main_m.main_menu(self)
        else:
            print("!!! Invalid Option! Please read the option carefully! !!!!!!!!!!!\n")
admin_obj = Admin()        
    

class Child(Admin) :
    count = 0 
    def child_login(self):
        print('\n\t ---------------------------- Login Menu-------------------- -----\n')
        child_id = input('Enter the User ID')
        child_pass = input('Enter the Password')
        child_file = open("Child_db.txt","r")
        for line in child_file:
            login_child = line.strip().split(",")
            if child_id == "lucy" and child_pass == login_child[2] and  wallet.blk_lucy== "U" :
                print('Welcome', login_child[1] )
                self.child_menu()
                return True
            elif child_id == "simba" and child_pass == login_child[2] and  wallet.blk_simba== "U":
                print('Welcome', login_child[1] )
                self.child_menu()
                return True
            elif child_id == "jack" and child_pass == login_child[2] and  wallet.blk_jack== "U":
                print('Welcome', login_child[1] )
                self.child_menu()
                return True
            elif child_id == "alex" and child_pass == login_child[2] and  wallet.blk_alex== "U":
                print('Welcome', login_child[1] )
                self.child_menu()
            elif child_id == "maria" and child_pass == login_child[2] and  wallet.blk_maria== "U":
                print('Welcome', login_child[1] )
                self.child_menu()
            elif child_id == "maggie" and child_pass == login_child[2] and  wallet.blk_maggie== "U":
                print('Welcome', login_child[1] )
                self.child_menu()
            elif child_id == "john" and child_pass == login_child[2] and  wallet.blk_john== "U":
                print('Welcome', login_child[1] )
                self.child_menu()
            elif child_id == "sandra" and child_pass == login_child[2] and  wallet.blk_sandra== "U":
                print('Welcome', login_child[1] )
            elif child_id == "kratos" and child_pass == login_child[2] and  wallet.blk_kratos== "U":
                print('Welcome', login_child[1] )
                self.child_menu()
            elif child_id == "alan" and child_pass == login_child[2] and  wallet.blk_alan== "U":
                print('Welcome', login_child[1] )
                self.child_menu()
                return True
        print('\n\n!!!!!!!!!!!!You entered the wrong Password or username or You are blocked the Admin ,Please try Again!!!!!!!!!!!\n')
        main_obj.main_menu()
        return False
    def child_pay(self):
        amount = int(input('Enter the amount to be paid'))
        if amount > 50:
            print('The entered amount exceeds the allowed limit \n  Would you like to request Mom for overpay ?')
            ch = input('Please press Y for Yes and N for No')

            if ch == 'Y' or 'y':
                Onetime = generateOTP()
           
                account_sid = "AC737c27831ed7e53ee7b1644e7e8215b2"
                auth_token = "18ccdf76c24452724a9d3aecc3155fc0"
                client = Client(account_sid, auth_token)

                sms = client.messages.create(from_="+19253969540",
                        body="Hello Mom/Dad, I need to pay more than 50$,would you please allow me.Please provide me with the OTP"+ Onetime ,
                        to="+15144310719"
                    )
                ot=(input("Enter The OTP : "))
                if ot == Onetime:
                    self.paymore()
                else:
                    print("Wrong OTP. Please Try again")
                    child_obj.child_pay()
        else:
            name = input('Enter the name of the Vendor/shop')
            amount = int(input('Enter the amount to be Paid'))
            child_name1 = input("Enter your name")
            dt = datetime.now()
            a = 50
            if amount > wallet.balance or wallet.balance<=0 or amount>=a :
                print('TRANSACTION DECLINED ! Insufficient Balance, please add money to your wallet')
                dt = datetime.now()
                child_obj.child_login()
            else:
                print('Payment successful to '+ name + ' at '+ "Time : "+ str(dt))
                wallet.balance = wallet.balance - amount
                print('Available Wallet balance :', wallet.balance)
                transact_file = open("transact.txt","a")
                transact_file.write('\n')
                transact_file.write('\n Paid By : '+ child_name1 +  '    Vendor Name : '+str(name) +   '    Amount Paid :' + str(amount) + '   Time : '+ str(dt) )
                transact_file.write('\n')
                transact_file.close()
                main_m.main_menu(self)
    def pay(self) :
        name = input('Enter the name of the Vendor/shop')
        amount = int(input('Enter the amount to be Paid'))
        dt = datetime.now()
        if amount > wallet.balance or wallet.balance==0 :
            print('TRANSACTION DECLINED ! Insufficient Balance, please add money to your wallet')
            main_m.main_menu(self)
            dt = datetime.now()
            main_m.main_menu(self)
        else:
            print('Payment successful to '+ name + ' at ',dt)
            wallet.balance = wallet.balance - amount
            walletobject.update_wallet()
            print('Available Wallet balance :', wallet.balance)
            transact_file = open("transact.txt","a")
            transact_file.write('\n')
            transact_file.write('\nVendor Name : '+str(name) + '    Amount Paid :' + str(amount) + '   Time : '+ str(dt) )
            transact_file.write('\n')
            transact_file.close()
            main_m.main_menu(self)



    def child_menu(self):

        print('1.Pay')
        print('2. Request Money into the wallet')
        select_menu = input('Please select the operation you want to perform(1/2/3/4)')
   
        if select_menu == '1': 
            self.count= self.count + 1
            if self.count<3:
                print('Ask permission from parents for the first and second payment of the day')
                admin_pass = input('Enter the Password')
                admin_file = open("Admin_db.txt","r")
                for line in admin_file:
                    login_admin = line.strip().split(",")
                    if admin_pass == login_admin[2] :
                        print('You have the permission to pay now' )
                        self.child_pay()
                        return False
                    else:
                        print("Wrong Password!! you are not permitted")
                        return True
            else:
                self.child_pay()



        elif select_menu == '2':
            self.request_mon()

        else:
            print("!!! Invalid Option! Please read the option carefully! !!!!!!!!!!!\n")
   


    def request_mon(self):
        account_sid = "AC737c27831ed7e53ee7b1644e7e8215b2"
        auth_token = "18ccdf76c24452724a9d3aecc3155fc0"
        client = Client(account_sid, auth_token)
        sms = client.messages.create(from_="+19253969540",
                body="Hello Mom/Dad , I need to use the wallet and the balance is low. Please transfer money from bank to the wallet",
                to="+15144310719"
                )   
    

    def paymore(self):
        user = input('Enter your name')
        name = input('Enter the name of the Vendor/shop')
        amount = int(input('Enter the amount to be Paid'))

        dt = datetime.now()
        if amount >= 0 and amount<wallet.balance and wallet.balance>=0 :

            print('Paymentof ',amount, 'successful to '+ name + ' at ')
            wallet.balance = wallet.balance - amount
            print('Available Wallet balance :', wallet.balance)
            transact_file = open("transact.txt","a")
            transact_file.write('\n')
            transact_file.write('Paid By   :'+ str(user) +'Vendor Name : '+str(name) + '    Amount Paid :' + str(amount) + '   Time : '+ str(dt) )
            transact_file.write('\n')
            transact_file.close()
            walletobject.update_wallet()
        else :
            print("Wallet balance is low or entered amount is incorrect . Please check and try again")
            main_m.main_menu(self)

child_obj = Child()
            

class main_m(Admin):
    
    def main_menu(self) :
        if wallet.balance<100:
            print("\n\n---------------Notification------------------")
            print("!!!!Please add money to your wallet the balance is below 100 dollars!!!!")
        opt_main_menu :str
        print('\n-----------------WELCOME TO FamPay----------------\n')
        print('--------MAIN MENU--------\n\n')
        print('1. Admin Login')
        print('2. Child Login')
        print('3. Quit')
        opt_main_menu =input('Please select your login as (1/2/3)\n')

        if opt_main_menu == '1' : 
            
            self.admin_login()
            
        elif opt_main_menu == '2' :
            child_obj.child_login()
        elif opt_main_menu =='3' :
            quit()
        else:
            print("!!! Invalid Option! Please read the option carefully! !!!\n")
            opt_main_menu=int(input("> Please select your login as (1/2/3): "))
            
main_obj= main_m()

main_obj.main_menu()






