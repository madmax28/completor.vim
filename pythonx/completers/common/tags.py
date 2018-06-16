from completor import Completor, vim
from completor.compat import to_unicode
from completers.common.buffer import get_encoding

class Tags(Completor):
    filetype = 'tags'
    sync = True

    def parse(self, base):
        nr = vim.current.buffer.number
        encoding = get_encoding(nr)

        tags = vim.eval('taglist("{}")'.format(to_unicode(base, encoding)))
        names = list(set([tag['name'] for tag in tags]))
        return [{'word': name, 'menu': '[Tag]'} for name in sorted(names)]
