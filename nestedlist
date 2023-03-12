if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total=0
    for i,j in student_marks.items():
        if i==query_name:
            for a in j:
                total+=a/3
    print("%.2f" %total)
        
           
        
