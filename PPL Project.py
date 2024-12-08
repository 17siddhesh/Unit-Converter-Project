print("Welcome to the Unit Converter!")
print("Choose the type of conversion:")
print("1. Length")
print("2. Weight")
print("3. Temperature")
print("4. Time")
print("5. Exit")

choice = input("Enter the number of your choice: ")

if choice == '1':
    # Length conversion
    print("Choose the unit you want to convert from:")
    print("1. Meters")
    print("2. Kilometers")
    print("3. Centimeters")
    from_unit_choice = int(input("Enter the number corresponding to your choice: "))

    print("Choose the unit you want to convert to:")
    print("1. Meters")
    print("2. Kilometers")
    print("3. Centimeters")
    to_unit_choice = int(input("Enter the number corresponding to your choice: "))

    if from_unit_choice == 1:
        from_unit = "meters"
    elif from_unit_choice == 2:
        from_unit = "kilometers"
    elif from_unit_choice == 3:
        from_unit = "centimeters"
    else:
        print("Invalid from_unit choice.")
        exit()

    if to_unit_choice == 1:
        to_unit = "meters"
    elif to_unit_choice == 2:
        to_unit = "kilometers"
    elif to_unit_choice == 3:
        to_unit = "centimeters"
    else:
        print("Invalid to_unit choice.")
        exit()

    value = float(input(f"Enter the value in {from_unit}: "))

    if from_unit == to_unit:
        result = value
    elif from_unit == "meters" and to_unit == "kilometers":
        result = value / 1000
    elif from_unit == "kilometers" and to_unit == "meters":
        result = value * 1000
    elif from_unit == "meters" and to_unit == "centimeters":
        result = value * 100
    elif from_unit == "centimeters" and to_unit == "meters":
        result = value / 100
    elif from_unit == "kilometers" and to_unit == "centimeters":
        result = value * 100000
    elif from_unit == "centimeters" and to_unit == "kilometers":
        result = value / 100000
    else:
        print("Invalid conversion units for length.")
        exit()

    print(f"{value} {from_unit} = {result} {to_unit}")

elif choice == '2':
    # Weight conversion
    print("Choose the unit you want to convert from:")
    print("1. Kilograms")
    print("2. Pounds")
    print("3. Grams")
    from_unit_choice = int(input("Enter the number corresponding to your choice: "))

    print("Choose the unit you want to convert to:")
    print("1. Kilograms")
    print("2. Pounds")
    print("3. Grams")
    to_unit_choice = int(input("Enter the number corresponding to your choice: "))

    if from_unit_choice == 1:
        from_unit = "kilograms"
    elif from_unit_choice == 2:
        from_unit = "pounds"
    elif from_unit_choice == 3:
        from_unit = "grams"
    else:
        print("Invalid from_unit choice.")
        exit()

    if to_unit_choice == 1:
        to_unit = "kilograms"
    elif to_unit_choice == 2:
        to_unit = "pounds"
    elif to_unit_choice == 3:
        to_unit = "grams"
    else:
        print("Invalid to_unit choice.")
        exit()

    value = float(input(f"Enter the value in {from_unit}: "))

    if from_unit == to_unit:
        result = value
    elif from_unit == "kilograms" and to_unit == "pounds":
        result = value * 2.20462
    elif from_unit == "pounds" and to_unit == "kilograms":
        result = value / 2.20462
    elif from_unit == "kilograms" and to_unit == "grams":
        result = value * 1000
    elif from_unit == "grams" and to_unit == "kilograms":
        result = value / 1000
    elif from_unit == "grams" and to_unit == "pounds":
        result = value / 453.592
    elif from_unit == "pounds" and to_unit == "grams":
        result = value * 453.592
    else:
        print("Invalid conversion units for weight.")
        exit()

    print(f"{value} {from_unit} = {result} {to_unit}")

elif choice == '3':
    # Temperature conversion
    print("Choose the unit you want to convert from:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    from_unit_choice = int(input("Enter the number corresponding to your choice: "))

    print("Choose the unit you want to convert to:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    to_unit_choice = int(input("Enter the number corresponding to your choice: "))

    if from_unit_choice == 1:
        from_unit = "Celsius"
    elif from_unit_choice == 2:
        from_unit = "Fahrenheit"
    elif from_unit_choice == 3:
        from_unit = "Kelvin"
    else:
        print("Invalid from_unit choice.")
        exit()

    if to_unit_choice == 1:
        to_unit = "Celsius"
    elif to_unit_choice == 2:
        to_unit = "Fahrenheit"
    elif to_unit_choice == 3:
        to_unit = "Kelvin"
    else:
        print("Invalid to_unit choice.")
        exit()

    value = float(input(f"Enter the value in {from_unit}: "))

    if from_unit == to_unit:
        result = value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result = (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        result = (value - 273.15) * 9/5 + 32
    else:
        print("Invalid conversion units for temperature.")
        exit()

    print(f"{value} {from_unit} = {result} {to_unit}")

elif choice == '4':
    # Time conversion
    print("Choose the unit you want to convert from:")
    print("1. Seconds")
    print("2. Minutes")
    print("3. Hours")
    from_unit_choice = int(input("Enter the number corresponding to your choice: "))

    print("Choose the unit you want to convert to:")
    print("1. Seconds")
    print("2. Minutes")
    print("3. Hours")
    to_unit_choice = int(input("Enter the number corresponding to your choice: "))

    if from_unit_choice == 1:
        from_unit = "seconds"
    elif from_unit_choice == 2:
        from_unit = "minutes"
    elif from_unit_choice == 3:
        from_unit = "hours"
    else:
        print("Invalid from_unit choice.")
        exit()

    if to_unit_choice == 1:
        to_unit = "seconds"
    elif to_unit_choice == 2:
        to_unit = "minutes"
    elif to_unit_choice == 3:
        to_unit = "hours"
    else:
        print("Invalid to_unit choice.")
        exit()

    value = float(input(f"Enter the value in {from_unit}: "))

    if from_unit == to_unit:
        result = value
    elif from_unit == "seconds" and to_unit == "minutes":
        result = value / 60
    elif from_unit == "minutes" and to_unit == "seconds":
        result = value * 60
    elif from_unit == "seconds" and to_unit == "hours":
        result = value / 3600
    elif from_unit == "hours" and to_unit == "seconds":
        result = value * 3600
    elif from_unit == "minutes" and to_unit == "hours":
        result = value / 60
    elif from_unit == "hours" and to_unit == "minutes":
        result = value * 60
    else:
        print("Invalid conversion units for time.")
        exit()

    print(f"{value} {from_unit} = {result} {to_unit}")

elif choice == '5':
    print("Exiting the Unit Converter. Goodbye!")
else:
    print("Invalid choice. Please restart the program.")

input("Press Enter to exit...")
