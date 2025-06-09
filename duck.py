import matplotlib.pyplot as plt

# Create an illustration of a baby duck
def draw_baby_duck():
    fig, ax = plt.subplots()

    # Body
    body = plt.Circle((0.5, 0.5), 0.3, color='yellow', ec='black')
    ax.add_patch(body)
    
    # Head
    head = plt.Circle((0.5, 0.75), 0.15, color='yellow', ec='black')
    ax.add_patch(head)
    
    # Eyes
    left_eye = plt.Circle((0.45, 0.8), 0.02, color='black')
    right_eye = plt.Circle((0.55, 0.8), 0.02, color='black')
    ax.add_patch(left_eye)
    ax.add_patch(right_eye)
    
    # Beak
    beak = plt.Polygon(((0.5, 0.75), (0.6, 0.72), (0.5, 0.7)), color='orange', ec='black')
    ax.add_patch(beak)
    
    # Legs
    left_leg = plt.Line2D([0.45, 0.45], [0.2, 0.3], color='orange', lw=2)
    right_leg = plt.Line2D([0.55, 0.55], [0.2, 0.3], color='orange', lw=2)
    ax.add_line(left_leg)
    ax.add_line(right_leg)
    
    # Wing
    wing = plt.Polygon(((0.4, 0.5), (0.6, 0.5), (0.5, 0.65)), color='yellow', ec='black')
    ax.add_patch(wing)

    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

draw_baby_duck()
