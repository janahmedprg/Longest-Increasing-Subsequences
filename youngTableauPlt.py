import matplotlib.pyplot as plt

def draw_young_tableau(tableau, fontsize=16):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.patch.set_alpha(0)
    ax.set_axis_off()

    # Draw the Young tableau
    rows = len(tableau)
    for i in range(rows):
        row_length = len(tableau[i])
        for j in range(row_length):
            cell_text = tableau[i][j]
            square = plt.Rectangle((j, -i), 1, 1, facecolor='white', edgecolor='black')
            ax.add_patch(square)
            ax.text(j + 0.5, -i + 0.5, cell_text, va='center', ha='center', fontsize=fontsize)

    ax.autoscale_view()
    # plt.show()
    plt.savefig(f"youngTableau{tableau[0]}.png",dpi=600,transparent=True)

# Example usage
tableau = [
    [1,3],[2],[3]
]
draw_young_tableau(tableau, fontsize=40)
