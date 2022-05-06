import pika

from datapackage import Package
package = Package('https://datahub.io/core/geo-countries/r/countries.geojson')

# get list of all resources:
resources = package.descriptor['features']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='machine_ip'))
channel = connection.channel()

channel.queue_declare(queue='hello')
for each in resources:
    data = str(each)
    channel.basic_publish(exchange='', routing_key='hello', body=data)    

connection.close()
