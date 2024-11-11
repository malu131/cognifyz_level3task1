import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Function to load the dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Function for Matplotlib visualization
def plot_matplotlib(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Sales'], marker='o', label='Sales', color='blue')
    plt.plot(data['Date'], data['Profit'], marker='o', label='Profit', color='orange')
    plt.title('Sales and Profit over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Function for Seaborn visualization
def plot_seaborn(data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='Date', y='Sales', label='Sales', color='blue', marker='o')
    sns.lineplot(data=data, x='Date', y='Profit', label='Profit', color='orange', marker='o')
    plt.title('Sales and Profit over Time (Seaborn)')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Function for Plotly visualization
def plot_plotly(data):
    fig = px.line(data, x='Date', y='Sales', title='Sales and Profit over Time')
    fig.add_scatter(x=data['Date'], y=data['Profit'], mode='lines', name='Profit', line=dict(color='orange'))
    fig.update_layout(title='Sales and Profit over Time (Plotly)', xaxis_title='Date', yaxis_title='Amount')
    fig.show()

# Main function to execute the tool
def main():
    file_path = 'C:/Users/Malu/PycharmProjects/DataVisualizationTool/custom_dataset.csv'  # Make sure this matches the path where you saved the CSV
    data = load_data(file_path)

    print("Choose a visualization:")
    print("1. Matplotlib")
    print("2. Seaborn")
    print("3. Plotly")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        plot_matplotlib(data)
    elif choice == '2':
        plot_seaborn(data)
    elif choice == '3':
        plot_plotly(data)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
