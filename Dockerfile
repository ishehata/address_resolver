FROM python:3.7-alpine

COPY . .

CMD python -m unittest -vv address_test.py
