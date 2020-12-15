from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
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

mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
cursor = mydb.cursor()

@login_required
def logout_request(request):
	logout(request)
	return redirect("/")

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print("898998989889899889989889",username)
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/index/')
			else:
				return HttpResponse("Your account was inactive.")
		else:
			print("Someone tried to login and failed.")
			print("They used username: {} and password: {}".format(username,password))
			return render(request, 'login.html', {})
	else:
		return render(request, 'login.html', {})





@login_required
def index(request):
	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	try:
		cursor.execute( "select * from groupb_users") #  show all user group B
		list_user_b = cursor.fetchall()
		all_user_ = []
		user_name_b = []
		following_name_b = []
		following_status_b = []
		for all_record in list_user_b:
			user_name_b.append(all_record[0])
			all_user_.append(all_record[0])
			following_name_b.append(all_record[1])
			following_status_b.append(all_record[2])
	except:
		pass
	try:
		cursor.execute( "select * from groupa_users") #  show all user group A
		list_user_a = cursor.fetchall()
		user_name_a = []
		following_name_a = []
		following_status = []
		for all_record in list_user_a:
			user_name_a.append(all_record[0])
			all_user_.append(all_record[0])
			following_name_a.append(all_record[1])
			following_status.append(all_record[2])
	except:
		pass
	try:

		for all_user__ in user_name_a:
			user__d = request.GET.get('Usernames')
			if all_user__ == user__d:
				sql = "SELECT * FROM groupa_users WHERE username = %s"
				adr = (user__d, )
				cursor.execute(sql, adr)
				myresult = cursor.fetchall()
				nes_user = []
				u_status = []
				for x in myresult:
					nes_user.append(x[0])
					u_status.append(x[1])
					print("user__duser__d",u_status,nes_user)
				return render(request, 'serachbar.html',{'user_name_a':nes_user,'following_name_a':u_status})
	except:
		pass
				
	try:
		for all_user__ in user_name_b:
			user__d = request.GET.get('Usernames')
			if all_user__ == user__d:
				sql = "SELECT * FROM groupb_users WHERE username = %s"
				adr = (user__d, )
				cursor.execute(sql, adr)
				myresult = cursor.fetchall()
				nes_user = []
				u_status = []
				for x in myresult:
					nes_user.append(x[0])
					u_status.append(x[1])
				print("user__duser__d",u_status,nes_user)   
				return render(request, 'serachbar.html',{'user_name_a':nes_user,'following_name_a':u_status})
	except:
		pass
	cursor.close()
	mylist1 = zip(user_name_a, following_name_a, following_status)

	context1 = {
			'mylist1': mylist1,
		}
	mylist2 = zip(user_name_b, following_name_b, following_status_b)

	context2 = {
			'mylist2': mylist2,
		}


	return render(request, 'userdashboard.html',{'users':all_user_,'user_name_b':user_name_b,'following_name_b':following_name_b,'user_name_a':user_name_a,'following_name_a':following_name_a,'statuss':following_status,'statasss':following_status_b,'mylist1': mylist1,'mylist2': mylist2 })





def show_following(request):

	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()

	sql = "DELETE FROM news_feed WHERE username='_fitness_spartans'"
	cursor.execute(sql,)
	mydb.commit()
	return HttpResponse("sdfsdfasdfsadfsd")  







@login_required
def follow_added_A(request):

	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	cursor.execute( "select * from demo_table") #  show all user group B
	list_user_b = cursor.fetchall()
	users_all = []
	for all_record in list_user_b:
		users_all.append(all_record[0])
	if len(users_all) == 0:
		return redirect('/insert_a/')
	else:
		cursor.execute( "select * from login_credentials") 
		login = cursor.fetchall()
		logins = []
		for login_credentail in login:
			logins.append(login_credentail)
		for username in logins:
			usernames = username[0]
			passwords =  username[1]
			try:
				driver = webdriver.Chrome('chromedriver.exe')
				driver.get('https://www.instagram.com/accounts/login/')
				time.sleep(6)
				driver.find_element_by_name('username').send_keys(usernames)
				time.sleep(6)
				driver.find_element_by_name('password').send_keys(passwords)
				time.sleep(4)
				driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
				time.sleep(4)
				driver.find_element_by_xpath("//button[contains(.,'Not Now')]").click()
				time.sleep(4)
				driver.find_element_by_xpath("//button[contains(.,'Not Now')]").click()
				for user in users_all:
					print(user)
					time.sleep(1)
					try:
						driver.get('https://www.instagram.com/'+str(user)+'/')
						time.sleep(2)
						user_status = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[1]/h2[1]').text
						print("user_status",user_status)
						time.sleep(2)
						if user_status == 'This Account is Private':
							time.sleep(2)
							followButton =driver.find_element_by_xpath('//section//section//div//div[1]//button[1]')
							followButton.click()
							time.sleep(1)
						elif user_status == 'Requested':
							pass
						time.sleep(15)
					except:
						print("pass")
				driver.close()
			except:
				driver.close()
				pass
		try:
			if users_all[-1] == user:
				for user_delete in users_all:
					sql = "DELETE FROM demo_table WHERE username = %s"
					adr = (user_delete, )
					cursor.execute(sql, adr)
					mydb.commit()
		except:
			pass
		cursor.close()         
		return redirect('/insert_a/')

@login_required
def follow_added_B(request):
	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	cursor.execute( "select * from demo_table") #  show all user group B
	list_user_b = cursor.fetchall()
	users_all = []
	for all_record in list_user_b:
		users_all.append(all_record[0])
	if len(users_all) == 0:
		return redirect('/insert_b/')
	else:
		cursor.execute( "select * from login_credentials") 
		login = cursor.fetchall()
		logins = []
		for login_credentail in login:
			logins.append(login_credentail)
		for username in logins:
			usernames = username[0]
			passwords =  username[1]
			try:
				driver1 = webdriver.Chrome('chromedriver.exe')
				driver1.get('https://www.instagram.com/accounts/login/')
				time.sleep(6)
				driver1.find_element_by_name('username').send_keys(usernames)
				time.sleep(6)
				driver1.find_element_by_name('password').send_keys(passwords)
				time.sleep(4)
				driver1.find_element_by_xpath("//button[contains(.,'Log In')]").click()
				time.sleep(4)
				driver1.find_element_by_xpath("//button[contains(.,'Not Now')]").click()
				time.sleep(4)
				driver1.find_element_by_xpath("//button[contains(.,'Not Now')]").click()
				for user in users_all:
					print(user)
					time.sleep(1)
					try:
						driver1.get('https://www.instagram.com/'+str(user)+'/')
						time.sleep(2)
						user_status = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[1]/h2[1]').text
						print("user_status",user_status)
						time.sleep(2)
						if user_status == 'This Account is Private':
							time.sleep(2)
							followButton =driver.find_element_by_xpath('//section//section//div//div[1]//button[1]')
							followButton.click()
							time.sleep(1)
						elif user_status == 'Requested':
								pass
						time.sleep(10)
					except:
						print("pass")
				driver1.close()
			except:
				driver1.close()
				pass
		try:
			if users_all[-1] == user:
				for user_delete in users_all:
					sql = "DELETE FROM demo_table WHERE username = %s"
					adr = (user_delete, )
					cursor.execute(sql, adr)
					mydb.commit()
		except:
			pass
		cursor.close()         
		return redirect('/insert_b/')



@login_required
def insert_a(request):
	if request.method == 'POST':
		mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
		cursor = mydb.cursor()
		name = request.POST["fname"]
		sql="select username from group_a_users where username=%s;"
		value=name
		is_exist = cursor.execute(sql,value)
		if is_exist==1:
			pass
		if is_exist==0:
			try:
				cursor.execute( "select * from group_a_users") 
				id_ = cursor.fetchall()
				for all_ in id_:
				  data = all_[0]
				 #user in put value
				increment  =  1 + int(data)
			except:
				increment = 1
			val = name
			sql="insert into group_a_users(id,username) values (%s,%s);"
			value=(increment,val)
			cursor.execute(sql,value)
			val = name
			sql="insert into demo_table(username) values (%s);"
			value=(val)
			cursor.execute(sql,value)
			mydb.commit()
			cursor.close()
	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	cursor.execute( "select * from group_a_users") #  show all user group A
	list_user_a = cursor.fetchall()
	user_name_a = []
	user_name_a_user = []
	for all_record in list_user_a:
		user_name_a.append(all_record[1])
		user_name_a_user.append(all_record[1])

	return render(request, 'insert.html',{'user_name_a':user_name_a,'user_name_a_user':user_name_a_user})

@login_required
def insert_group_b(request):
	if request.method == 'POST':
		mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
		cursor = mydb.cursor()
		name = request.POST["fname"]
		sql="select username from group_b_users where username=%s;"
		value=name
		is_exist = cursor.execute(sql,value)
		if is_exist==1:
			pass
		if is_exist==0:
			try:
				cursor.execute( "select * from group_b_users") 
				id_ = cursor.fetchall()
				for all_ in id_:
				  data = all_[0]
				increment  =  1 + int(data)
			except:
				increment = 1
			val = name 
			sql="insert into group_b_users(id,username) values (%s,%s);"
			value=(increment,val)
			cursor.execute(sql,value)
			val = name
			sql="insert into demo_table(username) values (%s);"
			value=(val)
			cursor.execute(sql,value)
			mydb.commit()
			cursor.close()

	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	cursor.execute( "select * from group_b_users") #  show all user group A
	list_user_a = cursor.fetchall()
	user_name_a = []
	user_name___b = []
	for all_record in list_user_a:
		user_name_a.append(all_record[1])
		user_name___b.append(all_record[1])

	return render(request, 'insert_delete.html',{'user_name_a':user_name_a,'user_name___b':user_name___b})


def delete_user_a(request):
	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	user_name = request.GET.get('order')
	print(user_name)
	sql = "DELETE FROM group_a_users WHERE username = %s"
	adr = (user_name, )
	cursor.execute(sql, adr)
	mydb.commit()
	return HttpResponseRedirect('/insert_a/')

def dell_search(request):
	user_name_s = request.GET.get('Usernames')
	return render(request, 'dello_.html',{'user_name_s':user_name_s})


def dell_search_b(request):
	user_name_b = request.GET.get('Usernames')
	print("user_name_b",user_name_b)
	return render(request, 'dell_b_u.html',{'user_name_b':user_name_b})


def delete_user_b(request):
	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	user_name = request.GET.get('order')
	print(user_name)
	sql = "DELETE FROM group_b_users WHERE username=%s"
	adr = (user_name, )
	cursor.execute(sql, adr)
	mydb.commit()
	return HttpResponseRedirect('/insert_b/')

@login_required
def feed_page(request):
	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	cursor.execute( "select * from time_updates")
	recordss = cursor.fetchone()
	show_times = recordss[0]
	current_times = recordss[1]
	feed = []
	follow_feed = []
	datetime_feed = []
	sql = "SELECT * FROM news_feed ORDER BY datetime DESC"
	cursor.execute(sql)
	records = cursor.fetchall()
	cursor.execute( "select * from group_a_users") #  demo table data
	list_user_a = cursor.fetchall()
	cursor.execute( "select * from group_a_users")
	rec_incheck = cursor.fetchall()
	listas = []
	for _check in rec_incheck:
		listas.append(_check[1]) 
	show_old_name = []  
	for x in records:
		a=x[1]
		if a == "Unfollowing @User doesn't exist":
			pass
		else:
			feed.append(x[0])
			show_old_name.append(x[3])  
			a=x[1]
			# print(a)
			if a[0] == 'C':
				print("------")
				data = a.split('C')
				aas = data[1]
				dds=aas.split(' ')
				print(dds[1])
				print(dds[2])
				use_star = dds[1] + "  a changé son nom et devient   " + dds[2]
				follow_feed.append(use_star)
				datetime_feed.append(x[2])
			else:
				if a[6] == 'a':
					print("dfsdfdsa")
					a = a.replace("S'est abonné",'')
					s="S'est abonné "
					a = a.replace('[','')
					a = a.replace(']','')
					a = a.replace(' ','')
					lista = a.split(',')
					for each_usr in lista:
						each_usr = each_usr.replace("'","")
						s+=f'{each_usr}, '
					if s[-2] == ',':
						stats = s[:-2]
					else:
						stats = s
					print("**************************************************",stats)
					follow_feed.append(stats)
				else:   
					a = a.replace("S'est désabonné",'')
					s="S'est désabonné "
					a = a.replace('[','')
					a = a.replace(']','')
					a = a.replace(' ','')
					lista = a.split(',')
					for each_usr in lista:
						each_usr = each_usr.replace("'","")
						s+=f'{each_usr}, '
					if s[-2] == ',':
						stats = s[:-2]
					else:
						stats = s
					s = s.replace('-',' ')
					follow_feed.append(stats)
				s=''
				datetime_feed.append(x[2])

	for feed_val in feed:
		user_feed = request.GET.get('Usernames')
		if feed_val == user_feed:
			sql = "SELECT * FROM news_feed WHERE username = %s"
			adr = (user_feed, )
			cursor.execute(sql, adr)
			myresult = cursor.fetchall()
			news_user = []
			feed_status = []
			datetime_status = []
			for x in myresult:
				news_user.append(x[0])
				a=x[1]
				if a[0] == 'C':
					data = a.split('C')
					aas = data[1]
					dds=aas.split(' ')
					use_star = dds[1] + "  a changé son nom et devient  " + dds[2]
					feed_status.append(use_star)
					datetime_status.append(x[2])
				else:
					if a[6] == 'a':                     
						a = a.replace("S'est abonné",'')
						s="S'est abonné "
						a = a.replace('[','')
						a = a.replace(']','')
						a = a.replace(' ','')
						lista = a.split(',')
						for each_usr in lista:
							each_usr = each_usr.replace("'","")
							s+=f'{each_usr}, '
						if s[-2] == ',':
							stats = s[:-2]
						else:
							stats = s
						feed_status.append(stats)
					else:   
						a = a.replace("S'est désabonné",'')
						s="S'est désabonné "
						a = a.replace('[','')
						a = a.replace(']','')
						a = a.replace(' ','')
						lista = a.split(',')
						for each_usr in lista:
							each_usr = each_usr.replace("'","")
							s+=f'{each_usr}, '
						if s[-2] == ',':
							stats = s[:-2]
						else:
							stats = s
						s = s.replace('-',' ')
						feed_status.append(stats)
					s=''
					datetime_status.append(x[2])
			return render(request, 'new_feed.html',{'users':feed,'feeds':news_user,'follow_feeds':feed_status,'nows':datetime_status})
	cursor.close()
	
	mylist = zip(feed, follow_feed, datetime_feed)

	context = {
			'mylist': mylist,
		}

	return render(request, 'feed.html',{'users':feed,'feeds':feed,'follow_feeds':follow_feed,'nows':datetime_feed,'showtimes':show_times,'current_time':current_times,
		'userssss':show_old_name,'jassssss':listas,'mylist': mylist,} )
	

def csv_download(request):
	mydb = pymysql.connect(host='localhost',user='root',password='Data@123',db='instagram_groups')    
	cursor = mydb.cursor()
	feed = []
	follow_feed = []
	follow_feedss = []
	datetime_feed = []
	sql = "SELECT * FROM news_feed ORDER BY datetime DESC"
	cursor.execute(sql)
	records = cursor.fetchall()
	for x in records:
		feed.append(x[0])
		a=x[1]
		if a[0] == 'C':
			data = a.split('C')
			aas = data[1]
			dds=aas.split(' ')
			use_star = dds[1] + "  a change son nom et devient  " + dds[2]
			print("Change Username_______list ",use_star)
			follow_feed.append(use_star)
		elif a[6] == 'a':   
			a = a.replace("S'est abonné",'')
			s="S'est abonné "
			a = a.replace('[','')
			a = a.replace(']','')
			a = a.replace(' ','')
			lista = a.split(',')
			for each_usr in lista:
				each_usr = each_usr.replace("'","")
				s+=f'{each_usr}, '
			if s[-2] == ',':
				stats = s[:-2]
			else:
				stats = s
				print(stats)
			follow_feed.append(stats)
		else:   
			a = a.replace("S'est désabonné",'')
			s="S'est désabonné "
			a = a.replace('[','')
			a = a.replace(']','')
			a = a.replace(' ','')
			lista = a.split(',')
			for each_usr in lista:
				each_usr = each_usr.replace("'","")
				s+=f'{each_usr}, '
			if s[-2] == ',':
				stats = s[:-2]
			else:
				stats = s
			s = s.replace('-',' ')
			follow_feed.append(stats)
		s=''
		datetime_feed.append(x[2])
	import csv
	cursor.close()
	for ddddd in follow_feed:
		import re
		find_u = "S'est abonné"
		song = "S'est abonne"
		temp = re.findall(find_u, ddddd)
		try:
			val = ddddd.replace(temp[0] ,song)
			follow_feedss.append(val)
		except:
			try:
				find_u = "S'est désabonné"
				song = "S'est desabonne"
				temp = re.findall(find_u, ddddd)
				val = ddddd.replace(temp[0] ,song)
				follow_feedss.append(val)
			except:
				follow_feedss.append(ddddd)
				print(ddddd)
				pass
		
	
	df=pd.DataFrame({'Username':feed,'Status':follow_feedss,'Datetime':datetime_feed,})
	df.to_csv('instagram_data.csv',index=True)
	filename     = "instagram_data.csv" # Select your file here.
	wrapper      = FileWrapper(open(filename))
	response = HttpResponse(content_type='csv')
	filename = "instagram_data.csv".format("data")
	fp = StringIO()
	response = HttpResponse(content_type='csv')
	response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
	writer =df.to_csv(response)

	return response

