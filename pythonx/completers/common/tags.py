from completor import Completor, vim

class Tags(Completor):
    filetype = 'tags'
    sync = True

    def parse(self, base):
        tags = vim.eval('taglist("{}")'.format(base))
        names = list(set([tag['name'] for tag in tags]))
        return [{'word': name, 'menu': '[Tag]'} for name in sorted(names)]
