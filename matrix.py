import torch

#проверка на доступность
if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

m, n, p, k = 4, 4, 4 , 4 

# задаем входящие тензоры
A = torch.randn(m, n).to(device)
B = torch.randn(p, k).to(device)




# функция
C = torch.mm(A, B) 


print(C)
print(C.shape)