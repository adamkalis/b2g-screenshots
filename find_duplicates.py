import json
import sys

if len(sys.argv) > 1:
  locale = sys.argv[1]
print '\n          ----====*'+ locale + '*====----\n'

json_file = open('locales/' + locale  +'/db.json')
db = json.load(json_file)
json_file.close()

id_dupl = 0
id_dupl_l10n = 0
id_tripl = 0
id_tripl_l10n = 0
id_quad = 0
id_quad_l10n = 0
id_multi = 0
id_multi_l10n = 0
ids = 0

for string in db:
  l10n_set = []
  position_set = []
  ids += 1
  size = len(db[string]) 
  if size > 1:
    if size == 2:
      id_dupl += 1
      for case in db[string]:
        l10n_set.append(case['l10n'])
        position_set.append(case['position'].split('/',2)[2])
      if len(set(position_set)) != 2:
        for position in set(position_set):
          if position_set.count(position) > 1:
            print '--- ' + string +'\nDuplicate at: ', position +'\n'
      if len(set(l10n_set)) > 1:
        id_dupl_l10n += 1
    elif size == 3:
      id_tripl += 1
      for case in db[string]:
        l10n_set.append(case['l10n'])
        position_set.append(case['position'].split('/',2)[2])
      if len(set(position_set)) != 3:
        for position in set(position_set):
          if position_set.count(position) > 1:
            print '--- ' + string +'\nDuplicate at: ', position +'\n'
      if len(set(l10n_set)) > 1:
        id_tripl_l10n += 1
    elif size == 4:
      id_quad += 1
      for case in db[string]:
        l10n_set.append(case['l10n'])
        position_set.append(case['position'].split('/',2)[2])
      if len(set(position_set)) != 4:
        for position in set(position_set):
          if position_set.count(position) > 1:
            print '--- ' + string +'\nDuplicate at: ', position +'\n'
      if len(set(l10n_set)) > 1:
        id_quad_l10n += 1
    else:
      id_multi += 1
      for case in db[string]:
        l10n_set.append(case['l10n'])
        position_set.append(case['position'].split('/',2)[2])
      if len(set(position_set)) != size:
        for position in set(position_set):
          if position_set.count(position) > 1:
            print '--- ' + string +'\nDuplicate at: ', position +'\n'
      if len(set(l10n_set)) > 1:
        id_multi_l10n += 1

print '2 entries with same id: ' + str(id_dupl)
print '2 entries with same id and l10n: ' + str(id_dupl_l10n)
print '3 entries with same id: ' + str(id_tripl)
print '3 entries with same id and l10n: ' + str(id_tripl_l10n)
print '4 entries with same id: ' + str(id_quad)
print '4 entries with same id and l10n: ' + str(id_quad_l10n)
print '>4 entries with same id: ' + str(id_multi)
print '>4 entries with same id and l10n: ' + str(id_multi_l10n)
print 'total ids: ' + str(ids) +'\n'
