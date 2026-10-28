import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter


# Postebis chamotvirtva
def fetch_posts(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        posts = response.json()

        print(f"User {user_id}: ჩამოიტვირთა {len(posts)} პოსტი")

        return posts

    except requests.exceptions.Timeout:
        print(f"User {user_id}: მოთხოვნას 5 წამზე მეტი დასჭირდა")
        return []

    except requests.exceptions.RequestException as error:
        print(f"User {user_id}: შეცდომა - {error}")
        return []


# datvla
def count_posts(all_posts):
    post_counts = Counter()

    for post in all_posts:
        user_id = post["userId"]
        post_counts[user_id] += 1

    return dict(post_counts)


#Post search
def find_longest_post(all_posts):
    if not all_posts:
        return None

    longest_post = max(
        all_posts,
        key=lambda post: len(post["body"])
    )

    return {
        "user_id": longest_post["userId"],
        "title": longest_post["title"],
        "body_length": len(longest_post["body"])
    }


# Title length
def average_title_length(all_posts):
    if not all_posts:
        return 0

    total_length = 0

    for post in all_posts:
        total_length += len(post["title"])

    average = total_length / len(all_posts)

    return average


# print
def print_results(post_counts, longest_post, average_length):
    print("\n" + "=" * 50)
    print("              პოსტების ანალიზი")
    print("=" * 50)

    print("მომხმარებელი      პოსტების რაოდენობა")
    print("-" * 40)

    for user_id in sorted(post_counts):
        print(f"User {user_id:<12} {post_counts[user_id]}")

    print("\nყველაზე გრძელი პოსტი:")

    if longest_post:
        print(f"მომხმარებელი: User {longest_post['user_id']}")
        print(f"სათაური: {longest_post['title']}")
        print(f"სიგრძე: {longest_post['body_length']} სიმბოლო")
    else:
        print("პოსტები ვერ მოიძებნა")

    print(
        f"\nსათაურების საშუალო სიგრძე: "
        f"{average_length:.2f} სიმბოლო"
    )

    print("=" * 50)


# მთავარი ფუნქცია
def main():
    user_ids = [1, 2, 3, 4, 5]

    # პოსტების ჩამოტვირთვა Thread-ებით
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(
            executor.map(fetch_posts, user_ids)
        )

    # ყველა მომხმარებლის პოსტების ერთ სიაში გაერთიანება
    all_posts = []

    for user_posts in results:
        all_posts.extend(user_posts)

    print(f"\nსულ ჩამოიტვირთა {len(all_posts)} პოსტი")

    # თუ ვერცერთი პოსტი ვერ ჩამოიტვირთა
    if not all_posts:
        print("ანალიზისთვის პოსტები არ მოიძებნა.")
        return

    # სამი ანალიზის პარალელურად შესრულება Processes-ით
    with ProcessPoolExecutor(max_workers=3) as executor:
        count_future = executor.submit(
            count_posts,
            all_posts
        )

        longest_future = executor.submit(
            find_longest_post,
            all_posts
        )

        average_future = executor.submit(
            average_title_length,
            all_posts
        )

        # პროცესებიდან შედეგების მიღება
        post_counts = count_future.result()
        longest_post = longest_future.result()
        average_length = average_future.result()

    # შედეგების დაბეჭდვა
    print_results(
        post_counts,
        longest_post,
        average_length
    )



if __name__ == "__main__":
    main()
