import Group

local_cluster = Group.group(True, 123, 100, 200, 300)
remote_cluster = Group.group(True, 123, 100, 200, 300)

cool = set()
cool.add(local_cluster)
cool.add(remote_cluster)
print(len(cool))