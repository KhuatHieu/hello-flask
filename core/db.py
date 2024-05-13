# chứa các cấu hình cần thiết để tạo kết nối đến database
# các query cần thực hiện sẽ sử dụng g.session được cấu hình ở đây

from flask import g

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

from .conf import Config

url = URL.create(
    drivername=Config.DB_DRIVER,
    host=Config.DB_HOST,
    port=Config.DB_PORT,
    username=Config.DB_USER,
    password=Config.DB_PASSWORD,
    database=Config.DB_DATABASE,
)

# engine: core dùng để taoj kết nối đến db
engine = create_engine(url)

# session: 1 connection kết nối đến db
# khi cần kết nối đến db: gọi session ra
# khi không cần kết nối nữa: đóng session lại
Session = sessionmaker(bind=engine)


# khi có request mới: tạo session mới
# khi mà trả kết quả về cho browser: đóng session
# session: tồn tại ử cấp độ GLOBAL: toàn ứng dụng

# khởi tạo 1 session mới ở cấp độ global
# gọi trước khi request được xử lý
def before_request():
    g.session = Session()


# đóng session
# sau khi đã trả kết quả về cho browser - client
def teardown_request(exception=None):
    # lấy session ra
    session = g.pop('session', None)

    # đóng session lại
    if session is not None:
        # kiểm tra: nếu có exception: rollback lại các lệnh vừa thực hiện
        #           ở trong session vừa rồi
        # ví dụ: đamg update 1 record nửa chùng thì mạng lỗi -> exception -> rollback lại
        if exception is not None:
            session.rollback()

        session.close()
