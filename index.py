import twint

# Configure
c = twint.Config()
c.Search = "#sawitbaik"
c.Lang = "in"
#! c.Since = "2020-01-01"
c.Until = "2019-09-16"

c.Output = "./sawit_baik.csv"
c.Store_csv = True
c.Count = True

# Run
twint.run.Search(c)
