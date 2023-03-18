import torch
import torch.onnx
from pytorch_model import Classifier, BasicBlock

# A model class instance (class not shown)
model = Classifier(BasicBlock, [2, 2, 2, 2])

# Load the weights from a file (.pth usually)
state_dict = torch.load("./pytorch_model_weights.pth")

# Load the weights now into a model net architecture defined by our class
model.load_state_dict(state_dict)

# Create the right input shape (e.g. for an image)
dummy_input = torch.randn(1, 3, 224, 224)

torch.onnx.export(model, dummy_input, "onnx_model_name.onnx", input_names=['input'])