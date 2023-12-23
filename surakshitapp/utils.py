import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image = buffer.getvalue()
    graph = base64.b64encode(image)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def plot(x, y):
    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(10, 5))

    # Set background color
    fig.set_facecolor('#f6f9ff')
    ax.set_facecolor('#f6f9ff')

    # Plot the data
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Max Richter Scale')

    # Add labels and title
    plt.title("Maximum Richter Scale by Year")
    plt.xlabel("Year")
    plt.ylabel("Maximum Richter Scale")
    
    # Add grid lines for better readability
    plt.grid(True, linestyle='--', alpha=0.7)

    # Add legend
    plt.legend()

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Add data labels
    for i, txt in enumerate(y):
        plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 5), ha='center')

    # Ensure tight layout
    plt.tight_layout()

    # Get the graph as base64-encoded image
    graph = get_graph()

    return graph


def bar_plot(x, y):
    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(10, 5))

    # Set background color
    fig.set_facecolor('#f6f9ff')
    ax.set_facecolor('#f6f9ff')

    # Plot the bar graph
    plt.bar(x, y, color='b', alpha=0.7, label='Total Casualties')

    # Add labels and title
    plt.title("Total Casualties by Year")
    plt.xlabel("Year")
    plt.ylabel("Total Casualties")

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Add data labels
    for i, txt in enumerate(y):
        plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 5), ha='center')

    # Add grid lines for better readability
    plt.grid(axis='y', linestyle='', alpha=0.7)

    # Ensure tight layout
    plt.tight_layout()

    # Get the graph as base64-encoded image
    graph = get_graph()

    return graph
