def common_element(l1,l2):
    common = []

    for element in l1:
        if element in l2 and element not in common:
         common.append(element)

    return common

l1=[5,6,7,3,4]
l2=[3,6,8,9,1]

common = common_element(l1,l2)
print("the common elements are:",common)


