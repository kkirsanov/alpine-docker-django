FROM alpine:3.7

ENV TZ 'Europe/Moscow'
COPY ./requirements /opt/app/requirements


RUN apk update && \\
cat /opt/app/requirements/apk.txt | xargs apk add  --no-cache && \\
cat /opt/app/requirements/apk_dev.txt | xargs apk add  --no-cache && \\
python3 -m pip install -r /opt/app/requirements/python-requirements.txt && \\
cp -r -f /usr/share/zoneinfo/$TZ /etc/localtime && \\
echo $TZ >  /etc/timezone && \\
cat /opt/app/requirements/apk_dev.txt | xargs apk del


COPY . /opt/app/
RUN chmod +x /opt/app/docker-entrypoint.sh
WORKDIR /opt/app/

EXPOSE 8000

VOLUME /opt/notificator/db/
VOLUME /opt/notificator/static/


ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]