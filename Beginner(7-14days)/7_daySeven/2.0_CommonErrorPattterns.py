# Common Error Handling Patterns
# 1.Catch Specific Exceptions: 
# try:
    # Some code 
# except (TypeError, ValueError) as e:
    # print(f"Error: {e}")


# 2.Logging Errors: 
# import logging
# logging.basicConfig(level=logging.ERROR)

# try:
#     #some code
# except Exception as e:
#     logging.error(f"An error occurred: {e}")