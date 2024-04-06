from flask import Flask, render_template, request, jsonify,url_for
import subprocess  
  
app = Flask(__name__,template_folder='templates',static_folder = 'static') 
# app.static_folder = 'static'  
  
@app.route('/')  
def index():  
    return render_template('index.html')  

@app.route('/execute_command', methods=['POST'])  
def execute_command():  
    command = request.json["command"]
    print(command)
    print(type(command))
    try:
        # 执行命令并获取输出
        result = subprocess.run(command,shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to service: {e}")
    # return jsonify({"status": "success"})
    return str(result)
@app.route('/check', methods=['POST']) 
def check_service_state():
    service_name = request.json["service_name"]
    # 运行sc query命令
    result = subprocess.run(['sc', 'query', service_name], stdout=subprocess.PIPE, text=True)
    # 使用正则表达式解析输出以获取state值
    import re
    state_match = re.search(r'STATE\s+:\s+(.*)', result.stdout, re.IGNORECASE)
    if state_match:
        return state_match.group(1)
    else:
        return "Unknown"

if __name__ == '__main__':
    # app.config['SERVER_NAME'] = '0.0.0.0'  
    # app.run(debug=True, port=8080)
    app.run(debug=True,port=8080,host='0.0.0.0')