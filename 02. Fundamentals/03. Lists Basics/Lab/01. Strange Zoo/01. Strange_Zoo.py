# tail = input()
# body = input()
# head = input()
# ody_list = [tail, body, head]
body_list = []
body_list.append(input()) #new elements
body_list.append(input())
body_list.append(input())

body_list[0], body_list[2] = body_list[2], body_list[0]
print(body_list)
