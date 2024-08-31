from flask import Flask, request, jsonify, render_template
from skills import file_io, workflow_management, openai_api_call
import os

app = Flask(__name__)

# Load configuration
config = file_io.read_yaml('config.yaml')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invoke_workflow', methods=['POST'])
def invoke_workflow():
    data = request.json
    template_name = data.get('template_name')
    variables = data.get('variables')

    # Load template and apply variables
    template_path = os.path.join(config['templates_dir'], f"{template_name}.yaml")
    template = file_io.read_yaml(template_path)
    prompt = template['template_content'].format(**variables)

    # Execute workflow based on the prompt
    response = workflow_management.execute_workflow([lambda: openai_api_call(prompt)])
    return jsonify(response)

# CRUM endpoints for managing templates, variables, and chat history
@app.route('/templates', methods=['GET', 'POST'])
def manage_templates():
    if request.method == 'POST':
        template = request.json
        file_path = os.path.join(config['templates_dir'], f"{template['template_name']}.yaml")
        file_io.write_yaml(file_path, template)
        return jsonify({"status": "Template added/updated successfully"})
    else:
        templates = [f for f in os.listdir(config['templates_dir']) if f.endswith('.yaml')]
        return jsonify(templates)

@app.route('/variables', methods=['GET', 'POST'])
def manage_variables():
    if request.method == 'POST':
        variables = request.json
        file_path = os.path.join(config['variables_dir'], f"{variables['name']}.yaml")
        file_io.write_yaml(file_path, variables)
        return jsonify({"status": "Variables added/updated successfully"})
    else:
        variables = [f for f in os.listdir(config['variables_dir']) if f.endswith('.yaml')]
        return jsonify(variables)

@app.route('/chat_history', methods=['GET', 'POST'])
def manage_chat_history():
    if request.method == 'POST':
        chat_history = request.json
        file_path = os.path.join(config['chat_history_dir'], f"{chat_history['name']}.yaml")
        file_io.write_yaml(file_path, chat_history)
        return jsonify({"status": "Chat history added/updated successfully"})
    else:
        history_files = [f for f in os.listdir(config['chat_history_dir']) if f.endswith('.yaml')]
        return jsonify(history_files)

@app.route('/tools_and_skills', methods=['POST'])
def add_tool_or_skill():
    data = request.json
    file_name = data.get('file_name')
    content = data.get('content')
    directory = data.get('directory')

    if directory not in ['skills', 'tools']:
        return jsonify({"error": "Invalid directory specified"}), 400

    file_path = os.path.join(directory, f"{file_name}.py")
    file_io.write_file(file_path, content)
    return jsonify({"status": f"{file_name} added/updated successfully in {directory}"})

if __name__ == '__main__':
    app.run(debug=True)
