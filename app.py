from flask import Flask, render_template
import pandas as pd
from flask import jsonify

app = Flask(__name__)

# Section 1
# Sequence
def generate_sequence(n):
    """
    Method to generate the sequence by taking integer input and return a list of elemements
    :param n:
    :return: sequence
    """
    sequence = []
    while (n != 1):
        sequence.append(n)
        # if n is even
        if (n % 2 == 0):
            n = n // 2
        else:
            # if n is odd
            n = (3 * n) + 1
    sequence.append(1)  # print 1 in the end
    return sequence

@app.route("/sequence/elem/<n>")
def get_sequence(n):
    """
    Method to return a sequence
    :param n:
    :return: sequence
    """
    try:
        sequence = generate_sequence(int(n))
        sequence = [str(i) for i in sequence]
        sequence = " -> ".join(sequence)
        return jsonify({"status": 0,
                        "message": "Success",
                        "data": sequence})
    except:
        return jsonify({"status": -1,
                        "message": "Please provide integer value as input.",
                        "data": []})

@app.route("/sequence/longest/<n>")
def get_max_sequence(n):
    """
    Method to return
    :param n:
    :return:
    """
    try:
        sequence_len = {}
        for i in range(1, int(n) + 1):
            sequence_len[i] = len(generate_sequence(i))
        # get the number with longest sequence and less than n
        longest_sequence = max(sequence_len, key=sequence_len.get)
        return jsonify({"status": 0,
                        "message": "Success",
                        "data": longest_sequence})
    except:
        return jsonify({"status": -1,
                        "message": "Please provide integer value as input.",
                        "data": []})

# Section 2
# Iris and Pandas
def read_csv():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
    try:
        data = pd.read_csv(url, sep=",")  # use sep="," for coma separation.
    except Exception as e:
        data = pd.DataFrame()
    return data

@app.route("/iris/group/sepal_length/<max>")
def iris_get_max_sepal_len(max):
    """
    :param max:
    :return:
    """
    # get the number with longest sequence and less than n
    if not isinstance(max.strip().isdigit(), (int, float)):
        return jsonify({"status": -1,
                        "message": "Please provide integer or float value as input.",
                        "data": []})
    df = read_csv()
    if not df.empty:
        df = df[df['sepal_length'] <= float(max)]
        out = df.sort_values(['species', 'sepal_length'], ascending=True).groupby('species').tail(1)
        return render_template('iris.html', tables=[out.to_html(classes='data')], titles="")
    else:
        return jsonify({"status": -2,
                        "message": "Failed to read iris csv file.",
                        "data": ""})

@app.route("/iris/describe")
def iris_describe():
    """
    :return:
    """
    df = read_csv()
    if not df.empty:
        out = df.describe()
        return render_template('iris.html', tables=[out.to_html(classes='data')], titles=out.columns.values)
    else:
        return jsonify({"status": -2,
                        "message": "Failed to read iris csv file.",
                        "data": None})


if __name__ == "__main__":
    app.run(debug=True)