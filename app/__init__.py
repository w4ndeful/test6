from flask import Flask, render_template, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    from .posts import posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    @app.route('/')
    def home():
        return redirect(url_for('posts.add_post'))

    @app.route('/favicon.ico')
    def favicon():
        return '', 204

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app
