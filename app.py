from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/arlogicmap')
def ar_logic_map():
    return render_template('ARlogicMap.html')

@app.route('/architecture')
def architecture_map():
    return render_template('architectureAR.html')   

@app.route('/unity')
def unity_map():
    return render_template('unity.html')   

@app.route('/blender')
def blender_map():
    return render_template('blender.html')  

@app.route('/guide_AR_VR_apps_creation')
def guide_map():
    return render_template('guide_AR_VR_apps_creation.html')  

@app.route('/unityhub_unityeditor_plagins')
def unityhub_map():
    return render_template('unityhub_unityeditor_plagins.html')      
 
@app.route('/ar_vr_devices')
def ar_vr_devices_map():
    return render_template('ar_vr_devices.html') 

@app.route('/rayban_firmware')
def rayban_firmware_map():
    return render_template('rayban_firmware.html') 

@app.route('/applevisionpro_software')
def applevisionpro_software_map():
    return render_template('applevisionpro_software.html')  

@app.route('/ar_vr_examples')       
def ar_vr_examples_map():       
    return render_template('ar_vr_examples.html')   

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
