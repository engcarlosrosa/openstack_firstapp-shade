from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

images = conn.list_images()
for image in images:
    print(image)

flavors =  conn.list_flavors()
for flavor in flavors:
    print(flavor)

image_id = 'c55094e9-699c-4da9-95b4-2e2e75f4c66e'
image = conn.get_image(image_id)
print(image)

flavor_id = '100'
flavor = conn.get_flavor(flavor_id)
print(flavor)

instance_name = 'testing'
testing_instance = conn.create_server(wait=True, auto_ip=True,
    name=instance_name,
    image=image_id,
    flavor=flavor_id)
print(testing_instance)

instances = conn.list_servers()
for instance in instances:
    print(instance)


conn.delete_server(name_or_id=instance_name)
