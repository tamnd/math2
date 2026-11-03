---
tag: XJRHJX2241
kind: problem
name: Travelling salesman problem
msc: [90C27, 68Q17]
uses: [00C0BR7D7H, 0HF30P75G4, MHA48AWBXN, JGZWHWA8P8, GVT2NKN37K]
about: [0HF30P75G4]
sources:
  - url: https://en.wikipedia.org/wiki/Travelling_salesman_problem
same_as:
  wikidata: Q322212
  wikipedia: Travelling salesman problem
history:
  posed_by: "Karl Menger"
  first_stated: "1930"
  notes: "Menger formulated it in 1930 as the messenger problem; related questions on Hamiltonian cycles go back to Hamilton and Kirkman in the 19th century."
---

## Problem

Let $n \ge 3$, and let $K_n$ be the complete [[graph|00C0BR7D7H]] on the vertex set $\set{1, \dots, n}$.
Let $w$ assign to each edge $\set{i, j}$ a nonnegative weight $w(i, j)$, the distance between cities $i$ and $j$.
A tour is a [[Hamiltonian cycle|0HF30P75G4]] in $K_n$, and its length is the sum of the weights of its edges.
The *travelling salesman problem* asks for a tour of minimum length.
In the decision version, an input $(n, w, B)$ with a number $B$ is given, and the question is whether some tour has length at most $B$.

## Remarks

The decision version is [[NP-complete|JGZWHWA8P8]], and the optimization version is [[NP-hard|MHA48AWBXN]].
Hardness follows from the Hamiltonian cycle problem.
Given a graph $G$ on $n$ vertices, give weight $1$ to its edges and weight $2$ to the other pairs.
Then $G$ has a Hamiltonian cycle exactly when some tour has length $n$.
Trying all $(n-1)!/2$ tours solves the problem.
The Held–Karp dynamic programming algorithm takes $O(n^2 2^n)$ steps.
When $w$ satisfies the triangle inequality, Christofides' algorithm finds a tour at most $3/2$ times the optimum in polynomial time.
Without the triangle inequality, no polynomial-time algorithm achieves any constant approximation factor unless $\mathrm{P} = \mathrm{NP}$.

## Explanations

### L1 human

A salesman must visit each of $n$ cities once and come back home.
The question is which order of visits makes the total distance smallest.
With $n$ cities there are $(n-1)!/2$ possible round trips, far too many to try for even a few dozen cities.
The problem is a standard test case for exact and approximate methods of combinatorial optimization.
