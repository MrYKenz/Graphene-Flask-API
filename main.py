from flask import Flask, request
import graphene
import json
from datetime import datetime

# initialise Flask app
app = Flask(__name__)

# define users
class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime()

# Graphql End Point for Queries - Read in CRUD 
class Query(graphene.ObjectType):
    users = graphene.List(User, limit=graphene.Int())

    def resolve_users(self, info, limit): # users {} query in GraphQL
        return [
            User(username='alpha', last_login=datetime.now()),
            User(username='beta', last_login=datetime.now()),
            User(username='delta', last_login=datetime.now()),
        ][:limit]

# define how user is created
class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments: # takes in arguments from GraphQL Mutation
        username = graphene.String()

    def mutate(self, info, username):
        # handles Graphql Context
        if info.context.get('isAdmin'):
            username = username.upper()

        user = User(username=username)
        return CreateUser(user=user)

# Graphql End Point for Mutations - Create in CRUD operations 
class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field() # createUser {} query in GraphQL

# Schema for GraphQL Query, Mutations and Subscriptions Classes above
schema = graphene.Schema(query=Query, mutation=Mutations) 

# flask routes
@app.route('/')
def hello():
    return "hello world"

# result1 = schema.execute(
#     '''
#     {
#         users(limit: 5) {
#             username
#             lastLogin
#         }
#     }
#     '''
# ) # QraphQL Query to run against the Query Endpoint resolve_users

# new_user = 'new'
# is_admin = True

# result2 = schema.execute(
#     '''
#     mutation createUser($usernameVar: String) {
#         createUser(username: $usernameVar) {
#             user {
#                 username
#             }
#         }
#     }
#     ''', variable_values={'usernameVar': new_user}, context={'isAdmin': is_admin}
# ) # QraphQL Mutation to run against the Mutation Endpoint create_user

# converted to a dictionary so that odict() can be parsed as JSON
#print(json.dumps(dict(result1.data.items()), indent=2))
#print(json.dumps(dict(result2.data.items()), indent=2))

