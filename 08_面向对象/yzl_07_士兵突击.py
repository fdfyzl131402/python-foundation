class Gun:
    def __init__(self, model):
        """定义属性"""
        # 1.枪的型号
        self.model = model
        # 2.枪的子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        """装填子弹"""
        self.bullet_count += count

    def shoot(self):
        """发射"""
        # 1.检查子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了...")
            return
        # 2.发射子弹 -1
        self.bullet_count -= 1
        # 3.提示发射信息
        print("【%s】 突突突...【%d】" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):

        # 1.定义姓名
        self.name = name
        # 2.枪  - 新兵没有枪
        self.gun = None

    def fire(self):

        # 1.判断士兵有没有枪
        # if self.gun == None:
        if self.gun is None:
            print("[%s] 没有枪..." % self.name)

            return
        # 2. 高喊口号
        print("冲啊...【%s】" % self.name)
        # 3.让枪装上子弹
        self.gun.add_bullet(50)
        # 4.开枪
        self.gun.shoot()


# 1.创建枪对象
ak47 = Gun("AK47")


# 2.创造许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)