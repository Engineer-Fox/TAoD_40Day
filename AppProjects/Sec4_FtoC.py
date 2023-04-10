print('Hello!  Welcome to the temperature conversion application!')

enter_f = input('Please enter the temperature you wish to convert in Farenheit: ')
print(f'You entered {enter_f} degrees Farenheit!')

convert_c = (float(enter_f)-32)*(5/9)
rounded_c = round(convert_c, 2)
print(f'The temperature would be approximately {rounded_c} in degrees Celcius!')
