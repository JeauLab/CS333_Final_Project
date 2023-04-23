# Simple Dockerfile
# Jeau Labyorteaux

# Set Python version
FROM python:3.11

ADD main.py .
ADD task.py .
ADD schedule.py .
ADD test_file.py .

#RUN python -m pip install -r requirements.txt

CMD [ "python", "main.py" ]