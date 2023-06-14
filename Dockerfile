FROM python:3.10
EXPOSE 8081
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY model_fashion_mnist ./model_fashion_mnist
COPY app.py ./app.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081"]
