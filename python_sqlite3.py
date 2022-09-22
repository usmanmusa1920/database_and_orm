# Database table most often contains one or more tables.
# Each tle is identify by a name (e.g students or staffs).
# Tabless contains records (row) with data.

import sqlite3


# the connection is just to the cpu, we will not get any benefit,
# after running the programm (no data save) i.e it will flush it out,
# since we did not specify a definate sqlite.db file
conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

cursor.execute(
  "CREATE TABLE `logs` ("
    # AUTO_INCREMENT will automatically increment in sqlite3
    " `id` INTEGER(11) NOT NULL,"
    " `text` varchar(250) NOT NULL,"
    " `user` varchar(250) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ")"
)

print('table created')
