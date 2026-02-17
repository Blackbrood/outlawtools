from os import system,name
from json import loads,dumps
from time import sleep,time
from hashlib import md5
from io import BytesIO
try:
	from requests import Session
	from requests.utils import quote
except:
	system('pip install requests')
	from requests import Session
	from requests.utils import quote
try:
	from PIL import Image
except:
	system('pip install Pillow')
	from PIL import Image

class edit:
	def __init__(self, sessionid: str,username: str) -> str:
		self.username = username
		self.cookies = {"sessionid": str(sessionid)}
		self.r = Session()
	
	def inforamtions(self):
		try:
			r = self.r.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}', headers={'x-ig-app-id': '936619743392459'}, data={'username': self.username}).json()['data']['user']
			return r['biography'],r['full_name'],r['profile_pic_url'],r['pronouns'],r['external_url']
		except:
			system('cls' if name == "nt" else "clear")
			report(sessionid=self.cookies['sessionid'],username=input('- Enter Username Targrt : ')).reportW()
	def csrfToken(self):
	      return self.r.get("https://i.instagram.com/api/v1/accounts/login/", headers={"User-Agent": "Instagram 64.0.0.11.97 Android (21/5.0.2; 240dpi; 540x886; LGE/lge; LG-D618; g2mds; g2mds; pt_BR)","Content-Type": "application/x-www-form-urlencoded"}).cookies["csrftoken"]
	      
       	
	def getMe(self):
		re = self.r.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers={'User-Agent': 'Instagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935; hero2lte; samsungexynos8890; en_US; 208061712)', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'x-ig-app-id': '936619743392459'}, cookies=self.cookies,timeout=6).text
		if 'message' in re: exit('- error sessionid')
		re = loads(re)
		return re['user']['email'],re['user']['phone_number'],re['user']['username'],re['user']['full_name']
			
	def editAccount(self,name=None):
		response = self.inforamtions()
		response1 = self.getMe()
		if name == False: name = response1[3]
		else: name = response[1]
		csrf = self.csrfToken()
		image = Image.open(BytesIO(self.r.get(response[2]).content))
		image.save(self.username+".jpg")
		ok = self.r.post("https://www.instagram.com/api/v1/web/accounts/edit/",headers={"X-Csrftoken": csrf,"X-Ig-App-Id": "936619743392459"},data={"biography": response[0],"chaining_enabled": "on","email": response1[0],"external_url": response[4],"first_name": name,"phone_number": response1[1],"username": response1[2]},cookies=self.cookies).text
		if '14 days.' in ok:
			print('- The Name has not been UpDated')
			edit(sessionid=self.cookies['sessionid'],username=self.username).editAccount(name=False)
		else: pass
		if '{"status":"ok"}' not in ok: print(ok)	
		response = self.r.post('https://www.instagram.com/api/v1/web/accounts/web_change_profile_picture/', headers={'X-Csrftoken': csrf,'X-Ig-App-Id': '936619743392459'}, files={'profile_pic': open(self.username+'.jpg', 'rb')},cookies=self.cookies,data={"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg","Content-Type": "image/jpeg"}).text
		if '"has_profile_pic":true' not in response: print('- The Avatar has not been UpDated')
		print('- The Account has been UpDated ✓')
		
		 
class report:
	def __init__(self,username: str,sessionid: str) -> str:
		self.username = username
		self.url = "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/"
		self.cookies = {'sessionid': sessionid}
		self.headers={"X-Ig-App-Id": "936619743392459",}
		self.s = Session()
	
	def getCsrf(self):
		return self.s.get("https://i.instagram.com/api/v1/accounts/login/", headers={"User-Agent": "Instagram 64.0.0.11.97 Android (21/5.0.2; 240dpi; 540x886; LGE/lge; LG-D618; g2mds; g2mds; pt_BR)"}).cookies["csrftoken"]
	
	def getID(self,username):
		return self.s.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers={'x-ig-app-id': '936619743392459'}, data={'username': username}).json()['data']['user']['id']

	def getContext(self):
		self.headers['X-Csrftoken'] = self.getCsrf()
		id = self.getID(self.username)
		return self.s.post(self.url, headers=self.headers,data = {"container_module": "profilePage","entry_point": 1,"location": 2,"object_id": id,"object_type": 5,"frx_prompt_request_type": 1},cookies=self.cookies).json()['response']['context'],self.headers['X-Csrftoken']
	
	def reportW(self):
		context , csrf = self.getContext()
		self.headers['X-Csrftoken'] = csrf
		count = 0
		system('cls' if name == "nt" else "clear")
		while True:
			response = self.s.post(self.url,data={"container_module": "profilePage","entry_point": 1,"location": 2,"context": context,"object_id": 5913002828228283,"object_type":5,"selected_tag_types": '["ig_user_impersonation_me"]',"action_type": 2,"frx_prompt_request_type": 2},headers=self.headers,cookies=self.cookies).json()['status']
			if response != "ok": print('- False Report | Report Count : '+str(count))
			else:
				count +=1
				print('- True Report | Report Count : '+str(count))

class Login:
    def __init__(self, username=None, password=None, sessionid=None):
        self.password = password
        self.username = username
        self.sessionid = sessionid
        self.url = "https://i.instagram.com/api/v1/accounts/login/"
        self.headers = {"User-Agent": "Instagram 64.0.0.11.97 Android (21/5.0.2; 240dpi; 540x886; LGE/lge; LG-D618; g2mds; g2mds; pt_BR)","Content-Type": "application/x-www-form-urlencoded"}
        self.r = Session()

    def csrfToken(self):
        return self.r.get(self.url, headers=self.headers).cookies["csrftoken"]

    def sessionID(self):
        response = self.r.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers={'User-Agent': 'Instagram 100.0.0.17.129 Android (28/9; 320dpi; 720x1422; HUAWEI; MRD-LX1F; HWMRD-M1; mt6761; ar_EG; 16147866)','Cookie': f'csrftoken={md5(str(time()).encode()).hexdigest()}; sessionid={self.sessionid};'})
        if response.json()['status'] != "ok":
        	system('cls' if name == "nt" else "clear")
        	Login(sessionid=input('- Bad SessionID\n- Enter SessionID : '),username=None,password=None).sessionID()
        return True

    def account(self):
        csrf = self.csrfToken()
        fi = self.r.post(self.url, headers=self.headers,data=f'signed_body=fd5f359e5560870ec4cdc326850186a0ebc0033465fdd7477d727e6bae6d575e.{quote(dumps({"_csrftoken": csrf, "adid": "bbe5bcdb-b1e3-4815-9e3b-9265c0740970", "country_codes": [{"country_code": "964", "source": ["default"]}], "device_id": "android-", "google_tokens": "[]", "guid": "064020d6-330c-471d-a7b2-fc1774dc7122", "login_attempt_count": 0, "password": self.password, "phone_id": "824595cb-7bf9-4b40-8075-685df82e23cc", "username": self.username}))}&ig_sig_key_version=4')
        if 'sessionid' in fi.cookies.get_dict().keys():
            return fi.cookies['sessionid']
        else:
            print(fi.json()['message'])
            sleep(3)
            system('cls' if name == "nt" else "clear")
            Login(username=input('- Enter Username : '), password=input('- Enter Password : ')).account()

def runCode():
    print('1 - Login From SessionID\n2 - Login From Account')
    choice= input('- ? ')
    system('cls' if name == "nt" else "clear")  
    if choice == '2':
        client = Login(username=input('- Enter Username : '), password=input('- Enter Password : '),sessionid=None).account()
    elif choice ==  '1':
        client = input('- Enter SessionID : ')
        clientZ = Login(sessionid=client, username=None, password=None).sessionID()
    else: system('cls' if name == "nt" else "clear") ; runCode()
    print('\n- Done Login : '+str(client)) ; sleep(2)
    if 1==1:
        system('cls' if name == "nt" else "clear")
        username = input('- Enter Username Targrt : ')
        edit(username=username,sessionid=client).editAccount()
        report(sessionid=client,username=username).reportW()

if __name__ == "__main__":
	runCode()