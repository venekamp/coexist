This repo is archived and will not see any active development.



This project has yet to start. It will be an attempt to create a web
app that manages groups of people and those people authorize themselves
with an identity they already own, e.g. at their organization or
a social identity.

An administrator or other authorized person will be able to manage a
group of people that are entitled, based on their membership, to have
access services.

The underlying data model has not be designed yet, but this README
serves as a marking point of the start of this endeavour.


# Getting Started
The development and test environment is built using containers. Docker
is used for that. The `scripts` directory contains a number of useful
scripts that aid in building and running containers. 

## Prerequisites
The build script passes on a public SSH key to the container being
built. This is used to get SSH access to the container and that is
necessary for Ansible to work. Before starting the first build, make
sure you have a valid public/private SSH key. You can generate one
as follows:
```
ssh-keygen -t rsa -f id_rsa
```

## Building and Starting Containers
To build a new
coexist container, use the following script:
```
./scripts/build_coexist
```
Once built, use
```
./scripts/start_coexist
```
to start the coexist container.

With a running container, provision as follows:
```
ansible-playbook -i environments/docker/inventory --limit coexist coexist.yml
```
