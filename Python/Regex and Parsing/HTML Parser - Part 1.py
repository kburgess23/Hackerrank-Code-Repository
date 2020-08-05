# https://www.hackerrank.com/challenges/html-parser-part-1/problem


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')


parser = MyHTMLParser()
html_code = ''.join([input() for _ in range(int(input()))])

parser.feed(html_code)

# github.com/ArutselvanManivannan
