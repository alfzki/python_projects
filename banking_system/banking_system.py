#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Banking system using OOP

Parent Class: User
Hold details about an user
Has a function to show user details

Child Class: Bank
Stores details about the account balance
Stores details about the amount
Allows for deposit, withdraw, and view balance
"""


class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details\n")
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}")


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Your balance has been updated: ${self.balance}")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"Your balance has been updated: ${self.balance}")
        else:
            print("Insufficient funds")
            self.show_balance()
            print(f"You were trying to withdraw ${amount}")

    def show_balance(self):
        print(f"Your balance is ${self.balance}")


# Testing code
b1 = Bank("alif", 15, "male")
b1.show_details()
b1.show_balance()
b1.deposit(50)
b1.withdraw(200)
b1.deposit(750)
b1.withdraw(100)
