class robot():
    def __init__(self,robot_name,robot_color,robot_velocity,robot_acceleration,robot_elapsed_time,hız_sensor,basınc_sensor,robot_distance):
        self.r_name=robot_name
        self.r_color=robot_color
        self.r_velocity=robot_velocity
        self.r_acceleration=robot_acceleration
        self.r_distance=robot_distance
        self.r_elapsed_time=robot_elapsed_time
        self.r_v_sensor=hız_sensor
        self.r_basınc_senor=basınc_sensor

    def robot_distance(self):
        self.r_distance=(self.r_v_sensor)*(self.r_elapsed_time)
        print(self.r_distance)
    def robo_print(self):
        print("robot_name={} \n robot_color={} \n robot_velocity={} \n robot_acceleration={}\n robot_distance={} \nhız_sensor={} \nbasınc_sensor={}\n robot_distance={}".format(self.r_name,self.r_color,self.r_velocity,self.r_acceleration,self.r_elapsed_time,self.r_v_sensor,self.r_basınc_senor,self.r_distance))






robot1=robot("transformers","red",22.11,10,100,True,True,0)

print(robot1.robot_distance())
robot1.robo_print()



