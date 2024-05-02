import common

delimiter = "####"
system_message = f"""
  Users will provide a json object containing object types. \ 
  you are expected to produce an equivalent graphql schema corresponding to the user input. \
  Do not provide any other output than the schema, and do not out "```graphql" tag.  
"""

def generate_graphql():
  user_input = """
    { \
      "Post": {
        "id": "Integer"
        "owner": "String"
        "comments: "Array"
        "date": "Date"
      }
    }
  """
  messages = [
    {'role': 'system',
     'content': system_message},
    {'role': 'user',
     'content': f"{delimiter}{user_input}{delimiter}"},
  ]
  return common.get_completion_from_messages(messages)

def driver():
  out = generate_graphql()
  print(out)

if __name__ == '__main__':
  driver()


