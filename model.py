import onnxruntime as ort
import torch


class OnnxModel:
    """To load and run onnx model"""

    def __init__(self, model_path) -> None:
        self.ort_sess = ort.InferenceSession(model_path)
    
    def infer(self, x):
        outputs_ort = self.ort_sess.run(None, {'input': x.numpy()})
        return torch.argmax(torch.tensor(outputs_ort[0])).item()
