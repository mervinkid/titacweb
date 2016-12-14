FROM python:3.5
ADD https://bootstrap.pypa.io/get-pip.py /tmp/get-pip.py
RUN python3 /tmp/get-pip.py > /dev/null
RUN rm /tmp/get-pip.py > /dev/null
COPY ./ /opt/titacweb/
RUN pip3 install -r /opt/titacweb/requirements.txt > /dev/null
RUN /opt/titacweb/manage.py collectstatic
EXPOSE 8000
WORKDIR /opt/titacweb
CMD gunicorn titacweb.wsgi:application --workers 1 --bind 0.0.0.0:8000 --worker-class gaiohttp