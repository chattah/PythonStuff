score = raw_input('Please enter a score between 0.0 and 1.0: ')
grade = ''

try:
    score = float(score)
    if score > 1: raise ValueError('Score was out of range')
except:
    print 'Error: Please enter a number between 0.0 and 1.0'
    quit()

if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'

print grade
