import json, os

tokenConfigPath = "storage/tokens.json"

class Config():
	def __init__(self, configPath: str=""):
		self.configPath = configPath

	def get_json_object(self):
		with open(self.configPath, "r") as jsonFile:
			jsonData = json.load(jsonFile)
		return jsonData

	def get_json_value_double(self, jsonObject: object, key: str, secondKey: str):
		return jsonObject[key][secondKey]

	def add_json_section(self, jsonObject: object, key: str):
		with open(self.configPath, "w") as jsonFile:
			jsonObject[key] = {
				"token": "",
				"prefix": ""
			}
			json.dump(jsonObject, jsonFile, indent=4)
		return

	def remove_json_section(self, jsonObject: object, key: str):
		with open(self.configPath, "w") as jsonFile:
			del jsonObject[key]["token"]
			del jsonObject[key]["prefix"]
			del jsonObject[key]
			json.dump(jsonObject, jsonFile, indent=4)
		return

	def edit_json_value_double(self, jsonObject: object, key: str, secondKey: str, value):
		with open(self.configPath, "w") as jsonFile:
			jsonObject[key][secondKey]=value
			json.dump(jsonObject, jsonFile, indent=4)
		return