---
tag: EST8JNY4Q4
kind: problem
name: Quadratic assignment problem
msc: [90C27, 90B80]
uses: [FJPER80BJC, K65YS73SBW, XJRHJX2241, MHA48AWBXN]
about: [FJPER80BJC]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_assignment_problem
same_as:
  wikidata: Q7268356
  wikipedia: Quadratic assignment problem
history:
  posed_by: "Tjalling Koopmans and Martin Beckmann"
  first_stated: "1957"
---

## Problem

Let $n \ge 1$, and let $F = (f_{ij})$ and $D = (d_{kl})$ be real $n \times n$ matrices.
Here $f_{ij}$ is the flow between facilities $i$ and $j$, and $d_{kl}$ is the distance between locations $k$ and $l$.
Let $S_n$ be the set of permutations of $\set{1, \dots, n}$, where $\pi(i)$ is the location of facility $i$.
The *quadratic assignment problem* asks for a permutation $\pi \in S_n$ that minimizes
$$\sum_{i=1}^{n} \sum_{j=1}^{n} f_{ij} \, d_{\pi(i) \pi(j)}.$$

## Remarks

The cost is quadratic in the $0$-$1$ variables $x_{ik}$, where $x_{ik} = 1$ means $\pi(i) = k$.
A linear cost $\sum_i c_{i \pi(i)}$ would give the [[assignment problem|K65YS73SBW]], which is solvable in polynomial time.
The quadratic problem is [[NP-hard|MHA48AWBXN]].
It contains the [[travelling salesman problem|XJRHJX2241]]: take $f_{ij} = 1$ when $j = i + 1$ or $(i, j) = (n, 1)$, and $f_{ij} = 0$ otherwise.
Then the cost of $\pi$ is the length of the tour $\pi(1), \dots, \pi(n)$.
The problem is also hard in practice: exact solution of instances with $n$ around $30$ already needs large computations.
Lower bounds come from the Gilmore–Lawler bound and from linear and semidefinite relaxations.

## Explanations

### L1 human

A company must place $n$ departments into $n$ rooms.
Some departments exchange a lot of paperwork, and some rooms are far apart.
The cost of a plan adds, for each pair of departments, their amount of traffic times the distance between their rooms.
The goal is the plan with least cost, so that busy pairs end up close together.
Because the cost depends on pairs of choices, not on single choices, the problem is much harder than assigning workers to jobs.
