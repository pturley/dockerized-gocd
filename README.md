# dockerized-gocd

This is an example repository for setting up a dockerized CI server using GoCD.

## Getting Started

* Install [Docker Toolbox](https://www.docker.com/products/docker-toolbox)
* `docker-machine create --driver virtualbox --virtualbox-memory "8096" default` You may specify whatever amount of memory you like, but a CI server with some agents chews up the default of 1GB of memory pretty quickly.
* `eval $(docker-machine env default)`
* `docker-compose up -d`
* `docker-machine ip default`
* Point your browser at http://\<the output of the previous command\>:8153/go/pipelines

## Scaling up the agents

We default you with one agent, but you might like to have more so that builds can run in parallel.

* `docker-compose scale go-agent=2` Replace the 2 for however many agents you would like

## Changing your pipeline configuration

* Make changes in gocd-configurer/configure_gocd.py
* `docker-compose restart go-configurer`

## Cleaning up after you are done

* `docker-compose down`
* `docker-machine kill default`
* `docker-machine rm default`
