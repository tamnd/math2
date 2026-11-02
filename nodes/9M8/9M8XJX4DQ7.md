---
tag: 9M8XJX4DQ7
kind: statement
role: theorem
name: Minkowski's first inequality
msc: [52A39, 52A40]
uses: [QB3Q5FBJ08, 437FSG3419, 2Z2QVWZ262]
about: [QB3Q5FBJ08]
sources:
  - url: https://en.wikipedia.org/wiki/Mixed_volume
---

## Statement

Let $n \ge 1$ and let $K, L$ be nonempty compact convex subsets of $\R^n$ ([[convex bodies|437FSG3419]]).
Let $V$ be the [[mixed volume|QB3Q5FBJ08]] and write $V_1(K, L) = V(K, \dots, K, L)$, with $K$ repeated $n - 1$ times.
Then
$$V_1(K, L)^n \ge \operatorname{vol}(K)^{n-1} \operatorname{vol}(L),$$
where $\operatorname{vol}$ is [[Lebesgue measure|2Z2QVWZ262]].
If $K$ and $L$ have nonempty interiors, equality holds if and only if $K$ and $L$ are homothetic.

## Remarks

One derivation uses the [[Brunn–Minkowski theorem|9B02RPN7XD]].
If $\operatorname{vol}(K) = 0$ the inequality is trivial, so assume $\operatorname{vol}(K) > 0$.
The function $f(t) = \operatorname{vol}(K + tL)^{1/n}$ is concave on $[0, \infty)$, so $f'(0) \ge f(1) - f(0) \ge \operatorname{vol}(L)^{1/n}$.
By the definition of mixed volumes, $\operatorname{vol}(K + tL) = \operatorname{vol}(K) + n V_1(K, L)\, t + O(t^2)$, so $f'(0) = V_1(K, L) \operatorname{vol}(K)^{(1-n)/n}$, which gives the inequality.
It also follows from the [[Alexandrov–Fenchel inequality|D3AVHVYQW9]].

Example: take $L = B$, the closed unit ball, of volume $\kappa_n$.
Then $n V_1(K, B)$ is the surface area $S(K)$, and the inequality becomes $S(K)^n \ge n^n \kappa_n \operatorname{vol}(K)^{n-1}$, the [[isoperimetric inequality|KBX8RBZ626]] for convex bodies.
For $n = 2$ this is $\operatorname{per}(K)^2 \ge 4 \pi \operatorname{area}(K)$.

## Explanations

### L1 human

The first mixed volume $V_1(K, L)$ measures how fast the volume of $K$ grows when a small multiple of $L$ is added to it.
Minkowski's first inequality bounds this growth rate from below by the sizes of $K$ and $L$.
With $L$ a ball it is the isoperimetric inequality: among convex bodies of given volume, the ball has the least surface area.

### L2 human

The inequality is a key step in the uniqueness part of the Minkowski problem: two convex bodies with the same surface area measure are translates of each other.
It is the case $K_3 = \cdots = K_n = K$ of a chain of inequalities obtained from the [[Alexandrov–Fenchel inequality|D3AVHVYQW9]].
Minkowski's second inequality, $V_1(K, L)^2 \ge \operatorname{vol}(K)\, V(K, \dots, K, L, L)$, is another case of that chain.
