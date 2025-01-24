from flask import Flask, request, render_template_string, send_from_directory, jsonify
import os
import subprocess

app = Flask(__name__)

# Diretórios
UPLOAD_FOLDER = 'uploads'
BUILD_FOLDER = 'tmp'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BUILD_FOLDER, exist_ok=True)

# Contador global para arquivos
file_counter = 0

# Página HTML
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>C Compiler Server</title>
    <style>
        body {
            background-color: yellow;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <h1>Upload a C File</h1>
    <form method="post" action="/upload" enctype="multipart/form-data">
        <input type="file" name="cfile" accept=".c" required />
        <button type="submit">Upload and Compile</button>
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/upload', methods=['POST'])
def upload_file():
    global file_counter

    # Verificar e salvar o arquivo enviado
    if 'cfile' not in request.files:
        return "No file part", 400

    file = request.files['cfile']
    if file.filename == '':
        return "No selected file", 400

    if not file.filename.endswith('.c'):
        return "Only .c files are allowed", 400

    # Salvar o arquivo
    c_file_path = os.path.join(UPLOAD_FOLDER, str(file_counter)+".c")
    file.save(c_file_path)

    # Nome do executável
    executable_name = f"{file_counter}.iso"
    executable_path = os.path.join(BUILD_FOLDER, executable_name)

    # Executar build.sh com o contador como argumento
    try:
        subprocess.run(['./starts.sh', str(file_counter)], check=True)  # Executa o script starts.sh

        result = subprocess.run(
            ['./build.sh', str(file_counter)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.getcwd()
        )
        subprocess.run(['./ends.sh', str(file_counter)], check=True)  # Executa o script starts.sh
        # Incrementar o contador
        file_counter += 1

        # Gravar o executável temporário
        if 0==0:
            return jsonify({
                'stdout': result.stdout,
                'stderr': result.stderr,
                'download_url': f'/download/{executable_name}'
            })
        else:
            return jsonify({'error': 'Compilation failed', 'stderr': result.stderr}), 400

    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Script execution failed', 'details': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(BUILD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
