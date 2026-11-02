---
tag: XWYXSRM5YS
kind: statement
role: theorem
name: Poncelet's closure theorem
msc: [51M04, 14H52]
uses: [0VKCCEXBJ1, 01R1HW3Y42]
about: [0VKCCEXBJ1]
sources:
  - url: https://en.wikipedia.org/wiki/Poncelet%27s_closure_theorem
same_as:
  wikidata: Q1785610
  wikipedia: Poncelet's closure theorem
---

## Statement

Let $C$ and $D$ be [[ellipses|0VKCCEXBJ1]] in the Euclidean plane with $D$ in the interior of $C$.
For $P_0 \in C$, build a sequence $P_0, P_1, P_2, \ldots$ on $C$ as follows.
From $P_k$ there are two [[tangent lines|01R1HW3Y42]] to $D$.
For $k \ge 1$, take the one other than the line $P_{k-1} P_k$; for $k = 0$, take either one.
Let $P_{k+1}$ be the second point where this tangent line meets $C$.
Suppose that for one starting point $P_0$ the sequence satisfies $P_n = P_0$ for some $n \ge 3$.
Then $P_n = P_0$ holds for every starting point $P_0 \in C$.

## Remarks

The polygon $P_0 P_1 \cdots P_{n-1}$ is inscribed in $C$ and circumscribed about $D$.
A modern proof considers the curve of pairs $(P, \ell)$ with $P \in C$ and $\ell$ a tangent line of $D$ through $P$.
Over the complex numbers this curve is an [[elliptic curve|427N6S6QQW]], and one step of the construction is a translation on it.
A translation that has a point of period $n$ has every point of period $n$.
Example: for two concentric circles with radii $R$ and $R/2$, every inscribed equilateral triangle is circumscribed about the inner circle, so every start closes after $3$ steps.
For a triangle and two circles, closure happens exactly when [[Euler's theorem|RFCQT6TKZF]] $d^2 = R(R - 2r)$ holds between the radii and the distance $d$ of the centres.

## Explanations

### L1 human

Draw an oval with a smaller oval inside it.
Start at a point of the outer oval and walk along straight lines that just graze the inner oval, bouncing from the outer one each time.
If, from one starting point, the path closes after some number of steps, then it closes after the same number of steps from every starting point.

### L2 human

Poncelet's theorem is a porism: the closing property is all or nothing.
It holds more generally for two smooth conics in general position in the complex projective plane.
Its proof through elliptic curves is a standard illustration of how the group law of a cubic curve solves a problem of elementary geometry.
