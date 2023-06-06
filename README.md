# What is EcoDrop?

EcoDrop’s goal is to take on the problem of pollution on the local level. We will do this by combining the functionality of a reverse-vending machine with a mobile app. Users start by recycling plastic bottles or aluminum cans at the reverse vending machine, where points will be rewarded to the user accordingly. On the mobile app, these points can then be redeemed for goods and services offered by our partners. Additionally, the app is intended to gamify the entire process in order to further incentivize users to recycle. The app is competitive and social, which is designed specifically to target university students.

# How we developed it...

We used Python for the hardware of the machine and Swift (https://github.com/CTxCodes/EcoDrop/tree/master/EcoDrop) and Java for the UI design and development.

We had trouble setting up the authentication process. Well, in general, Firebase was hard to use. We had electrical engineering problems as well.

In the end, we utilized a barcode API with computer vision on open CV. It stores user points in Firestore, and all of this is run on a Raspberry Pi.

https://devpost.com/software/ecodrop-jyfsve

# Flask
This is a web application project using Flask to perform multiple tasks i.e user OTP authentication and embedded high level programming .

In a single directory called myproject:

Directory Layout:

---app.py
---requirements.txt
----myproject----templates-----------all .html files.
             -----__init__.py
             -----forms.py
             -----models.py

All html files in one directory: templates.

# Flask-SQLAlchemy

Flask-SQLAlchemy is a wrapper around SQLAlchemy. You should follow the SQLAlchemy Tutorial to learn about how to use it, and consult its documentation for detailed information about its features. These docs show how to set up Flask-SQLAlchemy itself, not how to use SQLAlchemy. Flask-SQLAlchemy sets up the engine, declarative model class, and scoped session automatically, so you can skip those parts of the SQLAlchemy tutorial.
