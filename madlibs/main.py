print("Enter values for : ")
inputs={'food':3,'name':3,'adjective':1,'noun':4,'verb':3}

for k,v in inputs.items():
    ls=list()
    for i in range(v):
        ls_val=input(f"{k} : ")
        ls.append(ls_val)
    inputs[k]=ls


madlibs=f'It was {inputs["food"][0]} day at school, and {inputs["name"][0]} was super {inputs["adjective"][0]} for lunch. But when she went outside to eat, a {inputs["noun"][0]} stole her {inputs["food"][1]}! {inputs["name"][1]} chased the {inputs["noun"][1]} all over school. She {inputs["verb"][0]}, {inputs["verb"][1]}, and {inputs["verb"][2]} through the playground. Then she tripped on her {inputs["noun"][2]} and the {inputs["noun"][3]} escaped! Luckily, {inputs["name"][2]}’s friends were willing to share their {inputs["food"][2]} with her.'

print(madlibs)