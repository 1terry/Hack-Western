
class API:
    dict = {}
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

        data_list = data.decode("utf-8").split("}")
        # code for calories and attributes

        for i in range(1, len(data_list)-3):
            if (data_list[i]) != "":
                index = data_list[i].find('label')+8
                nutrient = ''
                while data_list[i][index] != "\"":
                    nutrient = nutrient + data_list[i][index]
                    index += 1
                print(nutrient)

                index = data_list[i].find('quantity') + 10
                value = ''
                while data_list[i][index] != ",":
                    value = value + data_list[i][index]
                    index += 1
                index = data_list[i].find('unit') + 7
                while data_list[i][index] != "\"":
                    value = value + data_list[i][index]
                    index += 1
                print(value)


api = API()
api.call_api("1", "tablespoon", "honey")




