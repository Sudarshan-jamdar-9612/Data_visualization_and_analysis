from contextlib import redirect_stderr

from flask import Flask, redirect, url_for, render_template
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('VPM_F.csv')

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hh():
    return render_template("index.html")

# @app.route("/home")
# def home():
#     return redirect("index.html")


@app.route("/graph")
def graph():
    return render_template("Graph.html")

@app.route("/option1")
def option1():
    print(">>>>>Reading opertion<<<<<<")
    df = pd.read_csv('VPM_F.csv')
    print(df.head())
    return render_template("result.html", head=df)

@app.route("/option2")
def option2():
    plt.bar(x=df['Project_name'], height=df['Quantity sold'], color='rgbwymc')
    plt.xticks(rotation=45)
    plt.title('Quantity of Software_products sold')
    plt.show()
    return render_template("Graph.html")

@app.route("/option3")
def option3():
    # describe = df.describe()
    # print(describe)
    return render_template("result2.html", df=df)

@app.route("/option4")
def option4():
    plt.bar(x=df['Project_name'], height=df['Profit_per_unit'])
    plt.xticks(rotation=45)
    plt.title('Profit of Software_products sold')
    plt.show()
    return render_template("Graph.html")

@app.route("/option5")
def option5():
    name = df['Project_name']
    net = df['Net_Income']
    plt.pie(net, labels=name, shadow=True, startangle=120, autopct='%1.1f%%')
    plt.show()
    print("Net Income of Project")
    return render_template("Graph.html")

ai = float(2.8);
bi = float(1.20);
EAF = float(1.15);
cb = float(2.5);
db = float(0.32);

@app.route("/num")
def num():
    return render_template("Num.html")

@app.route("/person_month_B")
def person_month_B():
    # E=ai(KLOC)^bi*(EAF)-->Person_month
    # D=cb*E^db------------>Months req for project
    # N=E/D---------------->manpower req for project
    # KLOC Change
    i = df.iloc[0, 17]
    # i=float(input("Enter number of lines of code :"))
    KLOC = float(pow(i, 1.20));
    E = ai * KLOC * EAF;
    print(E)
    print("--> Requires Person_monthly")
    Edb = float(pow(E, 0.32));
    D = cb * Edb;
    print(D)
    print("--> Months required to complete the project")
    N = E / D;
    print(N)
    print("--> Number of people approx required")
    return render_template("result1.html", E=E, D=D, N=N)


@app.route("/person_month_F")
def person_month_F():
    f = df.iloc[1, 17]
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
    return render_template("result1.html", E=E, D=D, N=N)


@app.route("/person_month_V")
def person_month_V():
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
    return render_template("result1.html", E=E, D=D, N=N)


@app.route("/person_month_T")
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
    return render_template("result1.html", E=E, D=D, N=N)


@app.route("/person_month_P")
def person_month_P():
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
    return render_template("result1.html", E=E, D=D, N=N)


@app.route("/person_month_H")
def person_month_H():
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
    return render_template("result1.html", E=E, D=D, N=N)



app.run(debug=True)
