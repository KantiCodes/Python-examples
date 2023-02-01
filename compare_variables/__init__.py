# file should run wihout any assertion error

a = 3
b = 3

assert a is b

aa = [1,2,3]
bb = [1,2,3]

assert aa == bb
assert aa is not bb

aaa = [[1,2,3]]
bbb = [[1,2,3,]]

assert aaa == bbb
assert aaa[0] == bbb[0]
assert aaa is not bbb