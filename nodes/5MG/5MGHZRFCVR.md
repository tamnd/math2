---
tag: 5MGHZRFCVR
kind: concept
name: Robust control
msc: [93B35, 93D09, 93B36]
specializes: [JXZ0GZXET1]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_control
same_as:
  wikidata: Q915157
  wikipedia: Robust control
---

## Summary

Robust control is the part of [[control theory|JXZ0GZXET1]] that designs controllers which keep working when the model of the plant is uncertain.
The uncertainty is described by a set of possible plants.
The controller must stabilize every plant of the set and meet the performance goals for all of them.
Its main tools are the [[small-gain theorem|1CF728E75M]], [[H-infinity control|E3WZ90H2XQ]], the [[structured singular value|2EASHBY4TX]] and [[loop-shaping|5TSW53EG92]].

## Explanations

### L1 human

A model of a machine is never exact: masses, frictions and delays are only known roughly.
A controller tuned perfectly for the model may fail on the real machine.
Robust control asks for a controller that works for every machine within the known error margins.
For example, a cruise control should keep the speed whether the car carries one passenger or five.
