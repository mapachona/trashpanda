import tika

from tika import parser
dbf_example = '/path/to/file.dbf'
parsed = parser.from_file(dbf_example)
import pdb; pdb.set_trace()
