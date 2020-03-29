#bmi
h,w=eval(input())
bmi=w/pow(h,2)
print("BMI数值为:{:.2f}".format(bmi))
who,nat="",""#国内，国际
if bmi<18.5:
    who,nat="偏瘦","偏瘦"#国内，国际
elif 18.5<=bmi<=24 :
    who,nat="正常","正常"#国内，国际
elif 24<bmi<25:
    who,nat="偏胖","正常"#国内，国际
elif 25<=bmi<28:
    who,nat="偏胖","偏胖"
elif 28<=bmi<30:
    who,nat="肥胖","偏胖"
else:
    who,nat="肥胖","肥胖"
print("BMI指标为:国际'{}',国内'{}'".format(nat,who))
    
    
