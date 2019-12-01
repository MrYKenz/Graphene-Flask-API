# Graphene Flask GraphQL API ![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/GraphQL_Logo.svg/240px-GraphQL_Logo.svg "GraphQL")

A simple GraphQL API using Flask and Flask Graqhql to create an API route for the server and Graphene to create Python based Schema. All dependencies (python modules/libraries) can be found in requirements.txt and installed with pip. 
```bash
pip install -r requirements.txt
```
However, I have used a Docker Container with the dependencies outlined in the Dockerfile, this can also be used to build a microservice in a microservice architecture but as GraphQL aims for one endpoint schema stitching or Apollo Federation should be used to join the API endpoints.

Flask Graphql provides a graphiql playground to run queries against the endpoint which can be used for testing.

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
              title
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
        id
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