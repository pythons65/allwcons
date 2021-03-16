
class Modules:
	def __init__(self,commandObj):
		self.commandsModule = {}
		self.commandObj = commandObj

	def addModule(self, cmdDict, moduleName):
	    self.commandsModule[moduleName] = cmdDict

	def delModule(self, moduleName):

		cmd = self.commandsModule[moduleName]
		for key, item in cmd.items():
			self.commandObj.delete(key)

		print("deleted")


