thisDir=$(shell pwd)

all: loaded


random.tsv:
	python randomNumbers.py > $@


loaded: random.tsv
	cd ../..; python OneClick.py supplementMetadataFromTSV $(thisDir)/random.tsv
