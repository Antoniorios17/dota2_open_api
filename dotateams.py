#!/bin/python3

#################################################################################################################################################################
#
# Author	:       Antonio Rios
# Date		:       9-15-2022
#
# Notes		:       This script is for interacting with the OPEN DOTA API:
#                       -The scrtips connects to the api to gather information about professional teams of Dota 2
#                       -These statistics include number of victories, losses, team name, team id, and a url for their logo
#                       -The information is formated as a csv file and it is compresed to show only a subset of all the data available
#                       -The csv file generated will be sorted by the number of all time won matches
#                       -The required python packages to install are:
#                           -requests
#                           -subprocess    
#                           -os
#                           -pandas  
#                                                 
# Bugs		:	    -The script is limited to create the files inside my own Downloads directory and that's something that can be updated to your particular case
#                   -The file location should be the same across all the times it is mentioned 
#                   -This is the absolute path to be changed to make sure the command runs properly
#                       /home/antonio/downloads/teams.csv
##################################################################################################################################################################


# to get started you need to have all of these libraries installed using the  "pip install <name of the library>"
import requests
import subprocess
import os
import csv
import pandas as pd

#For a cleaner and more understandable code I assigned the api to a variable
url = "https://api.opendota.com/api/teams"

#This part will use requests.get to access the database of the OPEN DOTA API and extract the information we are looking for
#it will come in json format so we need to format that data to work with it
#I assigned the data from the API to a variable to be able to call it later on 
response = requests.get(url)
myjson = response.json()


# In this section I was working on getting the right information from the api
# and after every time I ran the code the file kept being created
#to deal with this issue I made sure to delete the file if it exists to start
#fresh with an empty file to send the data

if os.path.exists("/home/antonio/Downloads/teams.csv"):
    os.remove("/home/antonio/Downloads/teams.csv")
subprocess.run("touch '/home/antonio/Downloads/teams.csv'", shell=True)

#this section makes sure to sort the data by columns to convert the json file into a csv file
#the csv file will follow the order of the teams variable
teams= ['team_id','rating','wins','losses','last_match_time','name','tag','logo_url']
with open('/home/antonio/Downloads/teams.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= teams)
    writer.writeheader()
    writer.writerows(myjson)

#to have a more clean look of the information I removed data I believe is not very relevant like rating
#becuase it is no accurate and last match time for the same reason
#it should return a data or time of the match but it seems it returns the match Id which is something
#completely different

data = pd.read_csv("/home/antonio/Downloads/teams.csv")
data.drop(['rating','last_match_time'], inplace=True, axis=1)
data.head(8).to_csv('/home/antonio/Downloads/teams.csv')

#to have a preview of the data I only included the first 6 values to assess the information
#this can be modified by removing the last line of the code or commenting it


#you will get a sample of the data when you run this command
subprocess.run("echo '**********************************'",shell=True)
subprocess.run("echo '**  Thank you for using my code **'",shell=True)
subprocess.run("echo '**********************************'",shell=True)
subprocess.run("echo ''",shell=True)
subprocess.run("echo 'Here is a sample of the output inside the file'",shell=True)
subprocess.run("echo ''",shell=True)
print(data.head(5))
