import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Test Payloads
SQLI_PAYLOAD = "' OR '1'='1"
XSS_PAYLOAD = "<script>alert('XSS_VULN')</script>"

def get_all_forms(url):
    """Web page se saare HTML forms extract karta hai"""
    try:
        response = requests.get(url, timeout=15)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[-] Error fetching URL {url}: {e}")
        return []

def get_form_details(form):
    """Form ki action, method, aur inputs details nikalta hai"""
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
        
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    """Form mein payload submit karke response return karta hai"""
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    
    for input_field in inputs:
        if input_field["type"] == "text" or input_field["type"] == "search":
            data[input_field["name"]] = value
        elif input_field["name"]:
            data[input_field["name"]] = "test"
            
    if form_details["method"] == "post":
        return requests.post(target_url, data=data, timeout=15)
    else:
        return requests.get(target_url, params=data, timeout=15)

def scan_vulnerabilities(url):
    """SQLi aur XSS vulnerabilities scan karta hai"""
    print(f"\n[*] Scanning Target: {url}")
    print("=" * 50)
    forms = get_all_forms(url)
    print(f"[+] Found {len(forms)} form(s) on target.")
    
    for i, form in enumerate(forms, 1):
        form_details = get_form_details(form)
        print(f"\n[!] Testing Form #{i} (Action: {form_details['action']})")
        
        # Test XSS
        xss_res = submit_form(form_details, url, XSS_PAYLOAD)
        if XSS_PAYLOAD in xss_res.text:
            print(f"    [VULNERABLE] XSS Detected in Form #{i}!")
        else:
            print(f"    [SAFE] XSS Payload neutralized.")
            
        # Test SQL Injection
        sqli_res = submit_form(form_details, url, SQLI_PAYLOAD)
        errors = ["mysql_fetch_array()", "you have an error in your sql syntax", "warning: mysql"]
        is_sqli = any(error in sqli_res.text.lower() for error in errors)
        
        if is_sqli:
            print(f"    [VULNERABLE] Potential SQL Injection in Form #{i}!")
        else:
            print(f"    [SAFE] SQLi Payload handled cleanly.")

if __name__ == "__main__":
    target = input("Enter Target URL to Scan (e.g., http://testphp.vulnweb.com/search.php?test=query): ").strip()
    if target:
        scan_vulnerabilities(target)