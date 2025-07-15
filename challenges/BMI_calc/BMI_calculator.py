def bmi_cal(weight_kg,height_cm):
    height_m=height_cm/100
    bmi=weight_kg/(height_m**2)
    return bmi
def bmi_category(bmi):
    if bmi<18.5:
        print('underweight')
    elif bmi<24.9:
        print('Normal weight')
    elif bmi>25 and bmi<29.9:
        print('over weight')
    elif bmi>30:
        print('obese')
def main():
    try:
        weight_kg=float(input('enter your weigth in kg :'))
        height_cm=float(input('enter your height in cm :'))

        bmi=bmi_cal(weight_kg,height_cm)
        print('your bmi : ',bmi)
        category=bmi_category(bmi)
    except:
        print('Enter a valid weigth/height !!')

if __name__ == '__main__':
    main()