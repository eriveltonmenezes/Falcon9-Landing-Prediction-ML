import matplotlib.pyplot as plt
import numpy as np

# 1. Define the data for the chart
# Model names (extracted from your printout)
models = ['Logistic Regression', 'Support Vector Machine', 'Decision Tree', 'K-Nearest Neighbors']

# Best accuracies (extracted from your printout - using the exact values from the previous step)
accuracies = [
    0.846285714285713, # logreg_score
    0.8482142857142856, # svm_score
    0.8875, # tree_score
    0.8482142857142858  # knn_score
]

# 2. Create the plot
plt.figure(figsize=(12, 6)) # Defines the figure size
bars = plt.bar(models, accuracies, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])

# 3. Add title and labels
plt.title('Comparison of Classification Model Accuracy', fontsize=16)
plt.xlabel('Model', fontsize=14)
plt.ylabel('Accuracy Score', fontsize=14)
plt.ylim(min(accuracies) - 0.01, 0.90) # Adjusts the Y-axis limit for better visualization

# 4. Add the accuracy value on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.001, f'{yval:.4f}', ha='center', va='bottom', fontsize=12)

# 5. Highlight the bar with the highest accuracy
best_index = np.argmax(accuracies)
bars[best_index].set_color('lightgreen')
bars[best_index].set_edgecolor('lightgreen')

# 6. Display the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=15) # Rotates model names for better readability
plt.tight_layout()
plt.show()
