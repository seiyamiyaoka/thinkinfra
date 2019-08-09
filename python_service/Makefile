install:
	pip3.7 install -r requirements.txt
s3upload:
	aws s3 sync ./ s3://pythonstudy
s3download:
	aws s3 sync s3://pythonstudy .
