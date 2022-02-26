#https://programmers.co.kr/learn/courses/30/lessons/92334
# 2022카카오/레벨1/신고 결과 받기
# 2022.02.19  15분

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    report_cnt = dict()
    report_mail = dict()
    for id in id_list:
        report_cnt[id] = 0
        report_mail[id] = 0
    report = set(report) ## 중복 처리 신고

    for r in report:
        report_cnt[r.split(' ')[1]] += 1

    for r in report:
        if report_cnt[r.split(' ')[1]] >= k:
            report_mail[r.split(' ')[0]] += 1

    return list(report_mail.values())

solution(id_list,report,k)