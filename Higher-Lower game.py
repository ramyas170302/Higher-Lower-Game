import random
data=data = [
    {
        "name": "Cristiano Ronaldo",
        "work": "Footballer",
        "followers": 635,
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "work": "Footballer",
        "followers": 503,
        "country": "Argentina"
    },
    {
        "name": "Selena Gomez",
        "work": "Singer & Actress",
        "followers": 430,
        "country": "USA"
    },
    {
        "name": "Kylie Jenner",
        "work": "Businesswoman & Model",
        "followers": 400,
        "country": "USA"
    },
    {
        "name": "Virat Kohli",
        "work": "Cricketer",
        "followers": 278,
        "country": "India"
    },
    {
        "name": "Zendaya",
        "work": "Actress & Singer",
        "followers": 190,
        "country": "USA"
    },
    {
        "name": "Dwayne Johnson",
        "work": "Actor & Wrestler",
        "followers": 396,
        "country": "USA"
    },
    {
        "name": "Taylor Swift",
        "work": "Singer-Songwriter",
        "followers": 310,
        "country": "USA"
    },
    {
        "name": "Narendra Modi",
        "work": "Prime Minister of India",
        "followers": 90,
        "country": "India"
    },
    {
        "name": "Shah Rukh Khan",
        "work": "Actor",
        "followers": 46,
        "country": "India"
    }
]
def info(compare):
    name=compare["name"]
    work=compare["work"]
    country=compare["country"]
    print(f"{name}, {work}, {country}")
def compare(guess,follower1,follower2):
    if follower1 > follower2:
        if guess==1:
            return True
        else:
            return False
    else:
        if guess==2:
            return True
        else:
            return False



score=0
print("WELCOME TO HIGHER-LOWER GAME..")
compare1=random.choice(data)
flag=True
while flag==True:
    compare2=random.choice(data)
    while compare2==compare1:
        compare2=random.choice(data)
    info(compare1)
    print("V/S")
    info(compare2)
    follower1=compare1["followers"]
    follower2=compare2["followers"]
    guess=int(input("who as more followers in insta 1 or 2:\n"))
    is_correct=compare(guess,follower1,follower2)
    compare1=compare2
    if is_correct==True:
        score+=1
        print(f"you are correct.your score is {score}")
        flag=True
    else:
        print(f"you are wrong.your score is {score}")
        flag=False
    print(f"1: {follower1} followers.")
    print(f"2:{follower2} followers.")
