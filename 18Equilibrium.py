def solution(A):
    # 2 daste chap o rast mikonim
    sum_left = A[0]#yedune tu chap baghie tu rast
    sum_right = sum(A) - A[0]
    diff = abs(sum_left - sum_right)#ekhtelaf ro ba ghadre motlagh migirim
    for i in range(1, len(A)-1):# be tedad araye ha yki kamtar
        sum_left += A[i]#be daste chap ezafe o b daste rast kam mikonim
        sum_right -= A[i]
        current_diff = abs(sum_left - sum_right)#ghadre motlagh jadid ro gerefte o moghayesash mikonim
        if diff > current_diff:
            diff = current_diff
    return diff



print(solution([3, 1, 2, 4, 3]))
