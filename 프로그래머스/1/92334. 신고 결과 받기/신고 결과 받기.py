def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported_dict = {x:0 for x in id_list}
    report = set(report)
    
    for r in report:
        reported_user = r.split()[1]
        reported_dict[reported_user] += 1
    for r in report:
        report_user, reported_user = r.split()
        if reported_dict[reported_user] >= k:
            answer[id_list.index(report_user)] += 1    
    
    return answer