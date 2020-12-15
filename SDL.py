from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from flask import Flask,render_template,url_for,redirect
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('VPM_F.csv')

ai=float(2.8);
bi=float(1.20);
EAF=float(1.15);
cb=float(2.5);
db=float(0.32);

def menu():
    print("Menu:")
    print("1:] Read CSV File")
    print("2:] Read How much quantity of products are sold")
    print("3:] Understand the Data")
    print("4:] Read How much Profit earned of products are sold")
    print("5:] Read How much Net Income of products ")
    print("6.] Know how many people in month work on a project")

def menu1():
    print("Project:")
    print("1.Book shop")
    print("2.E-farming")
    print("3.Virtual Project Management")
    print("4.Tracker")
    print("5.Personal Assistance")
    print("6.Health Assistance")

def option1():
    print(">>>>>Reading opertion<<<<<<")
    df = pd.read_csv('VPM_F.csv')
    print(df.head())
    # value = len(list(df))
    # print(value)


def option2():
    plt.bar(x=df['Project_name'], height=df['Quantity sold'], color='rgbwymc')
    plt.xticks(rotation=45)
    plt.title('Quantity of Software_products sold')
    plt.show()


def option3():
    d = df.describe()
    print(d)


def option4():
    plt.bar(x=df['Project_name'], height=df['Profit_per_unit'])
    plt.xticks(rotation=45)
    plt.title('Profit of Software_products sold')
    plt.show()


def option5():
    name = df['Project_name']
    net = df['Net_Income']
    plt.pie(net, labels=name, shadow=True, startangle=120, autopct='%1.1f%%')
    plt.show()
    print("Net Income of Project")

def person_month_B():
    # E=ai(KLOC)^bi*(EAF)-->Person_month
    # D=cb*E^db------------>Months req for project
    # N=E/D---------------->manpower req for project
    # KLOC Change
    i=df.iloc[0,17]
    #i=float(input("Enter number of lines of code :"))
    KLOC =float(pow(i,1.20));
    E=ai*KLOC*EAF;
    print(E)
    print("--> Requires Person_monthly")
    Edb=float(pow(E,0.32));
    D=cb*Edb;
    print(D)
    print("--> Months required to complete the project")
    N=E/D;
    print(N)
    print("--> Number of people approx required")

def person_month_F():
    f=df.iloc[1,17]
   #print(f)
    #i=float(input("Enter number of lines of code :"))
    KLOC =float(pow(f,1.20));
    E=ai*KLOC*EAF;
    print(E)
    print(" Requires Person_monthly")
    Edb = float(pow(E, 0.32));
    D = cb * Edb;
    print(D)
    print("--> Months required to complete the project")
    N = E / D;
    print(N)
    print("--> Number of people approx required")

def  person_month_V():
    f = df.iloc[2, 17]
    # print(f)
    # i=float(input("Enter number of lines of code :"))
    KLOC = float(pow(f, 1.20));
    E = ai * KLOC * EAF;
    print(E)
    print(" Requires Person_monthly")
    Edb = float(pow(E, 0.32));
    D = cb * Edb;
    print(D)
    print("--> Months required to complete the project")
    N = E / D;
    print(N)
    print("--> Number of people approx required")

def person_month_T():
    f = df.iloc[3, 17]
    # print(f)
    # i=float(input("Enter number of lines of code :"))
    KLOC = float(pow(f, 1.20));
    E = ai * KLOC * EAF;
    print(E)
    print(" Requires Person_monthly")
    Edb = float(pow(E, 0.32));
    D = cb * Edb;
    print(D)
    print("--> Months required to complete the project")
    N = E / D;
    print(N)
    print("--> Number of people approx required")

def  person_month_P():
    f = df.iloc[4, 17]
    # print(f)
    # i=float(input("Enter number of lines of code :"))
    KLOC = float(pow(f, 1.20));
    E = ai * KLOC * EAF;
    print(E)
    print(" Requires Person_monthly")
    Edb = float(pow(E, 0.32));
    D = cb * Edb;
    print(D)
    print("--> Months required to complete the project")
    N = E / D;
    print(N)
    print("--> Number of people approx required")

def  person_month_H():
    f = df.iloc[5, 17]
    # print(f)
    # i=float(input("Enter number of lines of code :"))
    KLOC = float(pow(f, 1.20));
    E = ai * KLOC * EAF;
    print(E)
    print(" Requires Person_monthly")
    Edb = float(pow(E, 0.32));
    D = cb * Edb;
    print(D)
    print("--> Months required to complete the project")
    N = E / D;
    print(N)
    print("--> Number of people approx required")

menu()
take = int(input("Enter value"))
# while take != 0:

if take == 1:
    option1()
elif take == 2:
    option2()
    print("Showing the Quantity of the product sold")
elif take == 3:
    option3()
    print("Understanding the data")
elif take == 4:
    option4()
    print("Showing the Profit per unit")
elif take == 5:
    option5()
    print("Showing the net income of the project")
elif take ==6:
        menu1()
        anal=int(input("For which project you want to see person_month:"))
        if anal==1:
            person_month_B()

        elif anal==2:
            person_month_F()

        elif anal==3:
            person_month_V()

        elif anal == 4:
            person_month_T()

        elif anal == 5:
            person_month_P()

        elif anal==6:
            person_month_H()

        else:
            print("Invaild")
else:
    print("invalid")

'''menu()
take = int(input("Enter value:"))
print("Thank you")'''