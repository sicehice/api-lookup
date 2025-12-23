import requests
import csv
import time
import progressbar
import argparse

def iplookup(ip, apikey):
    # API Request
    try:
        resp = requests.post(
            'https://sicehice.com/api/v2/getip', 
            headers={'apikey': apikey, 'query': ip},
            timeout=10 # Added a timeout for safety
        )
        resp_json = resp.json()
    except Exception:
        return [ip, "Error", "Error", "Error", "Error", "Error"]

    # 1. Extract Basic IP Info
    country, org, asn = "N/A", "N/A", "N/A"
    if 'query' in resp_json and resp_json['query']:
        item = resp_json['query'][0]
        country = item.get('country', 'N/A')
        org = item.get('org', 'N/A')
        asn = item.get('asn', 'N/A')

    # 2. Extract Sources
    sources = []
    if 'data' in resp_json:
        for item in resp_json['data']:
            source_val = item.get('source', 'N/A')
            if source_val != "N/A" and source_val not in sources:
                sources.append(source_val)
    source_str = ", ".join(sources) if sources else "No Results Found"

    # 3. Handle Variable Tags Structure
    tags_data = resp_json.get('tags', [])
    tags_str = "No Results Found" 

    if isinstance(tags_data, list):
        clean_tags = [str(t) for t in tags_data if t]
        if clean_tags:
            tags_str = ", ".join(clean_tags)
    elif isinstance(tags_data, dict):
        if tags_data.get('tags') == "N/A":
            tags_str = "No Results Found"
        else:
            tags_str = str(tags_data.get('tags', "No Results Found"))

    return [ip, country, org, asn, source_str, tags_str]

def main():
    # Set up Argparse
    parser = argparse.ArgumentParser(description="Lookup IP information and save to CSV.")
    parser.add_argument('-i', '--input', help='Path to the input text file containing IPs (one IP per line)', default='ips.txt')
    parser.add_argument('-k', '--key', help='API Key for sicehice.com')
    args = parser.parse_args()

    querytime = int(time.time())

    if args.key == '' or args.key is None:
    	print ("Please specify sicehice.com API key with -k")
    	exit()
    
    try:
        # Read IPs from file
        with open(args.input, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            total_ips = len(lines)

        if total_ips == 0:
            print("No IPs found in the input file.")
            return

        output_filename = f'sicehice-output-{querytime}.csv'
        
        # Initialize the progress bar
        widgets = [
            ' [', progressbar.Timer(), '] ',
            progressbar.Bar(),
            ' (', progressbar.ETA(), ') ',
        ]
        bar = progressbar.ProgressBar(max_value=total_ips, widgets=widgets).start()

        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['IP', 'Country', 'Org', 'ASN', 'Sources', 'Tags'])
        
            for index, ip in enumerate(lines):
                result = iplookup(ip, args.key)
                writer.writerow(result)
                bar.update(index + 1)
                
        bar.finish()
        print(f"\nSuccess! Data written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{args.input}' was not found.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
