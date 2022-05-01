# Introduction
Here we will use FastAPI, React and mongoDB as an example project.
The example is taken from https://www.youtube.com/watch?v=OzUzrs8uJl8&t=587s and some own flavour has been added to it. The next parts that will be written here will just act as explanations for some of the concepts.

## MongoDB
In this tutorial, mongoDB atlas is used (mongodb.com/cloud/atlas/signup). We will not necessarily use this. I will simply use a Docker container that will spin up a MongoDB instance, and afterwards we'll use MongoDB Compass to connect to it. 

The Dockerfile for this can be found under the backend folder. 