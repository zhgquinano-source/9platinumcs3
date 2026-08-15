## Requirements
a. Ask the user to enter a year of birth.  The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.

Example:
Enter your birth year: 1800
Invalid Year, it should not be earlier than 1900

d. Otherwise determine the chinese zodiac sign based on the following starting from 1900.  Note: A zodiac sign will recur after each 12 years.

i. Rat (鼠 / Shǔ)
ii. Ox (牛 / Niú)
iii. Tiger (虎 / Hǔ)
iv. Rabbit (兔 / Tù)
v. Dragon (龙 / Lóng)
vi. Snake (蛇 / Shé)
vii. Horse (马 / Mǎ)
viii. Goat (羊 / Yáng)
ix. Monkey (猴 / Hóu)
x. Rooster (鸡 / Jī)
xi. Dog (狗 / Gǒu)
xii. Pig (猪 / Zhū)

e. CONSIDER only the year of birth.

Example input and output:
Enter your birth year: 2000
Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)

## Code:
try:
    birth_year = int(input("Enter your birth year: "))
except ValueError:
    print("Invalid input. Please enter a valid year.")
    sys.exit()

if birth_year < 1900:
    print("Invalid year, it should not be earlier than 1900.")
    sys.exit()

zodiac_signs = ["Rat (鼠 / Shǔ)", 
"Ox (牛 / Niú)",   
"Tiger (虎 / Hǔ)", 
"Rabbit (兔 / Tù)", 
"Dragon (龙 / Lóng)", 
"Snake (蛇 / Shé)", 
"Horse (马 / Mǎ)", 
"Goat (羊 / Yáng)", 
"Monkey (猴 / Hóu)", 
"Rooster (鸡 / Jī)", 
"Dog (狗 / Gǒu)", 
 "Pig (猪 / Zhū)"]

index = (birth_year - 1900) % 12
zodiac_sign = zodiac_signs[index]
print(f"Your chinese zodiac sign is: {zodiac_sign}")

## Output
Screenshot:

<img width="2048" height="1379" alt="image" src="https://github.com/user-attachments/assets/f778c543-f383-4de7-bba1-f14eff7f9c31" />
