---
tag: 1FJ7QFJE2E
kind: proof
name: Proof of Minkowski's theorem from Blichfeldt's theorem
msc: [11H06]
proves: 0K387S2PKQ
uses: [Z4FSES3CZ0, A3FTHW4NES, 2Z2QVWZ262, 0K06X9QXDX]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski%27s_theorem
    locator: Proof
---

## Proof

Write $\lambda$ for Lebesgue measure on $\R^n$, so that the volume of $S$ is $\lambda(S)$. The hypothesis speaks of this volume, so $S$ is [[Lebesgue measurable|2Z2QVWZ262]].

1. Put $T = \frac{1}{2} S = \set{\frac{1}{2} s : s \in S}$.
2. The map $h(x) = \frac{1}{2} x$ is a bijection of $\R^n$. It sends each box to a box whose volume is $2^{-n}$ times as large, and $h^{-1}$ does the reverse.
3. So $h$ matches the countable covers of a set $A$ by boxes with those of $h(A)$. It multiplies the total volume by $2^{-n}$. Hence $\lambda^*(h(A)) = 2^{-n} \lambda^*(A)$ for every $A \subseteq \R^n$, where $\lambda^*$ is Lebesgue outer measure.
4. The set $S$ satisfies $\lambda^*(A) = \lambda^*(A \cap S) + \lambda^*(A \setminus S)$ for all $A$. Apply this to $h^{-1}(A)$ and use step 3. We get the same condition for $T$, so $T$ is measurable and $\lambda(T) = 2^{-n} \lambda(S)$.
5. By hypothesis $\lambda(S) > 2^n d(L)$, so $\lambda(T) > d(L)$. Here $d(L)$ is the covolume of the [[lattice|Z4FSES3CZ0]] $L$.
6. By [[Blichfeldt's theorem|A3FTHW4NES]], there are distinct points $x, y \in T$ with $x - y \in L$.
7. Write $x = \frac{1}{2} s$ and $y = \frac{1}{2} s'$ with $s, s' \in S$.
8. Since $S$ is symmetric about the origin, $-s' \in S$.
9. Since $S$ is [[convex|0K06X9QXDX]], the midpoint $\frac{1}{2} s + \frac{1}{2}(-s')$ of $s$ and $-s'$ lies in $S$.
10. This midpoint is $x - y$. So $x - y$ is a point of $L$ in $S$, and $x - y \ne 0$ because $x \ne y$.

## Idea

Shrink $S$ by the factor $2$; its volume becomes larger than $d(L)$.
Blichfeldt's theorem then gives two points of the shrunken set that differ by a lattice vector.
Symmetry and convexity show that this difference is the midpoint of two points of $S$, so it lies in $S$.
