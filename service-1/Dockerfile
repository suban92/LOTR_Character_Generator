FROM python:3.6
COPY . .
RUN pip3 install -r requirements.txt
RUN pip3 install requests
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
