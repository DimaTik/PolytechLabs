with open('../server_log.txt', 'r') as file:
	s = file.read().splitlines()

logger_messages = {
	'ERROR': len([i for i in s if 'ERROR' in i]),
	'WARNING': len([i for i in s if 'WARNING' in i]),
	'INFO': len([i for i in s if 'INFO' in i]),
}
with open('../report.txt', 'w') as file:
	file.write(str(logger_messages))
