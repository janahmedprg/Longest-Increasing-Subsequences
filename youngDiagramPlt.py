import matplotlib.pyplot as plt

def draw_young_diagram(shape):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_axis_off()

    # Draw the Young diagram
    for i in range(len(shape)):
        for j in range(shape[i]):
            square = plt.Rectangle((j, -i), 1, 1, facecolor='white', edgecolor='black')
            ax.add_patch(square)

    ax.autoscale_view()
    # plt.show()
    plt.savefig(f"youngDiagram{shape}.png",dpi=600,transparent=True)

# Example usage
shape = [5, 3, 3,1]
draw_young_diagram(shape)
