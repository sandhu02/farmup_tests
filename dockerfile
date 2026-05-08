FROM markhobson/maven-chrome:latest

# This image already has Chrome, ChromeDriver, Java, Maven
# Add Python for your tests
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install selenium pytest pytest-html

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest", "-v", "--html=report.html"]