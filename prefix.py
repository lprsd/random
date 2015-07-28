def prefix_eval(formula):
    x, stack = reversed(formula.split()), []
    for el in x:
        try:
            stack.append(int(el))
        except:
            op1, op2 = stack.pop(), stack.pop()
            stack.append(eval('%s%s%s'%(op2,el,op1),{},{}))
    return stack[0]

print prefix_eval("9")
print prefix_eval("+ 1 2")
print prefix_eval("+ + 1 2 30")
print prefix_eval("+ + 12 16 * 10 4")

#Output
9
3
33
68
[Finished in 0.1s]