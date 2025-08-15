#!/usr/bin/env python3
"""
Portfolio Application Test Suite
Comprehensive testing for all components and links
"""

import os
import sys
import time
import requests
import threading
from pathlib import Path
from urllib.parse import urljoin
import subprocess
import signal

class PortfolioTester:
    def __init__(self):
        self.base_url = "http://localhost:5000"
        self.server_process = None
        self.test_results = []
        
    def log_result(self, test_name, success, message=""):
        """Log test result"""
        status = "✅ PASS" if success else "❌ FAIL"
        self.test_results.append((test_name, success, message))
        print(f"{status}: {test_name}")
        if message:
            print(f"    {message}")
    
    def start_server(self):
        """Start the Flask server in background"""
        print("🚀 Starting Flask server...")
        try:
            # Try modular app first
            if Path("app/__init__.py").exists():
                cmd = [sys.executable, "-c", "from app import create_app; app = create_app(); app.run(debug=False, host='0.0.0.0', port=5000)"]
            else:
                cmd = [sys.executable, "app.py"]
            
            self.server_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid if os.name != 'nt' else None
            )
            
            # Wait for server to start
            time.sleep(5)
            
            # Test if server is running
            try:
                response = requests.get(self.base_url, timeout=5)
                print("✅ Server started successfully")
                return True
            except requests.exceptions.RequestException:
                print("❌ Server failed to start properly")
                return False
                
        except Exception as e:
            print(f"❌ Failed to start server: {e}")
            return False
    
    def stop_server(self):
        """Stop the Flask server"""
        if self.server_process:
            print("\n🛑 Stopping Flask server...")
            try:
                if os.name == 'nt':  # Windows
                    self.server_process.terminate()
                else:  # Unix
                    os.killpg(os.getpgid(self.server_process.pid), signal.SIGTERM)
                self.server_process.wait(timeout=5)
                print("✅ Server stopped")
            except Exception as e:
                print(f"⚠️  Error stopping server: {e}")
    
    def test_home_page(self):
        """Test home page"""
        try:
            response = requests.get(self.base_url, timeout=10)
            success = response.status_code == 200
            self.log_result("Home Page", success, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_result("Home Page", False, str(e))
            return False
    
    def test_chatbot_page(self):
        """Test chatbot page"""
        try:
            url = urljoin(self.base_url, "/chat")
            response = requests.get(url, timeout=10)
            success = response.status_code == 200
            self.log_result("Chatbot Page", success, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_result("Chatbot Page", False, str(e))
            return False
    
    def test_narrative_nexus(self):
        """Test Narrative Nexus page"""
        try:
            url = urljoin(self.base_url, "/narrative")
            response = requests.get(url, timeout=10)
            success = response.status_code == 200
            self.log_result("Narrative Nexus", success, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_result("Narrative Nexus", False, str(e))
            return False
    
    def test_api_endpoints(self):
        """Test API endpoints"""
        # Test that API blueprint is registered by checking for 405 on GET to POST-only endpoint
        try:
            url = urljoin(self.base_url, "/api/chat")
            response = requests.get(url, timeout=10)
            # Should return 405 Method Not Allowed since chat endpoint only accepts POST
            success = response.status_code == 405
            status_msg = "Method Not Allowed (Expected)" if success else f"Unexpected Status: {response.status_code}"
            self.log_result("API Blueprint Registration", success, status_msg)
        except Exception as e:
            self.log_result("API Blueprint Registration", False, str(e))
    
    def test_ai_chat(self):
        """Test AI chat functionality"""
        try:
            url = urljoin(self.base_url, "/api/chat")
            data = {"message": "Hello, can you write a short poem about coding?"}
            response = requests.post(url, json=data, timeout=15)
            
            if response.status_code == 200:
                result = response.json()
                success = "response" in result and len(result["response"]) > 0
                message = f"Response length: {len(result.get('response', ''))}"
            else:
                success = False
                message = f"Status: {response.status_code}"
            
            self.log_result("AI Chat", success, message)
            return success
        except Exception as e:
            self.log_result("AI Chat", False, str(e))
            return False
    
    def test_project_pages(self):
        """Test individual project pages"""
        project_slugs = [
            "american-sign-detection",
            "cmarl-thesis", 
            "crude-oil-prediction",
            "crypto-app",
            "data-augmentation",
            "divine-insights",
            "ecommerce-data-analysis"
        ]
        
        for slug in project_slugs:
            try:
                url = urljoin(self.base_url, f"/project/{slug}")
                response = requests.get(url, timeout=10)
                success = response.status_code == 200
                self.log_result(f"Project: {slug}", success, f"Status: {response.status_code}")
            except Exception as e:
                self.log_result(f"Project: {slug}", False, str(e))
    
    def test_static_files(self):
        """Test static file accessibility"""
        static_files = [
            "/static/css/style.css",
            "/static/images/logo-portfolio.png"
        ]
        
        for file_path in static_files:
            try:
                url = urljoin(self.base_url, file_path)
                response = requests.get(url, timeout=10)
                success = response.status_code == 200
                self.log_result(f"Static: {file_path}", success, f"Status: {response.status_code}")
            except Exception as e:
                self.log_result(f"Static: {file_path}", False, str(e))
    
    def test_content_loading(self):
        """Test content loading from files"""
        content_files = [
            "content/poems",
            "Poems.txt"
        ]
        
        for file_path in content_files:
            exists = Path(file_path).exists()
            self.log_result(f"Content: {file_path}", exists, 
                           "Found" if exists else "Missing")
    
    def run_all_tests(self):
        """Run all tests"""
        print("🧪 Starting Portfolio Application Tests")
        print("=" * 50)
        
        # Start server
        if not self.start_server():
            print("❌ Cannot run tests - server failed to start")
            return False
        
        try:
            # Run tests
            print("\n📄 Testing Pages...")
            self.test_home_page()
            self.test_chatbot_page() 
            self.test_narrative_nexus()
            
            print("\n🔌 Testing API Endpoints...")
            self.test_api_endpoints()
            self.test_ai_chat()
            
            print("\n📁 Testing Project Pages...")
            self.test_project_pages()
            
            print("\n🎨 Testing Static Files...")
            self.test_static_files()
            
            print("\n📚 Testing Content Loading...")
            self.test_content_loading()
            
        finally:
            # Stop server
            self.stop_server()
        
        # Print results summary
        self.print_summary()
        
        return True
    
    def print_summary(self):
        """Print test results summary"""
        print("\n" + "=" * 50)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 50)
        
        passed = sum(1 for _, success, _ in self.test_results if success)
        total = len(self.test_results)
        failed = total - passed
        
        print(f"Total Tests: {total}")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"Success Rate: {(passed/total)*100:.1f}%")
        
        if failed > 0:
            print("\n❌ Failed Tests:")
            for test_name, success, message in self.test_results:
                if not success:
                    print(f"   - {test_name}: {message}")
        
        print("\n" + "=" * 50)
        
        if failed == 0:
            print("🎉 All tests passed! Your portfolio is ready to go!")
        elif failed <= 3:
            print("⚠️  Most tests passed. Check failed tests above.")
        else:
            print("❌ Many tests failed. Check your setup and configuration.")

def main():
    """Main test function"""
    print("Portfolio Application Test Suite")
    print("Testing all components and functionality")
    print()
    
    # Check if we're in the right directory
    if not (Path("app.py").exists() or Path("app/__init__.py").exists()):
        print("❌ Error: app.py or app/ directory not found")
        print("Make sure you're running this from the portfolio directory")
        return False
    
    tester = PortfolioTester()
    
    try:
        return tester.run_all_tests()
    except KeyboardInterrupt:
        print("\n\n👋 Tests interrupted by user")
        tester.stop_server()
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        tester.stop_server()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
