# # # # immutable mutable的差異
# # # # py裡面的所以變數都是物件，所以運作很慢

# # # def test1(x):
# # #     x+=1
# # # x=3
# # # test1(x)
# # # print(id(x))   # -> 4545529712
# # # print(x)   # -> 3
# # # # 原因是因為 global local 的差別，不可以混淆

# # # # 會變動
# # # def test2(data):
# # #     data['x']+=1
# # # dd = {'x':3, 'y':4}
# # # test2(dd)
# # # print(dd['x'])



# # # def test3(data):
# # #     # x=data[1]
# # #     # x+=1     # 不會變
# # #     data[1]+=1 # 會變
# # # li = [0,1,5]
# # # test3(li)
# # # print(li[1])



# # # 定义证书文件路径和密钥文件路径
# # certfile_path = '/Users/fangsiyu/Desktop/secrets/ssl_fullchain.pem'  # SSL 证书
# # keyfile_path = '/Users/fangsiyu/Desktop/secrets/ssl_privkey.pem'    # 私钥文件

# # # 读取证书文件内容
# # with open(certfile_path, 'r') as cert_file:
# #     cert_content = cert_file.read()
# #     print("Certificate Content:")
# #     print(cert_content)

# # # 读取密钥文件内容
# # with open(keyfile_path, 'r') as key_file:
# #     key_content = key_file.read()
# #     print("\nKey Content:")
# #     print(key_content)


# import os
# from jose import JWTError, jwt, ExpiredSignatureError
# from datetime import datetime, timedelta
# from fastapi import  HTTPException


# ALGORITHM = "RS256"
# private_key_path = os.getenv("PRIVATE_KEY_PATH")
# with open(private_key_path, 'r') as file:
#     PRIVATE_KEY = file.read()
# public_key_path = os.getenv("PUBLIC_KEY_PATH")
# with open(public_key_path, 'r') as file:
#     PUBLIC_KEY = file.read()
# def token_verifier(token: str):
#     try:
#         decoded_jwt = jwt.decode(token, PUBLIC_KEY, algorithms=ALGORITHM)
#         return decoded_jwt
    
#     except ExpiredSignatureError:
#         raise HTTPException(
#             status_code=405,
#             detail="Token has expired, please login again.",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     except JWTError:
#         raise HTTPException(
#             status_code=401,
#             detail="the JWT token could not be validated",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
    

# token_verifier()

# token = request.cookies.get("access_token")
# if not token:
#     content_data = {"error": True, "message": "Please log-in to access the booking page."}
#             return JSONResponse(status_code=403, content=content_data, headers=headers)
        
#         try:
#             token_output = token_verifier(token)
#         except HTTPException as e:
#             # 处理token无效或过期的情况
#             content_data = {"error": True, "message": e.detail}
#             return JSONResponse(status_code=e.status_code, content=content_data, headers=headers)