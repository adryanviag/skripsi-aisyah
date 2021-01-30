import twint

c = twint.Config()
c.Search = "penurunan ukt"
# c.Limit = 0
c.Count = True

twint.run.Search(c)
