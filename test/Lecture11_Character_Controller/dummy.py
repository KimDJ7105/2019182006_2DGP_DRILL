class Star:
    name = 'Star'
    x = 100

    def change():
        x = 200
        print('x is ', x)

print('x is ', Star.x)
Star.change()

star = Star()
print(type(star))
print(star.x)

#star.change == Star.change(star) so error occur