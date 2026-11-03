---
tag: DK2X0ZZDBH
kind: concept
name: Benders decomposition
msc: [90C06, 90C11, 90C05]
sources:
  - url: https://en.wikipedia.org/wiki/Benders_decomposition
same_as:
  wikidata: Q3042795
  wikipedia: Benders decomposition
---

## Summary

Benders decomposition is a method for optimization problems whose variables split into hard "complicating" variables $y$ and easy continuous variables $x$.
For fixed $y$, the problem in $x$ is a [[linear program|VNMXB0J2KA]], and its [[dual|14VMJNXMDC]] gives inequalities in $y$ alone.
A master problem in $y$ is solved again and again, and each round adds one such inequality, called a Benders cut.
The method is a standard tool for large [[mixed-integer linear programs|3PX6EV34QK]] and for two-stage [[stochastic programs|2YW60J1GT6]].

## Explanations

### L1 human

Some decisions are hard, such as which warehouses to build, and some are easy once those are fixed, such as how to ship goods.
Benders decomposition makes a guess for the hard decisions, then solves the easy problem for that guess.
The easy problem reports back a simple rule of the form "with these choices the shipping cost is at least this much".
The rule is added to the problem for the hard decisions, and the next guess must respect it.
After enough rounds the guesses can no longer be improved, and the best plan has been found.
