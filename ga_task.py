# Author: Fernando Brandao

divider = "--------------------------------------------------------------------"

# Question 1
# S​uppose you are running a split test at your startup and you want to test a
# new landing page foryour users (call it ​Page B​, compared to the current one, ​Page A​).●
# Each user has a user_id, e.g.: 1, 2, 3, 4, 5..., 1001,..●
# Users who have an ​odd​ id will be in the experimental group (they will get Page B)●
# Users who have an ​even​ id will be in the control group (they will get Page A)

# Write a function `user_in_experiment` that takes a user_id (integer)
# and returns ​True​ if the user_id is odd and hence the user is in the experimental group,
# or returns ​False ​otherwise.

user_id = 12

def user_in_experiment(user_id):
    if(int(user_id % 2) == 0):
      return False
    else:
      return True
print(user_in_experiment(user_id))

print(divider)
# Question 2
# At this same startup, which happens to be a restaurant recommendation service,
# we want to add a website feature where users can filter by just the popular restaurants.

# Write a function `get_popular_restaurants` that takes a list of restaurant 'names' and
# returns only the ones that are in the popular list.
# Here's the popular list:
# POPULAR_RESTAURANTS = ['Laut', 'Rosa Mexicano', 'Ootoya', 'Dig Inn']

restaurant_list = ['Laut', 'Rosa Mexicano', 'Ootoya', 'Dig Inn', 'Nandos', 'Pizza Express']

def get_popular_restaurants(restaurant_lists):

  popular_restaurants = ['Laut', 'Rosa Mexicano', 'Ootoya', 'Dig Inn']

  if(restaurant_lists in popular_restaurants):
    return True
  else:
    return False

filtered_restaurants = filter(get_popular_restaurants, restaurant_list)

print('The most popular restaurants are: ')
for popular in filtered_restaurants:
  print(popular)

print(divider)
# Question 3
# At our amazing restaurant recommendation startup, we want to sort restaurants by rating.
# Given the following restaurant data below,
#
# write a function that returns a list of restaurants,
# sorted by rating (out of 10), from ​highest​ to ​lowest​.
# Restaurant Data:

restaurants = [{'name': 'Ootoya', 'rating': 8.0},
              {'name': 'Chipotle', 'rating': 6.6},
              {'name': 'Burger&Lobster', 'rating': 7.2},
              {'name': 'Laut', 'rating': 8.1}]

print("The top rated restaurants are: ")
print(sorted(restaurants, key = lambda i: i['rating'], reverse=True))

print(divider)
# Question 4
# Suppose we work at a company where our ​x^2 - 49 = COST​, and ​x​ is the number of facilitieswe manage.
# What value of​ x​ will make our ​COST​ equal to zero?

x = 7
cost = x**2 - 49
print(cost)

print(divider)
# Question 5
# Suppose we are at that same company and ​REVENUE = -x^2 + 5x +7​.
# What value of ​x maximizes revenue?

x = 2.5
revenue = (-x**2) + (5*x) + 7
print(revenue)
