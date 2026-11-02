---
tag: 2AVNDP8BJP
kind: concept
name: Markov kernel
msc: [60J05, 28A35]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_kernel
same_as:
  wikidata: Q6771323
  wikipedia: Markov kernel
---

## Summary

A Markov kernel from a space $X$ to a space $Y$ assigns to each point of $X$ a [[probability measure|059TJN0NZ1]] on $Y$.
The assignment must be measurable in the point.
It generalises the [[transition matrix|0F462493EA]] of a Markov chain to arbitrary state spaces.
Kernels describe random transitions, conditional distributions and randomised maps.
They can be composed, and together with a starting measure they build measures on product spaces.

## Explanations

### L1 human

A Markov kernel is a rule that says: if you are at point $x$, here is the probability distribution of where you go next.
For a finite set of states it is just a table whose rows are probability vectors.
For example, a random walk on $\Z$ that moves to $x + 1$ or $x - 1$ with probability $\tfrac12$ each is given by the kernel $\kappa(x, \cdot) = \tfrac12 \delta_{x+1} + \tfrac12 \delta_{x-1}$.
