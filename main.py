from app.api.api_client import APIClient


def main():
    client = APIClient(
        "https://jsonplaceholder.typicode.com"
    )

    users = client.get("/users")

    print(f"Fetched {len(users)} users")

    print(users[0])


if __name__ == "__main__":
    main()