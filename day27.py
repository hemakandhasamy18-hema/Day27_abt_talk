def detect_duplicates(posts, k):
    last_seen = {}
    suspicious = []

    for i, post in enumerate(posts):
        if post in last_seen:
            previous_index = last_seen[post]

            if i - previous_index <= k:
                suspicious.append(
                    (post, previous_index, i)
                )

        last_seen[post] = i

    return suspicious


def simulate_social_media():
    posts = [
        "Win a free phone!",
        "Hello everyone!",
        "Check this offer!",
        "Win a free phone!",
        "Good morning!",
        "Win a free phone!",
        "Hello everyone!"
    ]

    k = 3

    print("=" * 45)
    print("   SOCIAL MEDIA FRAUD DETECTION")
    print("=" * 45)

    print("\nSimulated social media posts:")
    for i, post in enumerate(posts):
        print(f"Post {i}: {post}")

    print(f"\nDuplicate detection window K = {k}")

    duplicates = detect_duplicates(posts, k)

    print("\nSuspicious repeated activity:")

    if duplicates:
        for post, first, current in duplicates:
            print(f"⚠️ Duplicate: '{post}'")
            print(f"   Previous index: {first}")
            print(f"   Current index: {current}")
            print(f"   Distance: {current - first}\n")
    else:
        print("No suspicious duplicates found.")

    print("Hashing makes duplicate lookups fast!")
    print("Fraud detection simulation completed.")


if __name__ == "__main__":
    simulate_social_media()