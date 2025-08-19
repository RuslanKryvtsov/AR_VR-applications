from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/immersive_world')
def cloning_methods():
    return render_template('immersive_world.html')

@app.route('/skill_set')
def ai_tools():
    return render_template('skill_set.html')

@app.route('/development_workflow')
def creative_projects():
    return render_template('development_workflow.html')

@app.route('/inside_AR_VR_technology')
def sites_ar():
    return render_template('inside_AR_VR_technology.html')   

@app.route('/creative_projects')
def coffeetime_intro():
    return render_template('creative_projects.html')
  

if __name__ == '__main__':
    app.run(debug=True, port=8080)
