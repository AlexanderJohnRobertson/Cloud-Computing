from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('awsarchitecturediagramsvg.html')

@app.route('/awsarchitecturediagramhtml')
def aws_architectural_diagram_html():
    return render_template('AWS Architectural Diagram.drawio.html')

@app.route('/cloudreadinessassessment')
def cloud_readiness_assessment():
    return render_template('cloudreadinessassessment.html')

@app.route('/ganttchart')
def gantt_chart():
    return render_template('ganttchart.html')

@app.route('/ganttchartdownload')
def gantt_chart_download():
    return render_template('ganttchartdownload.html')

if __name__ == '__main__':
    app.run()
