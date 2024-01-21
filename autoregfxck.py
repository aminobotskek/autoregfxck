import asyncio
from asyncNewmanga import asyncNewmanga
from async_mail import AsyncClient
from colorama import init, Fore, Back, Style
from nickname_generator import generate
from pyfiglet import figlet_format
async def register_account(password):
	try:
		email_client=AsyncClient()
		new_manga= asyncNewmanga()
		data = await email_client.new_email()
		email=data['email']
		await new_manga.register(email=email,password=password,login=generate("en"))
		print(f"account {email} register")
		accounts= open("manga_accounts.json", "a+")
		json_data={'email':email,'password':password}
		accounts.write(f"{json_data}\n")
		accounts.close()
	except Exception as e:
		print(e)
init()
print(f"{Fore.GREEN} script by Dos-kun \n github:https://github.com/l0v3m0n3y  \n{figlet_format('autoreg fxck',font='rectangles')}")
password=input("password»")
count=int(input("account count»"))
for i in range(count):
	loop = asyncio.get_event_loop()
	loop.run_until_complete(register_account(password))
