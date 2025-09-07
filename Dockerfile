FROM python:3.11

WORKDIR /app

# Copy only requirements first, install dependencies
COPY requirements.txt /app/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


# Now copy the rest of your app
COPY . /app

EXPOSE 8000

ENTRYPOINT [ "bash", "/entrypoint.sh" ]