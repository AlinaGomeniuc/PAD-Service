FROM python:3.8-slim
WORKDIR /pad-service
COPY . /pad-service/
RUN pip3 install -r requirements.txt
ENV PYTHONPATH .
CMD ["python3", "/pad-service//controller/user_controller.py"]