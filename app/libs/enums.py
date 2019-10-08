from enum import Enum

class ClientTypeEnum(Enum):
	USER_EMAIL = 100
	USER_MOBILE = 101
	USER_MINA = 200 #微信小程序
	USER_WX = 201
	
class Gender(Enum):
	male = 1
	female = 2