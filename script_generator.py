import random

USA_FACTS = [
    {
        "title": "Why Is Alaska So Huge?",
        "script": (
            "Did you know Alaska is larger than Texas, "
            "California, and Montana combined? "
            "It became part of the United States in 1867. "
            "Follow Hidden America 2030 for more amazing facts!"
        )
    },
    {
        "title": "America's Biggest State",
        "script": (
            "Alaska is the largest US state by land area. "
            "It is famous for glaciers, mountains, and wildlife. "
            "Would you visit Alaska? Tell us in the comments!"
        )
    }
]


def generate_script():
    fact = random.choice(USA_FACTS)

    print("TITLE:", fact["title"])
    print("\nSCRIPT:", fact["script"])

    return fact


if __name__ == "__main__":
    generate_script()
