FROM python
COPY . /app
WORKDIR /app
RUN sh chrome_install.sh
RUN apt install python-pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app.py