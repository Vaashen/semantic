FROM python

WORKDIR /app

COPY . /app

RUN pip install requirements.txt

CMD python semantic.py
