---
tag: NX8AMNXWG8
kind: statement
role: theorem
name: Grothendieck inequality
msc: [46B28, 46M05, 46B07]
uses: [HM2HHE3J51, 0NB0AWGJBW, 685ZV73JJ8]
about: [HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_inequality
same_as:
  wikidata: Q5610731
  wikipedia: Grothendieck inequality
---

## Statement

There is a constant $K$ with the following property.
Let $m, n \ge 1$ and let $(a_{ij})$ be a real $m \times n$ matrix.
Assume that $\abs{\sum_{i,j} a_{ij} s_i t_j} \le 1$ for all $s_1, \dots, s_m, t_1, \dots, t_n \in \set{-1, 1}$.
Let $H$ be a real [[Hilbert space|HM2HHE3J51]] and let $u_1, \dots, u_m, v_1, \dots, v_n$ be vectors of norm at most $1$ in $H$.
Then
$$\Big| \sum_{i=1}^m \sum_{j=1}^n a_{ij} \ip{u_i}{v_j} \Big| \le K.$$

## Remarks

The constant $K$ does not depend on $m$, $n$ or $H$.
The smallest such constant is the real Grothendieck constant $K_G$.
Its exact value is unknown.
Krivine proved $K_G \le \pi / (2 \log(1 + \sqrt{2})) \approx 1.78$.

One proof uses random Gaussian vectors $g$.
For unit vectors $u$ and $v$, the average of $\sgn \ip{g}{u} \sgn \ip{g}{v}$ is $\frac{2}{\pi} \arcsin \ip{u}{v}$.
So signs drawn at random from the vectors reproduce a function of the [[inner products|0NB0AWGJBW]].
Krivine first transforms the vectors so that this function becomes a fixed multiple of the inner product.

The inequality has a complex version, with a different constant.
In computer science it shows that a semidefinite relaxation approximates the cut norm of a matrix within a constant factor.

## Explanations

### L1 human

Replace numbers $\pm 1$ by unit vectors in some Euclidean space, and products by inner products.
A sum built from a matrix can only grow by a bounded factor under this replacement, whatever the size of the matrix.
This links a hard combinatorial maximum over signs with an easy geometric maximum over vectors.

### L2 human

Grothendieck stated the result in his work on tensor products of Banach spaces.
In that language it says that every bounded linear map from $L^1$ to $L^2$ is absolutely summing.
The inequality is a key tool in the study of the [[projective tensor product|685ZV73JJ8]] and of operator ideals.
