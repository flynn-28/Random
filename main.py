import random

num = '1234567890'

let = 'abcdefghijklmnopqrstuvwxyz'

die = '123456'

cards = ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs' , '6 of Clubs' , '7 of Clubs' , '8 of Clubs' , '9 of Clubs' , 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds', 'Joker']

coin = ['Heads', 'Tails']

col = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

ste = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

sym = '!@#$%^&*()_+=-{}|[]\:;?/>.<,"'

ele = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']

pas = sym + let + num 

hello = 9
b = 2

randNum = random.sample(num, 1)
randNum2 = random.sample(num, 2)
randLet = random.sample(let, 1)
randDie = random.sample(die, 1)
randCard = random.sample(cards, 1)
randCoin = random.sample(coin, 1)
randCol = random.sample(col, 1)
randSte = random.sample(ste, 1)
randEle = random.sample(ele, 1)
randSym = random.sample(sym, 1)
randPas = random.sample(pas, 8)

resultNum = ''.join(str(item) for item in randNum)
resultNum2 = ''.join(str(item) for item in randNum2)
resultLet = ''.join(str(item) for item in randLet)
resultDie = ''.join(str(item) for item in randDie)
resultCard = ''.join(str(item) for item in randCard)
resultCoin = ''.join(str(item) for item in randCoin)
resultCol = ''.join(str(item) for item in randCol)
resultSte = ''.join(str(item) for item in randSte)
resultSym = ''.join(str(item) for item in randSym)
resultEle = ''.join(str(item) for item in randEle)
resultPas = ''.join(str(item) for item in randPas)

print("Random Number (0-9): " +  resultNum)
print("Random 2 Digit Number (0-99): " +  resultNum2)
print("Random Letter (a-z): " +  resultLet)
print("Random Die Side (1-6): " +  resultDie)
print("Random Playing Card: " +  resultCard)
print("Side of Coin: " +  resultCoin)
print("Random Color: " +  resultCol)
print("Random State(US): " +  resultSte)
print("Random Symbol: " +  resultSym)
print("Random Element: " +  resultEle)
print("Random Password (8 Charecters): " + resultPas)

q1 = input("Would you like to see the lists? (y/n): ").lower()
if q1 == 'yes' or q1 == 'y':
  print(num)
  print(let)
  print(die)
  print(cards)
  print(coin)
  print(col)
  print(ste)
  print(sym)
  print(ele)
  print(pas)

elif q1 == 'no' or q1 == 'n':
     print("Goodbye!")
else:
      print("Not a valid answer! Please choose y, n, yes, or no")
