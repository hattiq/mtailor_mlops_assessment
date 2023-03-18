import unittest
from PIL import Image

from model import OnnxModel
from pytorch_model import Classifier, BasicBlock

class OnnxModelTest(unittest.TestCase):
  
    def setUp(self):
        self.torch_model = Classifier(BasicBlock, [2, 2, 2, 2])
        self.onnx_model = OnnxModel("./onnx_model_name.onnx")
  
    # Returns True or False. 
    def test_turtle(self):    
        img = Image.open("./n01667114_mud_turtle.JPEG")    
        x = self.torch_model.preprocess_numpy(img).unsqueeze(0)
        out = self.onnx_model.infer(x)
        self.assertTrue(out == 35)

    # Returns True or False. 
    def test_tench(self):    
        img = Image.open("./n01440764_tench.jpeg")    
        x = self.torch_model.preprocess_numpy(img).unsqueeze(0)
        out = self.onnx_model.infer(x)
        self.assertTrue(out == 0)
  
if __name__ == '__main__':
    unittest.main()
