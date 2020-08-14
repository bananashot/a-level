slogans = ["Still in Mama's arms", 'Preschool Maniac', 'Elementary school', 
           'Middle school', 'High school', 'College', 'Working for the man', 'The Golden Years']
ages = [list(range(0, 3)), list(range(3, 5)), list(range(5, 12)), list(range(12, 15)), list(range(15, 19)), list(range(19, 23)), list(range(23, 66)), list(range(66, 101))]

dict_age = dict(zip(slogans, ages))

age_choice = int(input('Choose your destiny: '))
    
for k, v in dict_age.items():
    if age_choice in v:
        print(k)          
    if age_choice > 100 or age_choice < 0 :
        print('This program is for humans')
        break
