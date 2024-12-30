from collections import defaultdict

def solution(id_list, report, k):
    report_set = set(report)
    reported_counts = defaultdict(int)
    notifications = defaultdict(int)
    
    for report_entry in report_set:
        reporter, reported = report_entry.split()
        reported_counts[reported] += 1
    
    for report_entry in report_set:
        reporter, reported = report_entry.split()
        if reported_counts[reported] >= k:
            notifications[reporter] += 1
    
    return [notifications[user_id] for user_id in id_list]