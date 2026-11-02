---
tag: A3FTHW4NES
kind: statement
role: theorem
name: Blichfeldt's theorem
msc: [11H06, 52C07]
uses: [WN9V7WSJKF, 2Z2QVWZ262]
about: [WN9V7WSJKF]
sources:
  - url: https://en.wikipedia.org/wiki/Blichfeldt%27s_theorem
same_as:
  wikidata: Q104902490
  wikipedia: Blichfeldt's theorem
---

## Statement

Let $n \ge 1$ and let $\Lambda \subset \R^n$ be a [[lattice|WN9V7WSJKF]] with covolume $\det \Lambda$.
Let $S \subseteq \R^n$ be a [[Lebesgue measurable|2Z2QVWZ262]] set with volume $\operatorname{vol}(S) > \det \Lambda$.
Then there are two distinct points $x, y \in S$ such that $x - y \in \Lambda$.

## Remarks

Let $P$ be a fundamental parallelepiped of $\Lambda$, so that the translates $P + v$ with $v \in \Lambda$ are pairwise disjoint and cover $\R^n$.
Cut $S$ into the pieces $S \cap (P + v)$ and translate each piece by $-v$ into $P$.
The translated pieces have total volume $\operatorname{vol}(S) > \operatorname{vol}(P) = \det \Lambda$, so two of them overlap; a common point gives $x - v = y - w$ with $x \ne y$ in $S$ and $v \ne w$ in $\Lambda$.
[[Minkowski's theorem|0K387S2PKQ]] follows: if $K$ is convex, symmetric about $0$, and $\operatorname{vol}(K) > 2^n \det \Lambda$, apply the theorem to $S = \tfrac12 K$.
It gives $x \ne y$ in $S$, and $x - y = \tfrac12(2x) + \tfrac12(-2y)$ is a nonzero point of $K \cap \Lambda$.
The bound is sharp: the half-open square $[0, 1)^2$ has area $1 = \det \Z^2$, and no two of its distinct points differ by an integer vector.
More generally, if $\operatorname{vol}(S) > k \det \Lambda$ for a positive integer $k$, the same argument gives $k + 1$ distinct points of $S$ whose pairwise differences lie in $\Lambda$.

## Explanations

### L1 human

Move every point of a region of the plane by whole steps left, right, up or down until it lands in the unit square.
If the region has area larger than $1$, the moved pieces cannot all fit in the square without overlapping.
So the region contains two points that differ by a whole-number shift.
The theorem says the same for any lattice in any dimension, with the volume of a lattice cell in place of $1$.

### L2 human

Blichfeldt's theorem is the measure-theoretic pigeonhole principle behind the geometry of numbers.
It gives a short proof of Minkowski's convex body theorem, and through it of results such as the two-square and four-square theorems.
It holds for any measurable set, convex or not, which makes it useful when the region of interest is not convex.
