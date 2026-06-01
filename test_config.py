# Test script for Music Bot configuration
import os
import sys
from dotenv import load_dotenv

def test_configuration():
    """Test if all configurations are set up correctly"""
    
    print("🔍 Testing Music Bot Configuration\n")
    
    # Load environment variables
    load_dotenv()
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Check .env file
    print("1. Checking .env file...")
    if os.path.exists('.env'):
        print("   ✅ .env file found")
        tests_passed += 1
    else:
        print("   ❌ .env file not found")
        print("   → Copy .env.example to .env and fill in your credentials")
        tests_failed += 1
    
    # Test 2: Check API_ID
    print("\n2. Checking API_ID...")
    api_id = os.getenv('API_ID', '')
    if api_id and api_id != '0':
        print("   ✅ API_ID is set")
        tests_passed += 1
    else:
        print("   ❌ API_ID not set or invalid")
        tests_failed += 1
    
    # Test 3: Check API_HASH
    print("\n3. Checking API_HASH...")
    api_hash = os.getenv('API_HASH', '')
    if api_hash:
        print("   ✅ API_HASH is set")
        tests_passed += 1
    else:
        print("   ❌ API_HASH not set")
        tests_failed += 1
    
    # Test 4: Check BOT_TOKEN
    print("\n4. Checking BOT_TOKEN...")
    bot_token = os.getenv('BOT_TOKEN', '')
    if bot_token:
        print("   ✅ BOT_TOKEN is set")
        tests_passed += 1
    else:
        print("   ❌ BOT_TOKEN not set")
        tests_failed += 1
    
    # Test 5: Check OWNER_ID
    print("\n5. Checking OWNER_ID...")
    owner_id = os.getenv('OWNER_ID', '')
    if owner_id and owner_id != '0':
        print("   ✅ OWNER_ID is set")
        tests_passed += 1
    else:
        print("   ❌ OWNER_ID not set")
        tests_failed += 1
    
    # Test 6: Check FFmpeg
    print("\n6. Checking FFmpeg...")
    result = os.system('ffmpeg -version > /dev/null 2>&1')
    if result == 0:
        print("   ✅ FFmpeg is installed")
        tests_passed += 1
    else:
        print("   ❌ FFmpeg not found")
        print("   → Install with: sudo apt-get install ffmpeg")
        tests_failed += 1
    
    # Test 7: Check Python packages
    print("\n7. Checking Python packages...")
    try:
        import pyrogram
        import pymongo
        import yt_dlp
        print("   ✅ All required packages are installed")
        tests_passed += 1
    except ImportError as e:
        print(f"   ❌ Missing package: {str(e)}")
        print("   → Install with: pip install -r requirements.txt")
        tests_failed += 1
    
    # Test 8: Check MongoDB
    print("\n8. Checking MongoDB...")
    try:
        from pymongo import MongoClient
        mongo_uri = os.getenv('MONGO_DB_URI', 'mongodb://localhost:27017')
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
        client.admin.command('ping')
        print("   ✅ MongoDB is accessible")
        tests_passed += 1
    except Exception as e:
        print("   ⚠️  MongoDB not accessible")
        print(f"   → Error: {str(e)}")
        print("   → Start MongoDB with: docker run -d -p 27017:27017 mongo")
        tests_failed += 1
    
    # Test 9: Check directories
    print("\n9. Checking directories...")
    dirs = ['downloads', 'logs']
    all_exist = True
    for dir_name in dirs:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
    print("   ✅ All directories created")
    tests_passed += 1
    
    # Summary
    print("\n" + "="*50)
    print("📊 Test Summary")
    print("="*50)
    print(f"✅ Tests Passed: {tests_passed}")
    print(f"❌ Tests Failed: {tests_failed}")
    print(f"📈 Success Rate: {(tests_passed/(tests_passed+tests_failed)*100):.1f}%\n")
    
    if tests_failed == 0:
        print("✅ All tests passed! You're ready to run the bot.")
        return True
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        return False

if __name__ == "__main__":
    success = test_configuration()
    sys.exit(0 if success else 1)
