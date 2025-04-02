def solution(info, n, m):
    ckpt = {0:0}
    for x, y in info:
        n_ckpt = {}
        for xx, yy in ckpt.items():
            if xx + x < n:
                if xx + x not in n_ckpt or n_ckpt[xx+x] > yy:
                    n_ckpt[xx + x] = yy
            if yy + y < m:
                if xx not in n_ckpt or n_ckpt[xx] > yy + y:
                    n_ckpt[xx] = yy + y
        if n_ckpt:
            ckpt = n_ckpt
        else:
            return -1
    return min(ckpt.keys())