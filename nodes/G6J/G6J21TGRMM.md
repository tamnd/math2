---
tag: G6J21TGRMM
kind: concept
name: Singular perturbation
msc: ["34E15", 34D15]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_perturbation
same_as:
  wikidata: Q7524249
  wikipedia: Singular perturbation
---

## Summary

A problem with a small parameter $\varepsilon$ is singularly perturbed when setting $\varepsilon = 0$ does not give a uniformly good approximation of its solutions.
A typical cause is a small parameter in front of the highest derivative.
Then the reduced equation has lower order and cannot meet all boundary or initial conditions.
The solutions then change rapidly in thin regions, such as boundary layers.
Singular perturbations appear in fluid flow at high Reynolds number, chemical kinetics and slow-fast systems.

## Explanations

### L1 human

Sometimes a tiny term in an equation can be dropped without much harm, and sometimes it cannot.
In $\varepsilon y'' + y' = 0$ with $y(0) = 0$ and $y(1) = 1$, dropping $\varepsilon y''$ leaves $y' = 0$, whose solutions are constants.
A constant cannot be $0$ at one end and $1$ at the other.
The true solution is close to $1$ on most of the interval, but it drops steeply to $0$ in a thin layer near $x = 0$.
That thin layer is the mark of a singular perturbation.
