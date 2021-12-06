import numpy

# 返回风力和风向
def uv2wsd(x, y):
    import numpy as np
    ws = np.sqrt(x ** 2 + y ** 2)
    wd = np.arctan2(y, x)
    wd = np.degrees(wd)  # 将弧度转化为角度
    return (ws, wd)

if __name__ == "__main__":
    ws, wd = uv2wsd(10, -10)
    print(ws, wd)