puts("아이디를 입력해주세요.\n")
input_id= gets.chomp()
# real_easyeah = "easyeah"
# real_k8805 = "k8805"
members = ['easyeah','k8805']

for member in members do
    if member == input_id
        print('Hello!, ' + member)
        exit
    end
end
print("who are you?")
