#1. Importar modulos json y .py

from AdminMod import MenuAdmin
import Bonificacion
import ModuloGestion
import ResportesMod
from Moduser import UserMENU
import json


#2. Crear las funciones para abrir y guardar


def abrirHistorial():
    abrir={}
    with open('./Historial.json','r') as openFile:
        abrir=json.load(openFile)
    return abrir

def abrirPerfiles():
    abrir2={}
    with open('./perfiles.json','r') as openFile:
        abrir2=json.load(openFile)
    return abrir2

def abrirRegistro():
    abrir3={}
    with open('./Registro.json','r') as openFile:
        abrir3=json.load(openFile)
    return abrir3

def abrirServicios():
    abrir4={}
    with open('./ServiciosPopulares.json','r') as openFile:
        abrir4=json.load(openFile)
    return abrir4




def guardarHistorial(cerrar):
    with open("./Historial.json",'w') as outFile:
        json.dump(cerrar,outFile)



def guardarPerfiles(cerrar2):
    with open("./perfiles.json",'w') as outFile:
        json.dump(cerrar2,outFile)



def guardarRegistro(cerrar3):
    with open("./HIstorial.json",'w') as outFile:
        json.dump(cerrar3,outFile)



def guardarServicios(cerrar4):
    with open("./HIstorial.json",'w') as outFile:
        json.dump(cerrar4,outFile)

#3. Crear Menu

print("#########################################")
print("########-------------------------########")
print("########--Bienvenido a Movistar--########")
print("########-------------------------########")
print("########-------------------------########")
print("########-------------------------########")
print("#########################################")
print("########--¿Quien Eres?--------------####")
print("#1.User-----------------------------####")
print("#2.Administrador--------------------####")
opcion= int(input(": "))

if opcion==1:
        UserMENU()

if opcion==2:
        MenuAdmin()

else:
    print("Opcion invalida!")