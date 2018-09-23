FROM python:3.5

LABEL maintainer="Sara <howtoanalyse.github.io/>"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

RUN git clone https://github.com/HowtoAnalyse/tpot.git tpotgit && \
    mv -v tpotgit/tpot ./

COPY . .

CMD ["python", "./tmp.py"]
