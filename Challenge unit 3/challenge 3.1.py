def linearsearchproduct(productlist, targetproduct):
 indices =[]
 for index,product in enumerate(productlist):
  if product == targetproduct:
    indices.append(index)
 return indices
#Example usage:
products  =["Shoes","Boot","loafer","Shoes","Sandal","Shoes"]
target ="Shoes"
result =linearsearchproduct(products, target)
print(result)
