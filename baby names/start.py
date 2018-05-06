'''
Author: Tony Hammack
Date: 6 May 2018
Version 1.0
Contact: hammack.tony@gmail.com

This is script receives user input to find a baby name. 

Thanks to Arul John to compile the baby names. I am using the most popular girls and boys names from 
2016.

You can find that repository at: https://github.com/aruljohn/popular-baby-names
'''

import json,random,string,sys
from time import sleep

class BabyName(object):
	
	def __init__(self):
		'''
		This initializes the class and provides prompts for user inputs for the gender of the child you want
		and the first letter you want the name to start with.
		'''
		while True:
			try:
				#Import names
				self.gender = str(input("Please enter the gender of the name: g for girl and b for boy. ")).strip()
				self.first_letter = str(input("Please enter the first letter of the name you want. ")).strip()
				# Validates input
				if not self.gender.isalpha() and not self.first_letter.isalpha(): # Makes sure input is a letter.
					print('You did not enter the correct format of the input.')
					continue
				elif not len(self.first_letter) == 1: # Makes sure length user entered a single letter.
					print('Please enter a single letter for first letter of name. ')
					continue
				else:
					if self.gender.lower() == "b":
						with open('names/boy_names_2016.json') as json_data:
							data = json.load(json_data)
							self.names = data["names"]
							break					
					elif self.gender.lower() == "g":
						with open('names/girl_names_2016.json') as json_data:
							data = json.load(json_data)
							self.names = data["names"]
							break
					else:
						# Checks to see if user entered the correct gender.
						print('Please enter either g or b for girl of boy.') 
						continue

			except TypeError:
				# Reveals if user entered non-alphabet characters.
				print('You did not enter the correct format of the input.')
				continue
			except FileNotFoundError:
				# Reveals that you do not have the files in the names directory.
				print('You do not have the files of either the girls or boys names.')
				sleep(2)
				sys.exit()
			else:
				break
					
	def choose_names(self):
		'''
		This function uses the random.choice function to pick out random name from either the boys
		or girls list according to the first letter you want.
		'''
		while True:
			self.name = random.choice(self.names)
			if self.name[0].lower() == self.first_letter.lower():
				return self.name.title()
 
if __name__ == '__main__':
	babyname = BabyName()
	name = babyname.choose_names()
	print(name)