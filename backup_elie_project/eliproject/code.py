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
import schedule
import time
user_dict_a = {}
user_dict_b = {}
def bot_scrape(login_name,password,list_user_a,list_user_b):
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("dfsdfsdfsad",login_name,password,list_user_a,list_user_b)
	# mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	# cursor = mydb.cursor()
	# start_scrapping = datetime.now()
	# now = datetime.now()
	# add_scrapping = start_scrapping + timedelta(hours=12)
	# save_date = add_scrapping.strftime("%Y-%m-%d %H:%M")
	# now_scrapping = start_scrapping.strftime("%Y-%m-%d %H:%M")
	# sql="update time_updates set time_date=%s ;"
	# value=(save_date)
	# cursor.execute(sql,value)
	# sql="update time_updates set now_date=%s ;"
	# value=(now_scrapping)
	# cursor.execute(sql,value)
	# mydb.commit()
	# now = datetime.now()
	pending_list_a = []
	pending_list_b = []
	# login_name = 'soccer_starrss'
	loader = Instaloader()
	login_nam = 'football___legends__'
	pasword = 'Legends1234'
	try:
		loader.login(login_nam, pasword)
	except:
		print('cannot login') 

	# user_dict_a = {}
	# cursor.execute( "select * from group_a_users")
	# list_user_a = cursor.fetchall() 
	# list_user_aa = ['aurel2fois_','eliemoussafir','william_saliba','lauriennnte','wilson_smk','nikhil.bhaskar']
	for i,each_profile in enumerate(list_user_a):
		al_following_a = []
		each_profiles = each_profile
		time.sleep(2)
		print(each_profiles)
		try:
			profile = Profile.from_username(loader.context, each_profiles)
			followees = profile.get_followees()
			print('\n')
			print('\n')
	
			print(f'profile number  {i}')
			loader.context.log('Profile {} has {} followees'.format(profile.username, profile.followees))
			print('\n')
			
	
			for followee in followees:
				al_following_a.append(followee.username)
			user_dict_a.update({each_profiles:al_following_a})
			print("******",al_following_a)
			if len(al_following_a) == 0 and profile.followees !=0:
				print('this user is private')
				pending_list_a.append(profile.username)
			
			time.sleep(40)
		except:
			print(f'user link does not exist   {i} {each_profiles}')
			user_dict_a.update({each_profiles: "User doesn't exist"})
			time.sleep(40)
			continue
	
	# user_dict_b = {}	
	time.sleep(300)
	# cursor.execute( "select * from group_b_users")
	# list_user_b = cursor.fetchall()
	#############################################################################################################################
	# All_user_b =['robindes_s' ,'footinveston_agency','mhn.93t','guy2zmo_78','daouda.weidmann','naaelaa94']
	loin_name = 'football___heros___'
	pasword = 'soccerstarts1234'
	loader = Instaloader()
	try:
		loader.login(loin_name, pasword)
	except:
		print('cannot login')

	for i,each_profile in enumerate(list_user_b):
		al_following_b = []
		each_profiles = each_profile
		time.sleep(2)
		try:
			profile = Profile.from_username(loader.context, each_profiles)
			followees = profile.get_followees()
			print(f'profile number  {i}')
			loader.context.log('Profile {} has {} followees'.format(profile.username, profile.followees))
			
	
			for followee in followees:
				al_following_b.append(followee.username)
			user_dict_b.update({each_profiles:al_following_b})
			print("******",al_following_b)
			if len(al_following_b) == 0 and profile.followees !=0:
				print('this user is private')
				pending_list_b.append(profile.username)
			time.sleep(40)
		except:
			print(f'user link does not exist  {i} {each_profiles}')
			print("user link doesn't exist")
			user_dict_b.update({each_profiles: "User doesn't exist"})
			time.sleep(40)
			continue
	
	return pending_list_a,pending_list_b

	

if __name__ == '__main__':
# def	instgram_data():	
	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
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
	now = datetime.now()
	list_user_a = []
	list_user_b = []
	cursor.execute( "select * from group_a_users")
	list_usera = cursor.fetchall() 
	for all_datat_ in list_usera:
		list_user_a.append(all_datat_[1])

	cursor.execute( "select * from group_b_users")
	list_usera = cursor.fetchall() 
	for all__datat_ in list_usera:
		list_user_b.append(all__datat_[1])
	# list_user_a = ['aurel2fois_','eliemoussafir','william_saliba','lauriennnte','wilson_smk','amandeepgill52']    
	# list_user_b = ['philnabe','olivierazan','yourfirstsports','robindes_s']
	# list_user_aa.extend(list_user_b)
	
	# print(list_user_a)

	# print(list_user_b)

	for i in range(1):
		bot_username = []
		bot_password = []
		cursor.execute( "select * from login_credentials") 
		login = cursor.fetchall()
		logins = []
		for login_credentail in login:
			bot_username.append(login_credentail[0])
			bot_password.append(login_credentail[1])
		# print(bot_username)
		# print(bot_password)
		login_name=bot_username[i]
		password = bot_password[i]
		list_user_a,list_user_b = bot_scrape(login_name,password,list_user_a,list_user_b) # returned target profile is pending list    
	
		


	print('this is prending list')
	print(len(list_user_a))
	print("list_user_a",list_user_a)
	print(len(list_user_b))
	print("list_user_b",list_user_b)
	user_dict = {}
	privete_dict = {}
	not_exist = {}
	# All_user_b =['robindes_s' ,'footinveston_agency','mhn.93t','guy2zmo_78','daouda.weidmann','naaelaa94']
	cursor.execute( "select * from group_a_users") #  demo table data
	list_user_a = cursor.fetchall()
	cursor.execute( "select * from group_b_users") #  demo table data
	list_user_b = cursor.fetchall()
	users___a = []
	users___b = []
	for all_record in list_user_a:
		users___a.append(all_record[1])
	for all_record in list_user_b:
		users___b.append(all_record[1])	
	
	for key,val in user_dict_a.items():
		user_list = []
		# if val == "User doesn't exist":
		# 	user_dict.update({key : "User doesn't exist"})
		# else:
		# 	pass
		if val == "User doesn't exist":
			not_exist.update({key : "User doesn't exist"})

		if len(val) == 0:
			if val == "User doesn't exist":
				pass
			else:
				privete_dict.update({key : 'No Followers'})
		else:
			for each_user in val:
				if each_user in users___b:
					print("*****************************************************",key,each_user)
					user_list.append(each_user)
				else:
					pass
				if len(user_list) == 0:
					if val == "User doesn't exist":
						pass
					else:
						user_dict.update({key : 'No Followers'})
				else:           
					user_dict.update({key : user_list})
	
	# All_user_a =['moussa.cisse3','wilson_smk','mih.management','olivierazan']
	for key,val in user_dict_b.items():
		user_list = []
		# if val == "User doesn't exist":
		# 	user_dict.update({key : "User doesn't exist"})
		# else:
		# 	pass
		if val == "User doesn't exist":
			not_exist.update({key : "User doesn't exist"})
		if len(val) == 0:
			if val == "User doesn't exist":
				pass
			else:
				privete_dict.update({key : 'No Followers'})
		else:
			for each_user in val:
				if each_user in users___a:
					print("*****************************************************",key,each_user)
					user_list.append(each_user)
				else:
					pass
			if len(user_list) == 0:
				if val == "User doesn't exist":
					pass
				else:
					user_dict.update({key : 'No Followers'})
			else:           
				user_dict.update({key : user_list})
	
	
	print("user_dict",user_dict)
	print("jasssssjasssssjasssssjasssssjasssssjasssss",not_exist)
	print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*",privete_dict)
	
	match_demo = {}
	match_all_table = {}
	for key,val in user_dict.items():
		val=str(val)
		sql="insert into demo_feed(username,group_followers) values (%s,%s);"
		value=(key,val)
		cursor.execute(sql,value)
		mydb.commit()
	for key,val in privete_dict.items():
		val=str(val)
		sql="insert into demo_feed(username,group_followers) values (%s,%s);"
		value=(key,val)
		cursor.execute(sql,value)
		mydb.commit()

	cursor.execute( "select * from demo_feed") #  show all user group B
	list_user = cursor.fetchall()
	user_name = []
	for all_record in list_user:
		user_name = all_record[0]
		following_nam = all_record[1]
		match_demo.update({user_name : following_nam})

	cursor.execute( "select * from groupa_users") #  show all user group B
	list_a = cursor.fetchall()
	for all_record in list_a:
		table_a = all_record[0]
		following_a = all_record[1]
		match_all_table.update({table_a : following_a})
	
	cursor.execute( "select * from groupb_users") #  show all user group B
	list_a = cursor.fetchall()
	for all_record in list_a:
		table_b = all_record[0]
		following_b = all_record[1]
		match_all_table.update({table_b : following_b})


	for demo_key,demo_val in match_demo.items():
		for both_key,both_val in match_all_table.items():
			if both_val == "User doesn't exist":
				pass
				print("user does not exist ",both_key)
			else:
				pass
			if  demo_key == both_key:
				if  demo_val == both_val:
					print(f'when equal  {demo_key}  {both_val}   {demo_val}')
					pass
				else:
					if both_val == "User doesn't exist":
						print("user does not exist ",both_key)
					else:
						pass
					if demo_val == 'No Followers':
						vals='Unfollowing @'+str(both_val)
					elif both_val == 'No Followers':
						vals ='Following @'+str(demo_val)
					else:   
						a = demo_val
						b = both_val
						if len(b)>len(a):
							status_foll = 'Unfollowing @'
						else:   
							status_foll = 'Following @'
						a = a.replace('[','')
						a = a.replace(']','')
						a = a.replace(' ','')

						lista = a.split(',')

						b = b.replace('[','')
						b = b.replace(']','')
						b = b.replace(' ','')

						listb = b.split(',')

						max_list=[]
						min_list=[]
						if len(lista)>len(listb):
							max_list = lista
							min_list = listb
						else:
							max_list = listb
							min_list = lista
						change_list=[]
						for each in max_list:
							if each in min_list:
								pass
							else:
								each = each.replace("'",'')
								change_list.append(each)
						if len(change_list) == 0:
							continue
						change_ = str(change_list)  
						vals = status_foll + change_    
						print(str(demo_key),status_foll,change_list)
					val=str(vals)
					sql="insert into news_feed(username,group_followers,datetime) values (%s,%s,%s);"
					value=(demo_key,val,now)
					cursor.execute(sql,value)
					mydb.commit()               
			else:
				pass
	
	cursor.execute( "select * from groupa_users")
	records = cursor.fetchall()
	for all_record in records:
		user_namess = all_record[0] 
		sql = "DELETE FROM groupa_users WHERE username = %s"
		adr = (user_namess, )
		cursor.execute(sql, adr)
		mydb.commit()    
	
	cursor.execute( "select * from groupb_users") #  show all user group B
	list_user = cursor.fetchall()
	for all_record in list_user:
		user_name = all_record[0] 
		sql = "DELETE FROM groupb_users WHERE username = %s"
		adr = (user_name, )
		cursor.execute(sql, adr)
		mydb.commit() 
	
	cursor.execute( "select * from group_a_users")
	records = cursor.fetchall()
	lista = []
	for x in records:
		lista.append(x[1])   
	

	for key,val in not_exist.items():
		if key in lista:#for group A
			try:
				Not_e = 'None'
				val=str(val)
				sql="insert into groupa_users(username,groupb_followers,request_status) values (%s,%s,%s);"
				value=(key,val,Not_e)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group A')
		else:
			try:
				Not_e =  'None'
				val=str(val)
				sql="insert into groupb_users(username,groupa_followers,request_status) values (%s,%s,%s);"
				value=(key,val,Not_e)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group bb')


	for key,val in privete_dict.items():
		if key in lista:#for group A
			try:
				pen = 'Pending'
				val=str(val)
				sql="insert into groupa_users(username,groupb_followers,request_status) values (%s,%s,%s);"
				value=(key,val,pen)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group A')
		else:
			try:
				pen = 'Pending'
				val=str(val)
				sql="insert into groupb_users(username,groupa_followers,request_status) values (%s,%s,%s);"
				value=(key,val,pen)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group bb')
	
	for key,val in user_dict.items():
		if key in lista:#for group A
			try:
				# if is_exist==1:
				#   #update
				#   sql="update groupa_users set groupb_followers=%s where username=%s;"
				#   value=(val,key)
				#   cursor.execute(sql,value)
				# if is_exist==0:
					#insert
				# if val == "User doesn't exist":
				# 	App = 'none'
				# else:
				App = 'Approve'
				val=str(val)
				sql="insert into groupa_users(username,groupb_followers,request_status) values (%s,%s,%s);"
				value=(key,val,App)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group A')
		#for group B
		else:
			
			try:
				# if val == "User doesn't exist":
				# 	App = 'none'
				# else:
				App = 'Approve'
				val=str(val)
				sql="insert into groupb_users(username,groupa_followers,request_status) values (%s,%s,%s);"
				value=(key,val,App)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group BB')
	
	cursor.execute( "select * from demo_feed") #  show all user group B
	list_user = cursor.fetchall()
	for all_record in list_user:
		user_name = all_record[0] 
		sql = "DELETE FROM demo_feed WHERE username = %s"
		adr = (user_name, )
		cursor.execute(sql, adr)
		mydb.commit()        
	
	mydb.commit()
	mydb.close()
	cursor.close()
	print("all Done")


# schedule.every(8).hours.do(instgram_data) 
# while True:
# 	print("Working")
# 	schedule.run_pending()
# 	time.sleep(1)
