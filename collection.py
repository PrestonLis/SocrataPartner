import pandas as pd
from sodapy import Socrata
import requests, os
from tqdm import tqdm


def get_url_status(url,username,password):
    try:
        response = requests.get(url,auth=(username,password))
        return response.status_code
    except requests.exceptions.RequestException:
        return " "
    
def get_api_status(api_endpoint,username,password):
    try:
        response = requests.get(api_endpoint,auth=(username,password))
        return response.status_code
    except requests.exceptions.RequestException:
        return " "

username = input("Username: ")
password = input("Password: ")
app_token = input("App Token: ")

client = Socrata("capmanagementllc.partner.socrata.com", app_token=app_token,username=username,password=password)
results = client.get("9vvb-qwmv", limit=1500)
results_df = pd.DataFrame.from_records(results)

results_df["url status"] = ""
results_df["api status"] = ""
results_df = results_df[["name", "url", "url status", "api_endpoint", "api status"]]
os.system("CLS")
print("Beginning Status Check")
print(f"Current Working Directory: {os.getcwd()}")

with tqdm(total=len(results_df)) as pbar:
    for index, row in results_df.iterrows():
        url = row["url"]
        api_endpoint = row["api_endpoint"]

        url_status = get_url_status(url,username,password)
        results_df.at[index, "url status"] = url_status

        api_status = get_api_status(api_endpoint,username,password)
        results_df.at[index, "api status"] = api_status

        results_df.to_csv("status_codes.csv", index=False)
        pbar.update(1)

print(f"CSV file saved in directory: {os.getcwd()}/status_codes.csv")