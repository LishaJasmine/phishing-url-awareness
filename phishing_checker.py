import re
from urllib.parse import urlparse


def check_url(url):
    warnings = []

    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        url = "http://" + url

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname or ""

    # Check 1: @ symbol
    if "@" in url:
        warnings.append(
            "The URL contains an '@' symbol, which may be used "
            "to disguise the destination."
        )

    # Check 2: Unusually long URL
    if len(url) > 100:
        warnings.append(
            "The URL is unusually long. Review it carefully."
        )

    # Check 3: IP address as hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
        warnings.append(
            "The hostname appears to be an IP address."
        )

    # Check 4: Many hostname segments
    if len(hostname.split(".")) >= 5:
        warnings.append(
            "The hostname has many dot-separated segments."
        )

    # Check 5: Punycode
    if any(label.startswith("xn--") for label in hostname.lower().split(".")):
        warnings.append(
            "The hostname contains a punycode label. "
            "Check the domain carefully."
        )

    # Check 6: HTTP instead of HTTPS
    if parsed_url.scheme.lower() == "http":
        warnings.append(
            "The URL uses HTTP instead of HTTPS."
        )

    return warnings


def main():
    print("=" * 50)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 50)
    print("Educational tool: checks URL text only.")
    print("It does not open or visit websites.")
    print("Type 'quit' to exit.\n")

    while True:
        url = input("Enter a URL to check: ").strip()

        if url.lower() in ("quit", "exit", "q"):
            print("\nThank you for using the checker!")
            break

        if not url:
            print("Please enter a URL.\n")
            continue

        try:
            warnings = check_url(url)

            print("\nURL checked:", url)
            print("-" * 50)

            if warnings:
                print("Warning signs found:")

                for number, warning in enumerate(warnings, start=1):
                    print(f"{number}. {warning}")

                print("\nResult: CAUTION")
                print("Review this URL carefully.")
            else:
                print("No listed warning signs found.")
                print("This does NOT prove the URL is safe.")

            print("\nRemember:")
            print("Never enter sensitive information without")
            print("verifying the website independently.")
            print("-" * 50, "\n")

        except ValueError:
            print("Invalid URL input. Please try again.\n")


if __name__ == "__main__":
    main()