class tupple_elements:
    def to_sum(self,numbers,target):

        lookup={}

        for i,j in enumerate(numbers):

            if target-j in lookup:
                return(lookup[target-j],i)

            lookup[j]=i

val=int(input("enter sum which u want to add search for"))

print(tupple_elements().to_sum((10,20,30,40,50,70,60),val))

