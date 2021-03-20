class Pager:
    def __init__(self, per_page, cur_page, total_num, page_view, url):
        '''

        :param per_page:    每一页的数据数
        :param cur_page:    当前页码
        :param total_num:   数据库总行数
        :param page_view:   一次显示出的页码
        :param url          url
        '''
        self.per_page = per_page
        try:
            self.cur_page = int(cur_page)
        except Exception as e:
            self.cur_page = 1
        # page_num 总页码
        a, b = divmod(total_num, 5)
        if b:
            self.page_num = a + 1
        else:
            self.page_num = a

        self.page_views = page_view
        self.url = url

    def begin(self):
        return (self.cur_page - 1) * self.per_page

    def end(self):
        return self.cur_page * self.per_page

    def pager(self):
        page = []
        half = int(self.page_views / 2)
        if self.page_num <= self.page_views:
            begin = 1
            end = self.page_num+1
        elif self.cur_page <= half:
            begin = 1
            end = self.page_views + 1
        elif self.cur_page >= self.page_num - half:
            begin = self.page_num - self.page_views
            end = self.page_num + 1
        else:
            begin = self.cur_page - half
            end = self.cur_page + half + 1
        if self.cur_page <= 1:
            page.append('''
            <li>
                 <a href="#" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
             </li>''')
        else:
            page.append('''
            <li>
                <a href="%s?page=%s" aria-label="Previous">
                     <span aria-hidden="true">&laquo;</span>
                 </a>
             </li>''' % (self.url, self.cur_page - 1))
        for i in range(begin, end):
            if i == self.cur_page:
                page.append("<li class='active'><a href='%s?page=%s'>%s</a><li>" % (self.url, i, i))
            else:
                page.append("<li><a href='%s?page=%s'>%s</a><li>" % (self.url, i, i))

        if self.cur_page >= self.page_num:
            page.append('''
            <li>
                 <a href="#" aria-label="Next">
                    <span aria-hidden="true">&laquo;</span>
                </a>
             </li>''')
        else:
            page.append('''
            <li>
                <a href="%s/?page=%s" aria-label="Next">
                     <span aria-hidden="true">&raquo;</span>
                 </a>
             </li>''' % (self.url, self.cur_page + 1))
        return "".join(page)
