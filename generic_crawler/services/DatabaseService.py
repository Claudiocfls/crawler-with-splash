import psycopg2
import base64

class DatabaseService:
  _instance = None

  def __init__(self):
    self.connection, self.cursor = self.open_connection()

  @classmethod
  def get_instance(cls):
    if cls._instance is None:
      cls._instance = cls()
    return cls._instance

  def open_connection(self):
    '''
    !IMPORTANT
    Change the database credentials before use.
    '''
    try:
      connection = psycopg2.connect(user = "DB_USER",
                                    password = "DB_PASS",
                                    host = "DB_HOST",
                                    port = "5432",
                                    database = "DB_NAME")

      cursor = connection.cursor()
      print ( connection.get_dsn_parameters(),"\n")

      cursor.execute("SELECT version();")
      record = cursor.fetchone()
      print("You are connected to - ", record,"\n")
      return connection, cursor

    except (Exception, psycopg2.Error) as error :
      print ("Error while connecting to PostgreSQL", error)
  
  def save_html(self, label, url, html):
    html_encoded = base64.b64encode(html)
    html_encoded_as_string = "".join(chr(x) for x in html_encoded)
    self.cursor.execute("INSERT INTO crawler_results (label, url, html) VALUES ('{}', '{}', '{}');".format(label, url, html_encoded_as_string))
    self.connection.commit()
