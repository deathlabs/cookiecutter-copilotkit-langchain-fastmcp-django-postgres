FROM alpine:3.24
LABEL image.authors="{{ cookiecutter.author }}"
SHELL ["/bin/ash", "-o", "pipefail", "-c"]
WORKDIR /home/tools/
COPY {{ cookiecutter.project_slug }}/ {{ cookiecutter.project_slug }}/
COPY {{ cookiecutter.project_slug }}/pyproject.toml pyproject.toml
COPY {{ cookiecutter.project_slug }}/uv.lock uv.lock
ENV UV_PYTHON_INSTALL_DIR=/home/tools/.uv-python
RUN apk add --no-cache python3=3.14.8-r0 uv=0.11.19-r0 && \
    apk upgrade --no-cache libcrypto3 libssl3 &&\
    uv sync --frozen --python /usr/bin/python3 && \
    uv run python -m pip uninstall pip -y || true &&\
    addgroup -g 1000 {{ cookiecutter.project_slug }} &&\
    adduser -D -G {{ cookiecutter.project_slug }} -u 1000 {{ cookiecutter.project_slug }} -h /home/tools/ &&\
    chown -R {{ cookiecutter.project_slug }}:{{ cookiecutter.project_slug }} /home/tools/
ENV PATH="/home/tools/.venv/bin:$PATH"
USER 1000
EXPOSE 8002
CMD [ "uv", "run", "python", "-m", "{{ cookiecutter.project_slug }}.main" ]
