import os
from settings import Settings
import json
from getpass import getpass
from user import User 
from profile import Profile

class Profile:

	def __init__(self):
		self.settings = Settings()
		self.login_attemps = 0
		self.user = None

	def clear_screen(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")


	def load_data(self):
		try:
			with open(self.settings.users_location, 'r') as file:
				self.settings.users = json.load(file)
		except:
			self.settings.users = {}

		try:
			with open(self.settings.profiles_location, 'r') as file:
				self.settings.profiles = json.load(file)
		except:
			self.settings.profiles = {}

	def save_data(self):
		with open(self.settings.profiles_location, 'w') as file:
			json.dump(self.settings.profiles, file)

	def logger(self):
		self.clear_screen()
		while self.login_attemps < 3:
			print("\nPlease Login")
			username = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.settings.users:
				if self.settings.users[username]['password'] == password:
					self.user = User(
								username,
								first=self.settings.users[username]['first'],
								last=self.settings.users[username]['last'],
								password=self.settings.users[username]['password']
						)
					return True
			else:
				print("\nLogin Failed")
			self.login_attemps += 1

		return False

	def show_menu(self):
		self.clear_screen()
		print("SAY THE NAME, SEVENTEEN")
		print("\nHai, welcome back",self.user.first.title(), self.user.last.title())
		print(self.settings.menu)

	def find_member(self, member):
		profiles = self.settings.profiles
		if member in profiles:
				print("\nMember Found!")
				print(f"Real name  : {profiles[member]['first'].title()} {profiles[member]['last'].title()}")
				print(f"Stage Name : {member}")
				print(f"MBTI       : {profiles[member]['MBTI']}")
				print(f"Hobby      : {profiles[member]['Hobby']}")
				return True
		
		print("\nThere is no member found")
		return False

	def check_option_user(self, char):
		if char == "q":
			self.settings.active = False
			print("good bye and have a nice day ><")

		elif char == "1":
			self.clear_screen()
			#print(self.settings.contacts)
			profiles = self.settings.profiles
			print("Stage Name\t\tReal Name\t\tMBTI\t\tHobby")

			for member, profile in profiles.items():
				print(f"{member}\t\t\t{profile['first'].title()} {profile['last'].title()}\t\t{profile['MBTI']}\t\t{profile['Hobby']}")

			input("\nPress ENTER to return")

		elif char == "2":
			self.clear_screen()
			member = input("Input Stage Name : ").upper()
			#profiles = self.settings.profiles

			self.find_member(member)

			input("\nPress ENTER to return")

		elif char == "3":
			self.clear_screen()
			member = input("Stage Name : ").upper()

			if self.find_member(member):
				print("\nEdit\n1. First name 2. Last name 3. MBTI 4. Hobby")
				option = input("Which data do you want to update ? (1/2/3/4) ")
				if option == "1":

					new_first = input("\nChange to : ")
					self.settings.profiles[member]["first"] = new_first
					self.save_data()
					print("New name has been updated")

				elif option == "2":
					
					new_last = input("\nChange to : ")
					self.settings.profiles[member]["last"] = new_last
					self.save_data()
					print("New last name saved")

				elif option == "4":
		
					new_hobby = input("\nHis new hobby is .. ")
					self.settings.profiles[member]["Hobby"] = new_hobby
					self.save_data()
					print("New hobby saved")

				elif option == "3":

					new_MBTI = input("\nUpdate MBTI to .. ")
					self.settings.profiles[member]["MBTI"] = new_MBTI
					self.save_data()
					print("New MBTI saved")

				else: 
					print("There is no member found!")

			input("\nPress ENTER to return")
	
		elif char == "4":
			self.clear_screen()
			
			with open('data.txt', 'r') as file:
				history = file.read()
			print(history)
			input("\nPress ENTER to return")
		
		elif char == "5":
			self.clear_screen()
			#introductions = self.settings.introductions
			print("Name\t\tShort story")

			with open('introductions.json', 'r') as file:
				members = json.load(file)

			for member, story in members.items():
				print(f"{member}\t\t{story}")

			input("\nPress ENTER to return")

	def run(self):
		self.load_data()
		if self.logger():
			self.settings.active = True
	
		while self.settings.active:
			self.show_menu()
			self.check_option_user(input("Option : ").lower())
			
if __name__ == '__main__':
	app = Profile()
	app.run()