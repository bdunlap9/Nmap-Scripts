import asyncio, nmap

class NmapScanner:
    def __init__(self, ip):
        self.ip = ip
        self.nm = nmap.PortScanner()

    async def run(self):
        await asyncio.sleep(1)

        self.nm.scan(self.ip, arguments="-sS -Pn -p- -g 53")
        for port in self.nm[self.ip].all_tcp():
            print("Port {} is {}".format(port, self.nm[self.ip]['tcp'][port]['state']))

async def main():
    ip = input(str(f'Target: '))
    scanner = NmapScanner(ip)
    await scanner.run()

if __name__ == '__main__':
    asyncio.run(main())