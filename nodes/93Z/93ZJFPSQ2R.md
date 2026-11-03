---
tag: 93ZJFPSQ2R
kind: definition
name: Random oracle model
msc: [94A60, 68Q10]
defines: 5K6G0G0F9P
uses: [Z5CCVBME2V, 02MY6WZXEQ, XJ8F3NQMGN]
sources:
  - url: https://en.wikipedia.org/wiki/Random_oracle
---

## Definition

Let $\ell \ge 1$.
A *random oracle* with output length $\ell$ is a function $\mathcal{O} \colon \set{0,1}^* \to \set{0,1}^\ell$ chosen uniformly among all such functions.
Equivalently, the values $\mathcal{O}(x)$ for distinct $x$ are independent and [[uniform|02MY6WZXEQ]] on $\set{0,1}^\ell$.
In the *random oracle model*, all algorithms of a scheme and every adversary are [[oracle machines|Z5CCVBME2V]] with access to the same random oracle $\mathcal{O}$.
A scheme is *secure in the random oracle model* if its security property holds when the probabilities are also taken over the choice of $\mathcal{O}$.

## Remarks

The oracle can be simulated by lazy sampling.
Keep a table of pairs $(x, y)$, initially empty.
On a query $x$ already in the table, return its $y$; otherwise draw $y$ uniformly, add $(x, y)$ to the table, and return $y$.
This produces exactly the distribution of a uniform function on the queried points, and it is the main tool of proofs in the model.

Example: with $\ell = 1$, the queries $x_1 = 0$, $x_2 = 1$, $x_3 = 0$ get answers $y_1, y_2, y_1$, with $y_1, y_2$ independent fair bits.

Non-example: a fixed function such as SHA-256 is not a random oracle.
It has a short public description, so an adversary can evaluate it without any query, and its values on distinct inputs are fixed rather than independent and uniform.
In the standard model one replaces $\mathcal{O}$ by a concrete [[hash function|XJ8F3NQMGN]], and a proof in the random oracle model then gives only heuristic evidence.
