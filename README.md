# Surfs Up!
Weather analysis for potential surf and ice cream shop

### Overview

My client wants to open a surf and ice cream shop in Hawaii, but wants to make sure it will be profitable all year long. To accomplish this, I am taking data from weather stations across the island to check for temperature and precipitation records. Specifically, I'm looking at the weather in June and December, as those should be extreme ends of the weather spectrum. From there, the investors can decide if they think the weather is good for surfing and ice cream!

### Results

* The average temperature in June is about 75 F. The standard deviation is only about 3.3 degrees. This tells us that the temperature is very consistant. 

![June Temperature summary stats](https://github.com/caseykotowski/surfs_up/blob/main/june_temp.png)

* The average temperature in December is about 71 F. The standard deviation is about 3.7 degrees. So there is more variation in December, but not noticiably colder. 

![December Temperature summary stats](https://github.com/caseykotowski/surfs_up/blob/main/dec_temp.png)

* The low temp in December is 56 F, but the low temp in June is 64 F. The average temps are still very close, though which tells me that low dips are not frequent in December. 


### Summary

Overall, the temperature is very consistent, which means it should not impact profits througout the year. I do want to continue with two more queries. First, I want to check the average amounts of precipitation per month. In tropical climate, there can be a wet season. Dedicated surfers might not mind a little rain, but that could impact how much ice cream is purchased. I would also want to query the temperature/rain by weather station. This would let us pick which side of the island the shop should be located. It might be rainier in the north, or south and we should find that out. 
