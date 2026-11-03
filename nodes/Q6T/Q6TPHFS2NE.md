---
tag: Q6TPHFS2NE
kind: statement
role: theorem
name: Polynomial-time submodular minimization
msc: [90C27, 68Q25, 05B35]
uses: [4WQA9XFA52, KTT5A73PK7, TJR5MQHNYE, T00W8RQT8E, T9B8T3FKRA, 535E3GPP4T]
about: [4WQA9XFA52]
sources:
  - url: https://en.wikipedia.org/wiki/Submodular_set_function
---

## Statement

Let $E$ be a finite set with $n$ elements, and let $f \colon 2^E \to \R$ be a [[submodular|4WQA9XFA52]] function.
Assume $f$ is given by a value oracle, which returns $f(A)$ for any queried $A \subseteq E$.
Then there is an algorithm that finds a set $A^* \subseteq E$ with $f(A^*) = \min_{A \subseteq E} f(A)$.
Its number of oracle calls and arithmetic operations is bounded by a polynomial in $n$.

## Remarks

Grötschel, Lovász and Schrijver gave the first polynomial algorithm, with the [[ellipsoid method|TJR5MQHNYE]].
It minimizes the [[Lovász extension|KTT5A73PK7]] $\hat f$, which is convex when $f$ is submodular, over the cube $[0, 1]^n$.
Combinatorial algorithms that avoid the ellipsoid method were found later, independently by Schrijver and by Iwata, Fleischer and Fujishige.

Example: take a directed graph with nonnegative capacities and two vertices $s, t$.
For a set $A$ of vertices other than $s$ and $t$, the capacity of the cut leaving $A \cup \set{s}$ is a submodular function of $A$.
Its minimum is the minimum $s$–$t$ cut, which is also found faster by maximum flow algorithms.

Submodularity is needed: minimizing a general set function given by a value oracle can require all $2^n$ queries.
Maximizing a submodular function is NP-hard, since it contains the [[maximum cut|T9B8T3FKRA]] problem.

## Explanations

### L1 human

Submodular functions model costs with diminishing returns, such as the cost of cuts in networks.
Among all $2^n$ subsets, the theorem says the one of least value can be found fast, without trying them all.
This is surprising, since for general functions on subsets no such shortcut exists.
The reason is that submodular functions behave like convex functions, and convex functions are easy to minimize.

### L2 human

The result is the discrete analogue of the fact that convex functions can be minimized efficiently.
The [[Lovász extension|KTT5A73PK7]] makes this precise: it turns $f$ into a convex function on the cube with the same minimum.
Many polynomial-time problems are special cases, such as minimum cuts, and the minimization of the rank sums in the [[matroid intersection|535E3GPP4T]] formula.
In [[time complexity|T00W8RQT8E]] terms, the bound does not depend on the size of the values of $f$, so the algorithm is strongly polynomial.
