# ------------------------------ Developer - Ayaz Saiyed M.
# ----------------- Final Release July,2020
# ------------- GasLeadGeneration

# https://consumerbenefit.pythonanywhere.com

# https://www.privacypolicygenerator.info/download.php?lang=en&token=CY80vaIyBrz4V2hqWOETg2aHVa6rhgur#


#AppID - 653796138509883
#MessengerID - m.me/107539167624388
    # fb.me/consumerbenefit 
    # send your Page messages at m.me/consumerbenefit.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from pydialogflow_fulfillment import DialogflowResponse, DialogflowRequest, SimpleResponse, Suggestions, LinkOutSuggestion
from django.http import HttpResponse, JsonResponse
from library.df_response_lib import *
from library.facebook_template_lib import *
import json
import smtplib 
import requests
import facebook
import time
import random
from .models import UsersDetails
from django.shortcuts import redirect
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl import load_workbook

from datetime import datetime



def homepage(request):
    return render(request,'./bot/index.html')

# token = 'EAAJxVO9CDNQBAFHw70ScBJtLU7mOXZCM9TU63GxYeTFws6pHzz1eO5MLhRmZBjXZAoUNABUog4XEQIm9aytCQvHLrQN60cbKyDgWeQIWoEkgB1Ero18ZBTLFYY960zZAxrENGtcssylaEfZAZCjGSQ9cgovSLfuZBBwvFCxgzCTGOEZAzX3i96f17'

# GasLeadFacebookPageToken 
# token = 'EAAKFRRsMxo4BADmxqtuYE2pSFB4jOmyF6Cq4atEFCpTnSOEdGdvPNIXZAnZB6ZA4gs3TgF154QTSh1yxhTCuIQiHq0ZBBwexdL3mZCZAiuhkDQMwCZCqSZCBkXi5ZAVQPfHmbvZATTpMluDd8lm8AUZCl2vpM3JJVUZBvwZBZCyMoQxWVDsLeIGcfKDczRjRXMeFjx30cZD'

# graph = facebook.GraphAPI(access_token=token, version = 2.8)

@csrf_exempt
def index_function(request):

    if request.method == "POST":

        print("Method ",request.method)

        if request.body:
            req = json.loads(request.body)
            dialogflow_request = DialogflowRequest(request.body)
            action = req.get('queryResult').get('action') 
            print("Action is ",action)
            



            if dialogflow_request.get_intent_displayName() == "AskingServices - LaptopIssueFetch - Final":
                print("First Intent - Laptop ")
                # print("City Selection") 
                QuerySet = req.get('queryResult').get('parameters')
                print("QuerySet ",QuerySet)
                dialogflow_response = DialogflowResponse("Perfecto, uno de nuestros 👨 ejecutivos se pondrá en contacto contigo en breve para solucionar el problema relacionado con tu portátil. Que tengas un buen día 🤝 Gracias 💫")
                customerNeed = "Laptop Issue"
                customerName = req.get('queryResult').get('parameters').get('username')
                customerEmail = req.get('queryResult').get('parameters').get('email')
                response = dialogflow_response.get_final_response()
                print("")
                print(" Customer name is ",customerName)
                print(" Customer email is ",customerEmail)
                print(" Customer Issue is ",customerNeed)
                print("")

                #Excel stuff

                workbook = Workbook()
                workbook = load_workbook(filename="SoporteMoreliaCustomers.xlsx")
                sheet = workbook.active

                # Details of User
                rows = [
                            [customerName,customerNeed,customerEmail]
                       ]


                for row in rows:
                    sheet.append(row)

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")

                for column_cells in sheet.columns:
                    length = max(len("fewopfewpfrewprjkeddwioprfdsfsdfdsffsdfsdsfdsfdsfdsfdsfjewpfdssdsdasdadrwpfrjipewr") for cell in column_cells)
                    # sheet.column_dimensions[column_cells[0].column_letter].width = int(20)

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")
                print(" Data Saved ")
                action = req.get('queryResult').get('action')   
                x = action
                response = dialogflow_response.get_final_response()


            if dialogflow_request.get_intent_displayName() == "AskingServices - ComputerIssueFetch - Final":
                print("Second Intent - Computer ")
                # print("City Selection") 
                QuerySet = req.get('queryResult').get('parameters')
                print("QuerySet ",QuerySet)
                dialogflow_response = DialogflowResponse("Perfecto, uno de nuestros 👨 ejecutivos se comunicará contigo en breve para solucionar tu problema informático. Que tengas un buen día 🤝 Gracias 💫")
                customerNeed = "Computer Issue"
                customerName = req.get('queryResult').get('parameters').get('username')
                customerEmail = req.get('queryResult').get('parameters').get('email')
                response = dialogflow_response.get_final_response()

                print("")
                print(" Customer name is ",customerName)
                print(" Customer email is ",customerEmail)
                print(" Customer Issue is ",customerNeed)
                print("")

                #Excel stuff

                workbook = Workbook()
                workbook = load_workbook(filename="SoporteMoreliaCustomers.xlsx")
                sheet = workbook.active

                # Details of User
                rows = [
                            [customerName,customerNeed,customerEmail]
                       ]


                for row in rows:
                    sheet.append(row)

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")

                for column_cells in sheet.columns:
                    length = max(len("fewopfewpfrewprjkeddwioprfdsfsdfdsffsdfsdsfdsfdsfdsfdsfjewpfdssdsdasdadrwpfrjipewr") for cell in column_cells)
                    sheet.column_dimensions[column_cells[0].column_letter].width = length

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")
                print(" Data Saved ")
                action = req.get('queryResult').get('action')   
                x = action
                response = dialogflow_response.get_final_response()


            if dialogflow_request.get_intent_displayName() == "AskingServices - Software":
                print(" Third Intent - Software ")
                # print("City Selection") 
                QuerySet = req.get('queryResult').get('parameters')
                print("QuerySet ",QuerySet)
                dialogflow_response = DialogflowResponse("Perfecto, uno de nuestros 👨 ejecutivos se comunicará con usted en breve para resolver su problema relacionado con el software. Que tengas un buen día 🤝 Gracias 💫")
                customerNeed = "Software Issue"
                customerName = req.get('queryResult').get('parameters').get('name')
                customerEmail = req.get('queryResult').get('parameters').get('email')
                response = dialogflow_response.get_final_response()

                print("")
                print(" Customer name is ",customerName)
                print(" Customer email is ",customerEmail)
                print(" Customer Issue is ",customerNeed)
                print("")

                #Excel stuff

                workbook = Workbook()
                workbook = load_workbook(filename="SoporteMoreliaCustomers.xlsx")
                sheet = workbook.active

                # Details of User
                rows = [
                            [customerName,customerNeed,customerEmail]
                       ]


                for row in rows:
                    sheet.append(row)

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")

                for column_cells in sheet.columns:
                    length = max(len("fewopfewpfrewprjkeddwioprfdsfsdfdsffsdfsdsfdsfdsfdsfdsfjewpfdssdsdasdadrwpfrjipewr") for cell in column_cells)
                    sheet.column_dimensions[column_cells[0].column_letter].width = length

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")
                print(" Data Saved ")
                action = req.get('queryResult').get('action')   
                x = action
                response = dialogflow_response.get_final_response()



            if dialogflow_request.get_intent_displayName() == "AskingServices - Puntos de venta":
                print("Fourth Intent - Sales ")
                # print("City Selection") 
                QuerySet = req.get('queryResult').get('parameters')
                print("QuerySet ",QuerySet)
                dialogflow_response = DialogflowResponse("Genial, uno de nuestros 👨 ejecutivos se pondrá en contacto contigo en breve para discutir las ventas en detalle. Que tengas un buen día 🤝 Gracias 💫")
                customerNeed = "Puntos de venta Issue"
                customerName = req.get('queryResult').get('parameters').get('name')
                customerEmail = req.get('queryResult').get('parameters').get('email')
                response = dialogflow_response.get_final_response()

                print("")
                print(" Customer name is ",customerName)
                print(" Customer email is ",customerEmail)
                print(" Customer Issue is ",customerNeed)
                print("")

                #Excel stuff

                workbook = Workbook()
                workbook = load_workbook(filename="SoporteMoreliaCustomers.xlsx")
                sheet = workbook.active

                # Details of User
                rows = [
                            [customerName,customerNeed,customerEmail]
                       ]


                for row in rows:
                    sheet.append(row)

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")

                for column_cells in sheet.columns:
                    length = max(len("fewopfewpfrewprjkeddwioprfdsfsdfdsffsdfsdsfdsfdsfdsfdsfjewpfdssdsdasdadrwpfrjipewr") for cell in column_cells)
                    sheet.column_dimensions[column_cells[0].column_letter].width = length

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")
                print(" Data Saved ")
                action = req.get('queryResult').get('action')   
                x = action
                response = dialogflow_response.get_final_response()




            if dialogflow_request.get_intent_displayName() == "AskingServices - Redes":
                print("Fifth Intent - Redes ")
                # print("City Selection") 
                QuerySet = req.get('queryResult').get('parameters')
                print("QuerySet ",QuerySet)
                dialogflow_response = DialogflowResponse("Seguro, uno de nuestros expertos en nuestra red se pondrá en contacto contigo para solucionar tu problema 👍 Que tengas un buen día 🤝 Gracias 💫 ")
                customerNeed = "Redes Issue"
                customerName = req.get('queryResult').get('parameters').get('username')
                customerEmail = req.get('queryResult').get('parameters').get('email')
                response = dialogflow_response.get_final_response()

                print("")
                print(" Customer name is ",customerName)
                print(" Customer email is ",customerEmail)
                print(" Customer Issue is ",customerNeed)
                print("")

                #Excel stuff

                workbook = Workbook()
                workbook = load_workbook(filename="SoporteMoreliaCustomers.xlsx")
                sheet = workbook.active

                if not customerName:
                    customerName=="None"
                if not customerEmail:
                    customerEmail=="None"
                # Details of User
                rows = [
                            [customerName,customerNeed,customerEmail]
                       ]


                for row in rows:
                    sheet.append(row)

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")

                for column_cells in sheet.columns:
                    length = max(len("fewopfewpfrewprjkeddwioprfdsfsdfdsffsdfsdsfdsfdsfdsfdsfjewpfdssdsdasdadrwpfrjipewr") for cell in column_cells)
                    # sheet.column_dimensions[column_cells[0].column_letter].width = int(20)
                    sheet.column_dimensions[column_cells[0].column_letter].width = length
                    # sheet.column_dimensions[column_cells[0].column_letter].width = int(20)

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")
                print(" Data Saved ")
                action = req.get('queryResult').get('action')   
                x = action
                response = dialogflow_response.get_final_response()



            if dialogflow_request.get_intent_displayName() == "AskingServices - Venta de Equip de Computo":
                print("Sixth Intent - Venta de Equip de Computo ")
                # print("City Selection") 
                QuerySet = req.get('queryResult').get('parameters')
                print("QuerySet ",QuerySet)
                dialogflow_response = DialogflowResponse("De acuerdo, nos comunicaremos con usted en breve para discutir en detalle sobre el equipo que se venderá. Que tengas un buen día 🤝 Gracias 💫")
                customerNeed = "Venta de Equip de Computo Issue"
                customerName = req.get('queryResult').get('parameters').get('name')
                customerEmail = req.get('queryResult').get('parameters').get('email')
                response = dialogflow_response.get_final_response()

                print("")
                print(" Customer name is ",customerName)
                print(" Customer email is ",customerEmail)
                print(" Customer Issue is ",customerNeed)
                print("")

                #Excel stuff

                workbook = Workbook()
                workbook = load_workbook(filename="SoporteMoreliaCustomers.xlsx")
                sheet = workbook.active

                # Details of User
                rows = [
                            [customerName,customerNeed,customerEmail]
                       ]


                for row in rows:
                    sheet.append(row)

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")

                for column_cells in sheet.columns:
                    length = max(len("fewopfewpfrewprjkeddwioprfdsfsdfdsffsdfsdsfdsfdsfdsfdsfjewpfdssdsdasdadrwpfrjipewr") for cell in column_cells)
                    sheet.column_dimensions[column_cells[0].column_letter].width = length

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")
                print(" Data Saved ")
                action = req.get('queryResult').get('action')   
                x = action
                response = dialogflow_response.get_final_response()




            if dialogflow_request.get_intent_displayName() == "AskingServices - Otro - Final":
                print("Seventh Intent - Otro")
                # print("City Selection") 
                QuerySet = req.get('queryResult').get('parameters')
                print("QuerySet ",QuerySet)
                dialogflow_response = DialogflowResponse("Pues uno de nuestros ejecutivos de soporte se comunicará contigo en breve para brindarte el mejor servicio👨. Que tengas un buen día 🤝 Gracias 💫")
                customerNeed = "Otro"
                customerName = req.get('queryResult').get('parameters').get('name')
                customerEmail = req.get('queryResult').get('parameters').get('email')
                response = dialogflow_response.get_final_response()


                print("")
                print(" Customer name is ",customerName)
                print(" Customer email is ",customerEmail)
                print(" Customer Issue is ",customerNeed)
                print("")

                #Excel stuff

                workbook = Workbook()
                workbook = load_workbook(filename="SoporteMoreliaCustomers.xlsx")
                sheet = workbook.active

                # Details of User
                rows = [
                            [customerName,customerNeed,customerEmail]
                       ]


                for row in rows:
                    sheet.append(row)

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")

                for column_cells in sheet.columns:
                    length = max(len("fewopfewpfrewprjkeddwioprfdsfsdfdsffsdfsdsfdsfdsfdsfdsfjewpfdssdsdasdadrwpfrjipewr") for cell in column_cells)
                    sheet.column_dimensions[column_cells[0].column_letter].width = length

                workbook.save(filename="SoporteMoreliaCustomers.xlsx")
                print(" Data Saved ")
                action = req.get('queryResult').get('action')   
                x = action
                response = dialogflow_response.get_final_response()



        else :
            response = {
                "error" : "1",
                "message" : "An error occurred."
            }
       
        return HttpResponse(response, content_type='application/json; charset=utf-8')
        # return HttpResponse("Yudiz Team")

    else:
        # print("3")

        raise Http404()


def get_user_first_name(user_id):
    '''
        Retrieves user first name using Facebook Graph API for a user with user_id
    '''
    user = graph.get_object(id=str(user_id))
    if user.get('first_name'):
        return user.get('first_name')
    else:
        return False




def temp(request):
    return render(request,'bot/yudizbot.html')


def option(request):
    return render(request,'bot/options.html')