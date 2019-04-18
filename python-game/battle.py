# let's battle
# simulation site https://yys.lufernew.com/#/guess/submit
# bougyoryoku keisannshiki shuttenn http://puyopuyo03.blogspot.com/2017/04/blog-post_54.html
temple = ['攻撃力','HP','防御力','素早さ','会心率','会心DMG','効果命中','効果抵抗','御魂(効果ごとに命令)']

Heiyou = [3014,20714,635,212,0.05,1.50,0.90,1.12]
Hannya = [3810,15297,731,210,0.10,1.50,0.9,1.12]

# xに自分の防御力, yに相手の攻撃力を代入
def dmg(x, y):
    my_keigenritsu =  1 - x/(x + 300)
    return y*my_keigenritsu

while Heiyou[1] > 0 or Hannya[1] > 0:
    if Heiyou[3]>Hannya[3]:
        Hannya[1] =- dmg(Hannya[2], Heiyou[0])
        print('ヘイヨウは般若に攻撃！般若のHPは↓になった！')
        print(Hannya[1])
        if Hannya[1] <= 0:
            break

        Heiyou[1] =- dmg(Heiyou[2], Hannya[0])
        print('般若はヘイヨウに攻撃！ヘイヨウのHPは↓になった！')
        print(Heiyou[1])

    else:
        print('これが表示されたらコードミスあり')

# 以下は早く改善したい　もうちょい何とかなるはず
# 現行案：グループのHPの和が０なら負け　or　グループのHPの和が大きい方が勝ち

if Heiyou[1] == 0:
    print('般若の勝ち')
else:
    print('ヘイヨウの勝ち')

total = 0
for val in range(40):
    total += val
    print(' ')
