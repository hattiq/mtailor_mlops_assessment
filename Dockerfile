# Must use a Cuda version 11+
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /

# Install git
RUN apt-get update && apt-get install -y git wget

# Install python packages
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# We add the banana boilerplate here
COPY . .

# Add your model weight files 
RUN wget https://www.dropbox.com/s/b7641ryzmkceoc9/pytorch_model_weights.pth
RUN python3 convert_to_onnx.py

EXPOSE 8000

CMD python3 -u server.py
