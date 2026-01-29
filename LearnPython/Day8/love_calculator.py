def calculate_love_score(name1, name2):
   combined_name = name1+name2

   combined_name.lower()

   t = combined_name.count("t")
   r = combined_name.count("r")
   u = combined_name.count("u")
   e = combined_name.count("e")

   l = combined_name.count("l")
   o = combined_name.count("o")
   v = combined_name.count("v")
   e = combined_name.count("e")
   true = t+r+u+e
   love = l+o+v+e
   score = int(str(true) +(str(love)))

   print(score)
    

calculate_love_score("Kanye West", "Kim Kardashian")  