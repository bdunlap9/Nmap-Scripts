#!usr/bin/python

import asyncio, nmap

class NmapScanner:
    def __init__(self, ip):
        self.ip = ip
        self.nm = nmap.PortScannerAsync()

    async def run(self):
        await asyncio.sleep(1)

        print(f"Starting scan on IP address {self.ip}")
        self.nm.scan(self.ip, arguments=f"-v -sS -Pn -p- -sV -g 53", callback=callback_result)
        while self.nm.still_scanning():
            print('Finishing scan!')
            
        print(f"""Scan completed for IP address {self.ip}
              Host: {self.nm[self.ip].hostname()}
              OS details: {self.nm[self.ip].os_fingerprint()}""")

        print('Open ports:')
        for port in self.nm[self.ip].all_tcp():
            print(f"Port {port} is {self.nm[self.ip]['tcp'][port]['state']}")
            if self.nm[self.ip].has_tcp(port):
                service = self.nm[self.ip]['tcp'][port]['name']
                product = self.nm[self.ip]['tcp'][port]['product']
                version = self.nm[self.ip]['tcp'][port]['version']
                print(f"""Service: {service}
                      Product: {product}
                      Version: {version}\n""")

async def main():
    ip = input(str(f'Target: '))
    scanner = NmapScanner(ip)
    await scanner.run()

if __name__ == '__main__':
    asyncio.run(main())
