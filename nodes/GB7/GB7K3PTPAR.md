---
tag: GB7K3PTPAR
kind: problem
name: Matrix completion
msc: [15A83, 65F55]
uses: [0VD9ZSWWJG, 0ZC9YTXZRY, 09VMDSRXWJ]
about: [0ZC9YTXZRY]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_completion
same_as:
  wikidata: Q6787865
  wikipedia: Matrix completion
history:
  posed_by: "Emmanuel Candès and Benjamin Recht"
  first_stated: "2009"
---

## Problem

Let $F$ be a field and let $m, n \ge 1$ be integers.
Let $\Omega$ be a set of positions $(i, j)$ with $1 \le i \le m$ and $1 \le j \le n$.
For each $(i, j) \in \Omega$, let a value $M_{ij} \in F$ be given.
Find an $m \times n$ [[matrix|0VD9ZSWWJG]] $X$ over $F$ such that $X_{ij} = M_{ij}$ for all $(i, j) \in \Omega$ and the [[rank|0ZC9YTXZRY]] of $X$ is as small as possible.

## Remarks

Without more structure the problem has no unique answer: the entries outside $\Omega$ can be anything, so one asks for the completion of lowest rank.
Low-rank completion is NP-hard in general.
Over $\R$, a standard relaxation replaces the rank by the nuclear norm, the sum of the [[singular values|09VMDSRXWJ]] of $X$, which gives a convex problem.
Candès and Recht proved in 2009 that nuclear norm minimization recovers the unknown matrix exactly with high probability, under some conditions.
The matrix must have low rank and satisfy an incoherence condition, and enough entries must be sampled at random.
Other versions ask for a completion that is positive semidefinite, or that has another prescribed property.

## Explanations

### L1 human

Imagine a table of ratings, one row per user and one column per film, where most cells are empty.
Matrix completion asks to fill the empty cells in the simplest way, meaning with a matrix of small rank.
For example, if the known entries are $X_{11} = 1$, $X_{12} = 2$ and $X_{21} = 3$, the completion of rank $1$ is forced: $X_{22} = 6$.
The problem became famous through recommender systems such as the Netflix Prize.
