import json
def main():
    input_file='./analytics.log'
    output_file='./endpoint_analytics.json'
    dict_analytics={}

    with open(input_file) as analytics:
        content = analytics.readlines()
        content = [x.strip() for x in content]
        content = [x.split() for x in content]
        content = [x[9] for x in content]
        for x in content:
        	a=x.split(",")
        	endpoint = a[0]
        	if endpoint in dict_analytics:
        		dict_analytics[endpoint] += 1
        	else:
        		dict_analytics[endpoint] = 1

    with open(output_file, 'w') as json_file:
    	json.dump(dict_analytics, json_file)
           
main()

