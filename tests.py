from main import schema
import json

result1 = schema.execute(
    '''
    {
        users(limit: 5) {
            username
            lastLogin
        }
    }
    '''
) # QraphQL Query to run against the Query Endpoint resolve_users

new_user = 'new'
is_admin = True

result2 = schema.execute(
    '''
    mutation createUser($usernameVar: String) {
        createUser(username: $usernameVar) {
            user {
                username
            }
        }
    }
    ''', variable_values={'usernameVar': new_user}, context={'isAdmin': is_admin}
) # QraphQL Mutation to run against the Mutation Endpoint create_user

# converted to a dictionary so that odict() can be parsed as JSON
print(json.dumps(dict(result1.data.items()), indent=2))
print(json.dumps(dict(result2.data.items()), indent=2))