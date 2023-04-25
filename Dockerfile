# start by pulling the python image
FROM gcr.io/cloud-builders/docker@sha256:08c5443ff4f8ba85c2114576bb9167c4de0bf658818aea536d3456e8d0e134cd

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