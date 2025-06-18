FROM python:3.12
# EXPOSE 5000 # Exposing is not needed if deploying to a cloud based docker service
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /app
# CMD ["flask", "run", "--host", "0.0.0.0"] # gunicorn offers better performance
CMD [ "gunicorn", "--bind", "0.0.0.0:80", "app:create_app()" ]