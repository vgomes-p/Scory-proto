#TO-DO
			#create a var for scory name
			#create a var for user name
			#make the code less ugly
			#translate to Portuguese
#IMPORTS AND LIBRARY
import time

dye = {'null':'\033[m', 'red+_': '\033[1;31m', 'red_':'\033[4;31m', 'red+':'\033[1;4;97;41m', 'green+':'\033[1;32m', 'green':'\033[4;32m', 'yell+':'\033[1;33m', 'yell':'\033[4;33m', 'red0':'\033[97;41m', 'cyan+':'\033[1;36m', 'pink+':'\033[1;35m', 'white+_':'\033[1;4;7;97m', '*':'\033[1m'}

#Valid float
def valid_score_input(prompt):
		while True:
				try:
					return float(input(prompt).replace(',', '.'))
				except ValueError:
						print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} {dye["red+"]}Invalid input. Please enter a numeric value. If your School report the scores as letter, please, use a score converter Letter-Number!{dye["null"]}')


#INTRO
time.sleep(1.5)
print(f'{dye["white+_"]}[You got into the chat]{dye["null"]}\n\n')
time.sleep(1.5)
print(f'''{dye["green+"]}=•=•=•=•=•=•=•=•=•=
WELCOME TO SCORYS
=•=•=•=•=•=•=•=•=•={dye["null"]}''')
time.sleep(4)
print(f'\n\n{dye["white+_"]}[Scory got into the chat]{dye["null"]}')
time.sleep(2.5)

#INTRO2
print(f'\n\n{dye["cyan+"]}| Scorys:{dye["null"]} Hello, my name is Scorys, I am a program developed to analyze your grades and calculate your GPA!')
time.sleep(1.5)
print('Before we start, may I know your name?')
time.sleep(1)
name = input(f'\n{dye["yell+"]}| -:{dye["null"]} ')
time.sleep(2)
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Okay {name}, nice to meet you!')
time.sleep(2)
print('From now on, I will be asking you your grade for each year of your highschool, please, have your school report in hands!')
time.sleep(2.5)
print(f'\n\n{dye["white+_"]}[Scory is opening the system]{dye["null"]}')
time.sleep(1.8)
print(f'\n\n{dye["cyan+"]}| Scorys:{dye["null"]} Okay, I managed to open the system, from now on, just answer the questions with numbers, no need to use n/a, if you have not taken a specific class, just answer (0), okay?')
time.sleep(2)
print('!!! We may start NOW !!!')
time.sleep(3.5)

#9TH GRADE SCORES
print(f'''\n{dye["green+"]}|———————————————|
|9TH GRADE SCORES|
|———————————————|{dye["null"]}''')
print(f'\n\n{dye["cyan+"]}| Scorys:{dye["null"]}Okay, {name}, what was your score for Portuguese?')
port9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Arts?')
arts9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} History?')
his9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Geography?')
geo9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Science?')
sci9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Biology?')
bio9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Chemistry?')
ch9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Physics?')
phy9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Mathematics?')
math9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} English Language?')
eng9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Spanish Language?')
spn9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Sociology?')
socio9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Philosophy?')
phi9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Physical Education?')
pe9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Religious Education?')
re9 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')

gpa9 = (port9 + arts9 + his9 + geo9 + sci9 + bio9 + ch9 + phy9 + math9 + eng9 + spn9 + socio9 + phi9 + pe9 + re9) / 15

#10TH GRADE SCORES
print(f'''\n{dye["green+"]}|—————————————|
|10TH GRADE	SCORES|
|—————————————|{dye["null"]}''')
print(f'\n\n{dye["cyan+"]}| Scorys:{dye["null"]}Okay, {name}, what was your score for Portuguese?')
port0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Arts?')
arts0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} History?')
his0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Geography?')
geo0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Science?')
sci0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Biology?')
bio0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Chemistry?')
ch0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Physics?')
phy0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Mathematics?')
math0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} English Language?')
eng0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Spanish Language?')
spn0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Sociology?')
socio0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Philosophy?')
phi0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Physical Education?')
pe0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Religious Education?')
re0 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')

gpa0 = (port0 + arts0 + his0 + geo0 + sci0 + bio0 + ch0 + phy0 + math0 + eng0 + spn0 + socio0 + phi0 + pe0 + re0) / 15

#11TH GRADE SCORES
print(f'''\n{dye["green+"]}|—————————————|
|11TH GRADE	SCORES|
|—————————————|{dye["null"]}''')
print(f'\n\n{dye["cyan+"]}| Scorys:{dye["null"]}Okay, {name}, what was your score for Portuguese?')
port1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Arts?')
arts1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} History?')
his1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Geography?')
geo1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Science?')
sci1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Biology?')
bio1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Chemistry?')
ch1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Physics?')
phy1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Mathematics?')
math1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} English Language?')
eng1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Spanish Language?')
spn1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Sociology?')
socio1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Philosophy?')
phi1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Physical Education?')
pe1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Religious Education?')
re1 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')

gpa1 = (port1 + arts1 + his1 + geo1 + sci1 + bio1 + ch1 + phy1 + math1 + eng1 + spn1 + socio1 + phi1 + pe1 + re1) / 15

#12TH GRADE SCORES
print(f'''\n{dye["green+"]}
|—————————————|
|12TH	GRADE SCORES|
|—————————————|{dye["null"]}''')
print(f'\n\n{dye["cyan+"]}| Scorys:{dye["null"]}Okay, {name}, what was your score for Portuguese?')
port2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Arts?')
arts2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} History?')
his2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Geography?')
geo2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Science?')
sci2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Biology?')
bio2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Chemistry?')
ch2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Physics?')
phy2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Mathematics?')
math2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} English Language?')
eng2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Spanish Language?')
spn2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Sociology?')
socio2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Philosophy?')
phi2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Physical Education?')
pe2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')
print(f'\n{dye["cyan+"]}| Scorys:{dye["null"]} Religious Education?')
re2 = valid_score_input(f'\n{dye["yell+"]}| {name}:{dye["null"]} ')

gpa2 = (port2 + arts2 + his2 + geo2 + sci2 + bio2 + ch2 + phy2 + math2 + eng2 + spn2 + socio2 + phi2 + pe2 + re2) / 15

#DATA DEFINES
gpa = (gpa9 + gpa0 + gpa1 + gpa2) / 4

subjects = {
	'Portuguese!': port9 + port0 + port1 + port2,
	'Arts!': arts9 + arts0 + arts1 + arts2,
	'History!': his9 + his0 + his1 + his2,
	'Geography!:': geo9 + geo0 + geo1 + geo2,
	'Science!:': sci9 + sci0 + sci1 + sci2,
	'Biology!:': bio9 + bio0 + bio1 + bio2,
	'Chemistry!:': ch9 + ch0 + ch1 + ch2,
	'Physics!:': phy9 + phy0 + phy1 + phy2,
	'Math!:': math9 + math0 + math1 + math2,
	'English!:': eng9 + eng0 + eng1 + eng2,
	'Spanish!:': spn9 + spn0 + spn1 + spn2,
	'Sociology!:': socio9 + socio0 + socio1 + socio2,
	'Philosophy!:': phi9 + phi0 + phi1 + phi2,
	'Physical Education!:': pe9 + pe0 + pe1 + pe2,
	'Religious Education!:': re9 + re0 + re1 + re2
}

sortsub = sorted(subjects.items(), key=lambda x: x[1], reverse=True)

if len(sortsub) >= 3:
		sub1, sub2, sub3 = sortsub[0][0], sortsub[1][0], sortsub[2][0]

#SCORE DATAS PRINT
time.sleep(1.5)
print(f'\n\n{dye["white+_"]}[Scory is calculating your datas]{dye["null"]}\n')
time.sleep(3.5)
print(f'''\n\n{dye["green+"]}=•=•=•=•=•=•=•=•=•=•=
GRADE DATAS
=•=•=•=•=•=•=•=•=•=•={dye["null"]}\n\n''')
time.sleep(1.5)
print(f'''{dye["cyan+"]}| Scorys:{dye["null"]} Okay, {name}, here is your score datas:
{dye["*"]}Your {dye["red+_"]}GPA{dye["null"]} is {gpa}
Your {dye["red+_"]}TOP 1{dye["null"]} subject is {sub1}
Your {dye["red+_"]}TOP 2{dye["null"]} subject is {sub2}
Your {dye["red+_"]}TOP 3{dye["null"]} subject is {sub3}{dye["*"]}

{dye["green+"]}CONGRATS{dye["null"]}, you did amazing on your High School!!''')
exit()