import random

weather = ['Sunny','Rainy','Cloudy']
forecast = {}


def generateForecast(day):
    weatherType = random.choice(weather)
    if weatherType == 'Sunny':
        temp = random.randint(35,50)
        humidity = random.randint(10,25)
    elif weatherType == 'Rainy':
        temp = random.randint(20,30)
        humidity = random.randint(60,100)
    else: 
        temp = random.randint(15,22)
        humidity = random.randint(0,20)

    return [weatherType,temp,humidity]


def statisticalSummary(forecast):
    if forecast:
        total_temp = 0
        total_humidity = 0
        temp = []
        humidity = []
        for key,value in forecast.items():
            total_temp += value[1]
            temp.append(value[1])
            total_humidity += value[2]
            humidity.append(value[2])

        avg_temp = total_temp/len(forecast)
        avg_humidity = total_humidity/len(forecast)

        return [avg_temp,avg_humidity],temp,humidity
    else: 
        return 
        

def main():
    print("Welcome to the Python Weather Forecast Simulator")
    number_of_days = int(input("Enter the number of days to simulate : "))
    if number_of_days<1:
        print("Enter valid number of days ie., greater than 0")
        number_of_days = int(input("Enter the number of days to simulate : "))

    day = 1
    
    while day <= number_of_days:
        data = generateForecast(day)
        forecast[day] = data
        day+=1
    while True:
        print()
        print("1. Weather Forecast for total days")
        print("2. Statistical report")
        print("3. Exit")
        operation = int(input("Enter a operation number from above: "))
        if operation == 1:
            for key,value in forecast.items():
                print()
                print(f"Day {key}:")
                print(f"Weather type : {value[0]} , temperature : {value[1]}° , humidity : {value[2]}% ")
                print()
            print("Total weather forecast data is displayed.")
            print("--------------------------------------------------------------------")
        elif operation == 2:
            repo,temp,humidity = statisticalSummary(forecast)
            if forecast:   
                print()
                print("Statistical report for the weather forecast: ")
                print()
                print(f"    Average temp : {repo[0]}° ")
                print(f"    Average humidity : {repo[1]}% ")
                print(f"    Minimum temperature : {min(temp)}° ")
                print(f"    Maximum temperature : {max(temp)}° ")
                print(f"    Minimum humidity : {min(humidity)}% ")
                print(f"    Minimum humidity : {max(humidity)}% ")
                print()
                print("End of report.")
            else: 
                print("No data found to display")
            print("--------------------------------------------------------------------")
        elif operation == 3:
            print()
            print("Thank you for using weather forecast simulator. Bye...")
            print("--------------------------------------------------------------------")
            return 

main()
    
    


                         