from json import load, dump
from os import system
from time import sleep

import feature

statusLoading = feature.loadData()

if statusLoading :
	passLogin = feature.login()
	if passLogin:
		print('Welcome!')
		sleep(2)
		menu_choice = ''

		while menu_choice != 'e':
			system('cls')
			feature.print_menu()
			menu_choice = input('Type in a number : ').lower()

			if menu_choice == '1':
				feature.print_scheduled_ticket()
				input('ENTER to EXIT')

			elif menu_choice == '2':
				feature.schedule_ticket()
				input('ENTER to EXIT')

			elif menu_choice == '3':
				feature.remove_ticket()
				input('ENTER to EXIT')

			elif menu_choice == '4':
				feature.lookup_ticket()
				input('ENTER to EXIT')	
			elif menu_choice == 'e':
				break
			else:
				print('Input Menu Choice Correctly')
	else:
		print('Failed to login')

else :
	print('Apps cannot run.')	



