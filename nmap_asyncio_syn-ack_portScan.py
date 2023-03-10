#!usr/bin/python

import asyncio, nmap

class NmapScanner:
    def __init__(self, ip, output):
        self.ip = ip
        self.output = output
        self.nm = nmap.PortScannerAsync()

    async def run(self):
        await asyncio.sleep(1)

        print(f"Starting scan on IP address {self.ip}")
        self.nm.scan(self.ip, arguments=f'-v -sS -Pn -p- -sV -g 53 -o {self.output}')
        while self.nm.still_scanning():
            print('Finishing scan!')

        print(f"""Scan completed for IP address {self.ip}
              Host: {self.nm[self.ip].hostname()}
              OS details: {self.nm[self.ip].os_fingerprint()}""")

        print('Open ports:')
        for port in self.nm[self.ip].all_tcp():
            print(f"Port {port} is {self.nm[self.ip]['tcp'][port]['state']}")
            if self.nm[self.ip].has_tcp(port):
                print(f"""Service: {self.nm[self.ip]['tcp'][port]['name']}
                      Product: {self.nm[self.ip]['tcp'][port]['product']}
                      Version: {self.nm[self.ip]['tcp'][port]['version']}\n""")

async def main():
    ip = input(str('Target: '))
    output = (input(str('Save results to: ')))

    scanner = NmapScanner(ip, output)
    await scanner.run()

if __name__ == '__main__':
    asyncio.run(main())
