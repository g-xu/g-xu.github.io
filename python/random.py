def gen_rand_string(cnt):
	chars = string.letters+string.digits
 	return ''.join(random.choice(chars) for _ in range(cnt))

def gen_rand_hex(cnt):
	chars = string.hexdigits
 	return ''.join(random.choice(chars) for _ in range(cnt))