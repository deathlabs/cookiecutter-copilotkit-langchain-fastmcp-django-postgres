FROM alpine:3.23
LABEL image.authors="{{ cookiecutter.author }}"
WORKDIR /home/docs/
COPY mkdocs.yml mkdocs.yml
COPY {{ cookiecutter.project_slug }}/ {{ cookiecutter.project_slug }}/
RUN apk add --no-cache --update mkdocs python3 py3-pip &&\
    adduser -D {{ cookiecutter.project_slug }} -h /home/docs &&\
    chown -R {{ cookiecutter.project_slug }}:{{ cookiecutter.project_slug }} /home/docs
USER {{ cookiecutter.project_slug }}
EXPOSE 5050
CMD [ "mkdocs", "serve", "--dev-addr=0.0.0.0:5050" ]
