#!/bin/sh
FECHA=$(date "+%Y%m%d")
DEST_FILE='censocath_dump_'$FECHA'.sql'

mysqldump --verbose --add-drop-database --add-drop-table --create-options --complete-insert --host=localhost --user=root --password=cuchara1 --single-transaction --dump-date --databases censocath > $DEST_FILE

