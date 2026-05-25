FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg curl unzip git ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Deno to /usr/local/bin (already in PATH)
RUN curl -fsSL https://deno.land/install.sh | DENO_INSTALL=/usr/local sh && \
    ln -sf /usr/local/bin/deno /usr/bin/deno && \
    chmod +x /usr/local/bin/deno

# CRITICAL: Verify both tools are accessible
RUN which deno && deno --version && \
    which ffmpeg && ffmpeg -version | head -1

# Set environment variables explicitly (some apps check these)
ENV DENO_INSTALL="/usr/local"
ENV PATH="/usr/local/bin:/usr/bin:${PATH}"
ENV FFMPEG_PATH="/usr/bin/ffmpeg"

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Make start script executable if it exists
RUN if [ -f start ]; then chmod +x start; fi

CMD ["bash", "start"]

