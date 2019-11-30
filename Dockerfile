FROM python:3-onbuild
COPY . /user/src/app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]