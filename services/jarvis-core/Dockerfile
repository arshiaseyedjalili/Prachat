FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir .
COPY app ./app
COPY migrations ./migrations
RUN useradd --create-home --uid 10001 jarvis && mkdir -p /data /workspaces /artifacts && chown -R jarvis:jarvis /app /data /workspaces /artifacts
USER 10001
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
