---
tag: 8NYK87K5DE
kind: statement
role: theorem
name: Dubins–Spanier theorems
msc: [91B32, 28A10]
uses: [059TJN0NZ1, SV96KN4WR9, 08QMKTWF9T, 2ZTQX5M0TK]
about: [KCVV28DH6R]
sources:
  - url: https://en.wikipedia.org/wiki/Dubins–Spanier_theorems
same_as:
  wikidata: Q24963391
  wikipedia: Dubins–Spanier theorems
---

## Statement

Let $(C, \mathcal{A})$ be a measurable space, the cake, and let $n \ge 2$ be the number of partners.
Let $\mu_1, \dots, \mu_n$ be [[non-atomic|SV96KN4WR9]] countably additive [[probability measures|059TJN0NZ1]] on $(C, \mathcal{A})$, where $\mu_i$ gives the values of partner $i$.
A division is a [[partition|08QMKTWF9T]] $(X_1, \dots, X_n)$ of $C$ into pieces $X_j \in \mathcal{A}$, where piece $X_j$ goes to partner $j$.
Its value matrix is the $n \times n$ matrix $M(X_1, \dots, X_n)$ with entries $\mu_i(X_j)$.
Let $\mathcal{M} \subseteq \R^{n \times n}$ be the set of value matrices of all divisions.

1. The set $\mathcal{M}$ is compact and convex.
2. For all real numbers $\alpha_1, \dots, \alpha_n \ge 0$ with $\alpha_1 + \cdots + \alpha_n = 1$, there is a division with $\mu_i(X_j) = \alpha_j$ for all $i$ and $j$. In particular, there is a division in which every partner values every piece at exactly $1/n$.
3. If the measures $\mu_1, \dots, \mu_n$ are not all equal, there is a division with $\mu_i(X_i) > 1/n$ for every $i$.

## Remarks

The convexity in part 1 comes from [[Lyapunov's convexity theorem|2ZTQX5M0TK]], applied to the vector measure $(\mu_1, \dots, \mu_n)$ on suitable refinements of divisions.
Part 2 follows from part 1.
The matrix with all rows equal to $(\alpha_1, \dots, \alpha_n)$ is a convex combination of the $n$ value matrices of the divisions that give the whole cake to one partner.
Part 3 uses convexity again.
Two partners with different measures can trade parts of the cake that each of them values relatively more, and the gain can be shared out.
Compactness gives the existence of divisions that are optimal for any continuous criterion, for example a division that maximizes $\sum_i \mu_i(X_i)$ or one that maximizes $\min_i \mu_i(X_i)$.
The theorems are existence results and do not give a finite procedure.
Non-atomicity is needed: if all the value sits in one point that all partners want, no division gives each of two partners half of the value.

## Explanations

### L1 human

A cake is to be shared among $n$ people who may like different parts of it.
The theorems say that, in principle, one can cut it so that everyone agrees every piece is worth exactly $1/n$.
If the people do not all have the same taste, one can even cut it so that each person gets more than a fair share in their own eyes.

### L2 human

These results are the measure-theoretic base of [[fair cake-cutting|KCVV28DH6R]].
They are proved by convexity, not by a cutting protocol, so they say what is possible but not how to find it.
Consensus divisions in part 2 are also called exact divisions, and their existence is the starting point for many results on proportional and envy-free division.
