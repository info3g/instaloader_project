import instaloader
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os,time,pandas,xlrd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import pymysql.cursors
import random   
from datetime import datetime,timedelta 
from instaloader import Instaloader, Profile
import pandas as pd 
import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from io import StringIO
import csv  
from instaloader import Instaloader, Profile
import random

user_dict_all = {}
# def instgram_data():
def bot_scrape(login_name,passwords,list_user_aa):
	print(login_name,passwords,list_user_aa)
	pending_list = []
	loader = Instaloader()
	try:
		loader.login(login_name, passwords)
	except:
		print('cannot login') 

	
	# cursor.execute( "select * from group_a_users")
	# list_user_a = cursor.fetchall() 
	for i,each_profile in enumerate(list_user_aa):
		print('dffsdfsd',each_profile)
		al_following_a = []
		time.sleep(2)
		try:
			profile = Profile.from_username(loader.context, each_profile)
			followees = profile.get_followees()
			print(f'profile number  {i}')
			loader.context.log('Profile {} has {} followees'.format(profile.username, profile.followees))
			for followee in followees:
				al_following_a.append(followee.username)
			
			user_dict_all.update({each_profile:al_following_a})
			print("******",al_following_a)
			if len(al_following_a) == 0 and profile.followees !=0:
				print('this user is private')
				pending_list.append(profile.username)

			# time.sleep(40)

		except:
			print(f'user link does not exist   {i} {each_profile}')
			user_dict_all.update({each_profile: "User doesn't exist"})
			# time.sleep(40)
			continue
	
	return pending_list
	



	# All_user_a =['moussa.cisse3','wilson_smk','mih.management','olivierazan']
	

	# for key,val in user_dict_b.items():
	# 	user_list = []
	# 	if val == "User doesn't exist":
	# 		print("fsdfsdfsfdsdsfdsfsdfsdfdsfdsfsdf-sdf-dsf*-sd*f-sd*-f*ds-f*-sd*f-sd*f*sdf-d",key)
	# 		user_dict.update({key : "User doesn't exist"})
	# 	else:
	# 		pass
	# 	if len(val) == 0:
	# 		user_dict.update({key : 'No Followers'})
	# 	else:
	# 		for each_user in val:
	# 			if each_user in users___a:
	# 				print("*****************************************************",key,each_user)
	# 				user_list.append(each_user)
	# 			else:
	# 				pass
	# 		if len(user_list) == 0:
	# 			user_dict.update({key : 'No Followers'})
	# 		else:           
	# 			user_dict.update({key : user_list})
	
	

if __name__ == '__main__':

	list_user_aa = ['aurel2fois_','eliemoussafir','lauriennnte','nikhil.bhaskar','moussa.cisse3','wilson_smk']    
	list_user_b = ['philnabe','olivierazan','yourfirstsports','maa_da_laddi_putt','robindes_s']
	list_user_aa.extend(list_user_b)
	




	for i in range(1):            
		bot_username = ['football___legends__']
		bot_password = ['Legends1234',]
		login_name=bot_username[i]
		password = bot_password[i]
		list_user_aa = bot_scrape(login_name,password,list_user_aa) # returned target profile is pending list    
	
		print('this is prending list')
		print(len(list_user_aa))
		print(list_user_aa)


	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()	

	pending_list = []

	start_scrapping = datetime.now()
	now = datetime.now()
	add_scrapping = start_scrapping + timedelta(hours=12)
	save_date = add_scrapping.strftime("%Y-%m-%d %H:%M")
	now_scrapping = start_scrapping.strftime("%Y-%m-%d %H:%M")
	sql="update time_updates set time_date=%s ;"
	value=(save_date)
	cursor.execute(sql,value)
	sql="update time_updates set now_date=%s ;"
	value=(now_scrapping)
	cursor.execute(sql,value)
	mydb.commit()

	user_dict = {}
	privete_dict = {}

	# cursor.execute( "select * from group_a_users") #  demo table data
	# list_user_a = cursor.fetchall()
	cursor.execute( "select * from group_b_users") #  demo table data
	list_user_b = cursor.fetchall()
	users___a = []
	users___b = []
	# for all_record in list_user_a:
	# 	users___a.append(all_record[1])
	for all_record in list_user_b:
		users___b.append(all_record[1])	
	
	for key,val in user_dict_all.items():
		user_list = []
		# if val == "User doesn't exist":
		# 	user_dict.update({key : "User doesn't exist"})
		# else:
		# 	pass
		if len(val) == 0:
			privete_dict.update({key : 'No Followers'})
		else:
			for each_user in val:
				if each_user in users___b:
					print("*****************************************************",key,each_user)
					user_list.append(each_user)
				else:
					pass
				if len(user_list) == 0:
					user_dict.update({key : 'No Followers'})
				else:           
					user_dict.update({key : user_list})
	
	# All_user_a =['moussa.cisse3','wilson_smk','mih.management','olivierazan']
	for key,val in user_dict_all.items():
		user_list = []
		# if val == "User doesn't exist":
		# 	user_dict.update({key : "User doesn't exist"})
		# else:
		# 	pass
		if len(val) == 0:
			privete_dict.update({key : 'No Followers'})
		else:
			for each_user in val:
				if each_user in users___a:
					print("*****************************************************",key,each_user)
					user_list.append(each_user)
				else:
					pass
			if len(user_list) == 0:
				user_dict.update({key : 'No Followers'})
			else:           
				user_dict.update({key : user_list})

	print('user_dictuser_dictuser_dictuser_dictuser_dict',user_dict)
	print('user_dictsuser_dicts',privete_dict)
	# match_demo = {}
	# match_all_table = {}
	# for key,val in user_dict.items():
	# 	val=str(val)
	# 	sql="insert into demo_feed(username,group_followers) values (%s,%s);"
	# 	value=(key,val)
	# 	cursor.execute(sql,value)
	# 	mydb.commit()

	# for key,val in user_dicts.items():
	# 	val=str(val)
	# 	sql="insert into demo_feed(username,group_followers) values (%s,%s);"
	# 	value=(key,val)
	# 	cursor.execute(sql,value)
	# 	mydb.commit()

	# cursor.execute( "select * from demo_feed") #  show all user group B
	# list_user = cursor.fetchall()
	# user_name = []
	# for all_record in list_user:
	# 	user_name = all_record[0]
	# 	following_nam = all_record[1]
	# 	match_demo.update({user_name : following_nam})

	# cursor.execute( "select * from groupa_users") #  show all user group B
	# list_a = cursor.fetchall()
	# for all_record in list_a:
	# 	table_a = all_record[0]
	# 	following_a = all_record[1]
	# 	match_all_table.update({table_a : following_a})
	
	# cursor.execute( "select * from groupb_users") #  show all user group B
	# list_a = cursor.fetchall()
	# for all_record in list_a:
	# 	table_b = all_record[0]
	# 	following_b = all_record[1]
	# 	match_all_table.update({table_b : following_b})
	


	# for demo_key,demo_val in match_demo.items():
	# 	for both_key,both_val in match_all_table.items():
	# 		if demo_val == "User doesn't exist":
	# 			print("user does not exist ",both_key)
	# 		elif both_val == "User doesn't exist":
	# 			pass
	# 		if  demo_key == both_key:
	# 			if  demo_val == both_val:
	# 				print(f'when equal  {demo_key}  {both_val}   {demo_val}')
	# 				pass
	# 			else:
	# 				# if demo_val or both_val == 'No Followers':
	# 				if demo_val == "User doesn't exist":
	# 					pass
	# 				elif both_val == "User doesn't exist":
	# 					pass
	# 				if demo_val == 'No Followers':
	# 					vals='Unfollowing @'+str(both_val)
	# 				elif both_val == 'No Followers':
	# 					vals ='Following @'+str(demo_val)
	# 				else:   
	# 					a = demo_val
	# 					b = both_val
	# 					if len(b)>len(a):
	# 						status_foll = 'Unfollowing @'
	# 					else:   
	# 						status_foll = 'Following @'
	# 					a = a.replace('[','')
	# 					a = a.replace(']','')
	# 					a = a.replace(' ','')

	# 					lista = a.split(',')

	# 					b = b.replace('[','')
	# 					b = b.replace(']','')
	# 					b = b.replace(' ','')

	# 					listb = b.split(',')

	# 					max_list=[]
	# 					min_list=[]
	# 					if len(lista)>len(listb):
	# 						max_list = lista
	# 						min_list = listb
	# 					else:
	# 						max_list = listb
	# 						min_list = lista
	# 					change_list=[]
	# 					for each in max_list:
	# 						if each in min_list:
	# 							pass
	# 						else:
	# 							each = each.replace("'",'')
	# 							change_list.append(each)
	# 					if len(change_list) == 0:
	# 						continue
	# 					change_ = str(change_list)  
	# 					vals = status_foll + change_    
	# 					print(str(demo_key),status_foll,change_list)
	# 				val=str(vals)
	# 				sql="insert into news_feed(username,group_followers,datetime) values (%s,%s,%s);"
	# 				value=(demo_key,val,now)
	# 				cursor.execute(sql,value)
	# 				mydb.commit()               
	# 		else:
	# 			pass
	
	# cursor.execute( "select * from groupa_users")
	# records = cursor.fetchall()
	# for all_record in records:
	# 	user_namess = all_record[0] 
	# 	sql = "DELETE FROM groupa_users WHERE username = %s"
	# 	adr = (user_namess, )
	# 	cursor.execute(sql, adr)
	# 	mydb.commit()    
	
	# cursor.execute( "select * from groupb_users") #  show all user group B
	# list_user = cursor.fetchall()
	# for all_record in list_user:
	# 	user_name = all_record[0] 
	# 	sql = "DELETE FROM groupb_users WHERE username = %s"
	# 	adr = (user_name, )
	# 	cursor.execute(sql, adr)
	# 	mydb.commit() 
	
	# cursor.execute( "select * from group_a_users")
	# records = cursor.fetchall()
	# lista = []
	# for x in records:
	# 	lista.append(x[1])   
	
	# for key,val in user_dicts.items():
	# 	if key in lista:#for group A
	# 		try:
	# 			pendi = 'Pending'
	# 			val=str(val)
	# 			sql="insert into groupa_users(username,groupb_followers,request_status) values (%s,%s,%s);"
	# 			value=(key,val,pendi)
	# 			cursor.execute(sql,value)
	# 		except:
	# 			print('something went wrong for group A')
	# 	#for group B
	# 	else:
	# 		try:
	# 			pendi = 'Pending'
	# 			val=str(val)
	# 			sql="insert into groupb_users(username,groupa_followers,request_status) values (%s,%s,%s);"
	# 			value=(key,val,pendi)
	# 			cursor.execute(sql,value)
	# 		except:
	# 			print('something went wrong for group A')

	# for key,val in user_dict.items():
	# 	if key in lista:#for group A
	# 		try:
	# 			if val == "User doesn't exist":
	# 				sta_ = 'none'
	# 			else:
	# 				sta_ = 'Approved'
	# 			val=str(val)
	# 			sql="insert into groupa_users(username,groupb_followers,request_status) values (%s,%s,%s);"
	# 			value=(key,val,sta_)
	# 			cursor.execute(sql,value)
	# 		except:
	# 			print('something went wrong for group A')
	# 	#for group B
	# 	else:
	# 		try:
	# 			if val == "User doesn't exist":
	# 				sta_ = 'none'
	# 			else:
	# 				sta_ = 'Approved'
	# 			val=str(val)
	# 			sql="insert into groupb_users(username,groupa_followers,request_status) values (%s,%s,%s);"
	# 			value=(key,val,sta_)
	# 			cursor.execute(sql,value)
	# 		except:
	# 			print('something went wrong for group A')
	
	

	# # cursor.execute( "select * from demo_feed") #  show all user group B
	# # list_user = cursor.fetchall()
	# # for all_record in list_user:
	# # 	user_name = all_record[0] 
	# # 	sql = "DELETE FROM demo_feed WHERE username = %s"
	# # 	adr = (user_name, )
	# # 	cursor.execute(sql, adr)
	# # 	mydb.commit()        
	# mydb.commit()
	# mydb.close()
	# cursor.close()
	# print("all Done")