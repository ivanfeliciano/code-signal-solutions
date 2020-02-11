def firstNotRepeatingCharacter(s):
	chars_set = set()
	not_answers = set()
	for i in s:
		if i not in chars_set:
			chars_set.add(i)
			continue
		not_answers.add(i)
	print(chars_set)
	print(not_answers)
	for i in not_answers:
		s= s.replace(i, "")
	return s[0] if len(s) > 0 else "_"

print(firstNotRepeatingCharacter("abacabad"))
