import requests
from bs4 import BeautifulSoup

class AternosAPI():
    def __init__(self, headers, TOKEN, user_agent):
        self.headers = {}
        self.TOKEN = TOKEN
        self.headers['User-Agent'] = user_agent
        self.headers['Cookie'] = headers
        self.SEC = self.getSEC()
        self.JavaSoftwares = ['Vanilla', 'Spigot', 'Forge', 'Magma','Snapshot', 'Bukkit', 'Paper', 'Modpacks', 'Glowstone']
        self.BedrockSoftwares = ['Bedrock', 'Pocketmine-MP']

    def getSEC(self):
        headers = self.headers['Cookie'].split(";")
        for sec in headers:
            if sec[:12] == "ATERNOS_SEC_":
                sec = sec.split("_")
                if len(sec) == 3:
                    sec = ":".join(sec[2].split("="))
                    return sec

        print("Invaild SEC")
        exit(1)

    def GetStatus(self):
        webserver = requests.get(url='https://aternos.org/server/', headers=self.headers)
        if not webserver.ok:
            return f'Failed to Connect: {webserver.status_code}'
        webdata = BeautifulSoup(webserver.content, 'html.parser')
        status = webdata.find('span', class_='statuslabel-label').get_text()
        status = status.strip()
        return status

    def StartServer(self):
        serverstatus = self.GetStatus()
        if serverstatus == "Failed to Connect":
            return serverstatus
        elif serverstatus == "Online":
            return "Server Already Running"
        else:
            parameters = {}
            parameters['headstart'] = 0
            parameters['SEC'] = self.SEC
            parameters['TOKEN'] = self.TOKEN
            startserver = requests.get(url=f"https://aternos.org/panel/ajax/start.php", params=parameters, headers=self.headers)
            return "Server Started"

    def StopServer(self):
        serverstatus = self.GetStatus()
        if serverstatus == "Failed to Connect":
            return serverstatus
        elif serverstatus == "Offline":
            return "Server Already Offline"
        else:
            parameters = {}
            parameters['SEC'] = self.SEC
            parameters['TOKEN'] = self.TOKEN
            stopserver = requests.get(url=f"https://aternos.org/panel/ajax/stop.php", params=parameters, headers=self.headers)
            return "Server Stopped"

    def GetServerInfo(self):
        ServerInfo = requests.get(url='https://aternos.org/server/', headers=self.headers)
        ServerInfo = BeautifulSoup(ServerInfo.content, 'html.parser')

        Software = ServerInfo.find('span', id='software').get_text()
        Software = Software.strip()

        if(Software in self.JavaSoftwares):
            IP = ServerInfo.find('div', class_='server-ip mobile-full-width').get_text()
            IP = IP.strip()

            IP = IP.split(" ")
            IP = IP[0].strip()

            Port = "25565(Optional)"

            return f"{IP},{Port},{Software}"

        elif(Software in self.BedrockSoftwares):
            IP = ServerInfo.find('span', id='ip').get_text()
            IP = IP.strip()

            Port = ServerInfo.find('span', id='port').get_text()
            Port = Port.strip()

            return f"{IP},{Port},{Software}"
