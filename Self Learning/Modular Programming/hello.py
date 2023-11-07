import messeges as msg

# Accessing a function from other module
msg.hello()
msg.bye()

# other way of accessing a modules
# contents, this way we don't need to alias

from messeges import hello, bye

hello()
bye()
