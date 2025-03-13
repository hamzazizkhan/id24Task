import pytest
from crawler import login, search


status = ["exited", "leave", "stay", "no match"]
# List of American companies to test
company_list = ["apple", "microsoft", "tesla", "google", "amazon", "netflix"]

def test_search():
    session, custom_headers = login()
    
    for company in company_list:
        status_code, data = search(session, custom_headers, company)
        
        assert status_code == 200, f"Failed for {company}"
        for item in data:
            assert item['status'] in status, f"Invalid status for {company}"
