RED = "red"
BLUE = "blue"
YELLOW = "yellow"
color1=str(input('Enter the First Primary color in lowercase letters:'))
color2=str(input('Enter the Second Primary color in lowercase letters:'))
if color1!=RED and color1!=BLUE and color1!=YELLOW:
    print('Error: Invalid Color1')
elif color2!=RED and color2!=BLUE and color2!=YELLOW:
    print('Error: Invalid Color2')
elif color1==color2:
    print('Error: The two colors you entered are same')
else:
    if color1==RED and color2==BLUE or color1==BLUE and color1==RED:
        print ('Purple')
    elif color1==YELLOW and color2==RED or color1==RED or color2==YELLOW:
        print ('Orange')
    elif color1==BLUE and color2==YELLOW or color2==YELLOW or color2==BLUE:
        print('Green)')
