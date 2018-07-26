FROM ubuntu:16.04

LABEL maintainer="Sara <howtoanalyse.github.io/>"

# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python3 \
        python3-dev \
		python3-pip \
        rsync \
        software-properties-common \
        unzip \
		openjdk-8-jre-headless \
		xvfb \
		libxi6 \
		libgconf-2-4 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip 
RUN ln -s -f /usr/bin/python3 /usr/bin/python
RUN python3 -m pip install pip --upgrade 
RUN python3 -m pip install wheel

WORKDIR /usr/local/bin 
ADD test.py /
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt 

# Versions
ENV CHROME_DRIVER_VERSION 2.40
ENV SELENIUM_STANDALONE_VERSION 3.4.0
ENV SELENIUM_SUBDIR 3.4

# Install Chrome.
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

# Install ChromeDriver.
RUN wget http://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip \
&& unzip chromedriver_linux64.zip \
&& rm chromedriver_linux64.zip
RUN chown root:root /usr/local/bin/chromedriver
RUN chmod 0755 /usr/local/bin/chromedriver

# Install Selenium.
RUN wget http://selenium-release.storage.googleapis.com/${SELENIUM_SUBDIR}/selenium-server-standalone-${SELENIUM_STANDALONE_VERSION}.jar
RUN chown root:root /usr/local/bin/selenium-server-standalone-${SELENIUM_STANDALONE_VERSION}.jar
RUN chmod 0755 /usr/local/bin/selenium-server-standalone-${SELENIUM_STANDALONE_VERSION}.jar

ENV PATH /usr/local/bin:$PATH


CMD ["python3"]