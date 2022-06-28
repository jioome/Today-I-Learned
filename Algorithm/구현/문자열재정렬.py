word = input()
count = 0
character = []
c = ''
for w in word:
    if w.isdigit():
        count += int(w)
    else:
        character.append(w)
character.sort()
for cha in character:
    c += cha
print(c + str(count))


print(''.join(sorted(character)))
