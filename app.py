from flask import Flask, render_template, request  # 导入 Flask 应用类和模板、请求模块。
import textblob
import google.generativeai as genai
import os

# api='AIzaSyDjtmA1IGXdw6YrGZp_dEFUYDzfLCAbDPQ'
api=os.getenv('makersuite')
model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key=api)

app = Flask(__name__)  # 创建一个 Flask 应用实例

@app.route("/", methods=['GET', 'POST']) #定义一个路由，将根 URL / 绑定到 index 函数，并允许 GET 和 POST 请求。
def index():
    return(render_template('index.html'))  # 定义 index 函数，当访问根路径时，渲染并返回 index.html 模板。

@app.route("/main",methods=["GET","POST"])
def main():
    name=request.form.get("q")
    return(render_template('main.html'))

@app.route("/SA", methods=['GET', 'POST']) 
def SA():
    return(render_template('SA.html'))

@app.route("/SA_result", methods=['GET', 'POST']) 
def SA_result():
    q=request.form.get("q")
    r=textblob.TextBlob(q).sentiment
    return(render_template('SA_result.html',r=r))

@app.route("/GenAI", methods=['GET', 'POST']) 
def GenAI():
    return(render_template('GenAI.html'))

@app.route("/GenAI_result", methods=['GET', 'POST']) 
def GenAI_result():
    q=request.form.get("q")
    r = model.generate_content(q)
    return(render_template('GenAI_result.html',r=r.candidates[0].content.parts[0].text))

@app.route("/paynow", methods=['GET', 'POST']) 
def paynow():
    return(render_template('paynow.html'))

if __name__=='__main__':
    app.run()

