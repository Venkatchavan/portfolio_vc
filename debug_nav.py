from app import create_app

app = create_app()
with app.test_client() as client:
    response = client.get('/narrative/nexus')
    content = response.get_data(as_text=True)
    
    # Find the navigation section
    nav_start = content.find('<ul class="nav-menu">')
    nav_end = content.find('</ul>', nav_start) + 5
    
    if nav_start != -1 and nav_end != -1:
        nav_content = content[nav_start:nav_end]
        print("Raw Flask navigation output:")
        print(nav_content)
    else:
        print("Navigation section not found")
        # Let's look for url_for patterns instead
        import re
        url_for_matches = re.findall(r'url_for\([^)]+\)', content)
        print(f"Found {len(url_for_matches)} url_for patterns:")
        for match in url_for_matches[:10]:  # Show first 10
            print(f"  {match}")
