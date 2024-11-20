import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="Exercise_logging.log",
    filemode="a"
)

while True:
    user_name = input("Enter your username (or type 'exit' to exit): ")
    if user_name.lower() == "exit":
        break
    logging.info(f"User successfully entered username. Username is: {user_name}")
    password = input("Enter your password: ")
    logging.info(f"User successfully entered password. Password is: {password}")