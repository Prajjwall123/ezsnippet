import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib
matplotlib.use('agg')


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image = buffer.getvalue()
    graph = base64.b64encode(image)
    graph = graph.decode('utf-8')
    buffer.close()
    plt.close()  # Close the matplotlib figure

    return graph

def plot(x, y):
    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(10, 5))

    # Set background color
    fig.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Plot the data
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Max Richter Scale')

    # Add labels and title
    # plt.title("Maximum Richter Scale by Year")
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
    fig.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Plot the bar graph
    plt.bar(x, y, color='b', alpha=0.7, label='Total Casualties')

    # Add labels and title
    # plt.title("Total Casualties by Year")
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


def plot_pie(data):
    # Set the background color
    plt.figure(figsize=(10, 4.5), facecolor='#ffffff')  # Set the figure size and facecolor

    labels = data.keys()
    values = data.values()

    plt.pie(values,autopct='%1.1f%%')
    plt.legend(title='Causes', labels=labels, loc='upper right')  # Adds a legend with customer type labels 
    plt.axis('equal')
    graph = get_graph()

    return graph


def flood_plot(x, y):
    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(8, 5))

    # Set background color
    fig.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Plot the data
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Min Rainfall')

    # Add labels and title
    # plt.title("Minimum Rainfall that caused Flood")
    plt.xlabel("Year")
    plt.ylabel("Minimum Rainfalls")
    
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


def glof_plot(x, y):
    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(9, 4))

    # Set background color
    fig.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Plot the data
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Max Richter Scale')

    # Add labels and title
    # plt.title("Maximum Richter Scale by Year")
    plt.xlabel("Year")
    plt.ylabel("Minimum Water Level")
    
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