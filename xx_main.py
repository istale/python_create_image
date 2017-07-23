from geometry_calculation import *
from create_image import *
import math

def get_layout_data():
	return '0.0@5_5_6_5_6_6_5_6,1.0@8_5_9_5_9_6_8_6,2.0@5_8_6_8_6_9_5_9,3.0@2_5_3_5_3_6_2_6,4.0@5_2_6_2_6_3_5_3,5.0@8_7_9_7_9_8_8_8,6.0@2_7_3_7_3_8_2_8,7.0@2_2_3_2_3_3_2_3,8.0@8_2_9_2_9_3_8_3'

def parse_layout_data_to_list(layout_string):
	return get_layer_and_coor_list(layout_string)
	

def get_relation(center_shape_coor_list, other_shape_coor_list):
	# return format [zone, distance]

	if check_shape_on_R_zone(center_shape_coor_list, other_shape_coor_list) == 1:
		zone = 'R'
		# only deal with rectangle case now
		center_shape_right_edge = [center_shape_coor_list[2], center_shape_coor_list[3], center_shape_coor_list[4], center_shape_coor_list[5]]
		other_shape_left_edge = [other_shape_coor_list[0], other_shape_coor_list[1], other_shape_coor_list[6], other_shape_coor_list[7]]
		distance = get_distance_between_two_parallel_line(center_shape_right_edge, other_shape_left_edge)
		return [zone, distance]

	if check_shape_on_L_zone(center_shape_coor_list, other_shape_coor_list) == 1:
		zone = 'L'
		# only deal with rectangle case now
		center_shape_left_edge = [center_shape_coor_list[0], center_shape_coor_list[1], center_shape_coor_list[6], center_shape_coor_list[7]]
		other_shape_right_edge = [other_shape_coor_list[2], other_shape_coor_list[3], other_shape_coor_list[4], other_shape_coor_list[5]]
		distance = get_distance_between_two_parallel_line(center_shape_left_edge, other_shape_right_edge)
		return [zone, distance]

	if check_shape_on_T_zone(center_shape_coor_list, other_shape_coor_list) == 1:
		zone = 'T'
		# only deal with rectangle case now
		center_shape_top_edge = [center_shape_coor_list[4], center_shape_coor_list[5], center_shape_coor_list[6], center_shape_coor_list[7]]
		other_shape_bottom_edge = [other_shape_coor_list[0], other_shape_coor_list[1], other_shape_coor_list[2], other_shape_coor_list[3]]
		distance = get_distance_between_two_parallel_line(center_shape_top_edge, other_shape_bottom_edge)
		return [zone, distance]

	if check_shape_on_B_zone(center_shape_coor_list, other_shape_coor_list) == 1:
		zone = 'B'
		# only deal with rectangle case now
		center_shape_bottom_edge = [center_shape_coor_list[0], center_shape_coor_list[1], center_shape_coor_list[2], center_shape_coor_list[3]]
		other_shape_top_edge = [other_shape_coor_list[4], other_shape_coor_list[5], other_shape_coor_list[6], other_shape_coor_list[7]]
		distance = get_distance_between_two_parallel_line(center_shape_bottom_edge, other_shape_top_edge)
		return [zone, distance]

	if check_shape_on_Q1_zone(center_shape_coor_list, other_shape_coor_list) == 1:
		zone = 'Q1'
		# only deal with rectangle case now
		center_shape_point = [center_shape_coor_list[4], center_shape_coor_list[5]]
		distance = get_corner_distance_between_two_polygon(center_shape_point, other_shape_coor_list)
		return [zone, distance]

	if check_shape_on_Q2_zone(center_shape_coor_list, other_shape_coor_list) == 1:
		zone = 'Q2'
		# only deal with rectangle case now
		center_shape_point = [center_shape_coor_list[6], center_shape_coor_list[7]]
		distance = get_corner_distance_between_two_polygon(center_shape_point, other_shape_coor_list)
		return [zone, distance]

	if check_shape_on_Q3_zone(center_shape_coor_list, other_shape_coor_list) == 1:
		zone = 'Q3'
		# only deal with rectangle case now
		center_shape_point = [center_shape_coor_list[0], center_shape_coor_list[1]]
		distance = get_corner_distance_between_two_polygon(center_shape_point, other_shape_coor_list)
		return [zone, distance]

	if check_shape_on_Q4_zone(center_shape_coor_list, other_shape_coor_list) == 1:
		zone = 'Q4'
		# only deal with rectangle case now
		center_shape_point = [center_shape_coor_list[2], center_shape_coor_list[3]]
		distance = get_corner_distance_between_two_polygon(center_shape_point, other_shape_coor_list)
		return [zone, distance]

	# error return -1
	return -1





if __name__ == '__main__':
    print('')
    print('***************************')
    print('*                         *')
    print('*      Porcess start      *')
    print('*                         *')
    print('***************************')
    print('')
    
    layout_string = get_layout_data()
    img_size = (300,300)
    create_layout_image_file(layout_string, 'eee.png', img_size)

    list_layout = parse_layout_data_to_list(layout_string)

    center_shape = list_layout[0]
    center_shape_coor_list = center_shape[1]

    list_other_shape = list_layout[1:]

    print('')
    for other_shape in list_other_shape:
    	other_shape_layer = other_shape[0]
    	other_shape_coor_list = other_shape[1]

    	relation = get_relation(center_shape_coor_list, other_shape_coor_list)
    	print(other_shape_layer)
    	print(relation)
    	print('')


    print('')
    print('Done!')
