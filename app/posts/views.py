from flask import render_template, redirect, url_for, flash, request
from .forms import PostForm
from . import posts_bp
import json

@posts_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = {
            "id": 1,
            "title": form.title.data,
            "content": form.content.data,
            "category": form.category.data,
            "is_active": form.is_active.data,
            "publication_date": "2024-12-16",
            "author": "SessionUser"
        }
        try:
            with open('posts.json', 'r') as f:
                posts = json.load(f)
        except FileNotFoundError:
            posts = []

        posts.append(post)

        with open('posts.json', 'w') as f:
            json.dump(posts, f, indent=4)

        flash(f'Post "{post["title"]}" added successfully!', 'success')
        return redirect(url_for('posts.add_post'))
    return render_template('posts/add_post.html', form=form)
