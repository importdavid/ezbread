FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN sh chrome_install.sh
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app.py