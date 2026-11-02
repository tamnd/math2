---
tag: 19JFF3GY9F
kind: example
name: Interval exchange transformation
msc: ["37E05", 37A05, 37A25]
instance_of: [556WBDAHNP]
uses: [2Z2QVWZ262, 2Q1J7RZ4TK, NZZE9KCAD8]
sources:
  - url: https://en.wikipedia.org/wiki/Interval_exchange_transformation
same_as:
  wikidata: Q17081747
  wikipedia: Interval exchange transformation
---

## Example

Let $d \ge 2$, let $\lambda_1, \dots, \lambda_d > 0$ be lengths with sum $\abs{\lambda} = \lambda_1 + \cdots + \lambda_d$, and let $\pi$ be a permutation of $\set{1, \dots, d}$.
Cut $I = [0, \abs{\lambda})$ into the intervals $I_j = [\lambda_1 + \cdots + \lambda_{j-1}, \lambda_1 + \cdots + \lambda_j)$, for $j = 1, \dots, d$.
The *interval exchange transformation* $T \colon I \to I$ translates each $I_j$ so that the intervals appear in the new order $I_{\pi^{-1}(1)}, I_{\pi^{-1}(2)}, \dots, I_{\pi^{-1}(d)}$ from left to right.
Explicitly, for $x \in I_j$,
$$T(x) = x - \sum_{i < j} \lambda_i + \sum_{\pi(i) < \pi(j)} \lambda_i.$$

Check that $T$ is a [[measure-preserving transformation|556WBDAHNP]] for [[Lebesgue measure|2Z2QVWZ262]].
Indeed, $T$ is a bijection of $I$, and it is a translation on each of the finitely many intervals $I_j$.
Translations preserve length, so for every Borel set $E \subseteq I$, $\abs{T^{-1}E} = \sum_j \abs{T^{-1}E \cap I_j} = \sum_j \abs{E \cap T(I_j)} = \abs{E}$.

Concrete case: $d = 2$ and $\pi$ the transposition, with $0 < \alpha < 1$ and lengths $\lambda_1 = 1 - \alpha$ and $\lambda_2 = \alpha$.
Then $T(x) = x + \alpha$ on $[0, 1 - \alpha)$ and $T(x) = x - (1 - \alpha)$ on $[1 - \alpha, 1)$, so $T(x) = x + \alpha \bmod 1$, the [[rotation of the circle|2Q1J7RZ4TK]].
Interval exchanges are thus a generalization of circle rotations.

For an irreducible permutation $\pi$ and Lebesgue almost every length vector, the interval exchange is [[uniquely ergodic|NZZE9KCAD8]].
Masur and Veech proved this independently in 1982.

## Explanations

### L1 human

Cut a stick into several pieces, shuffle the pieces into a new order without flipping them, and glue them back.
That rearrangement is an interval exchange.
Repeating it moves points around in a way that never changes the total length of any set.
With two pieces it is just a rotation of a circle; with more pieces it already leads to deep questions, linked to flat surfaces and billiards in polygons.
