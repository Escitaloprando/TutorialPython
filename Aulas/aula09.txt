frase = "Curso em Video Python"
#each charactere, spaces included, is alocated individualy. The adressing star by the number 0.
#|c|u|r|s|o| |e|m| |v|i|d|e|o| |p|y|t|h|o|n|
#|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|
print(frase[4]) #print only the charactere on space 4.
frase.count('o') #Counts how many times the string 'o' repeats
#output: 3
frase.find('android') 
#output: -1 | When the string doesn't exist, the output will be -1
frase.count('o', 0, 13) #Counts the quantity of 'o' strings between the positions 0 and 13(not taking the string on 13th postition in consideration)
frase.find('o') #Give the location of the string 'o'
'curso' in frase #verify the existence of the string 'curso'
#output: true (or false, when it doesn't exist)
#----transformação----#
frase.replace('Python','Android') #Change the 'Python' part for 'Android'
#output: Curso em Video Android
frase.upper() #the charaters will be all uppercase
frase.lower() #the characters will be all lowercase
frase.capitalize() #First charactere will be uppercase and the rest will be lowercase.
frase.title() #same thing as capitalize, but in every word
##
frase = "   Aprenda Python  "
#| | | |A|p|r|e|n|d|a| |P|y|t|h|o|n| | |
#|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|19|20|
frase.strip() #remove unecessary spaces
#output:|A|p|r|e|n|d|a| |P|y|t|h|o|n|
frase.rstrip() #Same thing, but only on the right end
frase.lstrip() #Same thing, but with the left end
##
#|c|u|r|s|o| |e|m| |v|i|d|e|o| |p|y|t|h|o|n|
#|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|
frase.split() #Creates a division where there is a empty space. Creates another listf for each word.
#output: |c|u|r|s|o| |e|m| |v|i|d|e|o| |p|y|t|h|o|n|
#        |0|1|2|3|4| |0|1| |0|1|2|3|4| |0|1|2|3|4|5|
'-'.join(frase) #Unites all the elements with a '-' in between.
#output: |c|u|r|s|o|-|e|m|-|v|i|d|e|o|-|p|y|t|h|o|n|