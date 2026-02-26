###         Question: JSON-Based API Response Processor          ###    
import json
json_response = '''{
          "id": "req_123",
          "status": "success",
          "result": {
                 "text": "Hello world",
                 "confidence": 0.98
  }
}
'''
data = json.loads(json_response)

print('Request ID:', data['id'])
print('Status:', data['status']) 
print('Text:', data['result']['text'])
print('Confidence:', data['result']['confidence'])

if data['result']['confidence'] < 0.9:
    print('Warning: Confidence is below 0.9')

follow_up_result = {
    "request_id": data['id'],
    "status": data['status'],
    "message": "Processed text: " + data['result']['text']
}
json_output = json.dumps(follow_up_result, indent=4)
with open('response.json', 'w') as f:
    json.dump(follow_up_result, f, indent=4)
