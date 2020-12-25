sub_card, sub_door = open('input.txt', 'r').read().split('\n')
pub_key_card = int(sub_card)
pub_key_door = int(sub_door)
sub_card = 7
sub_door = 7

loop_size_card = 0
loop_size_door = 0
encryption_card = []
encryption_door = []
max = 1000
start_card = 1
while True:
	start_card *= sub_card
	start_card %= 20201227
	loop_size_card+=1
	#print(start_card)
	if pub_key_card == start_card:
		break
start_door = 1
while True:
	start_door *= sub_door
	start_door %= 20201227
	loop_size_door+=1
	if pub_key_door == start_door:
		break

print(start_card, start_door)
print(loop_size_card, loop_size_door)
start_enc = 1
for _ in range(loop_size_card):
	start_enc*=pub_key_door
	start_enc%=20201227
	
print(start_enc)

