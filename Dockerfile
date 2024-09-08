FROM python:3-alpine

ENV port 8343
ENV name "?"
ENV gpio_number "?"



RUN cd /etc
RUN mkdir app
WORKDIR /etc/app
ADD *.py /etc/app/
ADD requirements.txt /etc/app/.
RUN pip install -r requirements.txt

CMD python /etc/app/motionsensor_webthing.py $port $name $gpio_number



