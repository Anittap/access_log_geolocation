import requests

def get_country(ip=None,api_key=None):
    
    if ip and api_key:
        
        ipgeolocation_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}"
        response = requests.get(url=ipgeolocation_url)
        ipgeolocation_dict = response.json()

        if 'country_name' in ipgeolocation_dict:

          return ipgeolocation_dict['country_name']
          
        else:
            return None
        
    else:

        return None
