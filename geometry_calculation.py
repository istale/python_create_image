import math

def check_import_ok():
	print('import geometry_calculation ok')
	return

def get_single_shape_bbox_coor_list(coor_list):
	list_x_coor = coor_list[0::2]
	list_y_coor = coor_list[1::2]

	min_x = min(list_x_coor)
	min_y = min(list_y_coor)
	max_x = max(list_x_coor)
	max_y = max(list_y_coor)

	list_return = [min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y]

	return list_return

def get_rectangle_4_coor_list(list_2_coor_list):
	x1 = list_2_coor_list[0]
	y1 = list_2_coor_list[1]
	x2 = list_2_coor_list[2]
	y2 = list_2_coor_list[3]
	list_return = [x1, y1, x2, y1, x2, y2, x1, y2]
	return list_return

def get_rectangle_2_coor_list(list_4_coor_list):
	x1 = list_2_coor_list[0]
	y1 = list_2_coor_list[1]
	x2 = list_2_coor_list[4]
	y2 = list_2_coor_list[5]
	list_return = [x1, y1, x2, y2]
	return list_return

def check_line_overlap(line1_x1, line1_x2, line2_x1, line2_x2):
	if line1_x1 > line1_x2:
		temp = line1_x1
		line1_x1 = line1_x2
		line1_x2 = temp
	if line2_x1 > line2_x2:
		temp = line2_x1
		line2_x1 = line2_x2
		line2_x2 = temp

	if line1_x2 - line2_x1 > 0 and line2_x2 - line1_x1 > 0:
		#overlap_interval = [ max(line1_x1, line2_x1), min(line1_x2, line2_x2) ]
		return 1

	return -1

def get_distance_between_two_points(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_distance_between_two_parallel_line(line1, line2):
	# line format as [x1,y1,x2,y2]
	
	# if x is equal for the same line, it mean lines are along y-axis
	if line1[0] == line1[2] and line2[0] == line2[2]:
		return abs(line1[0] - line2[0])

	# if y is equal for the same line, it mean lines are along x-axis
	if line1[1] == line1[3] and line2[1] == line2[3]:
		return abs(line1[1] -line2[1])

	# the lines may not be parallel
	return -1

def get_corner_distance_between_two_polygon(center_shape_point, other_shape_coor_list):
	list_distance = []
	list_x_coor_other_shape = other_shape_coor_list[0::2]
	list_y_coor_other_shape = other_shape_coor_list[1::2]

	for i in range(0, len(list_x_coor_other_shape)):
		x1 = center_shape_point[0]
		y1 = center_shape_point[1]
		x2 = list_x_coor_other_shape[i]
		y2 = list_y_coor_other_shape[i]

		distance = get_distance_between_two_points(x1, y1, x2, y2)
		list_distance.append(distance)

	return min(list_distance)

# could pending
def check_shape_overlap():
	return

def check_shape_on_R_zone(center_shape_coor_list, other_shape_coor_list):
	# get bbox
	list_bbox_center_shape = get_single_shape_bbox_coor_list(center_shape_coor_list)
	list_bbox_other_shape = get_single_shape_bbox_coor_list(other_shape_coor_list)
	center_shape_x2 = list_bbox_center_shape[2]
	other_shape_x1 = list_bbox_other_shape[0]

    # check if other_shape not on right side
	if other_shape_x1 < center_shape_x2:
	    return -9

	center_shape_y1 = list_bbox_center_shape[1]
	center_shape_y2 = list_bbox_center_shape[5]
	other_shape_y1 = list_bbox_other_shape[1]
	other_shape_y2 = list_bbox_other_shape[5]
	if check_line_overlap(center_shape_y1, center_shape_y2, other_shape_y1, other_shape_y2) > 0:
	    return 1

	# no overlap
	return -1

def check_shape_on_L_zone(center_shape_coor_list, other_shape_coor_list):
	# get bbox
	list_bbox_center_shape = get_single_shape_bbox_coor_list(center_shape_coor_list)
	list_bbox_other_shape = get_single_shape_bbox_coor_list(other_shape_coor_list)
	center_shape_x1 = list_bbox_center_shape[0]
	other_shape_x2 = list_bbox_other_shape[2]

    # check if other_shape not on left side
	if other_shape_x2 > center_shape_x1:
	    return -9

	center_shape_y1 = list_bbox_center_shape[1]
	center_shape_y2 = list_bbox_center_shape[5]
	other_shape_y1 = list_bbox_other_shape[1]
	other_shape_y2 = list_bbox_other_shape[5]
	if check_line_overlap(center_shape_y1, center_shape_y2, other_shape_y1, other_shape_y2) > 0:
	    return 1

	# no overlap
	return -1

def check_shape_on_T_zone(center_shape_coor_list, other_shape_coor_list):
	# get bbox
	list_bbox_center_shape = get_single_shape_bbox_coor_list(center_shape_coor_list)
	list_bbox_other_shape = get_single_shape_bbox_coor_list(other_shape_coor_list)
	center_shape_y2 = list_bbox_center_shape[5]
	other_shape_y1 = list_bbox_other_shape[1]

    # check if other_shape not on right side
	if other_shape_y1 < center_shape_y2:
	    return -9

	center_shape_x1 = list_bbox_center_shape[0]
	center_shape_x2 = list_bbox_center_shape[2]
	other_shape_x1 = list_bbox_other_shape[0]
	other_shape_x2 = list_bbox_other_shape[2]
	if check_line_overlap(center_shape_x1, center_shape_x2, other_shape_x1, other_shape_x2) > 0:
	    return 1

	# no overlap
	return -1

def check_shape_on_B_zone(center_shape_coor_list, other_shape_coor_list):
	# get bbox
	list_bbox_center_shape = get_single_shape_bbox_coor_list(center_shape_coor_list)
	list_bbox_other_shape = get_single_shape_bbox_coor_list(other_shape_coor_list)
	center_shape_y1 = list_bbox_center_shape[1]
	other_shape_y2 = list_bbox_other_shape[5]

    # check if other_shape not on right side
	if other_shape_y2 > center_shape_y1:
	    return -9

	center_shape_x1 = list_bbox_center_shape[0]
	center_shape_x2 = list_bbox_center_shape[2]
	other_shape_x1 = list_bbox_other_shape[0]
	other_shape_x2 = list_bbox_other_shape[2]
	if check_line_overlap(center_shape_x1, center_shape_x2, other_shape_x1, other_shape_x2) > 0:
	    return 1

	# no overlap
	return -1

def check_shape_on_Q1_zone(center_shape_coor_list, other_shape_coor_list):
	# get bbox
	list_bbox_center_shape = get_single_shape_bbox_coor_list(center_shape_coor_list)
	list_bbox_other_shape = get_single_shape_bbox_coor_list(other_shape_coor_list)

	# top-right corner coordinate
	center_shape_x = list_bbox_center_shape[4]
	center_shape_y = list_bbox_center_shape[5]

	# bottom-left corner coordinate
	other_shape_x = list_bbox_other_shape[0]
	other_shape_y = list_bbox_other_shape[1]

	if other_shape_x >= center_shape_x and other_shape_y >= center_shape_y:
		return 1
	
	return -1

def check_shape_on_Q2_zone(center_shape_coor_list, other_shape_coor_list):
	# get bbox
	list_bbox_center_shape = get_single_shape_bbox_coor_list(center_shape_coor_list)
	list_bbox_other_shape = get_single_shape_bbox_coor_list(other_shape_coor_list)

	# top-left corner coordinate
	center_shape_x = list_bbox_center_shape[6]
	center_shape_y = list_bbox_center_shape[7]

	# bottom-right corner coordinate
	other_shape_x = list_bbox_other_shape[2]
	other_shape_y = list_bbox_other_shape[3]

	if other_shape_x <= center_shape_x and other_shape_y >= center_shape_y:
		return 1
	
	return -1

def check_shape_on_Q3_zone(center_shape_coor_list, other_shape_coor_list):
	# get bbox
	list_bbox_center_shape = get_single_shape_bbox_coor_list(center_shape_coor_list)
	list_bbox_other_shape = get_single_shape_bbox_coor_list(other_shape_coor_list)

    # bottom-left corner coordinate
	center_shape_x = list_bbox_center_shape[0]
	center_shape_y = list_bbox_center_shape[1]

	# top-right corner coordinate
	other_shape_x = list_bbox_other_shape[4]
	other_shape_y = list_bbox_other_shape[5]

	if other_shape_x <= center_shape_x and other_shape_y <= center_shape_y:
		return 1
	
	return -1

def check_shape_on_Q4_zone(center_shape_coor_list, other_shape_coor_list):
	# get bbox
	list_bbox_center_shape = get_single_shape_bbox_coor_list(center_shape_coor_list)
	list_bbox_other_shape = get_single_shape_bbox_coor_list(other_shape_coor_list)

    # bottom-right corner coordinate
	center_shape_x = list_bbox_center_shape[2]
	center_shape_y = list_bbox_center_shape[3]

	# top-left corner coordinate
	other_shape_x = list_bbox_other_shape[6]
	other_shape_y = list_bbox_other_shape[7]

	if other_shape_x >= center_shape_x and other_shape_y <= center_shape_y:
		return 1
	
	return -1
