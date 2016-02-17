import time
# put the the log into the pipeline
def tail(file):
	file.seek(0,2)
	while True:
		n=1
		line = file.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

file = open("/var/log/apache2/access.log","r")
loglines = tail(file)

# filter the logs in the pipeline

def grep(field, lines):
	for line in lines:
		if field in line:
			yield line
# yield the line including "chen"
pipelines = grep("chen", loglines)

# pull the log from the pipeline
for line in pipelines:
	print line

