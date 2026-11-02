---
tag: D3AVHVYQW9
kind: statement
role: theorem
name: Alexandrov–Fenchel inequality
msc: [52A39, 52A40]
uses: [QB3Q5FBJ08, 437FSG3419]
about: [QB3Q5FBJ08]
sources:
  - url: https://en.wikipedia.org/wiki/Mixed_volume
---

## Statement

Let $n \ge 2$ and let $K_1, K_2, \dots, K_n$ be nonempty compact convex subsets of $\R^n$ ([[convex bodies|437FSG3419]]).
Let $V$ denote the [[mixed volume|QB3Q5FBJ08]].
Then
$$V(K_1, K_2, K_3, \dots, K_n)^2 \ge V(K_1, K_1, K_3, \dots, K_n)\, V(K_2, K_2, K_3, \dots, K_n).$$

## Remarks

The inequality was proved by Alexandrov, and independently by Fenchel, in the 1930s.
Alexandrov's proofs treat polytopes or smooth bodies first, by induction on the dimension, and then pass to general bodies by approximation.
Khovanskii and Teissier found a proof through the Hodge index theorem applied to toric varieties.

Example: for $n = 2$ the inequality reads $V(K, L)^2 \ge \operatorname{area}(K) \operatorname{area}(L)$.
With $L$ the unit disk, $V(K, L) = \frac12 \operatorname{per}(K)$, and one gets $\operatorname{per}(K)^2 \ge 4 \pi \operatorname{area}(K)$, the planar [[isoperimetric inequality|KBX8RBZ626]].

## Explanations

### L1 human

Mixed volumes measure how several convex shapes interact.
The Alexandrov–Fenchel inequality says that a mixed volume of two different shapes is at least the geometric mean of the "pure" mixed volumes of each shape with itself.
It is a far-reaching relative of the Cauchy–Schwarz inequality and of the isoperimetric inequality.

### L2 human

Applied with the remaining arguments chosen among $K_1$ and $K_2$, it shows that the sequence $V(K_1[i], K_2[n - i])$, for $i = 0, \dots, n$, is log-concave in $i$.
It implies [[Minkowski's first inequality|9M8XJX4DQ7]] and the [[Brunn–Minkowski theorem|9B02RPN7XD]] for convex bodies.
Stanley used it to prove that the numbers of linear extensions of a poset with a fixed element at a given position form a log-concave sequence.
Its equality cases are understood only in special situations, and their full description is a hard problem.
