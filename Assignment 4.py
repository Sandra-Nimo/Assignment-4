#list of car brands available
cars={'Nissan', ' BMW Group', 'Tesla', 'Ford General Motors', 'Hyundai', 
'Jeep', 'Mazda', 'Lexus', 'Honda motor company', 'Cadillac', 'Subaru',
'Toyota', 'Audi', 'Volvo', 'Porsche', 'Kia', 'Chrysler', 'Buick', 
'Subaru', 'Honda', 'Infinity', 'Ferari', 'Bugatti', 'Rolls Royce', 
'Maserati', 'Alfa Romeo','Jaguar', 'Volkswagen', 'Peugeot','Mercedes Benz'}
models={'Hyundai Elantra':150000,'Jeep Wrangler':200000, 'Mazda 3':180000, 
'Lexus 15':300000, 'Honda Civic':250000, 'Cadillac CTS':750000, 
'Sabaru Forester':90000, 'Toyota Corolla':60000, 'Audi R8':20000, 
'Volvo XC60':71000, 'Porsche 911':800000, 'KIA Morning':240000, 
'Chrysler Sebring':600000, 'Bruick Enclave':900000, 'Infiniti Q50':850000,
'Ferari 458Italia':2000000, 'Bugatti Veyron':3000000, 
'Rolls-Royce Ghost':5200000, 'Peugeot 3008':280000}
#get user input for cars
brandOfCars=input('What brand of cars are interested in purchasing? : ')
#check iif brand of car is in available list of cars
if brandOfCars in cars:
    print('Yes, it is available.')
else:
    print('sorry, it is not available.')
#if brand of car is available, specify model
modelOfCar=input('What specific car model are you interested in? ')
if modelOfCar in models :
    print('Yes, it is available.')
    priceOfCar=models[modelOfCar]
    print('The price is ${}.'.format(priceOfCar))
else:
    print('sorry, that model is not available.')
                      
        




          