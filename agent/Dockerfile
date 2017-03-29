FROM gocd/gocd-agent-ubuntu-16.04:v17.3.0
RUN apt-get update
RUN apt-get install -y curl git build-essential libmysqlclient-dev libssl-dev libsqlite3-dev libpq-dev parallel apache2-utils ruby1.9.3
RUN gem install rubygems-update --no-ri --no-rdoc
RUN update_rubygems
RUN gem install bundler --no-ri --no-rdoc

RUN \
  apt-get install -y software-properties-common && \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

ENV GRADLE_VERSION 2.7
ENV GRADLE_SHA cde43b90945b5304c43ee36e58aab4cc6fb3a3d5f9bd9449bb1709a68371cb06

RUN cd /usr/lib \
  && curl -fl https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o gradle-bin.zip \
  && echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c - \
  && unzip "gradle-bin.zip" \
  && ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \
  && rm "gradle-bin.zip"

RUN curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -zx \
  && mv cf /usr/bin
