import sys
import os
#import matplotlib.pyplot as plt - I was going to plot the fares on a chart
import pandas as pd
from menu import Menu

# I don't really like to use global variables 
# but just trying to get my idea to work
main_response=''
start_borough =''
end_borough =''
dftransportation = ''
pu_locations =''
do_locations = ''

# If I have more time I would figure out a better way to reference this data

YELLOW_CAB_FILE = "yellow_tripdata_2018-01.csv"
GREEN_CAB_FILE = "green_tripdata_2018-01.csv"
FOR_HIRE_FILE = "fhv_tripdata_2018-01.csv"
TAXI_ZONES_FILE = "taxi_zones.csv"

def main():
	global dftransportation
	global main_response
	# Display Main menu
	menu_option_dict = {'1': "Yellow Cab",
						'2': "Green Cab",
						'3': "Exit Program"}
	myMenu = Menu(menu_options=menu_option_dict)

	# Print out menu options to user and begin the main program loop
	myMenu.display_menu()
	while user_input := input("Selection: "):
		if myMenu.is_valid_input(user_input):
			main_response = int(user_input)
			
			if main_response == 1:
					dftransportation = load_csv(os.path.join(sys.path[0] + "\\" + YELLOW_CAB_FILE))
			if main_response == 2:
					dftransportation = load_csv(os.path.join(sys.path[0] + "\\" + GREEN_CAB_FILE))
			if main_response == 3:
				do_exit()  
			choose_start_borough()
		else:
			print("Invalid input. Please enter an option from the menu\n")

def load_csv(f):
	# These files are large. 
	# I could have loaded the data in chunks to conserve memory. 
	# Memory increased 18% on my labtop

	return pd.read_csv(f)
	

def choose_start_borough():
	global start_borough
	# If I had time I would have: 
	# 1. Included a Back option to go back
	# 2. Broke the display menu out to separate function

	pop_menu_option_dict = {'1': "Brooklyn",
							'2': "Bronx",
							'3': "Manhattan",
							'4': "Queens",
							'5': "Staten Island",
							'6': "Exit"}
	pop_menu = Menu(menu_title="Choose start borough:", menu_options=pop_menu_option_dict)

	pop_menu.display_menu()

	while user_input := input("Selection: "):
		if pop_menu.is_valid_input(user_input):
			print(user_input)
			if user_input == '6':
				do_exit()
			start_borough = pop_menu_option_dict[user_input]
			choose_end_borough()
		else:
			print("Invalid input. Please enter an option from the menu\n")
			pop_menu.display_menu()

def choose_end_borough():
	global end_borough
	# If I had time I would have included a Back option to go back
	pop_menu_option_dict = {'1': "Brooklyn",
							'2': "Bronx",
							'3': "Manhattan",
							'4': "Queens",
							'5': "Staten Island",
							'6': "Exit"}
	pop_menu = Menu(menu_title="Choose end borough", menu_options=pop_menu_option_dict)

	pop_menu.display_menu()
	while user_input := input("Selection: "):
		if pop_menu.is_valid_input(user_input):
			if user_input == '6':
				do_exit()
			end_borough = pop_menu_option_dict[user_input]
			get_location_ids()
		else:
			print("Invalid input. Please enter an option from the menu\n")
			pop_menu.display_menu()

def get_location_ids():
	global pu_locations
	global do_locations

	
	try:
		# Had to make sure error wouldn't happen if not ran from app folder 
		dftax_zones = load_csv(os.path.join(sys.path[0] + "\\" + TAXI_ZONES_FILE))
		pu_location = dftax_zones.BOROUGH == start_borough
		do_location = dftax_zones.BOROUGH == end_borough
		pu_locations = dftax_zones[pu_location].LOCATIONID
		do_locations = dftax_zones[do_location].LOCATIONID
	
		if main_response == 1:
			print_yellow_fare_data()
		if main_response == 2:
			print_green_fare_data()

	except Exception as err:
		print(err)

def print_yellow_fare_data():
	trip_data = dftransportation[["tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count", 
	"trip_distance", "PULocationID", "DOLocationID", "fare_amount", "extra", "mta_tax", "tip_amount", "total_amount"]]
	trip_data.head()
	print(trip_data[(trip_data.PULocationID.isin(pu_locations)) & (trip_data.DOLocationID.isin(do_locations))])
	do_exit()

def print_green_fare_data():
	trip_data = dftransportation[["lpep_pickup_datetime", "lpep_dropoff_datetime", "passenger_count", 
	"trip_distance", "PULocationID", "DOLocationID", "fare_amount", "extra", "mta_tax", "tip_amount", "total_amount"]]
	trip_data.head()
	print(trip_data[(trip_data.PULocationID.isin(pu_locations)) & (trip_data.DOLocationID.isin(do_locations))])
	do_exit()

def do_exit():
	sys.exit(0)

if __name__ == "__main__":
	main()