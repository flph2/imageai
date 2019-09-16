FROM python:3.6
RUN mkdir -p /opt/imageai/data
COPY requirements.txt /opt/imageai/
WORKDIR /opt/imageai
RUN pip install -v  -r requirements.txt 
COPY . /opt/imageai/
RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]
CMD []
