import common

delimiter = "####"

system_message = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{delimiter} characters.
Create output as instructed in the query using the \
below information regarding products under each category. \

Allowed products:

Computers and Laptops category:
TechPro Ultrabook
BlueWave Gaming Laptop
PowerLite Convertible
TechPro Desktop
BlueWave Chromebook

Smartphones and Accessories category:
SmartX ProPhone
MobiTech PowerCase
SmartX MiniPhone
MobiTech Wireless Charger
SmartX EarBuds

Televisions and Home Theater Systems category:
CineView 4K TV
SoundMax Home Theater
CineView 8K TV
SoundMax Soundbar
CineView OLED TV

Gaming Consoles and Accessories category:
GameSphere X
ProGamer Controller
GameSphere Y
ProGamer Racing Wheel
GameSphere VR Headset

Audio Equipment category:
AudioPhonic Noise-Canceling Headphones
WaveSound Bluetooth Speaker
AudioPhonic True Wireless Earbuds
WaveSound Soundbar
AudioPhonic Turntable

Cameras and Camcorders category:
FotoSnap DSLR Camera
ActionCam 4K
FotoSnap Mirrorless Camera
ZoomMaster Camcorder
FotoSnap Instant Camera
"""

def get_category_products():
  user_input = f"""
      return me a json object where the keys of each item represent the category \
      and the values of each item is a list of products that are within that category """
  messages = [
    {'role': 'system',
     'content': system_message},
    {'role': 'user',
     'content': f"{delimiter}{user_input}{delimiter}"},
  ]
  category_and_product_response_1 = common.get_completion_from_messages(messages)
  return category_and_product_response_1;

def driver():
  output = get_category_products()
  print(output)

if __name__ == '__main__':
  driver();
