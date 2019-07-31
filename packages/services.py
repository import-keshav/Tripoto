import ast


def to_dict(content):
	content_in_dict = ast.literal_eval(content)
	return content_in_dict


def dest_object_to_dict(dest):
	dest_dict = {}
	dest_dict['id'] = dest.id
	dest_dict['name']  = dest.name
	dest_dict['image_url'] = dest.img.url
	dest_dict['desc'] = dest.desc
	dest_dict['hotel_name'] = dest.hotel_name
	dest_dict['price'] = dest.price
	dest_dict['services'] = to_dict(dest.services)
	dest_dict['day_wise_desc'] = to_dict(dest.day_wise_desc)
	dest_dict['days'] = dest.days
	dest_dict['nights'] = dest.nights

	return dest_dict