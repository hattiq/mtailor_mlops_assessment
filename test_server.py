
import base64
import requests
import unittest
from io import BytesIO
from PIL import Image

def pil_to_b64(img):
    im_file = BytesIO()
    img.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
    im_b64 = base64.b64encode(im_bytes)

    return im_b64

class TestDeployment(unittest.TestCase):
  
    def setUp(self):
        self.url = ""
  
    # Returns True or False. 
    def test_turtle(self):    
        img = Image.open("./n01667114_mud_turtle.JPEG")    
        model_inputs = {'input': pil_to_b64(img)}

        res = requests.post(self.url, json = model_inputs)

        self.assertTrue(res.json() == 35)

    # Returns True or False. 
    def test_tench(self):    
        img = Image.open("./n01440764_tench.jpeg")      
        model_inputs = {'input': pil_to_b64(img)}

        res = requests.post(self.url, json = model_inputs)

        self.assertTrue(res.json() == 0)
  
if __name__ == '__main__':
    unittest.main()
