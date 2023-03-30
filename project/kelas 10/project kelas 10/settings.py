
class Settings:

	def __init__(self):
		self.active = False

		self.profiles_location = "data/profiles.json"
		self.users_location = "data/users.json"

		self.profiles = None
		self.users = None
		self.introductions = None

		self.menu = """
- SEVENTEEN INTRODUCTION -
1. View All Members
2. Find member's biodata by Name 
3. Update information about member
4. Knowing seventeen's history
5. View member's explanation (background)
Q. EXIT

p.s : there is no adding / removing option because seventeen is 13 members not more or less ^^
		"""