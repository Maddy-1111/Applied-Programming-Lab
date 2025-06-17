# def dedup(l):
#     X = {}
#     out = []
#     for i in range(len(l)):
#         if l[i] in X:
#             continue
#         else:
#             X[l[i]] = 1
#             out.append(l[i])
    
#     return l

# l = [4, 2, 9, 4, 7, 2, 5]

# print(dedup(l))

def create_poly_func(degree):
    return lambda x, *params : sum(params[i] * x**i for i in range(degree+1))

quadratic = create_poly_func(2)
y_data = quadratic(x_data, 1, 2, 1)