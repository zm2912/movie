# coding:utf8
from datetime import datetime
from werkzeug.security import generate_password_hash
from app import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())
    uuid = db.Column(db.String(255), unique=True)
    user_logs = db.relationship("UserLog", backref="user")  # 外键关系关联
    # db.relationship的第一个参数表示“many”一方的类名。backref参数定义了一个字段将"many"类的对象指回到"one"对象
    comments = db.relationship("Comment", backref="user")
    movie_cols = db.relationship("MovieCol", backref="user")

    def __repr__(self):
        return "<User %r>" % self.name


class UserLog(db.Model):
    __tablename__ = "user_log"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(100))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<UserLog %r>" % self.id


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())
    movies = db.relationship("Movie", backref="tag")

    def __repr__(self):
        return "<Tag %r>" % self.name


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)  # 简介
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    play_num = db.Column(db.BigInteger)  # 播放量
    comment_num = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 播放时长
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())
    comments = db.relationship("Comment", backref="movie")
    movieCols = db.relationship("MovieCol", backref="movie")

    def __repr__(self):
        return "<Movie %r>" % self.name


class Preview(db.Model):  # 预告
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<Preview %r>" % self.title


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<Comment %r>" % self.content


# 电影收藏
class MovieCol(db.Model):
    __tablename__ = "movie_col"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<MovieCol %r>" % self.content


class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<Auth %r>" % self.name


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(600))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())
    admins = db.relationship("Admin", backref="role")

    def __repr__(self):
        return "<Role %r>" % self.name


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())
    admin_logs = db.relationship("AdminLog", backref="admin")
    op_logs = db.relationship("OpLog", backref="admin")

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


class AdminLog(db.Model):
    __tablename__ = "admin_log"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<AdminLog %r>" % self.id


class OpLog(db.Model):
    __tablename__ = "op_log"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(600))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<OpLog %r>" % self.id


if __name__ == "__main__":
    db.create_all()
#     # role = Role(name="超级管理员", auths="")
#     # db.session.add(role)
#     # from werkzeug.security import generate_password_hash 生成密码
#     admin = Admin(name="imoocMovie", pwd=generate_password_hash("imoocMovie"), is_super=0, role_id=1)
#     db.session.add(admin)
#     db.session.commit()
