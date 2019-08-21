# dependencies
import random
import os
from PIL import Image
import math

def colorDiff(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def showPixel(x, y):
    for i in range(5):
        for j in range(5):
            img.putpixel((x - i, y - j), (0, 0, 0))


# 小人的底部颜色标识点
# 标识点选法：打开PS，->选择 ->色彩范围，容差设为0，使用吸管工具找底部连续同色区域
# 使用此法可以找到相对不动点，加固定偏移量可获得底部中心坐标
tokenC = (54, 60, 102)
def isToken(p):
    return colorDiff(p, tokenC) <= 1


if __name__ == '__main__':
	
	# 随机选取一个图片
	imgDir = '/home/kesci/input/jump6799'
	imgPath = random.choice(list(os.path.join(imgDir, name) for name in os.listdir(imgDir)))

	img = Image.open(imgPath)

	w, h = img.size


	tokenX, tokenY = 0, 0
	tokenXs = []

	boardX, boardY = 0, 0
	boardWidth = 0
	widthCnt = 0

	DIFF_THERESHOLD = 10

	# 寻找小人
	for i in range(h):
	    if i < h/3:
	        continue
	    tokenL, tokenR = 0, 0
	    # 左边界
	    for j in range(w):
	        p = img.getpixel((j, i))
	        if isToken(p):
	#             showPixel(j, i)
	            tokenL = j
	            tokenY = i
	            break
	    # 右边界
	    if tokenL:
	        for k in range(w):
	            j = w - k - 1
	            if j < tokenL:
	                break
	            p = img.getpixel((j, i))
	            if isToken(p):
	#                 showPixel(j, i)
	                tokenR = j
	                break
	    # 中心点
	    if tokenR:
	        tokenXs.append((tokenL + tokenR)/2)
	        
	# 微调, 定位 token 的底座中心点
	tokenX = sum(tokenXs)/len(tokenXs) + 5 
	tokenY = tokenY - 15

	showPixel(int(tokenX), tokenY)

	# 寻找跳板
	lastL, lastR = 0, 0

	for i in range(h):
	    if i < h/3:
	        continue
	    boardL, boardR = 0, 0
	    base = img.getpixel((0, i))
	    # 左边界
	    for j in range(w): 
	        # 跳过小人周围像素
	        if abs(j - tokenX) < 45:
	            continue
	        p = img.getpixel((j, i)) 
	        diff = colorDiff(p, base)
	        if diff > DIFF_THERESHOLD:
	            showPixel(j, i)
	            boardL = j
	            break
	    #右边界
	    if boardL:
	        for k in range(w):
	            j = w - k - 1
	            # 跳过小人周围像素
	            if abs(j - tokenX) < 45:
	                continue
	            if j < boardL:
	                break
	            p = img.getpixel((j, i)) 
	            diff = colorDiff(p, base)
	            if diff > DIFF_THERESHOLD:
	                showPixel(j, i)
	                boardR = j
	                break
	    if boardR:
	        if not boardX:
	            boardX = (boardR + boardL)/2
	        width = boardR - boardL + 1
	        if width > boardWidth:
	            boardWidth = width
	            widthCnt = 0
	        else:
	            boardY = i
	            # 这里连续寻找多次边界，防止圆形跳台的局部宽度稳定
	            widthCnt += 1
	            if widthCnt == 15:
	                break
	                
	# 减去多次边界寻找产生的溢出量
	boardY = boardY - 15

	showPixel(int(boardX), boardY)