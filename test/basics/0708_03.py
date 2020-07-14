class Country:
    local = ''
    count = 0
    def addr(self, *others):
        self.gu, self.load = others
        Country.count += 1

if __name__ == "__main__":
    me = Country()
    you = Country()
    me.addr('   ','선유로')
    you.addr('    ','인사동길')
    print(me.local,me.gu,me.load)
    print(you.local,you.gu,you.load)
    print(f'{id(me.gu), id(you.gu)}')
    print(Country.count)