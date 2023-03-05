from flask import Flask, request, jsonify
import json
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def handle_post():
    data = request.get_json() # assuming request body is in JSON format
    data = data.get('queryResult').get('parameters')
    print(data)
    msg = ""
    for x in data:
        if(not data[x]=='' and not data[x]==[]):
            msg+=x+" : "
            if(type(data[x])==list):
                msg+=" [ "
                for val in data[x]:
                    msg+=val + " "
                msg+=" ] "
            else:
                msg+=data[x]
    print(msg)
    res = {
        "fulfillmentText": f"{msg}",
        "source": "My Webhook"
    }
    # Return the response as a JSON object
    return jsonify(res)

if __name__ == 'main':
    app.run(debug=True,port=3000)
