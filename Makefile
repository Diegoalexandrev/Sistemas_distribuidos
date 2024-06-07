.PHONY: build

build:
	@docker build -t diego/spark-base-hadoop ./cluster-hadoop/hadoop/spark-base
	@docker build -t diego/spark-master-hadoop ./cluster-hadoop/hadoop/spark-master
	@docker build -t diego/spark-worker-hadoop ./cluster-hadoop/hadoop/spark-worker
