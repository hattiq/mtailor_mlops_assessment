from torchvision import transforms
import torch
from model import OnnxModel
from PIL import Image
from io import BytesIO
import base64


def preprocess_numpy(img):
    resize = transforms.Resize((224, 224))   #must same as here
    crop = transforms.CenterCrop((224, 224))
    to_tensor = transforms.ToTensor()
    normalize = transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    img = resize(img)
    img = crop(img)
    img = to_tensor(img)
    img = normalize(img)
    return img

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    
    device = 0 if torch.cuda.is_available() else -1
    model = OnnxModel('./onnx_model_name.onnx')

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model

    # Parse out your arguments
    prompt = model_inputs.get('input', None)
    print(prompt[:100])
    if prompt == None:
        return {'message': "No prompt provided"}
    
    img = Image.open(BytesIO(base64.b64decode(prompt)))
    inp = preprocess_numpy(img).unsqueeze(0)
    res = model.infer(inp)

    # Return the results as a dictionary
    return res
