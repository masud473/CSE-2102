def forall(domain,predicate):
    return all(predicate(x) for x in domain)
def forany(domain,predicate):
    return any(predicate(x) for x in domain)

p1= lambda x: x*x<=16
p2=lambda x:x*x==25
domain ={1,2,3,4,5}


def not_forall(domain,predicate):
    return any(not predicate(x) for x in domain)
def not_forany(domain,predicate):
    return all(not predicate(x) for x in domain)

print(not_forall(domain,p1))
print(not_forany(domain,p2))


