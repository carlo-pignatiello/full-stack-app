import os

env = os.getenv("POSTGRES_USER", "NA")

if __name__ == "__main__":
    print(env)