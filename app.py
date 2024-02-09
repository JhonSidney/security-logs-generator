import random
from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/computers', methods=['GET'])
def obter_informacoes_deepsecurity():

    host_names = ['AuroraServer', 'NebulaNode', 'QuantumGateway', 'CelestialHub', 'ZenithMachine', 'StellarServer', 'NovaNexus', 'GalaxiaGateway', 'InfinityHost', 'OrionCloud', 'EclipseEngine', 'CosmosCluster', 'SiriusSystem', 'TitanTower', 'PulsarPlatform']
    server_types = ['WebServer', 'DatabaseServer', 'FileServer', 'MailServer', 'ApplicationServer', 'ProxyServer', 'VirtualizationServer', 'BackupServer', 'PrintServer', 'FTP_Server', 'DNS_Server', 'MediaServer', 'AuthenticationServer', 'GameServer', 'IoTServer']
    server_descriptions = ['Serves web content', 'Manages databases',   'Stores and shares files', 'Handles email services','Runs specific applications', 'Routes network traffic',   'Manages virtual machines', 'Handles data backups','Manages print jobs', 'Facilitates file transfers','Resolves domain names', 'Streams media content', 'Authenticates users', 'Hosts online games', 'Supports IoT devices']
    ip_addresses = ['192.168.1.1', '10.0.0.1', '172.16.0.1', '192.168.0.100', '192.168.2.1', '10.1.1.1', '192.168.0.10', '172.17.0.1', '10.0.1.1', '192.168.1.10', '192.168.100.1', '10.0.0.10', '192.168.2.10', '172.18.0.1', '10.1.0.1']
    plat = ['linux','mcos','windows','android']
    numeric_tokens = ['12345', '67890', '54321', '98765', '23456', '87654', '34567', '10987', '76543', '21098', '43210', '87612', '54389', '09876', '32145']
    four_digit_tokens = ['1234', '5678', '4321', '9876', '2345', '8765', '3456', '1098', '7654', '2109', '3210', '8761', '5438', '9870', '2145']
    server_statuses = ['Running', 'Offline', 'Active', 'Maintenance', 'Idle', 'Error', 'Restarting', 'Backup in Progress', 'Updating', 'Paused', 'Initializing', 'Degraded', 'Suspended', 'Sleeping', 'Unknown']
    cyber_attack_types = ['Phishing', 'Ransomware', 'DDoS', 'Malware', 'Man-in-the-Middle', 'SQL Injection', 'Cross-Site Scripting', 'Zero-Day Exploit', 'Brute Force', 'Social Engineering', 'Credential Stuffing', 'DNS Spoofing', 'Session Hijacking', 'Clickjacking', 'Watering Hole Attack']
    urls = ["https://www.example.com", "https://malicious-site.com", "https://www.another-example.com", "https://suspicious-site.com", "https://www.trusted-site.com", "https://phishing-attempt.com", "https://www.another-safe-site.com", "https://drive-by-download.com", "https://www.example.com/subpage", "https://www.unclassified-site.com"]
    categories = ["Safe", "Malicious", "Safe", "Suspicious", "Safe", "Phishing", "Safe", "Malicious", "Safe", "Unclassified"]
    actions = ["Allowed", "Blocked", "Quarantined"]
    source_ipsx = ['192.168.1.10', '10.1.1.1', '172.16.0.1', '192.168.0.10', '10.0.0.1', '192.168.2.10', '172.18.0.1', '10.0.0.10', '192.168.1.1', '10.1.0.1']
    ordemx = ['0','1','0','2','3','4','5','6','7','8','9']
    destination_ips = ['10.0.0.1', '192.168.2.1', '192.168.0.100', '10.0.1.1', '192.168.1.10', '172.17.0.1', '10.1.0.1', '192.168.2.1', '10.0.1.1', '192.168.0.1']
    actions = ['ALLOW', 'BLOCK']
    protocols = ['TCP', 'UDP','ICMP']
    ports = ['80', '53', '22', 'None', '443', '8080', '123', '21', '500', 'None']
    versions = ['1.0','1.1','1.2','1.3','1.4','1.5','1.6', '2.0','2.1','2.2','2.3','2.4','2.5','3.0' '3.1', '3.2', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0', '10.0', '11.0', '12.0', '13.0', '14.0', '15.0', '16.0', '17.0', '18.0', '19.0', '20.0', '21.0', '22.0', '23.0', '24.0', '25.0', '26.0', '27.0', '28.0', '29.0', '30.0']


    computersList = []
    dictionary ={}

    data_e_hora_de_hoje = datetime.now()

    # Formatar a saída para "ANO-MÊS-DIA HORA:MINUTO:SEGUNDO"
    formato = "%Y-%m-%d %H:%M:%S"
    dateResponse = data_e_hora_de_hoje.strftime(formato)

    y =  random.randint(0, 30)

    for i in range(0,y):
        informacoes_deepsecurity = {"computers": {
                "timestamp": ''+ dateResponse,
                "hostName": ''+random.choice(host_names),
                "displayName": ''+random.choice(server_types),
                "description": ''+random.choice(server_descriptions),
                "lastIPUsed": ''+random.choice(ip_addresses),
                "platform": ''+random.choice(plat),
                "groupID": ''+random.choice(numeric_tokens),
                "type_attack": ''+random.choice(cyber_attack_types),
                "policyID": ''+random.choice(four_digit_tokens),
                "agentVersion": " "+ random.choice(versions),
                "computerStatus": {
                    "agentStatus": ''+random.choice(server_statuses),
                    "agentStatusMessages": ''+random.choice(server_statuses),
                    "applianceStatus": ''+random.choice(server_statuses),
                    "applianceStatusMessages":''+random.choice(server_statuses)
                },
                "webReputation": {
                    "state": ''+random.choice(server_statuses),
                    "moduleStatus": {
                        "agentStatus": ''+random.choice(server_statuses),
                        "categories": ''+random.choice(categories),
                        "applianceStatus":''+random.choice(server_statuses),
                        "urls": ''+random.choice(urls),
                        "applianceStatusMessage": "Módulo de Reputação na Web está inativo para o appliance",
                        "actions": ''+random.choice(actions)
                    }
                },
                "firewalls": {
                    "state": ''+random.choice(server_statuses),
                    "sources_ipsx": ''+random.choice(source_ipsx),
                    "globalStatefulConfigurationID":''+random.choice(ordemx),
                    "destination_ips" : ''+random.choice(destination_ips),
                    "actions": ''+random.choice(actions),
                    "protocols":''+random.choice(protocols),
                    "ports": ''+random.choice(ports),
                    "statefulConfigurationAssignments": {},
                    "ruleIDs": ''+random.choice(numeric_tokens)
                }
            }}
        computersList.append(informacoes_deepsecurity)


    dictionary["data"] = computersList
    return jsonify(dictionary)


if __name__ == '__main__':
    app.run(debug=True)