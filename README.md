# Graphene Flask GraphQL API

A simple GraphQL API using Flask and Flask Graqhql to create an API route for the server and Graphene to create Python based Schema. The tests.py file uses Graphene's schema to run queries and print JSON examples of the results, alternatively, Flask Graphql provides a graphiql playground to run queries against the enpoint. Dependencies /python modules/libraries can be found in requirements.txt and installed with pip. 
```bash
pip install -r requirements.txt
```
However, I have used a docker container for this project that can be used if building a microservice in a microservice architecture and the Dockerfile will run this command.

## Example Queries:

Create User
```graphql
mutation {
  createUser(username:"kenzy"){
    user{
      username
    }
  }
}
```
Create Post
```graphql
mutation {
  createPost(username:"kenzy", title:"Post 1", body:"Testing..."){
    post{
      title
      body
      author{
        username
      }
    }
  }
}
```
Fetch Users and Posts
```graphql
{
  allUsers {
    edges {
      node {
        username
        posts {
          edges {
            node {
              id
              body
            }
          }
        }
      }
    }
  }
}
```
Fetch Posts
```graphql
{
  allPosts{
    edges{
      node{
        title
        body
        author{
          username
        }
      }
    }
  }
}
```
### With Variables:

Create User
```graphql
mutation userCreate($usernameVar: String!){
  createUser(username: $usernameVar){
    user{
      username
    }
  }
}
```
Create Post
```graphql
mutation postCreate($usernameVar: String!, $titleVar: String!, $bodyVar: String!){
  createPost(username: $usernameVar, title: $titleVar, body: $bodyVar){
    post{
      title
      body
      author{
        username
      }
    }
  }
}
```