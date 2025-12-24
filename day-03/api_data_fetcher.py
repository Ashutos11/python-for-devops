import requests

key = "017b9f4078ad85cb37bd38e217665943"
try:
    limit = int(input("Enter the number of airlines you want data for: "))
except:
    print("The entered value is not an integer")
    exit(1)

base_url = f"https://api.aviationstack.com/v1/airlines?access_key={key}&limit={limit}"

def get_airline_status(limit):

    response = requests.get(url=base_url)
    airline_list = response.json()["data"]

    for i in range(0,limit):
        print(airline_list[i]["airline_name"], end=" ")
        print(airline_list[i]["status"])

get_airline_status(limit)