import twint

# Configure
c = twint.Config()
c.Search = "fpi ditembak"
c.Lang = "in"
#! c.Since = "2020-01-01"
#! c.Until = "2020-04-25"
c.Limit = 500

# c.Output = "./test.csv"
# c.Store_csv = True
c.Count = True

# Run
twint.run.Search(c)
