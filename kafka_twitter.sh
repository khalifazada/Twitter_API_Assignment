flume-ng agent --name kafka_twitter_agent --conf-file $FLUME_HOME/conf/kafka_twitter.conf

sleep 60

pkill flume

