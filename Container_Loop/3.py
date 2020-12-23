input_id=input("아이디를 입력해주세요.\n")

# real_easyeah = "easyeah"
# real_k8805 = "k8805"
members = ['easyeah','k8805']

for member in members :
    if member == input_id :
        print('Hello!, ' + member)
        import sys
        sys.exit()
print("who are you?")

# if real_easyeah == in_str :
#   print("Hello!, easyeah")
# elif real_k8805 == in_str :
#   print("Hello!, k8805")
# else :
#   print("Who are you")
