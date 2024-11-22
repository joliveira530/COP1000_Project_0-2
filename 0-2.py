AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def startProgram():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("\n1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")

while True:
    startProgram()
    response = input("")
    if (response == "1"):
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for cars in AllowedVehiclesList:
            print(cars)      
    if (response == "2"):
        make = input('\nPlease Enter the full Vehicle name: ')
        if make in AllowedVehiclesList:
            print(f'{make} is an authorized vehicle')
        else:
            print(f'{make} is not an authorized vehicle, if you received this in error please check the spelling and try again')
    if (response == "3"):
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        break