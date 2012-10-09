def find_link(text):
	links = re.findall('<a href=.*?</a>', text)
	return links


def sort_link(links):
	new_linkset = []
	for item in links:
		x = re.search('<a href="(http://t\.co.*?)>', str(item))
		if x:
			new_linkset.append(x.group(1))
	return new_linkset

def grab_title(sorted_links):
	titles = []
	for item in sorted_links:
		content = urllib.urlopen(item).read()
		title = re.search('<title>(.*?)</title>', content)
		if title:
			titles.append(title.group(1))
	return titles


def grab_h1(sorted_links):
	titles = []
	for item in sorted_links:
		content = urllib.urlopen(item).read()
		title = re.search('(<h1.*?/h1>)', content)
		if title:
                    edited = re.search('<.*?>(\w+)</.*?>', line)
                    titles.append(title.group(1))
	return titles
