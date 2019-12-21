import pandas as pd
import sqlalchemy as bd

x = "Olá! "
name = input("Qual o seu nome?\n")

if name[-1] == "a":
    y = "Seja Bem vinda, {0}.".format(name)
else:
    y = "Seja Bem vindo, {0}.".format(name)


print("{0}{1}".format(x,y))
