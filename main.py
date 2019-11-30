from flask import Flask
from flask_graphql import GraphQLView
import graphene
from datetime import datetime

# initialise Flask app
app = Flask(__name__)

# define users
class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime()

# define how user is created
class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments: # takes in arguments from GraphQL Mutation
        username = graphene.String()

    def mutate(self, info, username):
        # handles Graphql Context
        # if info.context.get('isAdmin'):
        #     username = username.upper()
        user = User(username=username)
        return CreateUser(user=user)

# Handle Graphql Queries / query schema 
class Query(graphene.ObjectType):
    users = graphene.List(User, limit=graphene.Int())

    def resolve_users(self, info, limit): # users {} query in GraphQL
        return [
            User(username='alpha', last_login=datetime.now()),
            User(username='beta', last_login=datetime.now()),
            User(username='delta', last_login=datetime.now()),
        ][:limit]

# Handle Graphql Mutations / mutation schema
class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field() # createUser {} query in GraphQL

# Schema for GraphQL Query, Mutations and Subscriptions Classes above
schema = graphene.Schema(query=Query, mutation=Mutations) 

# Flask Graphql Route
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# start here
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)