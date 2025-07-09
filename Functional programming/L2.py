# consonents in the string

string='luminartechnlab'
v='aeiou'
lst=len([i for i in string if i not in v])
print(lst)