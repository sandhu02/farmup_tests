FROM markhobson/maven-chrome:latest

# Install Python and packages with override
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv && \
    pip3 install --break-system-packages selenium pytest pytest-html

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --break-system-packages -r requirements.txt

COPY . .

CMD ["pytest", "-v", "--html=report.html"]