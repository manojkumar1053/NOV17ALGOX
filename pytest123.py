import requests


def get_req_test(url=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_response = response.json()
        print(json_response)
        ele_list = json_response["At what index is the needle?"]
        char_freq = {}
        print(ele_list.index("needle"))
        count = -1
        for ele in ele_list:
            # char_freq[ele] = char_freq.get(ele, 0) + 1
            count += 1
            if ele == "needle":
                return count
        return -1
    except requests.exceptions.HTTPError as http_err:
        return http_err


url = "https://us-central1-unity-security-interviews-test.cloudfunctions.net/haystack"
print(get_req_test(url))


