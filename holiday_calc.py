# Calculate users total holiday cost

# Four functions to calculate totals: 
# Hotel cost, plane cost, car rental, holiday cost

# Hotel cost function
def hotel_cost(nights, city):
    # Dict. with prices per night for each city
    city_hotel_cost = {'rome': 120,
                    'paris': 200,
                    'london': 200,
                    'chicago': 250,
                    'antalya': 100,
                    'shenzhen': 220,
                    'hanoi': 90,
                    'johannesburg': 90,
                    'macau': 70,
                    'bangkok': 200,
                    'nairobi': 95,
                    'singapore': 200,
                    'beijing': 250,
                    'istanbul': 100,
                    'delhi': 80,
                    'tokyo': 240,
                    'sydney': 150
                    }
    # Sum of total nights
    total = nights * city_hotel_cost[city]
    return total

# Plane cost function
def plane_cost(city):
    # Dict. with flight prices for each city
    city_flight_cost = {'rome': 100,
                    'paris': 175,
                    'london': 120,
                    'chicago': 300,
                    'antalya': 200,
                    'shenzhen': 275,
                    'hanoi': 130,
                    'johannesburg': 250,
                    'macau': 250,
                    'bangkok': 300,
                    'nairobi': 220,
                    'singapore': 320,
                    'beijing': 220,
                    'istanbul': 250,
                    'delhi': 150,
                    'tokyo': 290,
                    'sydney': 350
                    }
    # Cost of flight 
    total = city_flight_cost[city]
    return total

# Car rental cost function   
def car_rental(days, city):
    # Dict. with rental prices per day for each city
    city_car_cost = {'rome': 40,
                'paris': 50,
                'london': 60,
                'chicago': 60,
                'antalya': 30,
                'shenzhen': 45,
                'hanoi': 30,
                'johannesburg': 35,
                'macau': 20,
                'bangkok': 15,
                'nairobi': 30,
                'singapore': 50,                    
                'beijing': 50,
                'istanbul': 30,
                'delhi': 25,
                'tokyo': 60,
                'sydney': 55
                }
    # Sum of car rental total
    total = days * city_car_cost[city]
    return total

# Holiday cost total function
def holiday_cost(hotel, plane, car):
    # Sum of total hotel, plane and car 
    total = hotel + plane + car
    return total

# Cities list of available destinations
cities_list = ['rome', 'paris', 'london', 'chicago', 'antalya', 
               'shenzhen', 'hanoi', 'johannesburg', 
               'macau', 'bangkok', 'nairobi', 'singapore', 
               'beijing', 'istanbul', 'delhi', 'tokyo', 'sydney'
                ]

# Message to explain program to user
# Provide list of available cities
print("\nUse this tool to calculate the total cost of your holiday, "
      "including flights, hotel and car hire!\n")
print("We currently offer holidays in the following cities: \n")
for item in cities_list:
    cap_city = item.capitalize()
    print(cap_city)

# Request inputs from user

# While loop to check destination input is available
while True:
    city_flight = input("\nPlease enter the city you will be flying "
                        "to: ").lower()
    if city_flight not in cities_list:
        print("\nSorry there are no flights to your chosen destination. "
              "Please check the list provided for cities with "
              "available holidays.")
        continue
    else:
        break
    
# Try, except numeric inputs for no. of hotel nights and car rental days
while True:
    try:
        num_nights = int(input("\nPlease enter the number of nights you "
                               "will be staying in a hotel (e.g 3): "))
        if num_nights < 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("\nERROR: Invalid entry, please only enter a number (e.g 3).\n")
        continue
    else:
        break

while True:
    try:
        rental_days = int(input("\nPlease enter the number of days you will "
                                "be hiring a car (e.g 4): "))
        if rental_days < 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("\nERROR: Invalid entry, please only enter a number (e.g 3).\n")
        continue
    else:
        break

# Calculate costs using user inputs
    
hotel_total = hotel_cost(num_nights, city_flight)
plane_total = plane_cost(city_flight)
car_total = car_rental(rental_days, city_flight)
holiday_total = holiday_cost(hotel_total, plane_total, car_total)

# Print all details in a readable way
print("\nThe total cost for your holiday in {} is: £{:,.2f}\n"
      .format(city_flight.capitalize(), holiday_total))

print("Cost breakdown:")
print("Flight to {}: £{:,.2f}"
      .format(city_flight.capitalize(), plane_total))
print("Hotel stay for {} night(s): £{:,.2f}"
      .format(num_nights, hotel_total))
print("Car hire for {} day(s): £{:,.2f}\n"
      .format(rental_days, car_total))