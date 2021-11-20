
class API:

    def __init__(self):
        import http.client
        self.conn = http.client.HTTPSConnection("edamam-edamam-nutrition-analysis.p.rapidapi.com")

        self.headers = {
            'x-rapidapi-host': "edamam-edamam-nutrition-analysis.p.rapidapi.com",
            'x-rapidapi-key': "83a686583amsh4b5dd474b143968p1989f2jsnf3a850b88cd6"
        }

    def call_api(self, count, unit, item_name):
        data = "/api/nutrition-data?ingr=" + count + "%20" + unit + "%20" + item_name
        self.conn.request("GET", data, headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))



