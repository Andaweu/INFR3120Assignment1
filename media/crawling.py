import requests
from bs4 import BeautifulSoup
import networkx as nx
from urllib.parse import urljoin
from collections import deque
import time
import matplotlib.pyplot as plt
def is_valid_link(link):
    if not link or 'http' not in link:
        return False
    invalid_suffixes = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.svg', '.webp']
    return not any(link.lower().endswith(ext) for ext in invalid_suffixes)
def create_tree():
    return nx.DiGraph() # or nx.Graph() if you want undirected
def crawl(start_url, max_pages=100, save_interval=500, output_file='web_graph.gexf', link_limit=50):
    visited = set()
    graph = create_tree() # Use your graph creation function
    queue = deque([start_url])
    page_count = 0
    while queue and page_count < max_pages:
        current_url = queue.popleft()
        if current_url in visited:
            continue
        print(f"Crawling: {current_url}")
        visited.add(current_url)
        try:
            response = requests.get(current_url, timeout=5)
            if 'text/html' not in response.headers.get('Content-Type', ''):
                continue
        except requests.RequestException:
            continue
        soup = BeautifulSoup(response.text, 'html.parser')
        link_counter = 0
        for a_tag in soup.find_all('a', href=True):
            if link_counter >= link_limit:
                break
            href = a_tag['href']
            full_url = urljoin(current_url, href)
            if is_valid_link(full_url):
                graph.add_edge(current_url, full_url)
                if full_url not in visited:
                    queue.append(full_url)
                link_counter += 1
        page_count += 1
        if page_count % save_interval == 0:
            filename = f"{output_file.replace('.gexf', '')}_{page_count}.gexf"
            nx.write_gexf(graph, filename)
            print(f"Saved graph with {page_count} pages to {filename}")
    nx.write_gexf(graph, output_file)
    print(f"Final graph saved to {output_file} with {page_count} pages.")



def show_graph(graph):
    plt.figure(figsize=(12, 8)) # Optional: Set figure size
    pos = nx.spring_layout(graph, seed=11) # Layout for consistent display
    nx.draw(graph, with_labels=True, font_weight='bold', pos=pos, node_size=500,node_color='skyblue', edge_color='gray')
plt.title("Web Graph Visualization")
plt.show()
# Example usage
start_url = 'https://google.com'
crawl(start_url)
if __name__ == "__main__":
    g = create_tree()
    show_graph(g)
    nx.readwrite.gexf.read_gexf('web_graph.gexf')