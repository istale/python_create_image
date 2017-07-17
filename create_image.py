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
dict_layer_color['6.0'] = red
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

if __name__ == '__main__':
	print('Start~')
	
	layout_string = '6.0@50_50_300_100,17.0@100_0_150_200'

	list_layout = get_layer_and_coor_list(layout_string)

	# size of the image to create
	size = (500,300)       

	# create the image 
	im = Image.new('RGB', size) 

	# create a drawing object that is RGBA
	draw = ImageDraw.Draw(im, 'RGBA')   

	for shape in list_layout:
		layer = shape[0]
		print(layer)
		coor_list = shape[1]
		print(coor_list)
		draw_rectangle(draw, layer, coor_list, size)
	
	del draw

	# write to stdout
	im.save("ccc.png", "PNG")

	print('Done~')
