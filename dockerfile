FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    chromium \
    chromium-driver \
     # Add these essential dependencies
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils

# Set environment variable to avoid permission issues
ENV SELENIUM_MANAGER_CACHE_PATH=/tmp/selenium_cache    

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create cache directory with proper permissions
RUN mkdir -p /tmp/selenium_cache && chmod 777 /tmp/selenium_cache

CMD ["pytest", "-v", "--html=report.html"]