import math
print('Hello!  Welcome to the triangle app!')

leg_A_in = input('Please enter the angle of the first leg of the triangle (in inches): ')
leg_B_in = input('Please neter the angle of the first leg of the triangle (in inches): ')

print('The equation we will use to calculate the hypotenuse of the triangle is A^2+B^2=C^2.  Yay!')

leg_A = int(leg_A_in)
leg_B = int(leg_B_in)

hyp_C = round(math.sqrt((int(leg_A)**2)+(int(leg_B)**2)), 2)
print(f'The hypotenuse of the triangle is {hyp_C} inches!')

print('The formula we will use to calculate the area of the triangle is sqrt(semi_perimeter*(s-A)*(s-B)*(s-H))  !  Yay!!')

semi_perimeter = (leg_A+leg_B+hyp_C)/2
area_t = round(math.sqrt(semi_perimeter*(semi_perimeter-leg_A)*(semi_perimeter-leg_B)*(semi_perimeter-hyp_C)), 2)
print(f'The area of the triangle is {area_t} inches!')

