FROM python
COPY . /app
WORKDIR /app
RUN sh chrome_install.sh
RUN apt install python3-pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python app.py