FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"



CMD ["python", "app.py"]