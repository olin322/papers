#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import carla

# print("import carla success")

# import sys

# print(sys.version)


# In[2]:


# import carla
# import random

# # ./CarlaUE4.sh -quality-level=Low
# # ./CarlaUE4.sh -quality-level=epic
# # ./CarlaUE4.sh -RenderOffScreen


# # Connect to the client and retrieve the world object
# client = carla.Client('localhost', 2000)
# world = client.get_world()


# # Setting synchronous mode
# # By default, CARLA runs in asynchronous mode.
# # Synchronous mode must be enabled before loading or reloading the world: 
# # Differing timestamps can arise if the world is not in synchronous mode 
# # from the very beginning. This can generate small differences in physics 
# # simulation and in the life cycle of objects such as traffics lights.
# settings = world.get_settings()
# settings.synchronous_mode = True # Enables synchronous mode
# settings.fixed_delta_seconds = 0.02 # (default is 0.05)
# world.apply_settings(settings)

# # set no_rendering_mode
# settings = world.get_settings()
# settings.no_rendering_mode = True
# world.apply_settings(settings)
# # settings.no_rendering_mode = False
# # world.apply_settings(settings)

# #imoprt map
# client.load_world('Town01')


# # get blueprint
# level = world.get_map()
# weather = world.get_weather()
# blueprint_library = world.get_blueprint_library()

# step = 0
# while step <= 10:
#     world.tick()
#     print(step)
#     step += 1
    
# # carla.terminate() ???


# In[3]:


import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()
settings = world.get_settings()

# set rendering mode
# settings.no_rendering_mode = True

settings.synchronous_mode = True # Enables synchronous mode
settings.fixed_delta_seconds = 0.05 # (default is 0.05)

world.apply_settings(settings)

# load map
client.load_world('Town01')


# In[4]:



# get blueprint
level = world.get_map()
weather = world.get_weather()
blueprint_library = world.get_blueprint_library()

# Get the blueprint library and filter for the vehicle blueprints
vehicle_blueprints = world.get_blueprint_library().filter('*vehicle*')

# Get the map's spawn points
spawn_points = world.get_map().get_spawn_points()


# In[5]:



# Spawn 50 vehicles randomly distributed throughout the map 
# for each spawn point, we choose a random vehicle from the blueprint library
# for i in range(0,10):
#     world.try_spawn_actor(random.choice(vehicle_blueprints), random.choice(spawn_points))


# In[6]:


# print(spawn_points)
ego_vehicle_spawn_point = carla.Transform(carla.Location(x=151.119736, y=198.759842, z=0.299438), carla.Rotation(pitch=0.000000, yaw=0.000000, roll=0.000000))
# ego_vehicle = world.spawn_actor(random.choice(vehicle_blueprints.filter('tesla')), ego_vehicle_spawn_point)
# ego_vehicle = world.spawn_actor(blueprint_library.find('vehicle.tesla.model3'), ego_vehicle_spawn_point)
ego_vehicle = world.spawn_actor(blueprint_library.find('vehicle.ford.mustang'), ego_vehicle_spawn_point)


# In[7]:







# # Create a transform to place the camera on top of the vehicle
# camera_init_trans = carla.Transform(carla.Location(z=1.5))

# # We create the camera through a blueprint that defines its properties
# camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')

# # We spawn the camera and attach it to our ego vehicle
# camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to=ego_vehicle)

# # Start camera with PyGame callback
# camera.listen(lambda image: image.save_to_disk('out/%06d.png' % image.frame))


# for vehicle in world.get_actors().filter('*vehicle*'):
#     if vehicle != ego_vehicle:
#         vehicle.set_autopilot(True)


# Transform(Location(x=151.119736, y=198.759842, z=0.299438), Rotation(pitch=0.000000, yaw=0.000000, roll=0.000000))
spectator = world.get_spectator()


while True:    
    transform = ego_vehicle.get_transform()
    spectator.set_transform(carla.Transform(transform.location + carla.Location(x=-50, y=0,z=20), carla.Rotation(pitch=0)))
#     print(transform)
#     ego_vehicle.set_autopilot(True)
    ego_vehicle.apply_control(carla.VehicleControl(throttle=0.5, steer=0.1))
    world.tick()
    


# In[ ]:





# In[ ]:




# town = 'Town0'
# num = 1
# for i in range(5):
#     mapname = town+str(num+i)
#     print(mapname)
#     client.load_world(mapname)


#     # get blueprint
#     level = world.get_map()
#     weather = world.get_weather()
#     blueprint_library = world.get_blueprint_library()

#     step = 0
#     while step <= 10:
#         world.tick()
#         print(step)
#         step += 1

# carla.terminate()

