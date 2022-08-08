def cat_say(ip):
    print("            {}".format('_'*len(ip)))
    print("          < {} >".format(ip))
    print("            {}".format('-'*len(ip)))
    print("            /")
    print(" /\_/\     /")
    print("( o.o )  ")
    print(" > ^ <  ")

def main():
    ip = input("Enter the input to be displayed :")
    cat_say(ip)

if __name__ == '__main__':
    main()