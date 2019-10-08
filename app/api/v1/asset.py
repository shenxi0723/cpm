from app.libs.redprint import Redprint

api = Redprint('asset')

@api.route('',methods=['GET'])
def get_assets():
	return 'All Assets'