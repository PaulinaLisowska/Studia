def dodawane (a, b):
	wynik = a+b
	return wynik

def get_info():
	print("To jest porsty kalkulator")

get_info()

print ("wprowadz pierwsza liczbe")
z1=int(input())
print ("wprowadz druga liczbe")
z2=int(input())
print(dodawanie(z1, z2))
