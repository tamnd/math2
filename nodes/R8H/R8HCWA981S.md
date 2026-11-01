---
tag: R8HCWA981S
kind: statement
role: theorem
name: Hasse–Minkowski theorem
msc: ["11E12", "11E08", 11D09]
uses: [0RBQS1JJCR, BT6T702C28, EMAR4X3W8D, WFG4YMBYVQ, 0GNVN3CA2P]
about: [0RBQS1JJCR, EMAR4X3W8D]
sources:
  - url: https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem
same_as:
  wikidata: Q1938251
  wikipedia: Hasse–Minkowski theorem
---

## Statement

Let $Q$ be a nondegenerate [[quadratic form|0RBQS1JJCR]] in $n$ variables with coefficients in $\Q$.
For a prime $p$, let $\Q_p$ be the field of [[p-adic numbers|BT6T702C28]].
Then $Q$ has a zero $x \in \Q^n$ with $x \ne 0$ if and only if both of these hold:

1. $Q$ has a nonzero zero in $\R^n$.
2. $Q$ has a nonzero zero in $\Q_p^n$ for every prime $p$.

## Remarks

The direction "only if" is clear; the content is that local zeros give a global zero.
The proof goes by the number of variables, with the [[Hilbert symbol|WFG4YMBYVQ]] as the main tool.
The case $n = 3$ is essentially Legendre's theorem on $ax^2 + by^2 + cz^2 = 0$; the case $n = 4$ uses [[Dirichlet's theorem on arithmetic progressions|0GNVN3CA2P]], and the case $n \ge 5$ reduces to $n = 4$.
The theorem holds over every number field, with its completions in place of $\R$ and the $\Q_p$.
Example: $x^2 + y^2 - 3z^2$ has the real zero $(\sqrt{3}, 0, 1)$, but no nonzero zero in $\Q_3^3$; hence it has no nonzero rational zero.
A consequence: a nonzero $a \in \Q$ is represented by $Q$ over $\Q$ if and only if it is represented over $\R$ and over every $\Q_p$.
Another: two quadratic forms over $\Q$ are equivalent over $\Q$ if and only if they are equivalent over $\R$ and over every $\Q_p$.
The restriction to quadratic forms is necessary: Selmer's cubic $3x^3 + 4y^3 + 5z^3$ has nonzero zeros over $\R$ and every $\Q_p$, but none over $\Q$.

## Explanations

### L1 human

To decide whether a quadratic equation such as $ax^2 + by^2 + cz^2 = 0$ has a solution in fractions, it is enough to check real numbers and the $p$-adic numbers for each prime.
Each such check is a finite computation, and only finitely many primes need real work.
So the theorem turns an infinite search into a finite test.

### L2 human

This is the main example of the [[Hasse principle|EMAR4X3W8D]].
In practice one computes Hilbert symbols $(a, b)_p$ at the primes dividing $2$ and the coefficients; at all other primes a form of rank at least $3$ is automatically isotropic.
The theorem is the basis of the classification of quadratic forms over $\Q$ by discriminant, signature and Hasse invariants.
For cubic and higher degree equations the principle can fail, and the study of the failure leads to the Tate–Shafarevich group of elliptic curves.
