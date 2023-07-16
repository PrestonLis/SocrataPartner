# <Status - Capmanagementllc.Partner.Socrata>

## Description

My goal when developing this script was to automate the process of checking the status of all assets of the website [Capmanagementllc Partner Socrata](https://capmanagementllc.partner.socrata.com/). This was made to add efficiency to the task of checking status for the thousands of private assets given the proper authentification. 

## Installation

- Download the zip file and extract.
- CD to directory

```
cd "C:Users/Your/Directory/SocrataPartner
```
- Install requirements
```
pip install -r requirements.txt
```

- Run collection.py script.

```
python collection.py
```
## Usage

Because this page requires admin permissions, you have to enter your username (email) and password. This information is only used for authentification, and can be accompanied with an app token optionally.

```
Username:
Password:
App_token:
```
Will then proceed to load a .csv file in the directory with status codes being scraped, with a progress bar indicating how far into the process you are.


