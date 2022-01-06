while :
do
	msg="500 2000, 550 2000, 500 2000, 900 2000, 500 2000, 0 10000"
        echo mosquitto_pub -h 192.168.178.31 -t /xarm/set/timed -m "$msg"
        mosquitto_pub -h 192.168.178.31 -t /xarm/set/timed -m "$msg"
        sleep 10
	msg="500 2000, 550 2000, 500 2000, 900 2000, 500 2000, 800 10000"
        echo mosquitto_pub -h 192.168.178.31 -t /xarm/set/timed -m "$msg"
        mosquitto_pub -h 192.168.178.31 -t /xarm/set/timed -m "$msg"
        sleep 10
done
 
