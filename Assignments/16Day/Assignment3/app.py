from flask import Flask, render_template

app = Flask(__name__)

# Inappropriate words list
BAD_WORDS = ["dumb", "stupid"]

# Dummy comment data
comments = [
    {
        "username": "john",
        "comment": " This is a very nice post! ",
        "likes": 120,
        "flagged": False
    },
    {
        "username": "sarah",
        "comment": "This is a stupid idea and very dumb implementation.",
        "likes": 45,
        "flagged": True
    },
    {
        "username": "mike",
        "comment": "A" * 210,
        "likes": 10,
        "flagged": False
    }
]


# Custom filter to replace bad words
@app.template_filter("clean_words")
def clean_words_filter(text):
    for word in BAD_WORDS:
        text = text.replace(word, "***")
        text = text.replace(word.capitalize(), "***")
    return text


@app.route("/")
def show_comments():

    total_comments = len(comments)
    total_flagged = sum(1 for c in comments if c["flagged"])
    most_liked = max(comments, key=lambda x: x["likes"])
    usernames_joined = ", ".join(c["username"].upper() for c in comments)

    return render_template(
        "comments.html",
        comments=comments,
        total_comments=total_comments,
        total_flagged=total_flagged,
        most_liked=most_liked,
        usernames_joined=usernames_joined
    )


if __name__ == "__main__":
    app.run(debug=True)