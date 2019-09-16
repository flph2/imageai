FROM python:3.6
RUN mkdir -p /opt/imageai/data && \
    apt-get update && \
    apt-get install -y wget 

COPY requirements.txt /opt/imageai/
WORKDIR /opt/imageai
RUN pip install -r requirements.txt 
COPY . /opt/imageai/
RUN chmod +x start.sh 
RUN wget "https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5"
ENTRYPOINT ["./start.sh"]
CMD []
