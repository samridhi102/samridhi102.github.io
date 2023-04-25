# start by pulling the python image
FROM python:2
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app



# configure the container to run in an executed manner
EXPOSE 8080
ENTRYPOINT ["python3.7", "app.py"]
ENTRYPOINT ["gunicorn","--bind=0.0.0.0:8080","app:app"]