import random
import math
import time
import sys

#This is my WRC racing car game

#How many drivers to race against.
CPU_numbers = 9

#Initial Track record.
trackRecord = 1299.547

class Driver:
    def __init__(self, input_gname = "Juan", input_fname = "Perez", input_age = None, input_skill = None):
        # Given Name
        self.gname = input_gname
        # Family Name / Surname
        self.fname = input_fname
        # Driver's Age
        if input_age is None:
            input_age = random.randint(18, 45)
        self.age = input_age
        # Driver's skill level
        if input_skill is None:
            input_skill = random.randint(20,70)
        self.skill = input_skill
        # Three letter family name for the leaderboard.
        self.threeLettersName = self.fname[:3].upper()
        # Which cars belong to this driver.
        self.cars = []
    
    def __repr__(self):
        return "{given} {family}".format(given = self.gname, family = self.fname)

    def status(self):
        status = "This is the driver {given} {family}. {given} is {age} years old. ".format(given = self.gname, family = self.fname, age = self.age)
        if len(self.cars) > 1:
            status += "{given} has got {carsNumber} cars. ".format(given = self.gname, family = self.fname, carsNumber = len(self.cars))
        elif len(self.cars) == 1:
            status += "{given} has got {carsNumber} car, a {car}. ".format(given = self.gname, family = self.fname, carsNumber = len(self.cars), car = self.cars[0])
        else:
            status += "{given} haven't got a car. ".format(given = self.gname, family = self.fname)
        status += "Skill level as a driver is {skill}/100.".format(skill = self.skill)
        return status

    def greet(self):
        print("Hello, very nice to make your acquaintance, my name is {given} {family}.\n".format(given = self.gname, family = self.fname))

    def improveSkill(self, numberOfYears = 1):
        # Increases the value in self.skill by substracting the current value from 100, dividing that result by 4 and adding it to the original value. This way it is warantied it will never go over 100.
        if self.skill < 100:
            initialSkill = self.skill
            for i in range(0,numberOfYears):
                currentSkill = self.skill
                self.skill = math.ceil(((100-currentSkill)/4) + currentSkill)
            # print("Your skill level as a driver went from {old}/100 to {new}/100. Congratulations!\n".format(old = initialSkill, new = self.skill))
            return self.skill
        else:
            pass


class Car:
    def __init__(self, input_owner, input_make = "Volkswagen", input_model = "Golf GTI", input_colour = "White", input_BHP = None, input_tireCondition = None, input_onOff = False):
        # Who the owner of this car is.
        self.owner = input_owner
        self.make = input_make
        self.model = input_model
        self.colour = input_colour
        # Car's Brake Horse Power
        if input_BHP is None:
            input_BHP = random.randint(300,700)
        self.BHP = input_BHP
        # Tire condition. The higher the number the better the condition. It goes from 0 to 100.
        if input_tireCondition is None:
            input_tireCondition = random.randint(0,100)
        self.tireCondition = input_tireCondition
        # This switch determines wether the car is on or not.
        self.onOff = input_onOff
        # Appends this car to the owner's list of cars.
        self.owner.cars.append(self)
        
        
    def __repr__(self):
        return "{colour} {make} {model}".format(colour = self.colour, make = self.make, model = self.model)

    def status(self):
        status = "This is {given} {family}'s {colour} {make} {model}. It's got {BHP} of Brake Horse Power.".format(given = self.owner.gname, family = self.owner.fname, colour = self.colour, make = self.make, model = self.model, BHP = self.BHP)
        if self.tireCondition >= 100:
            status += " With brand new tires."
        elif self.tireCondition > 95:
            status += " With new tires."
        elif self.tireCondition > 80:
            status += " With relatively new tires."
        elif self.tireCondition > 40:            
            status += " With relatively old tires."
        else:
            status += " With very old tires."

        if self.onOff:
            status += " Currently the car is On.\n"
        else:
            status += " Currently the car is Off.\n"
        return status

    def turnOn(self):
        print("The car is On now.\n")
        self.onOff = True
        return self.onOff

    def getNewTires(self):
        self.tireCondition = 100
        # print("New tires have been fitted in your {make} {model}.\n".format(make = self.make, model = self.model))
        return self.tireCondition

    def addBHP(self, times = 1):
        if self.BHP < 750:
            initialBHP = self.BHP
            for i in range(0,times):
                currentBHP = self.BHP
                self.BHP = math.ceil(((750-currentBHP)/2) + currentBHP)
            # print("Your {make} {model}'s Brake Horse Power (BHP) has been increased from {old} to {new} BHP.\n".format(old = initialBHP, new = self.BHP, make = self.make, model = self.model))
            return self.BHP
        else:
            pass

class Track:
    def __init__(self, input_GorA = "Gravel", input_DorR = "Dry"):
        # Gravel or Asphalt. Track kind.
        self.GorA = input_GorA
        # Dry or Wet. Track condition.
        self.DorR = input_DorR
        # The higher the number, the more grip the track has got. Max number is 1,000. This number should be affected by track kind and track condition
        self.gripLevel = 0
        if self.GorA == "Asphalt":
            self.gripLevel += sorted((25, random.randint(15,75), 50))[1]
        else:
            self.gripLevel += sorted((0, random.randint(-20,35), 24))[1]
        
        if self.DorR == "Dry":
            self.gripLevel += sorted((25, random.randint(15,75), 50))[1]
        else:
            self.gripLevel += sorted((0, random.randint(-20,35), 24))[1]

    def __repr__(self):
        return "This track is of {type} and it is currently {condition}. With a grip level of {grip}/100.".format(type = self.GorA, condition = self.DorR, grip = self.gripLevel)

class ANSI:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    YELLOW = "\033[1;33m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

given_names = ['Wade', 'Dave', 'Seth', 'Ivan', 'Juan', 'Sebastien', 'Jorge', 'Dan', 'Brian', 'Roberto', 'Ramon', 'Miles', 'Liam', 'Ott', 'Ethan', 'Lewis', 'Milton', 'Claude', 'Joshua', 'Glen', 'Harvey', 'Blake', 'Antonio']
family_names = ['Smith', 'Johnson', 'Williams', 'Tanak', 'Jones', 'Loeb', 'Ogier', 'Garcia', 'Rodriguez', 'Wilson', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson', 'Perez', 'Lopez', 'Rovanpera', 'Neuville', 'Sordo', 'Evans', 'Katsuta', 'Breen', 'Lappi', 'Greensmith', 'Mikkelsen', 'Solberg', 'Sainz', 'Carrera', 'Burns', 'McRae', 'Mouton', 'Rohrl', 'Makinen', 'Gronholm', 'Sato']
cars_dict = {'Citroen':['Xsara', 'C4', 'DS3', 'C3'],
             'Toyota':['Corolla', 'Yaris'],
             'Ford':['Escort', 'Focus', 'Fiesta'],
             'Hyundai':['Accent', 'i20'],
             'Mitsubishi':['Lancer'],
             'Peugeot':['206', '307'],
             'Subaru':['Impreza'],
             'Volkswagen':['Polo', 'Golf GTI']}
coloursList = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'White', 'Black', 'Grey', 'Purple', 'Silver', 'Brown', 'Pink']

drivers = list()
cars = list ()

def DAC_Creator(numberDaC = 9):
    #creates a defined amount of drivers and cars (DAC)
    for i in range(numberDaC):
        lastname_list = random.sample(family_names, 40)
        drivers.append(Driver(random.choice(given_names), lastname_list[i]))
        carMakeSel = random.choice(list(cars_dict))
        carModelSel = random.choice(list(cars_dict[carMakeSel]))
        cars.append(Car(drivers[i], carMakeSel, carModelSel,random.choice(coloursList)))

def timeConvert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    decimalSplit = str(round(float(seconds), 3)).split('.')
    milliseconds = int(decimalSplit[1])
      
    return "%d:%02d:%02d.%02d" % (hour, minutes, seconds, milliseconds)

def timeConvertMinSec(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    decimalSplit = str(round(float(seconds), 3)).split('.')
    milliseconds = int(decimalSplit[1])
      
    return "%d:%02d.%02d" % (minutes, seconds, milliseconds)

def normalisation(input, min, max):
    # (max*OldValue)-((min*OldValue)-min) for 0 to 1
    # (max*(OldValue/100))-((min*(OldValue/100))-min) for 0 to 100
    return ((max*(input/100))-((min*(input/100))-min))


def stageTime(driver, car, track):
    time = 0
    maxV = 254.8
    minV = 304.8

    # For driver skill
    time += normalisation(driver.skill,minV, maxV)

    # For driver's age
    optimum_age = 25
    maxAgeMinus = 45 - optimum_age
    # x = (−max + min)/value, formula to determine incremental
    incremental = (((-1*maxV)+minV)/maxAgeMinus)
    # maxValue + (absolute(age - optimumAge) * (incremental)), formula to determine how much time to add depending of the age of driver.
    time += maxV+(abs(driver.age - optimum_age)*(incremental))

    # For car BHP    
    # NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
    time += (((car.BHP - 300) * (maxV - minV)) / (700 - 300)) + minV

    # For tire condition
    time += normalisation(car.tireCondition,minV, maxV)

    # For grip level
    time += normalisation(track.gripLevel,minV, maxV)

    return [timeConvert(time), time, "{initials} {time}\n".format(initials = driver.threeLettersName, time = timeConvert(time))]



def brakeTrackRecord(drivers_time, mainDriver): #Make it so that it updates if the track record has been broken.
    mainDriverTime = drivers_time
    global trackRecord
    if mainDriverTime < trackRecord:
        print("Congratulations, {name}!!! You broke the stage record by {diff} seconds!!!\nYour time was {new} and the previous record was {old}.\n".format(new = timeConvert(mainDriverTime), old = timeConvert(trackRecord), diff = round(trackRecord - mainDriverTime, 3), name = mainDriver.gname))
        trackRecord = mainDriverTime
    else:
        pass


def animation_seq ():
    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["🚗__________________Π",
                 "__🚗________________Π",
                 "____🚗______________Π",
                 "______🚗____________Π",
                 "________🚗__________Π",
                 "__________🚗________Π",
                 "____________🚗______Π",
                 "______________🚗____Π",
                 "________________🚗__Π",
                 "__________________🚗Π",]

    # animation = ["o=o___________________________",
    #             "___o=o________________________",
    #             "______o=o_____________________",
    #             "_________o=o__________________",
    #             "____________o=o_______________",
    #             "_______________o=o____________",
    #             "__________________o=o_________",
    #             "_____________________o=o______",
    #             "________________________o=o___",
    #             "___________________________o=o",]

    for i in range(len(animation)):
        time.sleep(0.5)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

def check_if_number_input(first_m, error_m):
    user_input_number = input(first_m)
    while not user_input_number.isdigit():
        print(error_m)
        user_input_number = input(first_m)
    return int(user_input_number)

def user_picker(choose_m, options):
    print(choose_m)

    for idx, e in enumerate(options):
        print("{}) {}".format(idx + 1, e))

    i = check_if_number_input("Enter number: ", "This isn't a number! Only numbers are allowed")
    try:
        if 0 < int(i) <= len(options):
            return int(i) - 1
    except:
        pass
    return None

#Race leaderboard
def theRace(mainDriver, track= Track()):
    #Makes the main(user) driver the first item in the drivers list.
    if mainDriver in drivers:
        pass
    else:
        drivers.insert(0, mainDriver)

    #empty presorted drivers and their respective time 2D list.
    pre_sorted_drivers_times = []

    #Goes through the drivers list and populates the pre sorted list with drivers first and then their time in seconds.
    for i in range(len(drivers)):
        pre_sorted_drivers_times.append([drivers[i], stageTime(drivers[i], drivers[i].cars[0], track)[1]])

    #Sorts the pre sorted drivers 2D list by time and stores it in this variable
    drivers_times = sorted(pre_sorted_drivers_times, key=lambda l:l[1])

    #Animation
    animation_seq ()
    
    #the leaderboard formatting string.
    leaderboard = '''
-----------------------------------------------------------
||-------|-------------------|-------------|-------------||
|| POS.  |     NAME          |    TIME     |     DIFF    ||
||-------|-------------------|-------------|-------------||
'''
    #populates the leaderboard with the drivers, their positions, times and difference to first place.
    for n in range(len(drivers_times)):
        
        #calculate difference of time for each driver to first place.
        diffTime = round((drivers_times[0][1] - drivers_times[n][1])*-1,3)

        #Name format for the board
        name_for_board = "{f_initial}. {family}".format(f_initial = drivers_times[n][0].gname[:1].upper(), family = drivers_times[n][0].fname.upper())
        
        #text for first place with '---' in difference. Also with text to identify the main driver.
        if n == 0:
            if drivers_times[n][0] == mainDriver:
                leaderboard += '||  {pos}.	 |  {tln}  | {time} |  {diff} || <--- This is you\n'.format(pos = str(n+1).zfill(2), tln = name_for_board.ljust(15,' '), time = str(timeConvert(drivers_times[n][1])).ljust(11,' '), diff = "------".ljust(10,' '))
            else:
                leaderboard += '||  {pos}.	 |  {tln}  | {time} |  {diff} ||\n'.format(pos = str(n+1).zfill(2), tln = name_for_board.ljust(15,' '), time = str(timeConvert(drivers_times[n][1])).ljust(11,' '), diff = "------".ljust(10,' '))
        
        #if main driver isn't first this adds the text to identify the main driver. Also has change to turn seconds to minutes if necessary.
        elif drivers_times[n][0] == mainDriver:
            if diffTime >= 60:
                leaderboard += '||  {pos}.	 |  {tln}  | {time} |  +{diff} || <--- This is you\n'.format(pos = str(n+1).zfill(2), tln = name_for_board.ljust(15,' '), time = str(timeConvert(drivers_times[n][1])).ljust(11,' '), diff = str(timeConvertMinSec(diffTime)).ljust(9,' ') )
            else:
                leaderboard += '||  {pos}.	 |  {tln}  | {time} |  +{diff} || <--- This is you\n'.format(pos = str(n+1).zfill(2), tln = name_for_board.ljust(15,' '), time = str(timeConvert(drivers_times[n][1])).ljust(11,' '), diff = str(diffTime).ljust(9,' ') )   
        
        #for the rest of the drivers. Also has change to turn seconds to minutes if necessary.
        else:
            if diffTime >= 60:
                leaderboard += '||  {pos}.	 |  {tln}  | {time} |  +{diff} ||\n'.format(pos = str(n+1).zfill(2), tln = name_for_board.ljust(15,' '), time = str(timeConvert(drivers_times[n][1])).ljust(11,' '), diff = str(timeConvertMinSec(diffTime)).ljust(9,' ') )
            else:
                leaderboard += '||  {pos}.	 |  {tln}  | {time} |  +{diff} ||\n'.format(pos = str(n+1).zfill(2), tln = name_for_board.ljust(15,' '), time = str(timeConvert(drivers_times[n][1])).ljust(11,' '), diff = str(diffTime).ljust(9,' ') )
    leaderboard +='||-------|-------------------|-------------|-------------||\n-----------------------------------------------------------\n'
    print(leaderboard)

    # Determines whether the main driver has broken the stage record
    brakeTrackRecord(pre_sorted_drivers_times[0][1], mainDriver)


def inputQuestions(first_m, confirm_m, first_alt_m):
    first = input(first_m)
    confirm = input("To confirm, "+confirm_m+" "+(ANSI.UNDERLINE + ANSI.BOLD + str(first) + ANSI.END)+", correct (y/n)?  ")
    while confirm != 'y' and confirm != 'n':
        print("It looks like you didn't input 'y' or 'n' as the answer. Please do so now:")
        confirm = input("To confirm, "+confirm_m+" "+(ANSI.UNDERLINE + ANSI.BOLD + str(first) + ANSI.END)+", correct (y/n)?  ")

    while confirm == 'n':
        if confirm == 'n':
            first = input(first_alt_m)
            confirm = input("To confirm, "+confirm_m+" "+(ANSI.UNDERLINE + ANSI.BOLD + str(first) + ANSI.END)+", correct (y/n)?  ")
            while confirm != 'y' and confirm != 'n':
                print("It looks like you didn't input 'y' or 'n' as the answer. Please do so now:")
                confirm = input("To confirm, "+confirm_m+" "+(ANSI.UNDERLINE + ANSI.BOLD + str(first) + ANSI.END)+", correct (y/n)?  ")
        else:
            break

    return first



def inputQuestions_mult_choice(options, first_m, confirm_m, first_alt_m):
    first = user_picker(first_m, options)
    confirm = input("To confirm, "+confirm_m+" "+(ANSI.UNDERLINE + ANSI.BOLD + str(options[first]) + ANSI.END)+", correct (y/n)?  ")
    while confirm != 'y' and confirm != 'n':
        print("It looks like you didn't input 'y' or 'n' as the answer. Please do so now:")
        confirm = input("To confirm, "+confirm_m+" \""+(ANSI.UNDERLINE + ANSI.BOLD + str(options[first]) + ANSI.END)+"\", correct (y/n)?  ")

    while confirm == 'n':
        if confirm == 'n':
            first = user_picker(first_alt_m, options)
            confirm = input("To confirm, "+confirm_m+" \""+(ANSI.UNDERLINE + ANSI.BOLD + str(options[first]) + ANSI.END)+"\", correct (y/n)?  ")
            while confirm != 'y' and confirm != 'n':
                print("It looks like you didn't input 'y' or 'n' as the answer. Please do so now:")
                confirm = input("To confirm, "+confirm_m+" \""+(ANSI.UNDERLINE + ANSI.BOLD + str(options[first]) + ANSI.END)+"\", correct (y/n)?  ")
        else:
            break

    return first


#CPU DRIVERS CREATION
DAC_Creator(CPU_numbers)

# #DRIVER'S GIVEN NAME
mainDriver_gname = inputQuestions(
    "Welcome to the Rally of Codecademy! Before we start, we will need to register you:\n\nWhat is your first (given) name? ",
    "your first (given) name is",
    "Enter your correct first (given) name here: "
)

# #DRIVER'S FAMILY NAME
mainDriver_fname = inputQuestions(
    "\nWhat is your last (family) name? ",
    "your last (family) name is",
    "Enter your correct last (family) name here: "
)

# # DRIVER'S AGE

mainDriver_age = check_if_number_input("\nWhat is your age? ", "Please input whole numbers only...")
confirm_age = input("To confirm, your age  is "+(ANSI.UNDERLINE + ANSI.BOLD + str(mainDriver_age) + ANSI.END)+", correct (y/n)?  ")

while confirm_age != 'y' and confirm_age != 'n':
    print("It looks like you didn't input 'y' or 'n' as the answer. Please do so now:")
    confirm_age = input("To confirm, your age  is "+(ANSI.UNDERLINE + ANSI.BOLD + str(mainDriver_age) + ANSI.END)+", correct (y/n)?  ")

while confirm_age == 'n':

    if confirm_age == 'n':
        mainDriver_age = check_if_number_input("\nWhat is your age? ", "Please input whole numbers only...")
        confirm_age = input("To confirm, your age  is "+(ANSI.UNDERLINE + ANSI.BOLD + str(mainDriver_age) + ANSI.END)+", correct (y/n)?  ")

        while confirm_age != 'y' and confirm_age != 'n':
            print("It looks like you didn't input 'y' or 'n' as the answer. Please do so now:")
            confirm_age = input("To confirm, your age  is "+(ANSI.UNDERLINE + ANSI.BOLD + str(mainDriver_age) + ANSI.END)+", correct (y/n)?  ")
    else:
        break

#MAIN DRIVER CREATION
mainDriver = Driver(mainDriver_gname,mainDriver_fname, mainDriver_age)


#CHOOSE CARE MANUFACTURER

#Car manufactures list with their respective available models
car_makes_list = []

#iterate through the keys (makes) in the cars_dict dictionary
for key in cars_dict.keys():
    name_to_append = (str(key).ljust(12, ' ')+"[")
    #if the make only has got 1 model avaible do the following
    if len(cars_dict.get(key)) > 1:
        #iterate through the list except for the last element
        for values in list(cars_dict.get(key))[:-1]:
            name_to_append += (values + " | ") 
        #iterate through last element of each list
        for values in list(cars_dict.get(key))[-1:]:
            name_to_append += (values) 
    else:
        for values in cars_dict.get(key):
            name_to_append += (values)
    name_to_append += "]"
    car_makes_list.append(name_to_append)

user_carMake_choice = inputQuestions_mult_choice(car_makes_list, 
                                                 "\nHey "+mainDriver.gname+" "+mainDriver.fname+", now that you're registered. Please tell us which car you want:\nFirst, choose one of the following car manufacturers:\n", 
                                                 "your car manufacturer choice is", 
                                                 "Choose one of the following car manufacturers:")

mainCar_make = list(cars_dict.keys())[user_carMake_choice]


#CHOOSE CAR MODEL
car_model_list = list(cars_dict.get(mainCar_make))

if len(car_model_list) > 1:
    user_carModel_choice = inputQuestions_mult_choice(car_model_list, 
                                                 "\nChoose one of the following models of your selected car manufacturer:", 
                                                 ("your chosen car model is the "+mainCar_make), 
                                                 "Choose one of the following models of your selected car manufacturer:")
    mainCar_model = list(cars_dict.get(mainCar_make))[user_carModel_choice]
else:
    mainCar_model = list(cars_dict.get(mainCar_make))[0]


# CHOOSE CAR COLOUR
user_carColour_choice = inputQuestions_mult_choice(coloursList, 
                                                 "\nChoose one of the available colours for your car: ", 
                                                 "your chosen car colour is", 
                                                 "Choose one of the following models of your selected car manufacturer:")
mainCar_colour = coloursList[user_carColour_choice]

#MAIN CAR CREATION
mainCar = Car(mainDriver, mainCar_make, mainCar_model, mainCar_colour)

#TRACK CREATION

mainTrack = Track()

print("\nOk, "+mainDriver.gname+", we got it. Your car is a "+mainCar.colour+" "+mainCar.make+" "+mainCar.model+".\n")
# print("\nAfter conducting some studies we assesed your current stats")


#put new tires on Main Driver's car
mainCar.getNewTires()


theRace(mainDriver, mainTrack)

while True:
    race_again = input("Would you like to race again (y/n)?  ")
    while race_again != 'y' and race_again != 'n':
        print("It looks like you didn't input 'y' or 'n' as the answer. Please do so now:")
        race_again = input("Would you like to race again (y/n)?  ")

    if race_again == 'y':
        drivers = list()
        DAC_Creator(CPU_numbers)
        mainDriver.improveSkill(2)
        mainCar.addBHP(2)
        # newTrack = Track()
        theRace(mainDriver, mainTrack)
    else:
        break



'''
FUTURE IDEAS:

"At this time, the best time you can make with your current settings is of X:XX:XX. There are somethings you can change to improve your time. You can change your tires if they're old, improve your driving skills
bla, bla."

NAME
LASTNAME
AGE
SKILL LEVEL
APROX TIME in current track with current skill level

Ask if would like to spend months training before racing. How many months? IF would he rather race?

Show new skill level

ask if want to keep training or would rather race

get main players new tires

Show time with current stats
Ask if would like to spend time training and improving.
Show stats
Ask if satisfied
if yes, move on
if no, go back to asking about training

show drivers

ask if start race

show results and finish


'''