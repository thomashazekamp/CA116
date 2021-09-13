#!/usr/bin/env python3

home_goals = 3
home_points = 5
away_goals = 2
away_points = 6

home_score = home_goals * (7 + home_points)
away_score = away_goals * (7 + away_points)

if home_score < away_score:
  print ("away win")
elif away_score < home_score:
  print ("home_win")
else:
  print ("draw")
