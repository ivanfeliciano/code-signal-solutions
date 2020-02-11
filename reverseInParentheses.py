def reverseInParentheses(s):
	ans = ""
	i_lbracket_stack = []
	for i in range(len(s)):
		if s[i] == "(":
			i_lbracket_stack.append(i)
		if s[i] == ")":
			i_last_bracket = i_lbracket_stack.pop()
			substr = s[i_last_bracket + 1 : i][::-1]
			s = s[:i_last_bracket + 1] + s[i_last_bracket + 1 : i][::-1] + s[i:]
	ans = s.replace("(", "")
	ans = ans.replace(")", "")
	return ans

def main():
	s = "foo(bar(baz))blim"
	print(s)
	print(reverseInParentheses(s))

if __name__ == '__main__':
	main()