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
	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	try:
		cursor.execute( "select * from group_a_users") #  demo table data
		list_user___a_ = cursor.fetchall()	
		cursor.execute( "select * from existing_table") #  show all user group B
		existing_table_d = cursor.fetchall()
		for all_records_ in list_user___a_:
			for list__bb_ds_d in existing_table_d:
				match_uers = list__bb_ds_d[0]
				a_grooup  = all_records_[3]
				if match_uers == a_grooup:
					update_users  = all_records_[1]
					val  = list__bb_ds_d[1]
					print(match_uers)
					print(a_grooup)
					print(update_users)
					sql="select username from existing_table where username=%s;"
					value=match_uers
					is_exist = cursor.execute(sql,value)
					print(is_exist)
					if is_exist==1:
						sql="update existing_table set username=%s where groua_bp_followers=%s;"
						value=(update_users,val)
						cursor.execute(sql,value)
						mydb.commit()
					if is_exist==0:
						sql="update existing_table set username=%s where groua_bp_followers=%s;"
						value=(update_users,val)
						cursor.execute(sql,value)
						mydb.commit()
	except:
		pass

	try:
		cursor.execute( "select * from group_b_users") #  demo table data
		list_user___a_ = cursor.fetchall()	
		cursor.execute( "select * from existing_table_1") #  show all user group B
		existing_table_1_u = cursor.fetchall()
		for all_records_ in list_user___a_:
			for list_b_ds_d_ in existing_table_1_u:
				match_uers = list_b_ds_d_[0]
				a_grooup  = all_records_[3]
				if match_uers == a_grooup:
					update_users_b  = all_records_[1]
					val  = list_b_ds_d_[1]
					print(match_uers)
					print(a_grooup)
					print(update_users_b)
					sql="select username from existing_table_1 where username=%s;"
					value=match_uers
					is_exist = cursor.execute(sql,value)
					print(is_exist)
					if is_exist==1:
						sql="update existing_table_1 set username=%s where groua_bp_followers=%s;"
						value=(update_users_b,val)
						cursor.execute(sql,value)
						mydb.commit()
					if is_exist==0:
						sql="update existing_table_1 set username=%s where groua_bp_followers=%s;"
						value=(update_users_b,val)
						cursor.execute(sql,value)
						mydb.commit()
	except:
		pass

	print("dfsdfsdfsad",login_name,password,list_user_a,list_user_b)
	
	pending_list_a = []
	pending_list_b = []
	loin_name = 'soccer_superstarzz_'
	pasword = 'soccer1234556'
	loader = Instaloader()
	try:
		loader.login(loin_name, pasword)
	except:
		print('cannot login')
	for i,each_profile in enumerate(list_user_a):
		al_following_a = []
		each_profiles = each_profile[1]
		ID = each_profile[2]
		time.sleep(2)
		print(each_profiles) 
		if i == 27:
			loin_name = 'football___foreverr___'
			pasword = 'soccerstarts123456'
			loader = Instaloader()
			try:
				loader.login(loin_name, pasword)
			except:
				print('cannot login') 

		if i == 54:
			loin_names = '_fitness_spartans'
			paswords = 'C@lesthenics1698'
			loader = Instaloader()
			try:
				loader.login(loin_names, paswords)
			except:
				print('cannot login')

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
			user_dict_a.update({each_profiles: "Cet utilisateur n'existe pas"})
			time.sleep(40)
			continue
		nowss = datetime.now()
		cursor.execute( "select * from group_b_users")
		records = cursor.fetchall()
		listbs = []
		for xss in records:
		  listbs.append(xss[1])

		match_all_table_1 = {}
		cursor.execute( "select * from existing_table") #  show all user group B
		list_users = cursor.fetchall()
		user_names = []
		for all_records in list_users:
			user_names = all_records[0]
			following_nams = all_records[1]
			# print("dsdsadas",following_nams)
			match_all_table_1.update({user_names : following_nams})
		for both_key_,both_val in match_all_table_1.items():
			if each_profiles == both_key_:
				demo_val = str(al_following_a)
				if both_val == "Cet utilisateur n'existe pas":
					print("User Not Exisit")
				else:
					print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
					if both_val == demo_val:
						print("********************************************************************************",demo_val)
					else:
						a = demo_val
						b = both_val
						if len(b)>len(a):
							status_foll = "S'est désabonné @"
						else:   
							status_foll = "S'est abonné @"
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
								print("print_________________",each)
								if each in listbs:
									change_list.append(each)
						if len(change_list) == 0:
							continue
						change_ = str(change_list)  
						vals = status_foll + change_    
						print(str(each_profiles),status_foll,change_list)                
						val=str(vals)
						sql="insert into news_feed(username,group_followers,datetime) values (%s,%s,%s);"
						value=(each_profiles,val,nowss)
						cursor.execute(sql,value)
					mydb.commit()
			else:
				pass 
		

	loin_names = 'football___idol___'
	paswords = 'soccerstarts1234'
	loader = Instaloader()
	try:
		loader.login(loin_names, paswords)
	except:
		print('cannot login')

	for i,each_profile in enumerate(list_user_b):
		al_following_b = []
		
		each_profiles = each_profile[1]
		ID = each_profile[2]
		time.sleep(2)  

		print(each_profiles)
		if i == 23:
			loin_names = '_fitness_spartans'
			paswords = 'C@lesthenics1698'
			loader = Instaloader()
			try:
				loader.login(loin_names, paswords)
			except:
				print('cannot login')
		
		if i == 55:
			loin_names = 'football___foreverr___'
			paswords = 'soccerstarts123456'
			loader = Instaloader()
			try:
				loader.login(loin_names, paswords)
			except:
				print('cannot login')
		if i == 78:
			loin_name = '_gods_of_soccer_'
			pasword = 'soccer1234'
			loader = Instaloader()
			try:
				loader.login(loin_name, pasword)
			except:
				print('cannot login')

		if i == 99:
			loin_name = 'soccer_superstarzz_'
			pasword = 'soccer1234556'
			loader = Instaloader()
			try:
				loader.login(loin_name, pasword)
			except:
				print('cannot login')


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
			user_dict_b.update({each_profiles: "Cet utilisateur n'existe pas"})
			time.sleep(40)
			continue
		nowss = datetime.now()
		cursor.execute( "select * from group_a_users")
		records = cursor.fetchall()
		listas = []
		for x in records:
		  listas.append(x[1])
		
		match_all_table1 = {}
		cursor.execute( "select * from existing_table_1") #  show all user group B
		list_users = cursor.fetchall()
		user_names = []
		for all_records in list_users:
			user_names = all_records[0]
			following_nams = all_records[1]
			# print("dsdsadas",following_nams)
			match_all_table1.update({user_names : following_nams})
		for both_key_,both_val in match_all_table1.items():
			if each_profiles == both_key_:
				demo_val = str(al_following_b)
				if both_val == "Cet utilisateur n'existe pas":
					print("User Not Exisit")
				else:
					print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
					if both_val == demo_val:
						print("-********************************************************************",both_val)
					else:
						a = demo_val
						b = both_val
						if len(b)>len(a):
							status_foll = "S'est désabonné @"
						else:   
							status_foll = "S'est abonné @"
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
								print("print_________________",each)
								if each in listas:
									change_list.append(each)
						if len(change_list) == 0:
							continue
						change_ = str(change_list)  
						vals = status_foll + change_    
						print(str(each_profiles),status_foll,change_list)                
						val=str(vals)
						sql="insert into news_feed(username,group_followers,datetime) values (%s,%s,%s);"
						value=(each_profiles,val,nowss)
						cursor.execute(sql,value)
						mydb.commit()
			else:
				pass
	
	return pending_list_a,pending_list_b

	

# if __name__ == '__main__':
def	instgram_data():	
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
		list_user_a.append(all_datat_)

	cursor.execute( "select * from group_b_users")
	list_usera = cursor.fetchall() 
	for all__datat_ in list_usera:
		list_user_b.append(all__datat_)
	
	# list_user_a =[(1, 'm.elarouch', '3116019831', 'momoo.el'), (1, 'aurel2fois_', '1340187927', '5445fsdfsdf'), (1, 'nathan_kln9', '1625600888', None), (1, 'adil_taoui', '5756945515', None), (1, 'exaumpmbl', '2245506029', None), (1, 'd.momo10', '1546082349', None), (1, 'titouanthomas_', '1938903117', None), (1, 'wilson.odobert', '6804055226', None), (1, 'ndombasi.n', '3611434068', None), (1, 'w.bianda', '1281165103', None), (1, 'naat_8', '6609940791', None), (1, 'l.gourna27', '1497933584', None), (1, 'i.gharbi10', '5921225183', None), (1, 'l.dacunha09', '2222796988', None), (1, 'o.solet_18', '1906989766', None), (1, 'n.mbuku', '6174778860', None), (1, 'lucienagoume', '8487547487', None), (1, 'ugo_bertelli_', '1464755102', None), (1, 'loic.jr', '4369401153', None), (1, 'amine_gouiri', '4264435206', None), (1, 'e.cama10', '1834475355', None), (1, 'khaliil.6', '12322289372', None), (1, 'emeran.n', '4329949626', None), (1, 'e.millot17', '1617291673', None), (1, 't.nianzou', '2142829208', None), (1, 'k.nagera7', '14565805753', None), (1, 'ntenda_02', '2527382125', 'ntenda.j'), (1, 'arnaud_kalimuendo', '1835122559', None), (1, 'johann_lpn', '5564101759', None), (1, 'alioutraore', '5328952357', None), (1, 'hnmassengo', 'None', None), (1, 'k.nsona', '2907270280', None), (1, 'soppy.brandon', '1733254542', None)]
	# list_user_b = [(1, 'availlant24', '8268833071', None), (1, 'guerra.frederic', '2365789157', None), (1, 'robindes_s', '6191653229', None), (1, 'footinveston_agency', '3068193848', None), (1, 'g_foot', '4642142050', None), (1, 'sparka_management', '34255355706', None), (1, 'anto.mng', '9895840338', None), (1, 'jl_sport_consulting', '18308458382', None), (1, 'rochilddzabana', '1429020770', None), (1, 'utopiagrp', '3571445318', None), (1, 'ludovicparadinas', '6191819223', None), (1, 'davidbonnan', '11390722864', None), (1, 'charlesdebris', '1644252042', None), (1, 'stmanagement.off', '16695624776', None), (1, '66.sedat', '7869152150', None), (1, 'bonnotalexandre', '8427482687', None), (1, 'mike_libz', '1526043965', None), (1, 'ljuboja.ljuboja.officiel', '561177650', None), (1, 'cabinet_3a', '12252062879', None), (1, 'florentvagnetti', '285842311', None), (1, 'playoff.club', '52037930', None), (1, 'njegary', 'None', None), (1, 'jonathan_totc', '16638459474', None), (1, 'tb.55', '1594570952', None), (1, 'sigmafootagency', '339588572', None), (1, 'fwsports', '6741236642', None), (1, 'kollo44', '1094797299', None), (1, 'djam_consulting', '5002537427', None), (1, 't_e_d_d_y_._', '50779816', None), (1, 'onsidegroup', '6276617861', None), (1, 'hermannmiller', '3604995291', None), (1, 'pascal_elbaz', '2667923289', None), (1, 'khams_1', '1933964691', None), (1, 'yat.agency', '30260875260', None), (1, 'h2hmanagement', '461393953', None), (1, 'florian_lefvr', '855298203', None), (1, '433_management', '7748797018', None), (1, 'anwarbakasse', '5972788427', None), (1, 'gadiricamarajr', '946341102', None), (1, 'borislvl10', '7410749057', None), (1, 'ad_avocat', '7566297058', None), (1, 'guidiala_adama', '402846056', None), (1, 'cracksmansport', '15305567801', None), (1, 'vscareermanagement', '8527731888', None), (1, 'niag_traore', '2033700629', None), (1, 'hugo_mlc', '9208945891', None), (1, 'romain_decool_442', '14777747994', None), (1, 'marinnicolas_16', '292908503', None), (1, 'general_junior', '183031009', None)]


	for i in range(1):
		bot_username = []
		bot_password = []
		cursor.execute( "select * from login_credentials") 
		login = cursor.fetchall()
		logins = []
		for login_credentail in login:
			bot_username.append(login_credentail[0])
			bot_password.append(login_credentail[1])
	
		login_name=bot_username[i]
		password = bot_password[i]
		list_user_a,list_user_b = bot_scrape(login_name,password,list_user_a,list_user_b) # returned target profile is pending list    
	
	user_dict = {}
	privete_dict = {}
	not_exist = {}
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
		if val == "Cet utilisateur n'existe pas":
			not_exist.update({key : "Cet utilisateur n'existe pas"})

		if len(val) == 0:
			if val == "Cet utilisateur n'existe pas":
				pass
			else:
				privete_dict.update({key : 'Personne'})
		else:
			for each_user in val:
				if each_user in users___b:
					print("*****************************************************",key,each_user)
					user_list.append(each_user)
				else:
					pass
				if len(user_list) == 0:
					if val == "Cet utilisateur n'existe pas":
						pass
					else:
						user_dict.update({key : 'Personne'})
				else:           
					user_dict.update({key : user_list})
	
	for key,val in user_dict_b.items():
		user_list = []
		if val == "Cet utilisateur n'existe pas":
			not_exist.update({key : "Cet utilisateur n'existe pas"})
		if len(val) == 0:
			if val == "Cet utilisateur n'existe pas":
				pass
			else:
				privete_dict.update({key : 'Personne'})
		else:
			for each_user in val:
				if each_user in users___a:
					print("*****************************************************",key,each_user)
					user_list.append(each_user)
				else:
					pass
			if len(user_list) == 0:
				if val == "Cet utilisateur n'existe pas":
					pass
				else:
					user_dict.update({key : 'Personne'})
			else:           
				user_dict.update({key : user_list})

	try:
		cursor.execute( "select * from group_a_users") #  demo table data
		list_user_a = cursor.fetchall()	
		cursor.execute( "select * from groupb_users") #  show all user group B
		list__bb_d = cursor.fetchall()
		for all_records in list_user_a:
			for list__bb_ds in list__bb_d:
				table_s = all_records[3]
				list_uu = []
				if table_s == None:
					pass
				else:
					list_uu.append(table_s)
				for find_u in list_uu:
					b_username = list__bb_ds[0]
					following_b = list__bb_ds[1]
					table__new_u = all_records[1]
					import re
					temp = re.findall(find_u, following_b)
					try:
						find_value = temp[0]
						song = table__new_u
						print(following_b.replace(find_value ,song))
						val = following_b.replace(find_value ,song)
						val=str(val)
						sql="select username from groupb_users where username=%s;"
						value=b_username
						is_exist = cursor.execute(sql,value)
						if is_exist==1:
							sql="update groupb_users set groupa_followers=%s where username=%s;"
							value=(val,b_username)
							cursor.execute(sql,value)
							mydb.commit()
						if is_exist==0:
							sql="update groupb_users set groupa_followers=%s where username=%s;"
							value=(val,b_username)
							cursor.execute(sql,value)
							mydb.commit()
					except:
						pass
	except:
		pass
	try:
		cursor.execute( "select * from group_b_users") #  demo table data
		list_user__b = cursor.fetchall()	
		cursor.execute( "select * from groupa_users") #  show all user group B
		list__bb_d = cursor.fetchall()
		for all_records_ in list_user__b:
			for list__bb_ds_d in list__bb_d:
				table_s = all_records_[3]
				list_uu = []
				if table_s == None:
					pass
				else:
					list_uu.append(table_s)
				for find_u in list_uu:
					b_username = list__bb_ds_d[0]
					# print(b_username)
					following__a = list__bb_ds_d[1]
					table__new_u = all_records_[1]
					import re
					temp = re.findall(find_u, following__a)
					try:
						find_value = temp[0]
						song = table__new_u
						print(following__a.replace(find_value ,song))
						val = following__a.replace(find_value ,song)
						val=str(val)
						sql="select username from groupa_users where username=%s;"
						value=b_username
						is_exist = cursor.execute(sql,value)
						# print(is_exist)
						if is_exist==1:
							sql="update groupa_users set groupb_followers=%s where username=%s;"
							value=(val,b_username)
							cursor.execute(sql,value)
							mydb.commit()
						if is_exist==0:
							sql="update groupa_users set groupb_followers=%s where username=%s;"
							value=(val,b_username)
							cursor.execute(sql,value)
							mydb.commit()
					except:
						pass
	except:
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
	
	cursor.execute( "select * from group_b_users")
	records = cursor.fetchall()
	listb = []
	for xs in records:
		listb.append(xs[1]) 

	for key,val in not_exist.items():
		if key in lista:#for group A
			try:
				Not_e = 'Utilisateur introuvable'
				val=str(val)
				sql="insert into groupa_users(username,groupb_followers,request_status) values (%s,%s,%s);"
				value=(key,val,Not_e)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group A')
		else:
			if key in listb:
				try:
					Not_e =  'Utilisateur introuvable'
					val=str(val)
					sql="insert into groupb_users(username,groupa_followers,request_status) values (%s,%s,%s);"
					value=(key,val,Not_e)
					cursor.execute(sql,value)
				except:
					print('something went wrong for group bb')
			else:
				pass


	for key,val in privete_dict.items():
		if key in lista:#for group A
			try:
				pen = "En attente d'acceptation"
				val=str(val)
				sql="insert into groupa_users(username,groupb_followers,request_status) values (%s,%s,%s);"
				value=(key,val,pen)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group A')
		else:
			if key in listb:
				try:
					pen = "En attente d'acceptation"
					val=str(val)
					sql="insert into groupb_users(username,groupa_followers,request_status) values (%s,%s,%s);"
					value=(key,val,pen)
					cursor.execute(sql,value)
				except:
					print('something went wrong for group bb')
			else:
				pass
		
	for key,val in user_dict.items():
		if key in lista:#for group A
			try:
				App = 'Demande acceptée'
				val=str(val)
				sql="insert into groupa_users(username,groupb_followers,request_status) values (%s,%s,%s);"
				value=(key,val,App)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group A')
		#for group B
		else:
			if key in listb:
				try:
					App = 'Demande acceptée'
					val=str(val)
					sql="insert into groupb_users(username,groupa_followers,request_status) values (%s,%s,%s);"
					value=(key,val,App)
					cursor.execute(sql,value)
				except:
					print('something went wrong for group BB')
			else:
				pass
	cursor.execute( "select * from existing_table") #  show all user group B
	list_user = cursor.fetchall()
	for all_record in list_user:
		user_name = all_record[0] 
		sql = "DELETE FROM existing_table WHERE username = %s"
		adr = (user_name, )
		cursor.execute(sql, adr)
		mydb.commit()

	cursor.execute( "select * from existing_table_1") #  show all user group B
	list_user = cursor.fetchall()
	for all_record in list_user:
		user_name = all_record[0] 
		sql = "DELETE FROM existing_table_1 WHERE username = %s"
		adr = (user_name, )
		cursor.execute(sql, adr)
		mydb.commit()

	for key,val in user_dict_a.items():
		val=str(val)
		sql="insert into existing_table(username,groua_bp_followers) values (%s,%s);"
		value=(key,val)
		cursor.execute(sql,value)
		mydb.commit()
	

	for key,val in user_dict_b.items():
		val=str(val)
		sql="insert into existing_table_1(username,groua_bp_followers) values (%s,%s);"
		value=(key,val)
		cursor.execute(sql,value)
		mydb.commit()       
	
	nows = datetime.now()
	for key,val in not_exist.items():
		if key in lista:#for group A
			try:
				Not_e = 'Utilisateur introuvable'
				val=str(val)
				sql="insert into groupa_users_backup(username,groupb_followers,request_status,datetime) values (%s,%s,%s,%s);"
				value=(key,val,Not_e,nows)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group A')
		else:
			if key in listb:
				try:
					Not_e =  'Utilisateur introuvable'
					val=str(val)
					sql="insert into groupb_users_backup(username,groupa_followers,request_status,datetime) values (%s,%s,%s,%s);"
					value=(key,val,Not_e,nows)
					cursor.execute(sql,value)
				except:
					print('something went wrong for group bb')
			else:
				pass
	for key,val in privete_dict.items():
		if key in lista:#for group A
			try:
				pen = "En attente d'acceptation"
				val=str(val)
				sql="insert into groupa_users_backup(username,groupb_followers,request_status,datetime) values (%s,%s,%s,%s);"
				value=(key,val,pen,nows)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group A')
		else:
			if key in listb:
				try:
					pen = "En attente d'acceptation"
					val=str(val)
					sql="insert into groupb_users_backup(username,groupa_followers,request_status,datetime) values (%s,%s,%s,%s);"
					value=(key,val,pen,nows)
					cursor.execute(sql,value)
				except:
					print('something went wrong for group bb')
			else:
				pass
		
	for key,val in user_dict.items():
		if key in lista:#for group A
			try:
				App = 'Demande acceptée'
				val=str(val)
				sql="insert into groupa_users_backup(username,groupb_followers,request_status,datetime) values (%s,%s,%s,%s);"
				value=(key,val,App,nows)
				cursor.execute(sql,value)
			except:
				print('something went wrong for group A')
		#for group B
		else:
			if key in listb:
				try:
					App = 'Demande acceptée'
					val=str(val)
					sql="insert into groupb_users_backup(username,groupa_followers,request_status,datetime) values (%s,%s,%s,%s);"
					value=(key,val,App,nows)
					cursor.execute(sql,value)
				except:
					print('something went wrong for group BB')
			else:
				pass
	mydb.commit()
	mydb.close()
	cursor.close()
	print("all Done")
schedule.every(12).hours.do(instgram_data) 
while True:
	print("Program is working")
	schedule.run_pending()
	time.sleep(1)
