---
tag: 7NYES2D0Z4
kind: concept
name: Feedback
msc: [93B52, 93D15]
sources:
  - url: https://en.wikipedia.org/wiki/Feedback
same_as:
  wikidata: Q183635
  wikipedia: Feedback
---

## Summary

Feedback is the use of the measured output of a system to choose its input.
The system and the rule that computes the input form a closed loop, in which cause and effect run around a circle.
Negative feedback acts against deviations from a target.
It can make an unstable system stable, and it can make a system insensitive to disturbances and to errors in the model.
Feedback is the central idea of [[control theory|JXZ0GZXET1]]; its algebra for linear systems is captured by the [[closed-loop transfer function|RYTSV821V8]].

## Explanations

### L1 human

When you steer a bicycle you watch where it goes and correct the handlebars: this is feedback.
Without looking, small errors would grow and you would fall.
A thermostat works the same way: it measures the temperature and heats only when the room is too cold.
For the system $x' = x + u$, the state runs away when $u = 0$, but the feedback $u = -2x$ gives $x' = -x$, and the state returns to $0$ from any start.
