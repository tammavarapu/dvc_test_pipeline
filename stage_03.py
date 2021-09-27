
with open('artifacts_01.txt','r') as rf:
    rf_text = rf.read()

with open('artifacts_02.txt','w') as wf:
    wf_text = wf.write(rf_text + "added lines")


print(wf_text)
print("stage 03 is completed!")