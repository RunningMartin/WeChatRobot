# 登录方式 SCAN MAIL
SCAN = "SCAN"
MAIL = "MAIL"
LOGIN_TYPE = MAIL

# QR
QR_PATH = "QR存放位置"

# 邮件信息设置
EMAIL_HOST = ""
EMAIL_PORT = ""
EMAIL_USER = ""
EMAIL_PASSWORD = ""
ACCEPT_EMAIL = ""

# 群监听
IS_LISTEN_GROUP = True

# 群分享监听
IS_LISTEN_SHARING = True

# 数据库
DATABASE_NAME = "WeChat.db"
# 聊天记录
CREATE_CHAT_TABLE_SQL = """CREATE TABLE IF NOT EXISTS CHAT(
        CHAT_GROUP       TEXT    NOT NULL,
        SENDER      TEXT    NOT NULL,
        SEND_TIME        TEXT    NOT NULL,
        CONTENT     TEXT    NOT NULL ,
        PRIMARY KEY (CHAT_GROUP,SENDER,SEND_TIME)
);"""

INSERT_CHAT_SQL = """
INSERT INTO CHAT (CHAT_GROUP,SENDER,SEND_TIME,CONTENT) 
      VALUES ('{0}', '{1}', '{2}', '{3}');
"""

QUERY_CHAT_BY_DATA_SQL = """
SELECT SENDER FROM CHAT WHERE CHAT_GROUP='{0}'  AND SEND_TIME BETWEEN '{1}' AND '{2}';
"""
# 群管理员
CREATE_ADMIN_SQL = """CREATE TABLE IF NOT EXISTS ADMIN(
        UUID               TEXT    NOT NULL, 
        CHAT_GROUP       TEXT    NOT NULL,
        ADMIN_NAME       TEXT    NOT NULL,
        PRIMARY KEY (UUID,CHAT_GROUP,ADMIN_NAME)
);"""

INSERT_ADMIN_SQL = """
INSERT INTO ADMIN (UUID,CHAT_GROUP,ADMIN_NAME) 
      VALUES ('{0}', '{1}', '{2}');
"""

DELETE_ADMIN_SQL = """
DELETE from ADMIN WHERE UUID='{0}' and CHAT_GROUP='{1}';
"""

QUERY_GROUP_ADMIN_SQL = """
SELECT UUID FROM ADMIN WHERE CHAT_GROUP='{0}';
"""

QUERY_ADMIN_SQL = """
SELECT UUID FROM ADMIN;
"""

# 监听群组
CREATE_LISTEN_CHAT_GROUP_SQL = """CREATE TABLE IF NOT EXISTS LISTEN_CHAT_GROUP(
        CHAT_GROUP_PUID       TEXT    NOT NULL,
        CHAT_GROUP_NAME       TEXT    NOT NULL,
        PRIMARY KEY (CHAT_GROUP_PUID,CHAT_GROUP_NAME)
);"""

INSERT_LISTEN_CHAT_GROUP_SQL = """
INSERT INTO LISTEN_CHAT_GROUP (CHAT_GROUP_PUID,CHAT_GROUP_NAME)
      VALUES ('{0}','{1}');
"""

DELETE_LISTEN_CHAT_GROUP_SQL = """
DELETE from LISTEN_CHAT_GROUP WHERE CHAT_GROUP_PUID='{0}';

"""
QUERY_LISTEN_CHAT_GROUP_SQL = """
SELECT CHAT_GROUP_NAME FROM LISTEN_CHAT_GROUP;
"""

# 指令
ADD_GROUP_ADMIN = "添加群管理员"
REMOVE_GROUP_ADMIN = "删除群管理员"

ADD_LISTEN_GROUP = "添加群监听"
REMOVE_LISTEN_GROUP = "移除群监听"

COUNT_MEMBER_BY_DATA = "按日期统计发言成员"

INTERNAL = " "
