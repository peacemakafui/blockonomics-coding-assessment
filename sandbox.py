import seder

#This Test Case Just takes in a simple nested dictionary
# test_dict1 = {'a':1,'b':'two','c':'three','d':2.5,'e':89,'f':'dabce in the moon',1:'vbn',5:'cgn','qw':{'s':23,'asdf':'me'}}
# seder.serialize(test_dict1,'myFileName')
# my_dict = seder.deserialize('myFileName.bin')
# print(my_dict)


#This Test Case takes in a nested dictionary with an array
# test_dict_list = {'t':'cl','f':{1:'cv'},1:{'ls':['my',3,23]}}
# seder.serialize(test_dict_list,'myFileName2')
# my_dict = seder.deserialize('myFileName2.bin')

#This Test Case takes in a large dict
# large_dict ={"id": "0001","type": "donut","name": "Cake","ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" },
# 						{ "id": "1002", "type": "Chocolate" },
# 						{ "id": "1003", "type": "Blueberry" },
# 						{ "id": "1004", "type": "Devil's Food" }
# 					]}, 
# 				"topping":[{ "id": "5001", "type": "None" },
# 				{ "id": "5002", "type": "Glazed" },
# 				{ "id": "5005", "type": "Sugar" },
# 				{ "id": "5007", "type": "Powdered Sugar" },
# 				{ "id": "5006", "type": "Chocolate with Sprinkles" },
# 				{ "id": "5003", "type": "Chocolate" },
# 				{ "id": "5004", "type": "Maple" }],

# 				"id1": "0002",
# 				"type1": "donut",
# 				"name1": "Raised",
# 				"ppu1": 0.55,
# 				"batters1":
# 					{
# 						"batter1":
# 							[
# 								{ "id": "1001", "type": "Regular" }
# 							]
# 					},
# 				"topping1":
# 					[
# 						{ "id": "5001", "type": "None" },
# 						{ "id": "5002", "type": "Glazed" },
# 						{ "id": "5005", "type": "Sugar" },
# 						{ "id": "5003", "type": "Chocolate" },
# 						{ "id": "5004", "type": "Maple" }
# 					],

# 							"id3": "0003",
# 		"type3": "donut",
# 		"name3": "Old Fashioned",
# 		"ppu3": 0.55,
# 		"batters3":
# 			{
# 				"batter3":
# 					[
# 						{ "id": "1001", "type": "Regular" },
# 						{ "id": "1002", "type": "Chocolate" }
# 					]
# 			},
# 		"topping3":
# 			[
# 				{ "id": "5001", "type": "None" },
# 				{ "id": "5002", "type": "Glazed" },
# 				{ "id": "5003", "type": "Chocolate" },
# 				{ "id": "5004", "type": "Maple" }
# 			],
# 					"id3": "0003",
# 		"type3": "donut",
# 		"name3": "Old Fashioned",
# 		"ppu3": 0.55,
# 		"batters3":
# 			{
# 				"batter3":
# 					[
# 						{ "id": "1001", "type": "Regular" },
# 						{ "id": "1002", "type": "Chocolate" }
# 					]
# 			},
# 		"topping3":
# 			[
# 				{ "id": "5001", "type": "None" },
# 				{ "id": "5002", "type": "Glazed" },
# 				{ "id": "5003", "type": "Chocolate" },
# 				{ "id": "5004", "type": "Maple" }
# 			],
# 				"id4": "0003",
# 		"type4": "donut",
# 		"name4": "Old Fashioned",
# 		"ppu4": 0.55,
# 		"batters4":
# 			{
# 				"batter4":
# 					[
# 						{ "id": "1001", "type": "Regular" },
# 						{ "id": "1002", "type": "Chocolate" }
# 					]
# 			},
# 		"topping4":
# 			[
# 				{ "id": "5001", "type": "None" },
# 				{ "id": "5002", "type": "Glazed" },
# 				{ "id": "5003", "type": "Chocolate" },
# 				{ "id": "5004", "type": "Maple" }
# 			],
			
# 		"id5": "0003",
# 		"type5": "donut",
# 		"name5": "Old Fashioned",
# 		"ppu5": 0.55,
# 		"batters5":
# 			{
# 				"batter5":
# 					[
# 						{ "id": "1001", "type": "Regular" },
# 						{ "id": "1002", "type": "Chocolate" }
# 					]
# 			},
# 		"topping5":
# 			[
# 				{ "id": "5001", "type": "None" },
# 				{ "id": "5002", "type": "Glazed" },
# 				{ "id": "5003", "type": "Chocolate" },
# 				{ "id": "5004", "type": "Maple" }
# 			]


# }
# seder.serialize(large_dict, 'myFileName3')
# my_dict = seder.deserialize('myFileName.bin')
