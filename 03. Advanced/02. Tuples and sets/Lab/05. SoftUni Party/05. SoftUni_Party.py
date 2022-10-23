number_of_guests = int(input())
vip = []
regular = []

for i in range(number_of_guests):
    guest = input()
    if len(guest) == 8:
        if guest[0].isdigit():
            if guest not in vip:
                vip.append(guest)
        else:
            if guest not in regular:
                regular.append(guest)


arriving_guests = input()
vips_who_came = set()
regulars_who_came = set()
while arriving_guests != "END":
    if arriving_guests in vip:
        vips_who_came.add(arriving_guests)
    else:
        regulars_who_came.add(arriving_guests)

    arriving_guests = input()
vips_who_did_not_come = [x for x in vip if x not in vips_who_came]
regulars_who_did_not_come = [y for y in regular if y not in regulars_who_came]
all_guests_who_came = len(vips_who_did_not_come) + len(regulars_who_did_not_come)
print(all_guests_who_came)
for vips in range(len(vips_who_did_not_come)):
    print(vips_who_did_not_come.pop())
for regulars in range(len(regulars_who_did_not_come)):
    print(regulars_who_did_not_come.pop())





