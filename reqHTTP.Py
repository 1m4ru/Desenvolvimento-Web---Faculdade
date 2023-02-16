from urllib import response
import requests

#requests.get( "https://weather.contrateumdev.com.br/api/weather/city/?city=palhoça=")



#solicitar do usuario qual a cidade que ele quer ver a temperatura, exibir a cidade, exibir a temperatura a minima e a maxima

#city = input("Digite a cidade para qual deseja as informações :")
#temp = ''
#temp_max = ''
#temp_min = ''

#response = requests.get( f"https://weather.contrateumdev.com.br/api/weather/city/?city={city }").json()
   
#print(response['name'], response['main']['temp'], response['main']['temp_max' ], response['main']['temp_min'])


digimon = input("Digite seu digimon: ")

response = requests.get(f"https://digimon-api.vercel.app/api/digimon/name/{digimon}").json()

print(response)
        


    
