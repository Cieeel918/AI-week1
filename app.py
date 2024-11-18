from flask import Flask, render_template, request  # 导入 Flask 应用类和模板、请求模块。

app = Flask(__name__)  # 创建一个 Flask 应用实例

@app.route("/", methods=['GET', 'POST']) #定义一个路由，将根 URL / 绑定到 index 函数，并允许 GET 和 POST 请求。
def index():
    return(render_template('index.html'))  # 定义 index 函数，当访问根路径时，渲染并返回 index.html 模板。

@app.route("/main",methods=["GET","POST"])
def main():
    name=request.form.get("q")
    return(render_template('main.html'))

if __name__=='__main__':
    app.run()

