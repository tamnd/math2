---
tag: ZJSW0HP75H
kind: statement
role: theorem
name: Cone theorem
msc: ["14E30", 14C20]
uses: [A4H4CZ2V35, W05VYY4HBR, 4HV4WTAX9P, RRK8P6TXG2, 0PF6TM8TWT]
about: [W05VYY4HBR]
sources:
  - url: https://en.wikipedia.org/wiki/Cone_of_curves
---

## Statement

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]] and let $X$ be a smooth [[projective variety|A4H4CZ2V35]] over $k$ of dimension $n$.
Let $K_X$ be its canonical divisor (see [[canonical bundle|W05VYY4HBR]]).
Let $N_1(X)$ be the real vector space of $1$-cycles on $X$ modulo numerical equivalence.
Let $\overline{NE}(X) \subseteq N_1(X)$ be the closure of the cone spanned by the classes of curves.
Write $\overline{NE}(X)_{K_X \ge 0} = \set{z \in \overline{NE}(X) : K_X \cdot z \ge 0}$, using the [[intersection pairing|4HV4WTAX9P]].
Then there are countably many rational curves $C_i \subset X$ with
$$0 < -K_X \cdot C_i \le n + 1$$
such that
$$\overline{NE}(X) = \overline{NE}(X)_{K_X \ge 0} + \sum_i \R_{\ge 0} [C_i].$$
Moreover, for every [[ample|RRK8P6TXG2]] divisor $H$ and every $\varepsilon > 0$, only finitely many of the $C_i$ are needed to write
$$\overline{NE}(X) = \overline{NE}(X)_{K_X + \varepsilon H \ge 0} + \sum_{i \text{ finite}} \R_{\ge 0} [C_i].$$

## Remarks

The theorem is due to Mori.
The rational curves come from his bend-and-break method: a curve on which $K_X$ is negative deforms a lot and breaks off rational curves.
The method works first in characteristic $p$ and then passes to characteristic $0$.
Example: on $\mathbb{P}^n$ the space $N_1$ is spanned by the class of a line $\ell$, and $-K \cdot \ell = n + 1$.
So the bound $n + 1$ is sharp, and $\overline{NE}(\mathbb{P}^n) = \R_{\ge 0} [\ell]$.
In characteristic $0$, the theorem extends to log terminal pairs, together with the contraction theorem which contracts each $K_X$-negative extremal ray.

## Explanations

### L1 human

The classes of curves on a variety span a cone in a finite-dimensional real vector space.
The theorem describes the part of this cone where the canonical class is negative.
That part is spanned by the classes of rational curves of bounded degree, one ray at a time, like the edges of a polyhedral cone.

### L2 human

The cone theorem is the first step of the minimal model program: it provides the extremal rays to contract.
With the contraction theorem, each $K_X$-negative extremal ray gives a morphism that contracts exactly the curves in that ray.
For surfaces, these rays are spanned by $(-1)$-curves, by fibres of a ruling, or by a line in $\mathbb{P}^2$.
