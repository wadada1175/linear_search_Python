import time


data = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
        151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
        199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
        263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
        317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
        383, 389, 397, 401, 409, 419, 421, 431, 433, 439]

sum_time = 0

for i in range(len(data)):
    target = data[i] #探索する値(全て)

    start = time.perf_counter() #時間計測開始
    found = False  # ←処理状況を管理する（初期値はFalse）
    for j in range(len(data)):
        if data[j] == target:
            sec_time = time.perf_counter() - start
            print(data[j])
            print(f'処理時間は{sec_time:.6f}s')
            sum_time += sec_time #処理時間の合計
            found = True  # ←見つかったことを処理状況としてセット

    if not found:  # ←見つからなかった場合
        print('Not Found ')
        print(f'処理時間は{sec_time:.6f}s')

ave_time = sum_time/i #平均処理速度の計算
print(f'平均処理時間は{ave_time:.6f}s')
