#!/usr/bin/env python3
import sys
import os

print("Testing Flask app...")

try:
    from app import app
    print("✅ Flask app imported successfully")
    
    # Test if all required templates exist
    template_files = ['index.html', 'chatbot.html', 'project_detail.html']
    for template in template_files:
        template_path = os.path.join('templates', template)
        if os.path.exists(template_path):
            print(f"✅ Template {template} exists")
        else:
            print(f"❌ Template {template} missing")
    
    # Test routes
    with app.test_client() as client:
        print("Testing routes...")
        
        # Test home route
        response = client.get('/')
        print(f"Home route status: {response.status_code}")
        
        # Test chatbot route
        response = client.get('/chatbot')
        print(f"Chatbot route status: {response.status_code}")
        
        # Test API chat route
        response = client.post('/api/chat', 
                              json={'message': 'hello'},
                              content_type='application/json')
        print(f"API chat route status: {response.status_code}")
        if response.status_code == 200:
            print(f"API response: {response.get_json()}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("Test complete!")
