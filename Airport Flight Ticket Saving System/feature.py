from json import load, dump
from os import system
from getpass import getpass
from time import sleep
from reportlab.pdfgen import canvas

import string
import random

fileUser = 'Duser.json'
fileTicket = 'Dticket.json'

user = {} 
ticket = {}

def loadData():
	global user, ticket

	with open(fileUser) as f:
		user = load(f)

	with open(fileTicket) as f:
		ticket = load(f)

	return True

def saveData():
	global user, ticket

	with open(fileUser, 'w') as f:
		dump(user, f)

	with open(fileTicket, 'w') as f:
		dump(ticket, f)


	return True

def login():
	counter = 1
	Username = input('Enter Username :')
	Password = getpass('Enter Password :')
	dataCheck = False
	passLogin = False
	if Username in user:
		dataCheck = True
		passLogin = (user[Username] == Password)

	while (not dataCheck) or (not passLogin):
		counter += 1
		if counter > 3:
			return False
		print('Combination Username and Password is Wrong')
		Username = input('Enter Username :')
		Password = getpass('Enter Password :')
		if Username in user :
			dataCheck = True
			passLogin = (user[Username] == Password)			
	else:
		print('Login Pass')
		return True

def print_menu():
	print('Welcome to Airport Flight Ticket Data Saving System')
	print('[1] Print Scheduled Ticket')
	print('[2] Schedule A Ticket')
	print('[3] Remove A Ticket')
	print('[4] Lookup A Ticket')
	print('[5] Print Ticket as PDF')
	print('[E] Exit')

def print_scheduled_ticket():
	if len(ticket) > 0:
		for info in ticket:
			print(f'Booking Code \t: {info}\nTicket Information\t: ')
			print(f'Airline \t: {ticket[info]["airline"]}\nPassenger \t: {ticket[info]["passenger"]}\nCategory \t: {ticket[info]["category"]}\nFlight Code \t: {ticket[info]["code"]}\nOrigin \t\t: {ticket[info]["origin"]}\nBoarding Date \t: {ticket[info]["boardingDates"]}\nBoarding Time \t: {ticket[info]["boardingTime"]}\nDestination \t: {ticket[info]["destination"]}\nArriving Date \t: {ticket[info]["arrivingDates"]}\nArriving Time \t: {ticket[info]["arrivingTime"]}\nBaggage \t: {ticket[info]["baggage"]}\nTicket Number \t: {ticket[info]["ticketNumber"]}\n')
	else:
		print('There is no ticket scheduled')

def schedule_ticket():
	print('Schedule a ticket\n')

	bookingCode = (random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)).upper()

	airline = input('Airline : ')

	passenger = input('Passenger : ')

	code = (random.choice(string.ascii_letters)+random.choice(string.ascii_letters)).upper()+'-'+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)

	origin = input('Origin : ')

	boardingDate, boardingMonth, boardingYear = input('Boarding Date :').split()
	boardingDate = str(boardingDate)
	boardingMonth = str(boardingMonth)
	boardingYear = str(boardingYear)
	boardingDates = (f"{boardingDate}/{boardingMonth}/{boardingYear}")

	boardingHour, boardingMinute = input('Boarding Time : ').split()
	boardingHour = str(boardingHour)
	boardingMinute = str(boardingMinute)
	boardingTime = (f"{boardingHour}:{boardingMinute}")

	destination = input('Destination : ')

	arrivingDate, arrivingMonth, arrivingYear = input('Arriving Date :').split()
	arrivingDate = str(arrivingDate)
	arrivingMonth = str(arrivingMonth)
	arrivingYear = str(arrivingYear)
	arrivingDates = (f"{arrivingDate}/{arrivingMonth}/{arrivingYear}")

	arrivingHour, arrivingMinute = input('Arriving Time : ').split()
	arrivingHour = str(arrivingHour)
	arrivingMinute = str(arrivingMinute)
	arrivingTime = (f"{arrivingHour}:{arrivingMinute}")

	category = input('Adult / Kid : ')

	baggage = input('Baggage Weight : ')

	ticketNumber = random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)

	ticket[bookingCode] = {
	'airline' : airline,
	'passenger' : passenger,
	'code' : code,
	'origin' : origin,
	'boardingDates' : boardingDates,
	'boardingTime' : boardingTime,
	'destination' : destination,
	'arrivingDates' : arrivingDates,
	'arrivingTime' : arrivingTime,
	'category' : category,
	'baggage' : baggage,
	'ticketNumber' : ticketNumber
	}

	saveData()
	print('Saving Data...')
	sleep(1.5)
	print('Data saved.')



def remove_ticket():
	print('Remove ticket that already land\n')

	bookingCode = input('Booking Code \t:')

	if bookingCode in ticket:
		del ticket[bookingCode]
		saveData()
		print('Removing Data...')
		sleep(1.5)
		print('Data saved.')
	else:
		print(f'{bookingCode} doesnot exists in ticket.')

def lookup_ticket():
	print('Lookup your ticket\n')

	bookingCode = input('Booking Code \t:')

	if bookingCode in ticket:
		print(f'Booking Code \t: {bookingCode}\nTicket Information\t: ')
		print(f'Airline \t: {ticket[bookingCode]["airline"]}\nPassenger \t: {ticket[bookingCode]["passenger"]}\nCategory \t: {ticket[bookingCode]["category"]}\nFlight Code \t: {ticket[bookingCode]["code"]}\nOrigin \t\t: {ticket[bookingCode]["origin"]}\nBoarding Date \t: {ticket[bookingCode]["boardingDates"]}\nBoarding Time \t: {ticket[bookingCode]["boardingTime"]}\nDestination \t: {ticket[bookingCode]["destination"]}\nArriving Date \t: {ticket[bookingCode]["arrivingDates"]}\nArriving Time \t: {ticket[bookingCode]["arrivingTime"]}\nBaggage \t: {ticket[bookingCode]["baggage"]}\nTicket Number \t: {ticket[bookingCode]["ticketNumber"]}')
	else:
		print(f'{bookingCode} does not exists in ticket')



def print_pdf():
	print('Print ticket as PDF')

	bookingCode = input('Booking Code \t:')

	if bookingCode in ticket:
		dataTicket = {bookingCode: {
			'passenger' : ticket[bookingCode]['passenger'],
			'airline' : ticket[bookingCode]['airline'],
			'code' : ticket[bookingCode]['code'],
			'origin' : ticket[bookingCode]['origin'],
			'boardingDates' : ticket[bookingCode]['boardingDates'],
			'boardingTime' : ticket[bookingCode]['boardingTime'],
			'destination' : ticket[bookingCode]['destination'],
			'arrivingDates' : ticket[bookingCode]['arrivingDates'],
			'arrivingTime' : ticket[bookingCode]['arrivingTime'],
			'category' : ticket[bookingCode]['category'],
			'baggage' : ticket[bookingCode]['baggage'],
			'ticketNumber' : ticket[bookingCode]['ticketNumber']}
		}


		class Data:

			def __init__(self, filename, documentTitle, heading):
				self.filename = filename
				self.documentTitle = documentTitle
				self.heading = heading
				self.info = dataTicket

		myData = Data(str(bookingCode+" - "+dataTicket[bookingCode]['passenger']+" - "+dataTicket[bookingCode]['airline']+".pdf"), "FLIGHT TICKET", f"BOOKING CODE: {bookingCode}")
		myPdf = canvas.Canvas(myData.filename)
		myPdf.setTitle(myData.documentTitle)

		myPdf.drawString(225,770,myData.heading)
		myPdf.line(30, 760, 560, 760)

		myText = myPdf.beginText(40,680)

		passenger = "Passenger : "+dataTicket[bookingCode]['passenger']
		airline = "Airlines : "+dataTicket[bookingCode]['airline']
		code = "Flight Code : "+dataTicket[bookingCode]['code']
		origin = "Origin : "+dataTicket[bookingCode]['origin']
		boardingDates = "Boarding Dates : "+dataTicket[bookingCode]['boardingDates']
		boardingTime = "Boarding Time : "+dataTicket[bookingCode]['boardingTime']
		destination = "Destination : "+dataTicket[bookingCode]['destination']
		arrivingDates = "Arriving Dates : "+dataTicket[bookingCode]['arrivingDates']
		arrivingTime = "Arriving Time : "+dataTicket[bookingCode]['arrivingTime']
		category = "Category : "+dataTicket[bookingCode]['category']
		baggage = "Baggage : "+dataTicket[bookingCode]['baggage']
		ticketNumber = "Ticket Number : "+dataTicket[bookingCode]['ticketNumber']
		
		Lines = [passenger, airline, code, origin, boardingDates, boardingTime, destination, arrivingDates, arrivingTime, category, baggage, ticketNumber]
		for line in Lines:
			myText.textLine(line)
		myPdf.drawText(myText)

		myPdf.save()


	else:
		print(f'{bookingCode} does not exist in ticket')