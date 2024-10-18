# WoopyMysqlAuth Class

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
[![GitHub](https://img.shields.io/badge/GitHub-WoppyMysql-black)](https://github.com/woopygit/woopyMysql)
[![Wppy.net](https://img.shields.io/badge/WpPy.net-WoppyMysql-black)](https://www.wppy.net/woopyMysql)

[woopyMysql](https://pypi.org/project/woopyMysql/)
```bash
    pip install woopyMysql
```

## Overview

The `WoopyMysqlAuth` class is designed to manage and validate the authentication credentials needed to connect to a MySQL database. It supports loading credentials from an environment file or directly from a dictionary. The class ensures that all required credentials are provided and valid before establishing a database connection.

## Features

- Load database credentials from a `.env` file or a provided dictionary.
- Validate the presence of all necessary credentials.
- Establish a connection to the MySQL database.

## Usage

### Initialization

The class can be initialized in two ways:
1. Using a dictionary containing the authentication credentials.
2. Loading credentials from a `.env` file.

#### Example 1: Initializing with a Dictionary

```bash
WoopyAuth = {
    "woopy_db_host_ip": "127.0.0.1",
    "woopy_db_name": "example_db",
    "woopy_db_user_name": "root",
    "woopy_db_user_password": "password",
    "woopy_db_table_prefix": "wp_"
}

auth = WoopyMysqlAuth(WoopyAuth=WoopyAuth)
```
#### Example 2: Initializing with an Environment File
```bash
auth = WoopyMysqlAuth(WoopyEnv='.env')
```
## Websites using 'woopy' library:
- [OffertaLampo.net](https://www.offertalampo.net)
- [PriceErrors.net](https://www.priceerrors.net)
- [Cpaff.net](https://www.cpaff.net)
- [Promozioni.net](https://www.promozioni.net)
- [buoni.net](https://www.buoni.net)
- [Polignano.net](https://www.polignano.net)
- [Trullit.com](https://www.trullit.com)
- [wppy.net](https://www.wppy.net)