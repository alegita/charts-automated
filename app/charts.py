import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()
    
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'./imgs/charts-pie.png')
    plt.close()
    
if __name__ == '__main__':
    labels = ['A','B','C']
    values = [10, 40, 800]
    generate_pie_chart(labels, values)