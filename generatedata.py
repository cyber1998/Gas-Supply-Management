from creation import *
from datetime import *

def func():
	aadhar = ['97452385050','344416065656', '368722948831','951229725600','912865950622','410213006308','529391778923','867988209118','442739695357','266810640325']
	user = ['aaravkumar','aarushgupta','aayushmahto','adviksingh','akarshnaskar','arnavpathak','aniruddhgoyal','bhavinmitra','chiragchoudhary','darshitsingh']
	address = ['21/3 Baghi Road','320 Wall Street','13B Lodhar Apartments','21, Skyline Villas','231 MG Road','40 Connaught Palace','2 Park Street','42A/2 Aradhna Apartments','66/4A Cosmos Nest','34 Beagle Street']
	password = ['321@Aarav','322@Aarush','323@Aayush','324@Advik','325@Akarsh','326@Arnav','327@Aniruddh','328@Bhavin','329@Chirag','330@Darshit']
	email = ['aaravkumar@gmail.com','aarushgupta@gmail.com','aayushmahto@gmail.com','adviksingh@gmail.com','akarshnaskar@gmail.com','arnavpathak@gmail.com','aniruddhgoyaal@gmail.com','bhavinmitra@gmail.com','chiragchoudhary@gmail.com','darshitsingh@gmail.com']
	name = ['Aarav Kumar','Aarush Gupta', 'Aayush Mahto','Advik Singh','Akarsh Naskar','Arnav Pathak','Aniruddh Goyal','Bhavin Mitra','Chirag Choudhary','Darshit Singh']
	city = ['New Delhi', 'Kolkata','Mumbai','Ahmedabad','Bangalore','New Delhi','Kolkata','Mumbai','Ahmedabad','Bangalore']
	for i in range(0,10):
		customerMainInsert(aadhar[i], user[i], password[i], email[i], name[i], address[i], city[i])
		userInsert(user[i], password[i], email[i])
		cusdetInsert(aadhar[i], email[i], user[i], password[i], name[i], address[i], city[i])
	return "Done"

func()


