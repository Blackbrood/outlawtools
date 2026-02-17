import requests
import time
from user_agent import *
import os
import webbrowser
webbrowser.open('https://t.me/REDX_64')

user = input('Enter Your Username => ')
paso = input('Enter Your Password => ')
n = input('Enter Your Number 0-9 => ')
target = input('Enter Your target => ')

os.system('clear')

def ss():
	while True:
		cookies = {
		    'ig_did': 'C5000B14-C007-4297-931D-988B622F5426',
		    'datr': 'L0h4aHX-XpN43taBi2bCfZ-B',
		    'ig_nrcb': '1',
		    'mid': 'aHhILwABAAFJkpRVlAEioZBcPfhc',
		    'ps_l': '1',
		    'ps_n': '1',
		    'dpr': '3.0234789848327637',
		    'rur': '"LDC\\05475249816137\\0541788375614:01feb35a606152211bee9c363d2e21a236001cb89f76118ffc0caafa7bdb185887dbff3c"',
		    'csrftoken': 'D234As1ujFaZk2kUeUeNmiu3fSGpkiAO',
		    'wd': '891x715',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    # 'cookie': 'ig_did=C5000B14-C007-4297-931D-988B622F5426; datr=L0h4aHX-XpN43taBi2bCfZ-B; ig_nrcb=1; mid=aHhILwABAAFJkpRVlAEioZBcPfhc; ps_l=1; ps_n=1; dpr=3.0234789848327637; rur="LDC\\05475249816137\\0541788375614:01feb35a606152211bee9c363d2e21a236001cb89f76118ffc0caafa7bdb185887dbff3c"; csrftoken=D234As1ujFaZk2kUeUeNmiu3fSGpkiAO; wd=891x715',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/?flo=true',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-asbd-id': '359341',
		    'x-csrftoken': 'D234As1ujFaZk2kUeUeNmiu3fSGpkiAO',
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': 'hmac.AR1kaBld9laPxP__D6hTaz92el1n0XsoOYAOm7LfvmkcFHUY',
		    'x-instagram-ajax': '1026585083',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': 'ms4k0g:f1u76t:axoe7o',
		}
		
		
		ti = str(time.time()).split(".")[0]
		data = {
		    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ti}:{paso}',
		    'caaF2DebugGroup': '0',
		    'isPrivacyPortalReq': 'false',
		    'loginAttemptSubmissionCount': '0',
		    'optIntoOneTap': 'false',
		    'queryParams': '{"flo":"true"}',
		    'trustedDeviceRecords': '{}',
		    'username': user,
		    'jazoest': '22750',
		}
		
		response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data).text
		
		if 'userid' in response:
			cookies = response.cookies.get_dct()
			ses = cookies['sessionid']
			print(ses)
			cookies = {
					    'ig_did': '14B3CA20-43A7-49DE-A14F-9B805FB50DBB',
					    'csrftoken': 'TdpLp175uY8P7kujPqQtuu',
					    'datr': 'NWFlaC3J3iL-Ki5FInRy3BKm',
					    'mid': 'aGVhYwABAAFFFiKshn6gv7Akg3MC',
					    'ig_nrcb': '1',
					    'ps_l': '1',
					    'ps_n': '1',
					    'dpr': '3.0234789848327637',
					    'wd': '891x1671',
					}
					
			headers = {
					    'authority': 'www.instagram.com',
					    'accept': '*/*',
					    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
					    # 'cookie': 'ig_did=14B3CA20-43A7-49DE-A14F-9B805FB50DBB; csrftoken=TdpLp175uY8P7kujPqQtuu; datr=NWFlaC3J3iL-Ki5FInRy3BKm; mid=aGVhYwABAAFFFiKshn6gv7Akg3MC; ig_nrcb=1; ps_l=1; ps_n=1; dpr=3.0234789848327637; wd=891x1671',
					    'referer': 'https://www.instagram.com/leomessi/',
					    'sec-ch-prefers-color-scheme': 'dark',
					    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
					    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
					    'sec-ch-ua-mobile': '?0',
					    'sec-ch-ua-model': '""',
					    'sec-ch-ua-platform': '"Linux"',
					    'sec-ch-ua-platform-version': '""',
					    'sec-fetch-dest': 'empty',
					    'sec-fetch-mode': 'cors',
					    'sec-fetch-site': 'same-origin',
					    'user-agent': str(generate_user_agent()),
					    'x-asbd-id': '359341',
					    'x-csrftoken': 'TdpLp175uY8P7kujPqQtuu',
					    'x-ig-app-id': '936619743392459',
					    'x-ig-www-claim': '0',
					    'x-requested-with': 'XMLHttpRequest',
					    'x-web-session-id': 'i6xcyp:8ohw5v:8jmp6e',
					}
					
			params = {
					    'username': target,
					}
					
			response = requests.get(
					    'https://www.instagram.com/api/v1/users/web_profile_info/',
					    params=params,
					    cookies=cookies,
					    headers=headers,
			).json()
					
			id = response['data']['user']['id']
			cookies = {
		    'ig_did': 'A46E1B64-3AD2-49AE-91E3-21588A9F5912',
		    'csrftoken': 'LFM6au8yxI9zEMa9i6tDBq',
		    'datr': 'oUi4aJmI0ZOELyBYvOlOjwlw',
		    'ps_l': '1',
		    'ps_n': '1',
		    'dpr': '3.0234789848327637',
		    'mid': 'aLhMGQAEAAFAoByMkfSIYC0BScU5',
		    'wd': '891x1671',
		    'ds_user_id': '75249816137',
		    'sessionid': ses,
		    'rur': '"CLN\\05475249816137\\0541788444768:01fe38fb1c02aa087025a25cd321517c65972fb0c499b89e24672171055cf9c741106b5f"',
		}
		
			headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    # 'cookie': 'ig_did=A46E1B64-3AD2-49AE-91E3-21588A9F5912; csrftoken=LFM6au8yxI9zEMa9i6tDBq; datr=oUi4aJmI0ZOELyBYvOlOjwlw; ps_l=1; ps_n=1; dpr=3.0234789848327637; mid=aLhMGQAEAAFAoByMkfSIYC0BScU5; wd=891x1671; ds_user_id=75249816137; sessionid=75249816137%3AEC0vBOUxuQ9ErL%3A6%3AAYc49dHrhnBnMN6vSyTnXCRjj2LtJ0wqnHehMVwWnw; rur="CLN\\05475249816137\\0541788444768:01fe38fb1c02aa087025a25cd321517c65972fb0c499b89e24672171055cf9c741106b5f"',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/emano_amon/',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-asbd-id': '359341',
		    'x-csrftoken': 'LFM6au8yxI9zEMa9i6tDBq',
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': 'hmac.AR1kaBld9laPxP__D6hTaz92el1n0XsoOYAOm7LfvmkcFBDF',
		    'x-instagram-ajax': '1026642206',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': 'snchvv:2pdx49:2mtj9g',
		}
		
			data = {
		    'container_module': 'profilePage',
		    'entry_point': '1',
		    'location': '2',
		    'object_id': id,
		    'object_type': '5',
		    'context': '{"tags":["ig_report_account"],"ixt_context_from_www":"QVFibFJpRUxnNW44V3ZKT3lRTXJtemdTZzhKZkh3MXRrX21DWGo0NXZzbGRiQVJEUk1WRWExZllRckc1MV9NaFVEMVFpREpaYnZ3TTZZNVEtaHFkbVVvbTV4eVJaaTJMZzIxMUFSdDAtWGpEMVloWnpPYkFyS3ZXYVVMX0d5eHE1bWdoNHVudnNFRGFIa0c4cVl3ZEYwNEdsRU5jaHZrYWZhdGI3cHNXaXdaR0cwZHRTZm9lckFkaXoyakptR0N6bG1MTXVSaFdaRHNLcGpGUG9UOFZzTElCUHMzejV6eHNCREljaXgxajJSTkNtNTNVWjlrT1VLRThUMDREeDltd3pPWS11RHVQX1FaRTJSQTZPREFYbnlucF9hR0VrUFpOT2JfalZpNS03X1RaYnJ1NEdNY2dsNkotVUd5bHpUVi1HdlhPTFNhdVZPYkt3a3dMd1dicHdPeDJ4Q2lLNXhhbi1ub1BPUjJLTnl1M196d2h5dTJ4cHlNUFc5UVlHSDZuZ3JudlRHR3RLN3Nhd1J5RTZMbW9rSDBldUY1VEtPR0J2NmRFTHJTQWRCV09xSWd2TG5lTk9sUF9NY19sbU1uZ0R1TmNFMTBocGtOUVR2NjAyUnRxMWlxSXdQS1lOT3FtVktrX3VIcGhYemFFTkpRS1NTdU0wMnp2NzRfeHAtTmtoWEVIanhVc29CbkstaVp0ejZVMnByTFM2SWJBeGd0RXlsVUhEOVZubURrOFBJbnF1OHNKU1BGRkRlenRNZm0xODQ0TFdZdkRfUm4yT2s5X3pqclVtOG9rekVLV21sOGJVdjJ2VDJvM2tXOE15WjZqUmsxVzVqRnctTWtHWjBkbUU5UnJVUEhXanZJa0JOZEVxd0tkeHg2bkxCajVEdFQ4VV9hTzJqYjJGQms1LVBkSjFSUmRhakc3NjF0eXQzTDZxZGYwbHcwbW1UZFhnbU9xRThwUTFSOXFwNmVmSDQwTGltQnAxaWZUbkowVzU3NXBqd25sak5ZLWRBU3BNYzBLMlAwV1pIWnNQRVFwUEt1WU9sQzFvWEhWVGtTalIxX20zRVVpTmt4bldIRThqVllXME4wal9oVTdnR0h1VEJrM3BZS0tiQ3ZKQ05RNnNzbEFlamEydjB3bWFhLUtiV0ZiOExFTGF2dkw3UWRxZUgtby1fNHk3STdESXpEaXhuRWFTRl9taUZpWFpFdHR2ZEZqZ1hmSUFQemtTaVVGWlR3aDV3aFVFcUJxUjRGVmV0YTZLX2FHcTBfRVVEUXg3UzdSR2pibVVoTmt1ZW4yMG9lMkxpVTFRV2hZVXVrcXdra3NhQkZlbERFMktRUmV0cE5tNEhCeXpEM3hjOTJ4b1YwaVlqa3N3dmVzdENtdVEtS3VpMzUxQUlodUhMODFZelZpdGJ4M0tjZEtEek5rcDhzSlJKdHRXZlQ0b1pwRGxYdjFuQnpyZGpaeFRZUGpQNkVhNWJwRVdsLW9jTFh3SnRDZmMtQXFkaE1RTjhhNG11VEN5WmJnekhFUkdNU19aQkdkc1BmS3kxV01oZnhIWVpRSzFFS2dDcXFmOGVqckRCZ0VfN2w1ZUI0cVkxbUdsR05fOE9kWVRtblRPbnRoczZ1UnNHNGxQcFZqX0ZmRTVsZzBaNFYweFAwOXRhbkVkWEk0SXNYM2RCdTRJQmo2NTJ5T1lwZEJ6ZV91UFJqbDhydFBPd0VMTlh5VEdlSXZsaW43aTYyMm5aYkRKX0ZDcVF5bnlKVU5qa0NyWXVlSEFmeFl4ZkVQSkVjOUhiRnB5NGlfZ3JnclNuQjZ4N094UWdtT1NjNjNhQ3AyRy1FQ21XOUpOaXRVOV9RdGRLS1o2V1kxSUx4aXQwV3dET3BmbzdYajNHRXNIdUdaUFg4cVBQb0xhbHRoTHFJcGhFY1ByUERXVzU4VE5Lc1JWWnBPOW03blhyMFJ6al9wQUo4Y0hndXJhNTdlQ1Z4SnBSUTJya0JCVjFKR2RSQ1VNNjlpb21hTE9uSDBGbU1JamYtcGJNWGFiVEhkWGpBQVZ5NXBQUGg3TUJLR1dVaDJsMVJudnRJSXN6OWZjMy1aS3pfQWItWXJaS3p1Ry1INUhnUTlJejBNdWtpdW9CSkpmUDk1S0JXLURvbDY5TUJGREp1X09BcWhuUjNDUjJqbW9YNDhia05CMl9EczMwZTc0N0pBX082WEdDS2d4dHZ2S3RmSnNNZVJIa29CZGphektQQ25zLWM5UkxZUmltZko5VzNRbmtFR0NzN1ZLR1dSQWdwaXhwMTNaZUNsVkRIWGE3d285STRLUW9oTjVsaHc3TU5DVU1KWXNkcXQ5V05qOHhMQVI3ZWYtRDZXVXhDMlBtZXRocGJzckk3eVJGczQyNnh0aThhQ1lHOFQzdUxsOUowQ0ZrVFJZbWcwVEJMYUVyb3BHUkZQbFNpVUlYQ0hrbXFidU5DVi1LU2xkcXl1VEpJdkx4NlR1Y3o5Z0huOEFmeWlNOVBOWWl4Sy00MFpMT29IeEl0eHJHcjcwX19ocFBjVjNvZDdhX3ZzMmo1OWVqbmFtNU5Ddlp4UC1UNm94SGY2SXFMY1ZGZzVhYzRQbG9qZnBFR3hOQXVQVXp2N0QyamxKOW00aVNibkpQQk8wM2Q5b2pOemx4bmZvX29MYlUwdDUyLUFJU1FuclNHM0lZOGdqR21heVpyaWRMQVdqeEwxS3V5eWhUMThpdG1LZXBMWjFWLXhDNW01dEdjUVhjUVZjNnEwYlY4MlRKeFBya044M3JMbmI5bUNZbWszNjBZdW9aaXI1SHJpUklpZFJBMHJsWFNSbHZZSFdZTWNTT01pMDRzOXVMbzJiS042R0w4ZXNobXh3LUluUmRNSlRPU1NQZ1ZxcG4yTl9mUVBUcW1najgzNk1FNUZFeGx4WTljSWtfeTRmVXNsaW1fWEotTEl1ckM5eVRVTkEtNDl5V0JGbENybWVjOWtUdEVvWFJpajdlYkNNWjEzbVRyRG9DUWppTXlLR3RjZ3lnRktaRmRJWlZON0l5RTJqRV9RSzl6VTNVNENpb0daVXZrQS1TbDRmcURHQjlsdVFsbFNhSWxqbm80WW9BUXg1b2hzMmhRVmRwZkxPWHFuanNjSTN1ejdXSWFVMjRlZC1BRzE5cDdsWUNiY2tLZVhZV080NFh4bVNQSkhrOHNBaVNvdTVMNFFSYk9sOUFvejlXal9EYTJZaFZUYkQ2SnpWSHF6WERtWk5CQy16OUg2TWVOOFRIcHlhWmhjTC1rZXhlcmJIcUFhLXB3V2ozMDZFaVBIVnlXRVZpdG1WQnpHVy04TXd5U1BVMTBOX1hwZDIzd1pTZGc5dU91N1phUDdJbnppUkdqeTctcjcxMDgxRDRrMi1NVzlKOHo1clJZdHMweEo0MU1HaHM4WE9OQjRYWnBVN3lUYno2ejdTY193YVUxM0pQYWE4SGk4NjZJRXlzU19FS0hIbW5JYnU0Q1hoMGt0d2t6VTJwN3VnNzctYS1XVHJXTld3NmVmYVByZ0hoZmRuLVBzbC1qZGk3TzlzMklRb2Y0ZFBVdXd6cHVFaUw3NGk0eTdHQUFkSEI3dnpfWWZoTHJEWEdkd2RScXJYdGp2QWloVndRd2RDMnZMRGRxalI0WEVFeDBEZUs3aUE2eTZqbXdsNjYwUmV1emRmLUU3dkRuSV9VSVUxSGpnRHNlX2x6U3hUdm5Yb1dRcW9oSFdLRXJIdFRmTzZ3bFpySUpncWpkdTBVUVdVVVBsNWlZUmhGMS1Zc0JPcmNxNFExZW9BRnd1X0YwUDM2RWlBdlJDcVZhNWdtRVB0cXJYdjMxc0F4M3ZzMndIb1dXWmtvaVFwZjVPRTZ6NXhUZV9zYWJmNl9PdldzalRhSHdsa2xUS3RQcUE5cjF6cks2RnBVZVZPQjRLNFI2bWVPWGlaQ1BDcFM5aUF1VHh6NVRmNVRJWWNfa0FUbS1OaW1Fejlqcnkxd2NTb3lMUlVaY2xRNVpaWENxdXU4R0xkRDloWUo2d3VYQTZ4bktsZTVJQUs1MDVNSi1yYXRaa3RvZnRoZDhDbkdLbmFnSUVXNWJwb3hXOFNfNjJQMUsweEZNeW5ycVFaTkZBbUJuRzZ6WG1KOUVZdGp2NzF1UEtRTlRJTmU4VlhrNk4tRld1NlBvODFOZDczTlVWMDZKTzJNZkJVWlowSWIyT3YtOGVxSm1vc3c=","frx_context_from_www":"{\\"location\\":\\"ig_profile\\",\\"entry_point\\":\\"chevron_button\\",\\"session_id\\":\\"87849f54-2cdc-4787-afc2-be58399cefb6\\",\\"tags\\":[\\"ig_report_account\\"],\\"object\\":\\"{\\\\\\"user_id\\\\\\":\\\\\\"54542175994\\\\\\"}\\",\\"reporter_id\\":17841475124126227,\\"responsible_id\\":17841454719827771,\\"locale\\":\\"ar_AR\\",\\"app_platform\\":4,\\"extra_data\\":{\\"container_module\\":\\"profilePage\\",\\"app_version\\":\\"None\\",\\"is_dark_mode\\":null,\\"app_id\\":936619743392459,\\"sentry_feature_map\\":\\"JpLJ6NOwBBgNMzcuMjM3LjEzNi4zMxhlTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTM3LjAuMC4wIFNhZmFyaS81MzcuMzYYBWFyX0FSHBggZjdiN2ZlYmYyNzY0YTllNmYwN2ZmMTM4Yjg0Y2ZmNGIYABggMWUwNTA2ZTgxYWYzZjQzZmRiMTM2MGJlYzcwNGQwM2EYJHF1aWMwZDM5ZTFjNTdmYWMwOWVmMzYyOWMzNjFjYmU1ODcyNTggZDUzOTZjNjZhMjM0NDBkOWYxMDQ5MjJhN2U1NGNiODAYJHExM2QwMzExaDNfNTViMzc1YzVkMjJlXzVhMWYzMjNlZjU2ZAA8LBgcYUxoTUdRQUVBQUZBb0J5TWtmU0lZQzBCU2NVNRbQhsr+oWYAHBUIKwGIAm9zA1gxMQAiPDkVABkVADkVAAAYIDhkNjkyZWEzOGUwNzRkOTY5ZjdiYzQ5NzUwNmM5ZDRlFQIREhgPOTM2NjE5NzQzMzkyNDU5HBawq+W1+Z28PxhAMDA1NDRmMDRmZTAxNDUyZDI1MTZmNTk4N2JlOTFiMDM4NjE1ZTMzMGQyMmU5ZmRiNDNjNjExYTliYjIzM2NiMxgYNzUyNDk4MTYxMzc6NjoxNzU2OTA4NjIzABwVBAASKCVodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL2VtYW5vX2Ftb24vGA5YTUxIdHRwUmVxdWVzdAAWpojXsMSusT8oIy9hcGkvdjEvd2ViL3JlcG9ydHMvZ2V0X2ZyeF9wcm9tcHQvFgwWnrHCiw1YATQYBVZBTElEAA==\\",\\"shopping_session_id\\":null,\\"logging_extra\\":null,\\"is_in_holdout\\":null,\\"preloading_enabled\\":null},\\"frx_feedback_submitted\\":false,\\"ufo_key\\":\\"ufo-25040a55-163e-4905-aec3-bca3c8c5abad\\",\\"additional_data\\":{\\"is_ixt_session\\":true,\\"frx_validation_ent\\":\\"IGEntUser\\"},\\"profile_search\\":false,\\"screen_type\\":\\"frx_tag_selection_screen\\",\\"ent_has_music\\":false,\\"evidence_selections\\":[],\\"is_full_screen\\":false}"}',
		    'selected_tag_types': '["ig_its_inappropriate"]',
		    'frx_prompt_request_type': '2',
		    'jazoest': '21862',
		}
		
			response = requests.post(
		    'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',
		    cookies=cookies,
		    headers=headers,
		    data=data,
		).json()
			rep = response['response']["report_tags"][n]["tag_type"]
			cookies = {
		    'ig_did': 'A46E1B64-3AD2-49AE-91E3-21588A9F5912',
		    'csrftoken': 'LFM6au8yxI9zEMa9i6tDBq',
		    'datr': 'oUi4aJmI0ZOELyBYvOlOjwlw',
		    'ps_l': '1',
		    'ps_n': '1',
		    'dpr': '3.0234789848327637',
		    'mid': 'aLhMGQAEAAFAoByMkfSIYC0BScU5',
		    'wd': '891x1671',
		    'ds_user_id': '75249816137',
		    'sessionid': ses,
		    'rur': '"CLN\\05475249816137\\0541788444772:01fe2c9cbf3f77a3335863f9237972a00ad296fac055365aee8042b1577e5d25d0e2b3bb"',
		}
		
			headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    # 'cookie': 'ig_did=A46E1B64-3AD2-49AE-91E3-21588A9F5912; csrftoken=LFM6au8yxI9zEMa9i6tDBq; datr=oUi4aJmI0ZOELyBYvOlOjwlw; ps_l=1; ps_n=1; dpr=3.0234789848327637; mid=aLhMGQAEAAFAoByMkfSIYC0BScU5; wd=891x1671; ds_user_id=75249816137; sessionid=75249816137%3AEC0vBOUxuQ9ErL%3A6%3AAYc49dHrhnBnMN6vSyTnXCRjj2LtJ0wqnHehMVwWnw; rur="CLN\\05475249816137\\0541788444772:01fe2c9cbf3f77a3335863f9237972a00ad296fac055365aee8042b1577e5d25d0e2b3bb"',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/emano_amon/',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-asbd-id': '359341',
		    'x-csrftoken': 'LFM6au8yxI9zEMa9i6tDBq',
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': 'hmac.AR1kaBld9laPxP__D6hTaz92el1n0XsoOYAOm7LfvmkcFBDF',
		    'x-instagram-ajax': '1026642206',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': 'snchvv:2pdx49:2mtj9g',
		}
		
			data = {
		    'container_module': 'profilePage',
		    'entry_point': '1',
		    'location': '2',
		    'object_id': id,
		    'object_type': '5',
		    'context': '{"tags":["ig_report_account","ig_its_inappropriate","suicide_or_self_harm_or_eating_disorder_concern"],"ixt_context_from_www":"QVFhTUR6U1VUdTlobUFPWXRaVnNUcGV1QkZ3QzlvNHNOVVMyaE9oMXplbUhWU3hlZjJfbXdtQ25MNmE3SnJkM1d1aTN4VHNabnU4V09mdGFTd1BEM01fbERzdHhPdVdHdFNFSE92eGJ4bWtSZzRXLXVVWUU0WHNReHcyN2N4VWZOcG5tbC1tT0hyNU9lRHdHckpuV2pMVDd6WVBYeHoxOVhZOVF6Unl2djA2N2pCeloxc1R6bmExS3hVS0JXeWwtQU0xaXZZeGN6UjdjU0dwNUMyQUFZMk9mUEdyZWdhUy1rczliMkYzOVdrSHFEb2wtdnREZTh6OGJ1aGN2M2IxTnNGQ0lPWllHb0s3ai0yLUlxMGVaN3hET1lnVnNkNmtvS00yU0EtTk9uZ01yRGUzeGN4LURsbHk0V0dNQjJOallha21BWlJ0Mmw4QU52ZzBIU1VCRkNPUVZtVV9sSWtGcXFGRmxuaVl2QjRkQ3lvaURBaWN0QXBURUxKY2laUmZsR1dibFRLazdodmRPajQydzRlb0RramNWeVZfLW15M0VHSGhVWWJIZDJmVF9DYW9aYnBkenFROGxOeWVQTWpTaUtqc2p5eFhGeERKVTFkU3dhamotN0VTcl8xSmROWmxjdnBsNmNydEpTeEhrend0YmFZLWNoOEJ5aGJndTlBOVpEajRXTml0b0xMX2FxcWNrU09DUkgtV3V0MThBUzY3clh5MUxTRWsyajdJTXh6ZDZFQVVPbXhpV2N1aFpJaWh1LVJ3aUtFSzVRYUxpTGxPREZ3S0cxZnhoZWpGdE1KZlctR2FOX25iNFo2cXZfbjAxLTY1R1J5c3YzUVB0RzRjYXlmZldjTVl1YmNCTEpRQklrREprMHlXaWR2RUI0cnhLZE01V19tZVhFZE40ZW0zdlpJMVFrYkRTV0xLQ1VFUXBxbEVDeTBJWFQtQVZNS25ic01qTzJCWkx0ZjVoS3BpRG9jM2ZyM0ZYd2FJaFRsVi00MGw2aTFrejFGYThWSVhBLXgtYnlnUG91bllkQmtVRXhDbElWQXllRGFScUVSZi1PZ21RazgzYjNYZi1GMVFpQTVQRk9qT2NwdFZVWDBpTXd6VVRWWGFvemVPajEwY3RGV1pYYktBWTlDZWhHOGlsQmc2VjlfaGxLcjZUYWJFeWh3SGFKZlNyS2hwMU8zaG51N0VmdWZ5SjBZTUlhZDZfd05RM3dka0NKZ1Z4WFJWOTE4NjRmSmR2eVA2U0dMcFNvbEhjTWJqcUF1a1RjNnJ2N1lDcjhoWlZuMTVQSHpseGNCX3JCcnNQQW5SSWhtd25DbTdWcFNYWnRvMVRMdEJJbnhra3RKRUlIU09uajJyVTBXTW5hZ0xONUNhdEhCTFF2UkRZX1JXWGRPSFBFQVNpUk9NZk5mY04yMlFRbDN5WmJLMUF2RzBoQ0lVNFRTVVBNMkdMMkF5OUZ3UzlLZ2NpOUU4eE5UOXAxSkJTMnV5aThPSlhCVlNkT016R3lpb0pqTzEzTXYtTVA4TXVyWDF3Z0FTeXJuSm5CbXlVaTM2bWxlcHdTRG9UMEFQY0FaVkozeHh4Zl92dXR6cUR1Y3d1eDF5amFIdzhsM0h3VG8yUV96Uzc2aGx6N3BianlBQVRlUkpZczlDWEhveE9qU1N2NmczdFlaWC1lOU1tQkZwMHRSQU13amRYQXpZYVBwMVVJR096YUJmSTJUcEVHSUdOVVo4QVBmTmNNalkwVGF6VGZmcG4waUNjQU8xWV9PUTVrclRPN2FGRmlFUTRSN3lnSlQ4d1haeHdwcHRyUmdzMDBSOEJEdWhVdGNnZDZYSlY3aWdOZUxCbFVTVERzMWk5ZF8ydTd3eW5ZUldGVWZSZXliV29VeUk3Yk5HNFlyaWxrdGVxQ0F5TTMtS0dOaVZHTjF6Q19SZnQtd21rYVNzTGVQQU51Tm5MYXVBSnpYcUxVS0FIdmkzYkJjLWNwOHQ5eHF6dm5wZllTdFk2X2kwUFUxcHNDWlBYWVVBaWdTb1pBRXNTVjdNMjNfeW5OaURSUzRkVVNJbHNsYm93eXpLRTVROE5EbGloR3NoUmd5MHVVcUp3ZGJ5QXZrNWQwZEhmb1EtQjQ2QmtfQWszLThQcFBWUGNWQzN1ajVHeTlPbGR1a2VDY2RJcFFnSk5rYWRLdmpyZmhKTDk0WE90eXN2OXFnR1RLay1CSFdmUzJGb09PS3lrUy1Wcl95ZWdZWkhKdXlodlN3dTUzYVdLNlFuaEdlZjZxYkZReXpKVHlsTFFyRG5JSDR4WHJvd3c2aWdOTXR5Ymc4cW10UW4tY3Nka2N6SXZYd3I2NUZrT2Jnd0R4cmRNN25DUlhFOExpRnFicURmTEV4YlpUV05zWDB6QWsxaXd1c2J5NVptM2xZd2R0cW5PMFZOWmhodUFpUmljejJKNTh2MjhGVEZpbkZKVF9EUTBoTkFUZEV3dFNGRTBBbjVPcXRXUFJyVHNuRDhGSkNJb0h2Q3B5NlFpelNOcmtGOUZEemVTZDgteFFMa0JzZjlfQWpsQWRXbnhYdGhLdUlqX1EtSWpIRm45YjVfRjJ6bThiNXllVHI3RUMxVWZ4dm5PeXFSY3RYS1lwdzlZYVRMNnNUcGE1a3hnMjlaYW5kY2RzcDhLNGRBWWpKUktuSlR1UnQ4WEdGMmcyU0d4RHFXMEdqRzNyQXVuaFduVjgxWXp6MFBpdTFHQW1wMllhbUxvbFdUSzF6azVyclpjUVZ4dlRnRnBmMFZqWGZUR0lvbmJyMVdkNThVWlptclBQUEE3akRmTGQ5cmtpM01FUjkwalNOZmJMazB3VHFqVHpsZVlkRFlMbWRwaHZ5WkhUOVIzNGFNa19IRlhJZ0c3a2EtVUhYX2tGX1AyTGlhTXhlYXpNVjNYNl9Ub0FWVFVwdk9sdndxdm9xRW5DUFJaWURzUGxvRXB2cTZPclNkcFJHMWlLRHQ4R0F5ZW15SkQ1NXFjdDdpcUFpVmtsdG51NUgyQXlLWjBWTFlFUUxEc05sTlRmQlhPZExJekV6TXI0UllaWG9iSE5odW5udC1zUTZzNW5BeUd4Rl85dVFTYTFsLS1hQlAyWW1JUjFhUVBDN3pUMzR1SFVWQ1ZMZno4RE5idGFsZnRJVG1YUERqZmFjOXFwYkJtZ1c0MUJadTh6eHlGblM2VTlWRzdmcVZlakNvQm1zNjhPTHFPejB2dnZUZUZtd2FiYnlNb2lIWGJXVGdiVHhZOWd0ZGFtQ2QtbWVwV0x4SnBSZ0dzdFp4VUFFbHRLRk5xN3RPb2RBZ1VxU3hfVXUzNllnWjg0bmVpZmxqUkhoZlFnYk5rbHBBMks2UGVxYWZZVVpCRVIxN2hLSDA5ZHRwZGtDVm5la1RDVnM0bmdLU2NlamJMenphT1BGdmV5NXI3R3Z3bDJWQmxQaHBUUDU5bzR3Vm5qczdUSGNtbjZJc0N2UldDeUNUZjdURDEyTno4NzB2RGwyQmFQRUU5TzktNmpubERuTHVfS0RSLXpXQTBvck05SzVLWFFQc1pwb2Y4YWlPNTQ4SnlYcmp4MGIzMklrTF9JVGhBQ1hnOVVFZ2JVbDhocUgyUnNmQzUzUEZ2UUtObUh2NkZ6QkhIODJBWjBPWEU5MzdKT1BLNEZYRzJsS1FwNk8yd3BmQTNPa0tfWnlXRVppR3ZETklGV1lKTGdJd0tua1cyTXI4MFduUDI4VTZxNV83TzlJMl81NlpjOFpGRnNNV3l0WTRGVVNmU25vYWwwNEhlMGRSRVhoa0dScVhGT3Ywcjl1UktwbGdudThBQmMwX1pTUUdyMDVxUzFmZHd0NVd3ZGlUQ2dtZmJERmQ5OFZMb2RCTWhkTFljR2tYTElQYkpybnVLTnlHNjlPSzUwekU3Tnl5QjJkaEVuSTB4UnBUek1DNm92S1cxcmw4UDA5TUhpWjhvYTlTcU5tZVRIQ1prSlMtUERUQWUxV0o5blNyd0czSURwSVJ1aDRnblI3QXY2eEZGa0h0OEVmUk9qd0xYeWRCbEhjM1BDYVBxcXhOTEJhbk1OM0JlVWdWTVZsaFAtbzYwLWJSdldoejRsTW1ZMThDZEtUWTFXNmJNV1hISGN6SVo4c0NFVWkzMjFyOXdVRjdCVHI5NnEwc0xpWTloOEtmNWhoM05kOUlQN3ZiWXJmaVZYNkFfUnNKWUpabXg4ZFJQZFFnbXRXbGlYeGhaTlR3R2w0cEtFbnpHTVprOVZIZUt3NklqZlVQMlNYT2VhdTR0c1dySXozQ0xSNG0xTzFNQzltdzU3TDhzelltaDQ3a0EzNUVXY0VSTXc3TjFKUDVwVmhhVkl5Rlc=","frx_context_from_www":"{\\"location\\":\\"ig_profile\\",\\"entry_point\\":\\"chevron_button\\",\\"session_id\\":\\"87849f54-2cdc-4787-afc2-be58399cefb6\\",\\"tags\\":[\\"ig_report_account\\",\\"ig_its_inappropriate\\",\\"suicide_or_self_harm_or_eating_disorder_concern\\"],\\"object\\":\\"{\\\\\\"user_id\\\\\\":\\\\\\"54542175994\\\\\\"}\\",\\"reporter_id\\":17841475124126227,\\"responsible_id\\":17841454719827771,\\"locale\\":\\"ar_AR\\",\\"app_platform\\":4,\\"extra_data\\":{\\"container_module\\":\\"profilePage\\",\\"app_version\\":\\"None\\",\\"is_dark_mode\\":null,\\"app_id\\":936619743392459,\\"sentry_feature_map\\":\\"JpLJ6NOwBBgNMzcuMjM3LjEzNi4zMxhlTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTM3LjAuMC4wIFNhZmFyaS81MzcuMzYYBWFyX0FSHBggZjdiN2ZlYmYyNzY0YTllNmYwN2ZmMTM4Yjg0Y2ZmNGIYABggMWUwNTA2ZTgxYWYzZjQzZmRiMTM2MGJlYzcwNGQwM2EYJHF1aWMwZDM5ZTFjNTdmYWMwOWVmMzYyOWMzNjFjYmU1ODcyNTggZDUzOTZjNjZhMjM0NDBkOWYxMDQ5MjJhN2U1NGNiODAYJHExM2QwMzExaDNfNTViMzc1YzVkMjJlXzVhMWYzMjNlZjU2ZAA8LBgcYUxoTUdRQUVBQUZBb0J5TWtmU0lZQzBCU2NVNRbQhsr+oWYAHBUIKwGIAm9zA1gxMQAiPDkVABkVADkVAAAYIDhkNjkyZWEzOGUwNzRkOTY5ZjdiYzQ5NzUwNmM5ZDRlFQIREhgPOTM2NjE5NzQzMzkyNDU5HBawq+W1+Z28PxhAMDA1NDRmMDRmZTAxNDUyZDI1MTZmNTk4N2JlOTFiMDM4NjE1ZTMzMGQyMmU5ZmRiNDNjNjExYTliYjIzM2NiMxgYNzUyNDk4MTYxMzc6NjoxNzU2OTA4NjIzABwVBAASKCVodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL2VtYW5vX2Ftb24vGA5YTUxIdHRwUmVxdWVzdAAWpojXsMSusT8oIy9hcGkvdjEvd2ViL3JlcG9ydHMvZ2V0X2ZyeF9wcm9tcHQvFgwWnrHCiw1YATQYBVZBTElEAA==\\",\\"shopping_session_id\\":null,\\"logging_extra\\":null,\\"is_in_holdout\\":null,\\"preloading_enabled\\":null},\\"frx_feedback_submitted\\":false,\\"ufo_key\\":\\"ufo-25040a55-163e-4905-aec3-bca3c8c5abad\\",\\"additional_data\\":{\\"is_ixt_session\\":true,\\"frx_validation_ent\\":\\"IGEntUser\\"},\\"profile_search\\":false,\\"screen_type\\":\\"frx_tag_selection_screen\\",\\"ent_has_music\\":false,\\"evidence_selections\\":[],\\"is_full_screen\\":false}"}',
		    'selected_tag_types': f'["{rep}"]',
		    'frx_prompt_request_type': '2',
		    'jazoest': '21862',
		}
		
			response = requests.post(
		    'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',
		    cookies=cookies,
		    headers=headers,
		    data=data,
			).text
			if '"text":"It was completed"' in response:
				print(f'report Done : {target}')
			else:
				print(f'Error report : {target}')
				
		
		
		elif '"user":true' in response and '"authenticated":true' in response:
			print(f'GOOD Login: {user} : {paso}')
			
		elif '"user":true' in response and '"authenticated":false' in response:
			print(f'The password is wrong. : {user} : {paso}')
			
		elif '"user":false' in response and '"authenticated":true' in response:
			print(f'Wrong Eliezer : {user} : {paso}')
			
		else:
			print(f'Verify login means go back to the account and click I tried to log in: {user} : {paso}')
		exit()
		
ss()		
	
