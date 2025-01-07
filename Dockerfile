FROM python:3.13.1-bookworm

RUN set -eux; \
	apt update; \
	apt install -y --no-install-recommends cmake; \
	rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    pip install \
    setuptools \
    pillow \
    face_recognition \
    git+https://github.com/ageitgey/face_recognition_models

COPY __main__.py /app/__main__.py

CMD ["python", "/app/__main__.py"]
