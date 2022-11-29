# CTB CLONE PYGAME

*by Aaron Zhang A01316218*

**future feature todo**
  - usernames
  - graphical stage selection
  - better stage creation / editing
  - variable movement speed and fall speed modifiers

## Controls

**A / Left Arrow** - move left

**D / Right Arrow** - move right

**Left Shift** - boost

## Gameplay

Catch the points as they fall from the top of the screen.

![gameplay](images/gameplay.png)

Different points are worth different score values:

![310](sprites/point_boost.png)
**310 points**

![300](sprites/point_300.png)
**300 points**

![100](sprites/point_100.png)
**100 points**

Try to maintain your combo by catching points without missing any.

## Flask Web Application

Flask web application displays all scores (scores.json).

![flask_home](images/flask_home.png)

By default, scores are sorted by time registered.

App also allows for sorting scores by stage name, score, or accuracy.

![flask_sort](images/flask_sort.png)
