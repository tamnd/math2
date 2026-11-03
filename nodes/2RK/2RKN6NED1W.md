---
tag: 2RKN6NED1W
kind: concept
name: Iterative learning control
msc: [93C55, 93B52, 93C83]
sources:
  - url: https://en.wikipedia.org/wiki/Iterative_learning_control
same_as:
  wikidata: Q6094414
  wikipedia: Iterative learning control
---

## Summary

Iterative learning control is a method for systems that perform the same task again and again over a fixed time interval.
After each trial, the input for the next trial is corrected with the tracking error of the trial just finished.
Under suitable conditions the error shrinks from trial to trial, even when the model of the system is poor.
It is used for robots, machine tools and other repetitive processes, and it adds learning across trials to ordinary [[feedback|7NYES2D0Z4]] within a trial.

## Explanations

### L1 human

Think of a basketball player who practises the same free throw.
After each shot the player sees how far the ball missed and adjusts the next throw.
Iterative learning control does this with a whole input signal.
The error at each moment of one trial corrects the input at the same moment of the next trial.
For example, if a robot arm lags behind its target path at time $t$ in one run, the next run pushes harder near time $t$.
After enough runs the arm follows the path closely.
