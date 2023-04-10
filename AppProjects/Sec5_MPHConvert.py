print('Welcome to the MPH Converter App!')

enter_mph = input('Please enter your speed in miles per hour: ')

kph = round(float(enter_mph)*1.60934)
print(f'You entered a speed of {enter_mph} (mph) miles per hour, which is approximately {kph} (kph) kilometers per hour!')
