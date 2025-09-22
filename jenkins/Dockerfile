FROM jenkins/jenkins:lts-jdk17

USER root

# Install Docker CLI inside the Jenkins container
RUN apt-get update \
 && (apt-get install -y docker.io || apt-get install -y docker-cli) \
 && rm -rf /var/lib/apt/lists/*

# Match the host docker.sock group id so the jenkins user can use the socket
# DOCKER_GID will be passed at build time from the host
ARG DOCKER_GID=0
RUN if ! getent group ${DOCKER_GID} >/dev/null; then groupadd -g ${DOCKER_GID} dockersock; fi \
 && usermod -aG ${DOCKER_GID} jenkins

USER jenkins
