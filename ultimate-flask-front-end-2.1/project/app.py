from flask import Flask, request, render_template
import collaborative_filtering_handler

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    performance_svd = []
    performance_nmf = []
    performance_als = []
    performance_sgd = []
    performance_knn = []
    if request.method == 'POST':
        if 'predict' in request.form:
            print("Request successful")
            user_id = request.form.get('user_id')
            print(user_id)
            performance_svd = collaborative_filtering_handler.use_svd()
            performance_knn = collaborative_filtering_handler.use_knn()
            performance_als = collaborative_filtering_handler.use_als()
            performance_sgd = collaborative_filtering_handler.use_sgd()
            performance_nmf = collaborative_filtering_handler.use_nmf()
            # predictions = collaborative_filtering_handler.make_predictions(user_id)

    return render_template('index.html', performance_svd=performance_svd, performance_knn=performance_knn,
                           performance_als=performance_als, performance_sgd=performance_sgd,
                           performance_nmf=performance_nmf)


@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
