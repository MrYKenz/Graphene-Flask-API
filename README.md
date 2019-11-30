# Graphene Flask GraphQL API

A simple GraphQL API using Flask and Flask Graqhql to create an API route for the server and Graphene to create Python based Schema. The tests.py file uses Graphene's schema to run queries and print JSON examples of the results, alternatively, Flask Graphql provides a graphiql playground to run queries against the enpoint. Dependencies /python modules/libraries can be found in requirements.txt and installed with pip. 
```bash
pip install -r requirements.txt
```
However, I have used a docker container for this project that can be used if building a microservice in a microservice architecture and the Dockerfile will run this command. 