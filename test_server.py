import sys
import base64
import requests
import unittest
from io import BytesIO
from PIL import Image
import banana_dev as banana

api_key = "c6347ad5-dcb8-4fbc-a168-060c40514fc1"
model_key = "232a2d90-ab31-4037-b6b4-e336886e9316"

def pil_to_b64(img):
    im_file = BytesIO()
    img.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
    im_b64 = base64.b64encode(im_bytes).decode()

    return im_b64


class TestDeployment(unittest.TestCase):
  
    def setUp(self):
        self.url = ""


        return self
  
    # Returns True or False. 
    def test_turtle(self):    
        img = Image.open("./n01667114_mud_turtle.JPEG")    
        model_inputs = {'input': pil_to_b64(img)}
        out = banana.run(api_key, model_key, model_inputs)
        self.assertTrue(out['modelOutputs'][0] == 35)

    # Returns True or False. 
    def test_tench(self):    
        img = Image.open("./n01440764_tench.jpeg")      
        model_inputs = {'input': pil_to_b64(img)}
        out = banana.run(api_key, model_key, model_inputs)
        self.assertTrue(out['modelOutputs'][0] == 0)
  
if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 1:
        unittest.main()
    else:
        img = Image.open(sys.argv[1])      
        model_inputs = {'input': pil_to_b64(img)}
        out = banana.run(api_key, model_key, model_inputs)
        print("Class ID:", out['modelOutputs'][0])
