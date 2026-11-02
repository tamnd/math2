---
tag: WRY0M7SW59
kind: concept
name: Discrete harmonic function
msc: [31C20, 05C81]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_Laplace_operator
---

## Summary

A discrete harmonic function is a function on the vertices of a graph equal at each vertex to a weighted average of its neighbouring values.
It is the discrete analogue of a [[harmonic function|0DEB0JMN0W]], and it is exactly a function killed by the [[graph Laplacian|TN6M6DVZRP]].
Discrete harmonic functions describe voltages in an [[electrical network|T7KRE7J3B4]] and hitting probabilities of a [[random walk|04VZE3FZXF]].
They satisfy discrete versions of the mean value property and the maximum principle.

## Explanations

### L1 human

Put a number on every vertex of a graph.
The function is harmonic at a vertex if the number there is the average of the numbers at the neighbouring vertices.
On the integers, with neighbours $n - 1$ and $n + 1$, the harmonic functions are the straight lines $f(n) = an + b$.
A harmonic function cannot have a strict maximum at an interior vertex, since an average cannot exceed all its terms.
If a random walker moves to a uniformly chosen neighbour at each step, then a harmonic function keeps its expected value along the walk.
