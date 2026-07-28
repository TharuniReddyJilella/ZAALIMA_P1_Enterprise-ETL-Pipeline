from app.extract.stripe_extractor import StripeExtractor
from app.utils.file_writer import FileWriter


def main():

    extractor = StripeExtractor()

    users = extractor.extract_users()

    filename = FileWriter.save_json(users, "users")

    print(f"Saved to: {filename}")


if __name__ == "__main__":
    main()