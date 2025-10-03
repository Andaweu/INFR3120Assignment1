from bs4 import BeautifulSoup
import urllib3 as urllib
import networkx as nx
import matplotlib.pyplot as plt

def findUrls(root):
    #Your code here

    http = urllib.PoolManager() #creates a PoolManager to handle requests
    graph = nx.Graph() #creates an nx graph
    graph.add_node(root) #uses the root (base url) as the root node of the star

    try: #attempt to connect to the root url
        resp = http.request("GET", root) #sent a GET request to the root url
        soup = BeautifulSoup(resp.data, 'html.parser') #BeautifulSoup paraphrases the HTML content to search the url Tree

        for link in soup.find_all('a', href=True): #Loops through all the HTML <a> tags with an href attribute
            url = link['href'] #takes the href attribute from the url

            if url.startswith('http'): #only looks for urls that start with http
                graph.add_node(url) #adds the url to the graph
                graph.add_edge(root, url) #adds an edge between the root and the found url nodes

    
    except Exception as error: #creates an exception should the url not connect
        print(f"error fetching {root}: {error}")



    return graph


"""
CODE TO TEST YOUR FUNCTIONS BEGINS HERE (DON'T MODIFY)
"""

url = "http://google.ca"


plt.figure(figsize=(12, 10))


graph = findUrls(url)
plt.subplot(111)
nx.draw(graph, with_labels=True)
plt.show()
print('\n Graph Nodes = ', graph.nodes)
print('\n Number of URLs = ', len(graph.nodes))
