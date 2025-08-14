from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # la instancia vive aquí; app.py la inicializa con init_app()

# Tabla intermedia muchos-a-muchos entre Post y Category
post_categories = db.Table(
    "post_categories",
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True),
    db.UniqueConstraint("post_id", "category_id", name="uq_post_category"),
)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    posts = db.relationship("Post", back_populates="author", cascade="all, delete-orphan")
    comments = db.relationship("Comment", back_populates="author", cascade="all, delete-orphan")
    likes = db.relationship("Like", back_populates="user", cascade="all, delete-orphan")

class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    author = db.relationship("User", back_populates="posts")

    comments = db.relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    likes = db.relationship("Like", back_populates="post", cascade="all, delete-orphan")
    categories = db.relationship("Category", secondary=post_categories, back_populates="posts")

class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False, index=True)

    author = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")

class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    slug = db.Column(db.String(80), nullable=False, unique=True)

    posts = db.relationship("Post", secondary=post_categories, back_populates="categories")

class Like(db.Model):
    __tablename__ = "like"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False, index=True)

    user = db.relationship("User", back_populates="likes")
    post = db.relationship("Post", back_populates="likes")

    __table_args__ = (
        db.UniqueConstraint("user_id", "post_id", name="uq_user_post_like"),
    )
