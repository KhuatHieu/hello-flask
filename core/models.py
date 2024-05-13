from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase


# core model để các models khác sẽ kế thừa
class BaseModel(DeclarativeBase):
    # khai báo model này không thể được khởi tạo thành 1 instance
    # vì class này chỉ là base, hông cần khởi tạo
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

    # lưu thời gian record được tạo ra lần đầu
    created_at = Column(DateTime, default=datetime.utcnow)

    # lưu thời gian reecord được cập nhật
    # onupdate=datetime.utcnow: mỗi khi record đc cập nhật: tự động cập nhật
    #                                                       updated_at thành thời gian hiện tại
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # soft delete - xóa mềm - sẽ dùng cột để biểu thị xem record đã xóa hay chưa
    # thay vì là xóa cứng
    # đánh dấu thời gian record được xóa
    deleted_at = Column(DateTime, default=datetime.utcnow)
