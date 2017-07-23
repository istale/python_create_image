from PIL import Image, ImageDraw

#im = Image.open("lena.pgm")
#im = Image.new('RGBA', (100,100))

#draw = ImageDraw.Draw(im)
#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)
#del draw

red = (255,0,0,125)
blue = (0,0,255,125)

dict_layer_color = {}
dict_layer_color['0.0'] = blue
dict_layer_color['1.0'] = red
dict_layer_color['2.0'] = red
dict_layer_color['3.0'] = red
dict_layer_color['4.0'] = red
dict_layer_color['5.0'] = red
dict_layer_color['6.0'] = red
dict_layer_color['7.0'] = red
dict_layer_color['8.0'] = red
dict_layer_color['17.0'] = blue


def y_from_top(y_from_bottom, img_height):
	new_y_coor = img_height - y_from_bottom
	return new_y_coor

def draw_rectangle(draw_obj, layer_name, list_coor, img_size):
	                            
	list_coor[1] = y_from_top(list_coor[1],img_size[1])
	list_coor[3] = y_from_top(list_coor[3],img_size[1])

	text_coor_x = list_coor[0]
	text_coor_y = list_coor[1] - 20
	text_pos = (text_coor_x, text_coor_y) # top-left position of our text
	text = layer_name # text to draw

	fill_color = dict_layer_color[layer_name]

	# Now, we'll do the drawing: 
	draw_obj.text(text_pos, text, fill=fill_color)
	draw_obj.rectangle(list_coor, fill=fill_color, outline=None)

def draw_polygon(draw_obj, layer_name, list_coor, img_size):
	      
	for i in range(1, len(list_coor), 2):
		list_coor[i] = y_from_top(list_coor[i],img_size[1])

	text_coor_x = list_coor[0]
	text_coor_y = list_coor[1] - 20
	text_pos = (text_coor_x, text_coor_y) # top-left position of our text
	text = layer_name # text to draw

	fill_color = dict_layer_color[layer_name]

	# Now, we'll do the drawing: 
	draw_obj.text(text_pos, text, fill=fill_color)
	draw_obj.polygon(list_coor, fill=fill_color, outline=None)

def get_layer_and_coor_list(layout_string):
	list_return = []

	list_shape = layout_string.split(',')
	for shape in list_shape:
		layer = shape.split('@')[0]
		coor_string = shape.split('@')[1]
		coor_list = coor_string.split('_')
		coor_list = list(map(int, coor_list))
		list_this_shape = [layer, coor_list]
		list_return.append(list_this_shape)

	return list_return

def get_img_coor_by_img_size(list_layout_original_coor, img_size):
	list_layout_img_coor = []

	list_all_x_coor = []
	list_all_y_coor = []
	for shape in list_layout_original_coor:
		layer = shape[0]
		coor_list = shape[1]

		list_x_coor = coor_list[0::2]
		list_all_x_coor.extend(list_x_coor)

		list_y_coor = coor_list[1::2]
		list_all_y_coor.extend(list_y_coor)

	max_x = max(list_all_x_coor)
	max_y = max(list_all_y_coor)

	expand_ratio_x = img_size[0]/max_x
	expand_ratio_y = img_size[1]/max_y	

	for shape in list_layout_original_coor:
		layer = shape[0]
		coor_list = shape[1]

		for i in range(0, len(coor_list)):
			if i % 2 == 0:
				coor_list[i] = coor_list[i] * expand_ratio_x
			elif i % 2 == 1:
				coor_list[i] = coor_list[i] * expand_ratio_y

		list_shape = []
		list_shape.append(layer)
		list_shape.append(coor_list)

		list_layout_img_coor.append(list_shape)

	return list_layout_img_coor


def draw_layout(list_layout, image_obj, size):

	# create a drawing object that is RGBA
	draw = ImageDraw.Draw(image_obj, 'RGBA')   

	for shape in list_layout:
		layer = shape[0]
		coor_list = shape[1]
		print(coor_list)
		if len(coor_list) == 4:
			draw_rectangle(draw, layer, coor_list, size)
		elif len(coor_list) > 4:
			draw_polygon(draw, layer, coor_list, size)
	
	del draw

def get_all_shape_bbox_coor_list(list_layout):

    list_all_x_coor = []
    list_all_y_coor = []
    for shape in list_layout:
	    layer = shape[0]
	    coor_list = shape[1]

	    list_x_coor = coor_list[0::2]
	    list_all_x_coor.extend(list_x_coor)

	    list_y_coor = coor_list[1::2]
	    list_all_y_coor.extend(list_y_coor)

    min_x = min(list_all_x_coor)
    min_y = min(list_all_y_coor)
    max_x = max(list_all_x_coor)
    max_y = max(list_all_y_coor)

    most_bottom = min_y - 50
    most_left = min_x - 50
    most_right = max_x + 50
    most_top = max_y + 50
    tuple_return = (int(most_right - most_left), int(most_top - most_bottom))
    return tuple_return

def create_layout_image_file(layout_string, img_file_name, img_size):
    # size of the image to create
    list_layout_original_coor = get_layer_and_coor_list(layout_string)
    list_layout_img_coor = get_img_coor_by_img_size(list_layout_original_coor, img_size)

	# resize to create the image 
    img_size = (img_size[0] + 100, img_size[1]+100)
    img_obj = Image.new('RGB', img_size) 

    draw_layout(list_layout_img_coor, img_obj , img_size)

	# write to stdout
    img_obj.save(img_file_name, "PNG")


if __name__ == '__main__':
    print('Start~')

    img_size = (300,300)

	#layout_string = '6.0@50_50_300_100,17.0@100_0_150_200,17.0@200_0_250_200'
    layout_string = '0.0@5_5_6_5_6_6_5_6,1.0@8_5_9_5_9_6_8_6,2.0@5_8_6_8_6_9_5_9,3.0@2_5_3_5_3_6_2_6,4.0@5_2_6_2_6_3_5_3,5.0@8_7_9_7_9_8_8_8,6.0@2_7_3_7_3_8_2_8,7.0@2_2_3_2_3_3_2_3,8.0@8_2_9_2_9_3_8_3'

	# size of the image to create
    #list_layout_original_coor = get_layer_and_coor_list(layout_string)
    #list_layout_img_coor = get_img_coor_by_img_size(list_layout_original_coor, img_size)

	# create the image 
    #img_size = (500,500)
    #im = Image.new('RGB', img_size) 

    #draw_layout(list_layout_img_coor, im , img_size)

	# write to stdout
    #im.save("ccc.png", "PNG")

    create_layout_image_file(layout_string, 'ddd.png', img_size)

    print('Done~')
