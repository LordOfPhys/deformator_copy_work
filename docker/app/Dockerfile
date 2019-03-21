FROM python:2.7.12
ENV PYTHONUNBUFFERED 1

# Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Configure
COPY ./docker/app/uwsgi.ini /etc/uwsgi.ini
WORKDIR /app
EXPOSE 80

# Copy shell scripts
COPY ./docker/app/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh && \
    chmod +x /entrypoint.sh

COPY ./docker/app/start-uwsgi.sh /start-uwsgi.sh
RUN sed -i 's/\r//' /start-uwsgi.sh && \
    chmod +x /start-uwsgi.sh

ENTRYPOINT ["/entrypoint.sh"]
