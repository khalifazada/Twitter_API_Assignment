#!/bin/bash

echo "***	STARTING FLUME AGENT"

flume-ng agent --name kafka_twitter_agent --conf-file $FLUME_HOME/conf/kafka_twitter.conf

sleep 10

pkill flume

