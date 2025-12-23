# api-lookup
API lookup script for sicehice.com

You can register for an account and receive an API key for free at https://sicehice.com/register

## Usage

Install required dependencies:

```python3 -m pip install -r requirements.txt```

Run the script:

```python3 sicehice-api-lookup.py -i <ip_addresses.txt> -k <api_key>```


## Example Output

| IP | Country | Org | ASN | Sources | Tags |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 185.100.87.166 | Romania | FlokiNET ehf | 200651 | TOR Project, Net.UA, NUBI, BlockList.de, Rutgers DROP, Binary Defense, GreenSnow, Proxy Egress, Malcore, Sblam! | blocklist, proxy, osint, tor, bruteforce, anonymous, honeypot_detection |
| 146.190.40.2 | United States | DIGITALOCEAN-ASN | 14061 | Binary Defense, AbuseIPDB, Sicehice Honeypot | blocklist, osint, CVE-2021-44228, bruteforce, CVE-2022-1388, honeypot_detection |
| 34.112.62.27 | United States | GOOGLE | 15169 | No Results Found | No Results Found |
| 154.213.190.250 | Japan | ZILLION-NETWORK | 54801 | Turris Greylist, Net.UA, Inquest, Sicehice Honeypot, AlienVault OTX, NUBI, Sicehice Malware Labs | blocklist, osint, mirai, bruteforce, malware, CVE-2023-1389, honeypot_detection |
| 52.116.83.184 | United States | SOFTLAYER | 36351 | No Results Found | No Results Found |
| 152.32.170.129 | Hong Kong | UCLOUD INFORMATION TECHNOLOGY HK LIMITED | 135377 | No Results Found | No Results Found |
| 45.155.205.100 | Germany | FOP Malshina | 202685 | Turris Greylist, Net.UA, Sicehice Honeypot, NUBI, AlienVault OTX | blocklist, osint, mirai, bruteforce, malware, honeypot_detection |
| 118.193.39.11 | Hong Kong | CHINANET-BACKBONE | 4134 | No Results Found | No Results Found |
| 167.94.138.125 | United States | CENSYS-AS | 398101 | Censys, Sicehice Honeypot | blocklist, osint, scanning, honeypot_detection |
| 23.224.71.187 | United States | INTERNAP-2 | 12189 | No Results Found | No Results Found |
