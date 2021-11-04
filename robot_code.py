initial_pos=0;
final_pos=float(input("enter final position of robot"));
velocity=float(input("enter velocity of robot"));
travalled_distance=final_pos-initial_pos;
elapsed_time:float=travalled_distance/velocity;

print("travelled distance:\n",travalled_distance);
print("elapsed time:\n",elapsed_time);