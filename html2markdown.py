def html2markdown(self, html):
  # convert html to markdown.
  # specification:
  # remove all tag exccept tags listed in the cleanbody._repl 
  # when p/div tags are in the table tag, markdown converter (htmlformatter)
  # confuses. so it is removed

  # we need following in the header
  import re, html2text
  from bs4 import BeautifulSoup
  CLEANBODY_RE = re.compile(r'<(/?)(.+?)>', re.M)
  htmlformatter = html2text.HTML2Text()
  htmlformatter.ignore_links = True
  htmlformatter.ignore_images = True
  htmlformatter.body_width = 0

  def remove_non_table_tags_within_table_tag(html):
    def _repl(match):
      tag = match.group(2).split(' ')[0].lower()
      if tag in ( 'table', 'tr', 'td', 'th'):
          return match.group(0)
      return u''
      
    soup =  BeautifulSoup(html, "lxml")
    for table in soup.find_all('table'):
      # find all table element

      # convert to string
      table_html = str(table)

      # remove tags other than  'table', 'tr', 'td', 'th'
      clean_table = CLEANBODY_RE.sub(_repl, table_html)

      # put back to the original html
      table.replace_with(BeautifulSoup(clean_table, "lxml"))
    return str(soup)

  def non_document_tag_remover(match):
    tag = match.group(2).split(' ')[0].lower()
    if tag in ( 'br', 'ul', 'li', 'p',  'h1','h2','h3','h4','h5','h6','div','table', 'tr', 'td', 'th'):
      return match.group(0)
    return u''
    
  #main routine
  if html.lower().find('table') > -1:
    # clean tags within table tag
    html = remove_non_table_tags_within_table_tag(html)

  # strip unrelated tags
  clean_html = CLEANBODY_RE.sub(non_document_tag_remover, html)

  # convert it to markdown
  markdown =  htmlformatter.handle(clean_html)

  return markdown
