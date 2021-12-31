input_file = open('crime_scene.txt', 'r')
W, T = input_file.readline().split()
W, T = int(W), int(T)
N = int(input_file.readline())
evidencelst = input_file.read().split('\n')
input_file.close()
evidence_dict = dict()
recentlst_of_evidence = list()
evidence_combination_lst = list()
for i in range(len(evidencelst)):
    if evidencelst[i]!='':
        evidence_lst = [int(k) for k in evidencelst[i].split()]
        evidence_dict[evidence_lst[0]] = evidence_lst[1:]
evidence_id_lst = list(evidence_dict.keys())
max_value=0
max_id_list=[]
max_weight_value=0
max_id_weight_list=[]
max_time_value=0
max_id_time_list=[]
i=0
def forsort(value_list):
    for i in range(len(value_list)):
        for k in range(i+1,len(value_list)):
            if value_list[i]>value_list[k]:
                value_list[i], value_list[k] = value_list[k], value_list[i]
    return value_list
def cweight_check(evidence):
    if 0==len(evidence):
        return 0
    return evidence_dict[evidence[0]][0] + cweight_check(evidence[1:])
def ctime_check(evidence):
    if 0 == len(evidence):
        return 0
    return evidence_dict[evidence[0]][1] + ctime_check(evidence[1:])
def recent_value(evidence):
    if 0 == len(evidence):
        return 0
    return evidence_dict[evidence[0]][2] + recent_value(evidence[1:])
def weight_check(evidence):
    if cweight_check(evidence)>W:
        return False
    return True
def time_check(evidence):
    if ctime_check(evidence)>T:
        return False
    return True
def evidence_combination(gvnlst):
    if len(gvnlst) == 0:
        #if any problem occurs in that part while checking with tester please change global with nonlocal
        global max_value
        global max_id_list
        global max_weight_value
        global max_id_time_list
        global max_id_weight_list
        global max_time_value
        if weight_check(recentlst_of_evidence) and time_check(recentlst_of_evidence):
                if recent_value(recentlst_of_evidence)>max_value:
                    max_id_list=[]
                    max_value = recent_value(recentlst_of_evidence)
                    max_id_list.extend(recentlst_of_evidence)
        if weight_check(recentlst_of_evidence):
            if recent_value(recentlst_of_evidence)>max_weight_value:
                max_id_weight_list=[]
                max_weight_value=recent_value(recentlst_of_evidence)
                max_id_weight_list.extend(recentlst_of_evidence)
        if time_check(recentlst_of_evidence):
            if recent_value(recentlst_of_evidence)>max_time_value:
                max_id_time_list=[]
                max_time_value=recent_value(recentlst_of_evidence)
                max_id_time_list.extend(recentlst_of_evidence)

        return
    evidence_combination(gvnlst[1:])
    recentlst_of_evidence.append(gvnlst[0])
    evidence_combination(gvnlst[1:])
    recentlst_of_evidence.pop()

evidence_combination(evidence_id_lst)
solutionpart1=open('solution_part1.txt', 'w')
max_id_weight_liststr=[]
for k in (forsort(max_id_weight_list)):
    max_id_weight_liststr.append(str(k))
solutionpart1.write(str(max_weight_value)+'\n'+' '.join(max_id_weight_liststr))
solutionpart1.close()

solutionpart2=open('solution_part2.txt', 'w')
max_id_time_liststr=[]
for k in (forsort(max_id_time_list)):
    max_id_time_liststr.append(str(k))
solutionpart2.write(str(max_time_value)+'\n'+' '.join(max_id_time_liststr))
solutionpart2.close()

solutionpart3=open('solution_part3.txt', 'w')
max_id_liststr=[]
for k in (forsort(max_id_list)):
    max_id_liststr.append(str(k))
solutionpart3.write(str(max_value)+'\n'+' '.join(max_id_liststr))
solutionpart3.close()
