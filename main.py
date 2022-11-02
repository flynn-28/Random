import random

num = '1234567890'

let = 'abcdefghijklmnopqrstuvwxyz'

die = '123456'

cards = ['Joker', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs' , '6 of Clubs' , '7 of Clubs' , '8 of Clubs' , '9 of Clubs' , 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds', 'Joker']

coin = ['Heads', 'Tails']

col = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

pas = 'qwertyuiopasdfghjklzxcvbnm1234567890,.;:/\|][{}]-_=+)(*&^%$#@!)'

randNum = random.sample(num, 1)
randLet = random.sample(let, 1)
randDie = random.sample(die, 1)
randCard = random.sample(cards, 1)
randCoin = random.sample(coin, 1)
randCol = random.sample(col, 1)
randPas = random.sample(pas, 8)

resultNum = ''.join(str(item) for item in randNum)
resultLet = ''.join(str(item) for item in randLet)
resultDie = ''.join(str(item) for item in randDie)
resultCard = ''.join(str(item) for item in randCard)
resultCoin = ''.join(str(item) for item in randCoin)
resultCol = ''.join(str(item) for item in randCol)
resultPas = ''.join(str(item) for item in randPas)


print("Random Number (0-9): " +  resultNum)
print("Random Letter (a-z): " +  resultLet)
print("Random Die Side (1-6): " +  resultDie)
print("Random Playing Card: " +  resultCard)
print("Side of Coin: " +  resultCoin)
print("Random Color: " +  resultCol)
print("Random  Password (8 Charecters): " + resultPas)
