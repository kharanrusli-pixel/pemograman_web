from flask import Flask, render_template_string

app = Flask(__name__)
no_1_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>No 1 - Responsive Box Layout</title>
    <style>
        body { margin: 0; font-family: Arial, sans-serif; }
        .container {
            display: flex;
            justify-content: flex-start;   
            align-items: flex-start;      
            height: 100vh;
            gap: 20px;
            padding: 20px;
        }
        .box {
            width: 200px;
            height: 200px;
            background-color: white;      
            color: black;                 
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            border-radius: 8px;
            border: 2px solid black;      
        }
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
                align-items: flex-start;
            }
            .box {
                width: 150px;
                height: 150px;
                border: 2px solid black;  
            }
            .box:nth-child(1) { background-color: red; margin-left: 0px; }
            .box:nth-child(2) { background-color: yellow; margin-left: 200px; }
            .box:nth-child(3) { background-color: green; margin-left: 400px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
    </div>
</body>
</html>
"""

no_2_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>No 2 - Responsive Box Layout</title>
    <style>
        body { margin:0; font-family: Arial,sans-serif; min-height: 200vh; }
        .container {
            display: flex;
            justify-content: center;   
            align-items: center;
            gap: 20px;
            padding: 20px;
            width: 100%;
            background-color: #f5f5f5;
            position: fixed;   
            bottom: 0;         
            left: 0;
        }
        .box {
            width: 200px;
            height: 200px;
            background-color: white;   
            color: black;                 
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            border-radius: 8px;
            border: 2px solid black;      
        }
        @media (max-width: 768px) {
            .container { flex-direction: column; align-items: center; }
            .box { width: 150px; height: 150px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box">3</div>
    </div>
</body>
</html>
"""

no_3_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>No 3 - Responsive Box Layout</title>
    <style>
        body { margin:0; font-family: Arial,sans-serif; min-height: 200vh; }
        .container {
            display: flex;
            justify-content: center;   
            align-items: center;
            gap: 20px;
            padding: 20px;
            width: 100%;
            background-color: #f5f5f5;
            position: fixed;   
            top: 0;         
            left: 0;
        }
        .box {
            width: 200px;
            height: 200px;
            background-color: white;   
            color: black;                 
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            border-radius: 8px;
            border: 2px solid black;      
        }
        @media (max-width: 768px) {
            .container { flex-direction: column; align-items: center; }
            .box { width: 150px; height: 150px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
    </div>
</body>
</html>
"""

no_4_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    html, body { margin:0; padding:0; height:100%; background:#fff; overflow-x:hidden; overflow-y:scroll; }
    .scroll-container {
        height: 10000vh; 
        display: flex;
        flex-direction: column;
        align-items: flex-end; 
        position: relative;
    }
    .sticky-box-group {
        position: sticky;
        top: 50vh; 
        transform: translateY(-50%); 
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        padding-right: 10px;
        margin-top: 440px; 
    }
    .box {
        width: 100px;
        height: 100px;
        margin-bottom: 20px; 
        background-color: rgb(126, 7, 205);   
        border-radius: 5px;
        flex-shrink: 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        font-weight: bold;
        transition: transform 0.3s ease-out, opacity 0.3s ease;
    }
</style>
</head>
<body>
    <div class="scroll-container">
        <div class="sticky-box-group">
            <div class="box"></div>
            <div class="box"></div>
            <div class="box"></div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return """
    <h1>Menu Halaman</h1>
    <ul>
        <li><a href="/no_1">monitor 1</a></li>
        <li><a href="/no_2">monitor 2</a></li>
        <li><a href="/no_3">monitor 3</a></li>
        <li><a href="/no_4">monitor 4</a></li>
    </ul>
    """

@app.route('/no_1')
def no_1():
    return render_template_string(no_1_html)

@app.route('/no_2')
def no_2():
    return render_template_string(no_2_html)

@app.route('/no_3')
def no_3():
    return render_template_string(no_3_html)

@app.route('/no_4')
def no_4():
    return render_template_string(no_4_html)

if __name__ == '__main__':
    app.run(debug=True)