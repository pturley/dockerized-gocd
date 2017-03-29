FROM python:2.7

RUN pip install gomatic
ADD . /var/run/gomatic

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /var/run/wait-for-it.sh
RUN chmod +x /var/run/wait-for-it.sh

VOLUME /var/run/gomatic

ENTRYPOINT [ "/var/run/wait-for-it.sh", "go-server:8153", "-t", "0", "-s", "-q", "--" ]
CMD [ "python", "/var/run/gomatic/configure_gocd.py" ]
