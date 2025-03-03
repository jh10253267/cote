def solution(tickets):
    answer = []
    visited = {}
    ticket_dict = {}
    sorted_tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    
    for start, end in sorted_tickets:
        if start not in ticket_dict:
            ticket_dict[start] = []
        ticket_dict[start].append(end)
    
    for start, end in sorted_tickets:
        if (start, end) not in visited:
            visited[(start, end)] = 0
        visited[(start, end)] += 1
        
    answer = []
    def dfs(current):
        answer.append(current)
        # 종료조건
        if len(answer) == len(tickets)+1:
            return True
        # 경로가 끊긴경우
        if current not in ticket_dict:
            return False

        for end in ticket_dict[current]:
            if visited[(current, end)] > 0:
                visited[(current, end)] -= 1
                if dfs(end):
                    return True
                visited[(current, end)] += 1
                answer.pop()
                
        return False
    
    
    dfs("ICN")
    return answer