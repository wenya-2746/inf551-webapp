from flask import *
from firebase import firebase
from flask_bootstrap import Bootstrap
from datetime import timedelta
from config import Config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'seanxiao'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
bootstrap = Bootstrap(app)

data = firebase.FirebaseApplication('https://inf551project-d9bd6.firebaseio.com', authentication=None)
data_lst = data.get('/', None)
for item1 in data_lst:
    item1['Amount in USD'] = float(item1['Amount in USD'])
labels = data_lst[0].keys()


@app.route('/')
def hello_world():
    return render_template('base.html', title=None)


# @app.route('/login')
# def login():
#     f = LoginForm()
#     return render_template('login.html', title='Sign in', form=f)


@app.route('/table', methods=['GET', 'POST'])
def table():
    table_lst, industry_vertical_dic = [], {}
    # retrieve the data;
    # get it for 8 chart
    data_date_dic = {"H1/16": 0, "H2/16": 0,
                     "H1/17": 0, "H2/17": 0,
                     "H1/18": 0, "H2/18": 0,
                     "H1/19": 0, "H2/19": 0}

    temp_date_dic = {"H1/16": 0, "H2/16": 0,
                     "H1/17": 0, "H2/17": 0,
                     "H1/18": 0, "H2/18": 0,
                     "H1/19": 0, "H2/19": 0}

    def add_to_date_dic(dic):
        result = ''
        date_lst = dic['Date ddmmyyyy'].split('/')
        result += 'H1' if 1 <= int(date_lst[1]) <= 6 else 'H2'
        result += '/{}'.format(date_lst[2][2:]) if len(date_lst) == 3 else '/{}'.format(date_lst[1][4:])
        return result
    for temp in data_lst:
        data_date_dic[add_to_date_dic(temp)] += 1

    if request.method == 'POST':
        count = 0
        lower_name, min_v, max_v = request.form['name'].lower(), (request.form['range-min']), (request.form['range-max'])
        min_v = float(min_v) if min_v != '' else 0
        max_v = float(max_v) if max_v != '' else 1.8446744e+19
        for item in data_lst:
            curr_name = item['Industry Vertical'].lower()
            if lower_name in curr_name and min_v <= item['Amount in USD'] <= max_v:
                table_lst.append(item)
                temp_date_dic[add_to_date_dic(item)] += 1
                if curr_name in industry_vertical_dic.keys():
                    industry_vertical_dic[curr_name] += 1
                else:
                    industry_vertical_dic[curr_name] = 1
                count += 1
        industry_vertical_lst = []
        for key, value in industry_vertical_dic.items():
            industry_vertical_lst.append([key, float(value) / count])
        print(industry_vertical_lst)
        return render_template('table.html', labels=labels, data_lst=table_lst,
                               industry_vertical_lst=industry_vertical_lst,
                               temp_date_dic=temp_date_dic,
                               data_date_dic=data_date_dic)
    count = 0
    for item in data_lst:
        curr_name = item['Industry Vertical'].lower()
        if curr_name in industry_vertical_dic.keys():
            industry_vertical_dic[curr_name] += 1
        else:
            industry_vertical_dic[curr_name] = 1
        count += 1
    industry_vertical_lst = []
    for key, value in industry_vertical_dic.items():
        industry_vertical_lst.append([key, float(value) / count])
    print(data_date_dic)
    return render_template('table.html', labels=labels, data_lst=data_lst, industry_vertical_lst=industry_vertical_lst,
                           temp_date_dic=data_date_dic,data_date_dic=data_date_dic)


if __name__ == '__main__':
    app.run(debug=True)
