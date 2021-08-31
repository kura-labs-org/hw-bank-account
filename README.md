# Bank Account Class Homework

So for this assignment, I originally started with a dictionary that contained account number and user names. I also had another string that contained balance info but I felt it was too complicated to parse through two different data types. 

After some digging I found out you can put a list in a dictionary so I went with this. In the key value pair of a dictionary, the key is the user's name and the value is a list which contains account number (in index 0), account balance (in index 1) and everything after contains a list of transactions.

There are 3 users with 3 different pins
Ricardo Deodutt - 877393
Daniel Adeyanju - 123456
Saiho Yip - 112233

There is a verification method that basically looks up the user's pin. If its false it keeps asking the user to input it. I found the deposit and withdraw methods to be very similar to each other. They both append the transaction to the list in the key value pair. Transfer was very simple also.

Overall, I wrote comments for every line so people can understand. If I had to redo this project I would try to introduce databases. When I used databases for the Flask homework, I found it very interesting. I hope you go over databases in class a little more because I feel it's a very important topic.
