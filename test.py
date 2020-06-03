def longestPalindrome(self,s):
	reversedS = reverse(s)
	palindrome = ""
	for index, char in enumerate(s):
		if char == reversedS[index]:
			palindrome.append(char)
		else:
			break
	return palindrome

				


s = "tracecars"
print(longestPalindrome(s))
