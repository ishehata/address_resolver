FROM python:3.7-alpine

COPY . .

CMD python address_resolver.py 
