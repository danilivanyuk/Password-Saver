import sqlite3
import base64

password = '1'
input_password = input('Enter password: \n')

while input_password != password:
	input_password = input('Enter password: \n')
	print('enter correct password: \n')

if input_password == password:
	conn = sqlite3.connect('passwords.db')
	cursor = conn.cursor()

	try:
		cursor.execute("""CREATE TABLE passwords(
			SITE_NAME text, PASSWORD text) """)
		print('Your safety created')
	except:
		print('You have your safety!')

while True:
	print('$' * 15)
	print('Choose what you want to do: \n' + 'q - quit \n' + 's - save new password \n' + 'o - show password')
	print('$' * 15)
	choose_input = input(': ').lower()

	if choose_input == 's':
		site_name = input('Enter site name: \n')
		password_ = input('Enter password: \n')
		password_ = password_.encode("UTF-8")
		password_ = base64.b64encode(password_)

		data = [site_name, password_]
		print(data)
		cursor.execute(("INSERT INTO passwords VALUES (?,?)"), data)
		conn.commit()

	if choose_input == 'o':
		site_name = input('Enter site name: \n')
		cursor.execute("SELECT * FROM passwords WHERE SITE_NAME=" + '"' + site_name + '"')
		p = ""
		print(p)
		for row in cursor:
			p = row[1]
			print(site_name)
			print(base64.b64decode(p))

	if choose_input == 'q':
		break