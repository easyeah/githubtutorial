puts ("아이디를 입력해주세요.\n")
input_id = gets.chomp()
puts("비밀번호를 입력해주세요.\n")
input_pwd = gets.chomp()

real_id = "easyeah"
real_pwd = "11"

if real_id == input_id and real_pwd == input_pwd
  puts("Hello!")
else
  puts("Wrong Id & Password")
end
