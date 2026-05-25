FROM python:3.10-slim

WORKDIR /workspace

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg curl ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    curl -fsSL https://deno.land/install.sh | DENO_INSTALL=/usr/local sh

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x start

CMD ["./start"]
web: ./start
#!/bin/bash
set -e
python bootstrap.py
chmod +x start
git add bootstrap.py start Procfile
git commit -m "Add bootstrap with monkey patch for ensure_dirs"
git push





