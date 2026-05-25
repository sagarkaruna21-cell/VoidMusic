FROM nandyalu/python-ffmpeg:latest

WORKDIR /workspace

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "anony"]
