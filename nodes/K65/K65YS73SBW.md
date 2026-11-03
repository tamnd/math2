---
tag: K65YS73SBW
kind: problem
name: Assignment problem
msc: [90B80, 90C27, 05C70]
uses: [0ZVQKTRKVQ, 0NHK9MFFW9, 0MJ04A50QW]
about: [0NHK9MFFW9]
sources:
  - url: https://en.wikipedia.org/wiki/Assignment_problem
same_as:
  wikidata: Q620614
  wikipedia: Assignment problem
history:
  posed_by: "Harold W. Kuhn"
  first_stated: "1955"
  notes: "Kuhn formulated the problem and gave the Hungarian method in 1955, the earliest well-documented algorithmic treatment. The method rests on earlier results of Dénes Kőnig and Jenő Egerváry, whose 1931 paper treated weighted bipartite matchings."
---

## Problem

Let $n \ge 1$ be an integer and let $C = (c_{ij})$ be a real $n \times n$ matrix, where $c_{ij}$ is the cost of giving task $j$ to agent $i$.
Find a permutation $\sigma$ of $\set{1, \dots, n}$ that minimizes
$$\sum_{i=1}^n c_{i \sigma(i)}.$$
Equivalently, find a minimum-weight [[perfect matching|0NHK9MFFW9]] in the complete [[bipartite graph|0ZVQKTRKVQ]] $K_{n,n}$, where the edge between agent $i$ and task $j$ has weight $c_{ij}$.

## Remarks

There are $n!$ permutations, so listing them all is hopeless for large $n$.
The [[Hungarian algorithm|7DJ7P8RSJN]] solves the problem with $O(n^3)$ arithmetic operations.
The problem is also the linear program of minimizing $\sum_{i,j} c_{ij} x_{ij}$ over the [[doubly stochastic matrices|JJA90EB2PS]] $x$.
By the Birkhoff–von Neumann theorem, the vertices of the [[Birkhoff polytope|ADEXY830S8]] are the permutation matrices, so this linear program has an optimal solution that is a permutation matrix.
It is the special case of the [[transportation problem|2B9QWY4APJ]] with $m = n$ and all supplies and demands equal to $1$.
Example: take the cost matrix
$$C = \begin{pmatrix} 4 & 1 & 3 \\ 2 & 0 & 5 \\ 3 & 2 & 2 \end{pmatrix}.$$
Give task $2$ to agent $1$, task $1$ to agent $2$ and task $3$ to agent $3$.
This assignment has cost $1 + 2 + 2 = 5$, the least of the $6$ possible costs.
Variants include the maximization version, rectangular cost matrices and the [[quadratic assignment problem|EST8JNY4Q4]], which is NP-hard.

## Explanations

### L1 human

There are $n$ workers and $n$ jobs, and each worker would take a known time for each job.
Each worker must get exactly one job, and each job exactly one worker.
The assignment problem asks for the pairing with the least total time.
Trying all pairings takes too long, but clever methods find the best one quickly.
