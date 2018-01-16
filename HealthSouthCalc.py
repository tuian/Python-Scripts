# Severity dictionary

def severity_calc(use_case):

    severity = {'Anonymous Logon from the Internet': 7,
                'Bluecoat - Botnet Activity Detected': 5,
                'Bluecoat - Botnet Outbreak Detected': 5,
                'Brute Force Login Attempts': 7,
                'Brute Force Login Attempts - Internet Blacklist IPs': 2,
                'CP - SmartDefense Distributed Attack Detected': 7,
                'Cisco - Interface State Changed': 3,
                'Cisco - Lost Failover communications with mate': 3,
                'Cisco - Possible Failure or High-Load': 3,
                'Citrix - Possible Device Failure': 3,
                'FireEye - Email of Interest': 3,
                'FireEye - Interesting Network Traffic': 5,
                'FireEye - Malware Outbreak': 5,
                'HealthSouth - OWA Failed Authentication Multiple Accounts': 7,
                'Inbound Network Sweep from Blacklist IP': 2,
                'Inbound Service Enumeration Scan': 2,
                'Internal Service Enumeration Scan': 5,
                'Login Success from Internet Blacklist IPs': 10,
                'Massive SSH Access from a Blacklist IP': 2,
                'Microsoft ATA - Suspicious Activity Detected': 7,
                'Microsoft SCCM - AV Virus Outbreak': 5,
                'Microsoft SCCM - Critical Detection': 10,
                'Microsoft SCCM - Repeat Infection': 5,
                'Outbound Traffic to Internet Blacklist IPs - FW Permitted': 3,
                'P2P BitTorrent uTorrent Protocol Detected': 3,
                'PaloAlto - Attempted IPS Bash Remote Code Execution Detected': 7,
                'PaloAlto - Spyware Detected': 5,
                'PaloAlto - Virus Outbreak Detected': 7,
                'PaloAlto - Vulnerability Scanning Detected': 7,
                'ProSOC Destination IP Watchlist': 5,
                'ProSOC User Agent Watchlist': 5,
                'Snort - Excessive Trojan Activity Detected': 3,
                'Snort - Multiple Trojan Activity Signatures Triggered': 3,
                'Snort - Signature Watchlist': 3,
                'Snort - Vulnerability Scanning Detected': 7,
                'TippingPoint - Distributed Attack': 7,
                'TippingPoint - Vulnerability Scanning Detected': 7,
                'Unauthorized Internal Horizontal Sweep': 5,
                'VPN Account Attack': 7,
                'VPN Authentication Outside of Home Location': 3,
                'Windows Account Locked Out - Multiple Times in 3 hours': 3,
                'Windows Active Directory - Potential Sign of Compromise': 3,
                'Windows Critical Group Change': 3,
                'Windows Install Service Attempt': 3,
                'Windows Lockout Policy Changed': 3,
                'Windows Password Policy Changed': 3,
                'Windows - Account Attack': 7,
        }

    if use_case in severity:
        severity_value = severity[use_case]
        return severity_value