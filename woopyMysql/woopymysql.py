import os
import logging
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import errorcode
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class WoopyMysqlAuth:
    def __init__(self, WoopyAuth=None, WoopyEnv='.env'):
        if WoopyAuth:
            self._update_auth_from_dict(WoopyAuth)
        else:
            load_dotenv(WoopyEnv)  # Carica il file .env specificato
            self._load_env_variables()
        self._validate_variables()  # Assicura che la validazione avvenga dopo il caricamento delle variabili

    def _load_env_variables(self):
        self.woopy_db_host_ip = os.environ.get("WOOPY_DB_HOST_IP", "")
        self.woopy_db_name = os.environ.get("WOOPY_DB_NAME", "")
        self.woopy_db_user_name = os.environ.get("WOOPY_DB_USER_NAME", "")
        self.woopy_db_user_password = os.environ.get("WOOPY_DB_USER_PASSWORD", "")
        self.woopy_db_table_prefix = os.environ.get("WOOPY_DB_TABLE_PREFIX", "")

    def _update_auth_from_dict(self, WoopyAuthDict):
        self.woopy_db_host_ip = WoopyAuthDict.get("woopy_db_host_ip", "")
        self.woopy_db_name = WoopyAuthDict.get("woopy_db_name", "")
        self.woopy_db_user_name = WoopyAuthDict.get("woopy_db_user_name", "")
        self.woopy_db_user_password = WoopyAuthDict.get("woopy_db_user_password", "")
        self.woopy_db_table_prefix = WoopyAuthDict.get("woopy_db_table_prefix", "")

    def _validate_variables(self):
        if not self.woopy_db_host_ip:
            logger.error("Missing required variable: woopy_db_host_ip")
            raise ValueError("Missing required variable: woopy_db_host_ip")
        if not self.woopy_db_name:
            logger.error("Missing required variable: woopy_db_name")
            raise ValueError("Missing required variable: woopy_db_name")
        if not self.woopy_db_user_name:
            logger.error("Missing required variable: woopy_db_user_name")
            raise ValueError("Missing required variable: woopy_db_user_name")
        if not self.woopy_db_user_password:
            logger.error("Missing required variable: woopy_db_user_password")
            raise ValueError("Missing required variable: woopy_db_user_password")

    def connect_to_db(self):
        """
        Establishes a connection to the MySQL database.

        Returns:
            MySQLConnection: A MySQL connection object.
        """


        try:
            connection = mysql.connector.connect(
                host=self.woopy_db_host_ip,
                user=self.woopy_db_user_name,
                password=self.woopy_db_user_password,
                database=self.woopy_db_name

            )
            logger.info("Connected to the database successfully.")
            return connection
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logger.error("Invalid credentials for the database.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logger.error("Database does not exist.")
            else:
                logger.error(f"Database connection error: {err}")
            raise

    def query_db(self, query, params=None):
        """
        Executes a query on the MySQL database.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Optional parameters to pass with the query.

        Returns:
            list: A list of tuples containing the query results.
        """
        connection = self.connect_to_db()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            results = cursor.fetchall()
            logger.info(f"Query executed successfully: {query}")
            return results
        except mysql.connector.Error as err:
            logger.error(f"Query execution error: {err}")
            raise
        finally:
            cursor.close()
            connection.close()
            logger.info("Database connection closed.")

    def query_db_fetchone(self, query, params=None):
        """
        Executes a query on the MySQL database.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Optional parameters to pass with the query.

        Returns:
            list: A list of tuples containing the query results.
        """
        connection = self.connect_to_db()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            results = cursor.fetchone()
            logger.info(f"Query executed successfully: {query}")
            return results
        except mysql.connector.Error as err:
            logger.error(f"Query execution error: {err}")
            raise
        finally:
            cursor.close()
            connection.close()
            logger.info("Database connection closed.")

    def check_table_exists(self, table_name=None):
        connection = self.connect_to_db()
        if table_name is None:
            raise ValueError("table name can't be empty")

        cursor = connection.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False