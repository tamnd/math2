---
tag: ZJVKZ8D64P
kind: statement
role: theorem
name: Adams' theorem on Hopf invariant one
msc: [55Q25, 55S20]
uses: [TEGTSY7XMX, P976WYEFMB, M5AKNYC4QQ]
about: [TEGTSY7XMX]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_invariant
---

## Statement

Let $n \ge 1$.
If there is a continuous map $f \colon S^{4n-1} \to S^{2n}$ whose [[Hopf invariant|TEGTSY7XMX]] $H(f)$ equals $1$, then $2n \in \set{2, 4, 8}$.

## Remarks

Conversely, maps of Hopf invariant one exist for $2n = 2, 4, 8$: they are the [[Hopf fibrations|M5AKNYC4QQ]] $S^3 \to S^2$, $S^7 \to S^4$ and $S^{15} \to S^8$, built from the complex numbers, the quaternions and the octonions.

Adams proved the theorem in 1960 with secondary cohomology operations.
A map of Hopf invariant one gives a two-cell complex $X = S^{2n} \cup_f D^{4n}$ with $Sq^{2n}$ nonzero from $H^{2n}(X; \F_2)$ to $H^{4n}(X; \F_2)$.
For $2n$ not a power of $2$, the Adem relations write $Sq^{2n}$ through lower squares, which vanish on $H^{2n}(X; \F_2)$ because they land in zero groups, so this is impossible.
For $2n = 2^k$ with $k \ge 4$, Adams decomposed $Sq^{2^k}$ through secondary operations.
A shorter proof by Adams and Atiyah uses the Adams operations in complex K-theory.

The theorem has several consequences.
For $m \ge 1$, the sphere $S^{m}$ admits the structure of an H-space only for $m \in \set{1, 3, 7}$.
The space $\R^m$ has the structure of a real division algebra, with bilinear multiplication and no zero divisors, only for $m \in \set{1, 2, 4, 8}$.
For $m \ge 1$, the sphere $S^{m}$ is parallelizable only for $m \in \set{1, 3, 7}$.

## Explanations

### L1 human

The Hopf invariant is an integer attached to a map from a sphere of dimension $4n - 1$ to a sphere of dimension $2n$.
Adams showed that it can equal one only in the three dimensions where the complex numbers, the quaternions and the octonions give an example.
This explains why there are no other number systems like these in which one can divide.

### L2 human

The theorem settles the Hopf invariant one problem.
In the Adams spectral sequence for the sphere at the prime $2$, it says that the classes $h_j$ in $\operatorname{Ext}^{1, 2^j}$ survive only for $j \le 3$.
For $j \ge 4$ there is a nonzero differential $d_2(h_j) = h_0 h_{j-1}^2$.
Through the stable homotopy groups of spheres, it is linked to the image of the J-homomorphism and to the vector fields on spheres problem.
