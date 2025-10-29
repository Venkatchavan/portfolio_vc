"""
Content Verification and Duplicate Removal Utility
Checks for empty files and potential duplicates in content directories
"""

import os
from pathlib import Path
from typing import List, Dict, Set
import hashlib

def get_file_hash(file_path: Path) -> str:
    """Calculate hash of file content"""
    if file_path.stat().st_size == 0:
        return "EMPTY"
    
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def check_content_directory(content_type: str) -> Dict:
    """
    Check content directory for issues
    
    Args:
        content_type: 'poems' or 'blogs'
    
    Returns:
        Dict with analysis results
    """
    base_path = Path("content") / content_type
    
    if not base_path.exists():
        return {
            'error': f"Directory not found: {base_path}",
            'files': []
        }
    
    results = {
        'total_files': 0,
        'empty_files': [],
        'valid_files': [],
        'duplicates': [],
        'hash_map': {}
    }
    
    # Collect all files and their hashes
    for file_path in base_path.glob("*.txt"):
        results['total_files'] += 1
        file_hash = get_file_hash(file_path)
        
        if file_hash == "EMPTY":
            results['empty_files'].append(str(file_path.name))
        else:
            results['valid_files'].append({
                'name': file_path.name,
                'size': file_path.stat().st_size,
                'hash': file_hash
            })
            
            # Check for duplicates
            if file_hash in results['hash_map']:
                results['duplicates'].append({
                    'file1': results['hash_map'][file_hash],
                    'file2': file_path.name,
                    'hash': file_hash
                })
            else:
                results['hash_map'][file_hash] = file_path.name
    
    return results

def verify_content_format(file_path: Path) -> Dict:
    """Verify that content file has proper format"""
    issues = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            issues.append("File is empty")
            return {'valid': False, 'issues': issues}
        
        # Check for Title:
        if 'Title:' not in content:
            issues.append("Missing 'Title:' field")
        
        # Check for Content:
        if 'Content:' not in content:
            issues.append("Missing 'Content:' field")
        
        return {
            'valid': len(issues) == 0,
            'issues': issues
        }
    
    except Exception as e:
        return {
            'valid': False,
            'issues': [f"Error reading file: {str(e)}"]
        }

def remove_empty_files(content_type: str, dry_run: bool = True) -> List[str]:
    """
    Remove empty files from content directory
    
    Args:
        content_type: 'poems' or 'blogs'
        dry_run: If True, only report what would be deleted
    
    Returns:
        List of deleted file names
    """
    base_path = Path("content") / content_type
    deleted = []
    
    for file_path in base_path.glob("*.txt"):
        if file_path.stat().st_size == 0:
            deleted.append(file_path.name)
            if not dry_run:
                file_path.unlink()
                print(f"Deleted empty file: {file_path.name}")
            else:
                print(f"Would delete: {file_path.name}")
    
    return deleted

def generate_content_report():
    """Generate a comprehensive content report"""
    print("=" * 70)
    print("PORTFOLIO CONTENT VERIFICATION REPORT")
    print("=" * 70)
    print()
    
    # Check Poems
    print("📝 POEMS DIRECTORY")
    print("-" * 70)
    poems_results = check_content_directory('poems')
    print(f"Total files: {poems_results['total_files']}")
    print(f"Valid files: {len(poems_results['valid_files'])}")
    print(f"Empty files: {len(poems_results['empty_files'])}")
    print(f"Duplicates: {len(poems_results['duplicates'])}")
    
    if poems_results['empty_files']:
        print("\n⚠️  Empty poem files:")
        for file in poems_results['empty_files']:
            print(f"   - {file}")
    
    if poems_results['duplicates']:
        print("\n⚠️  Duplicate poems found:")
        for dup in poems_results['duplicates']:
            print(f"   - {dup['file1']} == {dup['file2']}")
    
    print()
    
    # Check Blogs
    print("📰 BLOGS DIRECTORY")
    print("-" * 70)
    blogs_results = check_content_directory('blogs')
    print(f"Total files: {blogs_results['total_files']}")
    print(f"Valid files: {len(blogs_results['valid_files'])}")
    print(f"Empty files: {len(blogs_results['empty_files'])}")
    print(f"Duplicates: {len(blogs_results['duplicates'])}")
    
    if blogs_results['empty_files']:
        print("\n⚠️  Empty blog files:")
        for file in blogs_results['empty_files']:
            print(f"   - {file}")
    
    if blogs_results['duplicates']:
        print("\n⚠️  Duplicate blogs found:")
        for dup in blogs_results['duplicates']:
            print(f"   - {dup['file1']} == {dup['file2']}")
    
    print()
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    total_empty = len(poems_results['empty_files']) + len(blogs_results['empty_files'])
    total_duplicates = len(poems_results['duplicates']) + len(blogs_results['duplicates'])
    
    print(f"Total empty files: {total_empty}")
    print(f"Total duplicates: {total_duplicates}")
    
    if total_empty > 0:
        print("\n✅ Recommendation: Remove empty files")
        print("   Run: python verify_content.py --clean")
    
    if total_duplicates > 0:
        print("\n✅ Recommendation: Review and remove duplicate files manually")
    
    print()
    
    return {
        'poems': poems_results,
        'blogs': blogs_results
    }

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--clean":
        print("🧹 CLEANING EMPTY FILES...")
        print()
        
        # Remove empty poem files
        print("Cleaning poems directory...")
        deleted_poems = remove_empty_files('poems', dry_run=False)
        print(f"Deleted {len(deleted_poems)} empty poem files")
        print()
        
        # Remove empty blog files
        print("Cleaning blogs directory...")
        deleted_blogs = remove_empty_files('blogs', dry_run=False)
        print(f"Deleted {len(deleted_blogs)} empty blog files")
        print()
        
        print("✅ Cleanup complete!")
        print()
    else:
        # Just generate report
        generate_content_report()
        print()
        print("💡 To remove empty files, run: python verify_content.py --clean")
        print()
