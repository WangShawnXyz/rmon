"""
    rmon.models
    实现所有的model类以及相应的序列化类
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Server(db.Model):
    """
        Redis服务器模型
    """
    __tablename__ = 'redis_server'
    id = db.Column(db.Integer, primary_key=True)
    # 不允许redis的服务器名有重复  unique=True
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer, default=6379)
    password = db.Column(db.String())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Server(name=%s, port=%d)" % (self.name, self.port)
    def save(self):
        """
            保存redis数据库信息到数据库中
        """
        db.session.add(self)
        db.session.commit()
    def delete(self):
        """
            从数据库中删除当前redis服务器信息
        """
        db.session.delete(self)
        db.session.commit()

        