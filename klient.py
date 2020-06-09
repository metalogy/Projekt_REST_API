# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:05:29 2020

@author: user
"""
import requests
import json

adress='http://localhost:5000/'

def create_set(id):
    request=requests.post(adress+'sets', json={'set_id':'%s' %(id)})
    print(request)
    
def remove_set(id):
    request=requests.delete(adress+'sets/%s' %(id))
    print(request)
    
def put_set_info(id):
    name=input("Input set name: ")
    year=input("Input year of set production: ")
    bricks_number=input("Input number of bricks in set: ")
    minifig_number=input("Input number of minifigures in set: ")
    theme=input("Input set theme: ")
    request=requests.put(adress+'sets/%s' %(id), json={'name':name,'year':int(year),'bricks_number':int(bricks_number),'minifigs_number':int(minifig_number),'theme':theme})
    print(request)
    
def get_info(id):
    response=requests.get(adress+'sets/%s' %(id))
    print(response, '\n')
    if not response.status_code==404:
        response_dict=json.loads(response.text)
        print('Info about set:',id)
        for key in response_dict[id]:
            print(key,':',response_dict[id][key])
        
def get_info_all():
    response=requests.get(adress+'sets')
    response_dict=json.loads(response.text)
    print(response)
    print ("List of sets: ")
    for i in response_dict:
        print("Nr of set: ",i)

menu = {}
menu['1']="Get list of sets" 
menu['2']="Add set id"
menu['3']="Update set info"
menu['4']="Get set info"
menu['5']="Delete set"
menu['6']="Exit"

while True: 
  options=menu.keys()
  for entry in options: 
      print(entry, menu[entry])
  print('\n')
  select=input("Select function:") 
  
  if select =='1':  
      get_info_all()
      
  elif select == '2': 
      id=input("Input id of set to create: ")
      create_set(id)
      
  elif select == '3':
      id=input("Update set data \n  Input id of set to update: ")
      put_set_info(id)
      
  elif select == '4': 
      id=input("Get set data \n Input set id: ")
      get_info(id)
      
  elif select == '5': 
      id=input("Delete set data \n Input id of set to delete: ")
      remove_set(id)
      
  elif select == '6': 
      print("Exit")
      break
  
  else: 
      print ("Unknown operation \n \n") 
  print('\n \n \n')