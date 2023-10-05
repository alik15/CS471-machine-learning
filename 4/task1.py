import pandas


names_and_cms ={"fahad":337795,"hamdah":345592,"maryam":229938}

serialized_names_and_cms=pandas.Series(names_and_cms)

print(serialized_names_and_cms)

print(pandas.DataFrame(serialized_names_and_cms))