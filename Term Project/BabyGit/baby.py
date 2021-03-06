'''
This class will handle:
	1) creation of a BabyGit repo (invoked by alias)
	2) pushing updates to your current repo
	3) pulling the most current updates from repo
	4) cloning a BabyGit repo from the server

@author Ron Rounsifer, Bryce Hutton
@version 10.27.2018 (10.26.2018)
'''
#!/usr/bin/python
from client import *
import sys
import os
import gzip


class Baby(Client):
	def __init__(self, initArgs):
		self.args = initArgs
		self.command = args[0]
		
		
	def parseCommand(self, command):
		if command == "init":
			repo_name = None
			# Assign name to repo if passed
			if len(args) == 2:
				repo_name = args[1]
			self.repoInit(repo_name)
		elif command == "stage":
			self.stage()
		elif command == "commit":
			self.commit()
		elif command == "push":
			pass
		# Initialize the repository
		self.repoInit(repo_name)
		

	#### Method Definitions ####
	def stage(self):
		#todo
		pass

	'''Commit changes to the file.'''
	def commit(self):
		cwd = (os.getcwd())
		#todo: Change the version.
		version = "0"
		directory = cwd + "/"
		'''For each file in the directory that is listed and staged in the git file'''
		for filename in os.listdir(cwd):
			#Todo: If statement a placeholder for checking if the file has been staged
			if 0 == 0:
				fin = open(filename)
				#Todo: Add identifier for the file
				#todo: Maybe a specific identifier for each repo cloned
				#todo: Then an identifier for each version from that repo
				fout = gzip.open(filename + '.' + version + '.bby', 'wb')
				fout.writelines(fin)
				fout.close()
				fin.close()





	def repoInit(name):
		'''Initialize a BabyGit repository
		
		[description]
		
		Arguments:
			directory {[type]} -- the current working directory of the user.
			name {str} -- the name of the repository to be made.
						  Defaults to current directory if not passed.
		'''

		# Now we must get the intialized repositories onto the server.
		# 
		# 2 options:
		#	1) Create files server side and pull to client
		#		- USING THIS MODEL
		#   2) Create files client side and send to server
		#		- if 2+ people make the same repo it could cause problems


		cwd = (os.getcwd())

		directory = cwd + "/"
		
		# Initialize named repo created in the current directory
		if name != None:

			# Absolute path for repo to create
			repo_name = name
			directory = directory + repo_name
			directory_after_init = directory + "/.babygit"
		
			# Setup hidden babygit repo file if it does not exist
			try:
				# Create .babygit directory
				absolute_path = directory + "/.babygit"
				os.makedirs(absolute_path, exist_ok=False)

				# Create HEAD directory
				absolute_path = directory + "/HEAD"
				os.makedirs(absolute_path, exist_ok=False)

			except:
				print("This directory is already initialized." +
					"\nDelete all BabyGit related files and try again.")

		# Initialize the current directory
		else:
			#todo figure out what you want repo_name to be named
			repo_name = "?"
			directory_after_init = directory + "/.babygit"
		
			# Setup hidden babygit repo file if it does not exist
			try:

				# Create .babygit directory
				absolute_path = directory + repo_name + "/.babygit"
				os.makedirs(absolute_path, exist_ok=False)

				# Create HEAD directory
				absolute_path = absolute_path + "/HEAD"
				os.makedirs(absolute_path, exist_ok=True)

			except:
				print("This directory is already initialized." +
					"\nDelete all BabyGit related files and try again.")
		

			# now that the directories have been created, we need to upload them
			# to the server

		
		# Print if success
		success_msg = "Initialized empty BabyGit repository in " + directory_after_init + "/"
		print(success_msg)


#### Script ####

args = sys.argv[1:]
b = Baby(args)
'''
# Initialize a BabyGit repo
if command == "init":
	# Assign name to repo if passed
	if len(args) == 2:
		repo_name = args[1]
	else:
		repo_name = None
	# Initialize the repository
	repoInit(repo_name)
'''

