#! /bin/sh

sleep 120
rosservice call /generate_graph
rosservice call /solve_graph
rosservice call /save_pcd_map /home/hasitha/Documents/FinalYearProject/Maps/Map.pcd
