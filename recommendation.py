movies = {
    "action": ["Mad Max", "John Wick", "Avengers"],
    "comedy": ["The Mask", "Superbad", "Hangover"],
    "drama": ["Forrest Gump", "Shawshank Redemption", "Fight Club"],
    "sci-fi": ["Interstellar", "Inception", "Matrix"]
}

print("🎬 Welcome to Movie Recommendation System")
print("Available genres:")
for genre in movies:
    print("-", genre)

choice = input("\nEnter a genre you like: ").lower()

if choice in movies:
    print("\nRecommended movies for you:")
    for movie in movies[choice]:
        print("👉", movie)
else:
    print("❌ Sorry, genre not found.")
