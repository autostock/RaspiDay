package mqtt;

import java.util.Vector;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MqttSubscribeSample implements MqttCallback {

	private static MqttClient client;
	private static Vector<String> queue = new Vector<String>();

	public static void main(String[] args) throws MqttException, InterruptedException {
        String topic        = "/sensor/+";
		String broker = "tcp://raspberrypi3:1883";

		client = new MqttClient(broker,	MqttClient.generateClientId());
		client.setCallback(new MqttSubscribeSample());
		client.connect();
		client.subscribe(topic);
		String data="";
		for (int i = 0; ; i++) {
			if (queue.size()>0) {
				while(queue.size()>0) {
					data=queue.remove(0);
		            MqttMessage message = new MqttMessage(data.getBytes());
		            message.setQos(2);
		            client.publish("/actor/linoino", message);
				}
			} else {
//	            MqttMessage message = new MqttMessage(data.getBytes());
//	            message.setQos(2);
//	            client.publish("/actor/linoino", message);
			}
            Thread.sleep(100);
		}
	}

	public void connectionLost(Throwable throwable) {
		System.out.println("Connection to MQTT broker lost!");
	}

	public void messageArrived(String topic, MqttMessage mqttMessage)	throws Exception {
		String data = new String(mqttMessage.getPayload()).replace("\r", "");
		if (topic.endsWith("/lirc0")) {
			long code=0;
			for (int i = 0; i < data.length()/8; i++) {
				int duration=(int)Long.parseLong(data.substring(i*8, i*8+8), 16);
				duration=Integer.reverseBytes(duration)&0x00ffffff;
				code=2*code+(duration>1000?1:0);
//				if ((i%16)==0) System.out.println();
//				System.out.printf("%08x ", duration);
			}
			System.out.printf(" -> %016x\n", code);
		} else if (topic.endsWith("/midi1")) {
			System.out.println("Message received:\t"	+topic + ", " + data);
			if (data.startsWith("902")) {
				queue.add(data.substring(3,4));
			}
		} else {
			System.out.println("Message received:\t"	+topic + ", " + data);
		}
	}

	public void deliveryComplete(IMqttDeliveryToken iMqttDeliveryToken) {
	}
}
