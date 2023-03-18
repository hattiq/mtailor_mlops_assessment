**Deploy Classification Neural Network on Serverless GPU platform of Banana Dev**

### Dependencies
Assuming pytorch is already installed.
```bash
pip install -r requirements.txt
pip install banana-dev
```
Download the model from [dropbox](https://www.dropbox.com/s/b7641ryzmkceoc9/pytorch_model_weights.pth?dl=0) and place it in the repo directory.

### Converting model to ONNX
```bash
python convert_to_onnx.py
```

## Testing ONNX model
```bash
python test_onnx.py
```

## Testing banana.dev deployment
```bash
python test_server.py
```

