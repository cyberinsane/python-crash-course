"""
Scripting:
- Getting response from API
- JSON to CSV
- JSON to Excel
- Plotting graphs

Install requests
$ pip3 install requests

Install matplotlib - Graph plotting library
$ pip3 install matplotlib

Install pandas - Highly optimized data analysis & manipulation tool
$ pip3 install pandas

"""

import matplotlib.pyplot as plt
import json
import pandas
import requests


def get_expenses():
    response = requests.get('http://0.0.0.0:8000/expenses')
    # print(f"Status Code: {response.status_code}")
    # print(f"Content: {response.content}")
    return response.content


# Pandas to convert to csv
def convert_to_csv():
    pandas.read_json(get_expenses()).to_csv('expenses.csv', index=False)


# Pandas to convert to  xlsx
def convert_to_excel():
    pandas.read_json(get_expenses()).to_excel('expenses.xlsx', index=False)


# Plot monthly expenses in a pie chart
def plot_pie_chart():
    expenses_dict = get_monthly_expenses()

    labels = expenses_dict.keys()
    values = expenses_dict.values()

    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, autopct='%1.1f%%')
    plt.show()


# Plot monthly expenses in bar chart
def plot_bar_chart():
    expenses_dict = get_monthly_expenses()

    labels = expenses_dict.keys()
    values = expenses_dict.values()

    y_pos = range(len(labels))
    plt.bar(y_pos, values, align='center')
    plt.xticks(y_pos, labels)
    plt.ylabel('Expenditure')
    plt.title('Monthly Expense')
    plt.show()


def get_monthly_expenses():
    info_dic = {}
    data = json.loads(get_expenses())
    for item in data:
        month = item['month'].lower()
        if month in info_dic.keys():
            info_dic[month] = info_dic[month] + item['amount']
        else:
            info_dic[month] = item['amount']
    return info_dic