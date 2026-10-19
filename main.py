"""Write your exercise solution here."""


def solve(text: str) -> str:
    """Reverse the words in text, separating them with a single space."""
    return " ".join(reversed(text.split()))


if __name__ == "__main__":
    # Change this input to try your solution manually.
    print(solve("hello world"))
