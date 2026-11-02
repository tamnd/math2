---
tag: QQ717VSFNN
kind: conjecture
name: Vojta's conjecture
msc: [11J97, 11G50, 14G40]
uses: [MWBDFS2KJ5, F1FF505PWH, W05VYY4HBR, RRK8P6TXG2, Z9DN23DAE2, 8SQK7RTB63, SWJYG87QQH]
about: [F1FF505PWH, SWJYG87QQH]
sources:
  - url: https://en.wikipedia.org/wiki/Vojta%27s_conjecture
same_as:
  wikidata: Q7939859
  wikipedia: Vojta's conjecture
history:
  posed_by: "Paul Vojta"
  first_stated: "1987"
---

## Statement

Let $F$ be an [[algebraic number field|MWBDFS2KJ5]] and let $X$ be a smooth projective variety over $F$.
Let $D$ be an effective reduced [[divisor|Z9DN23DAE2]] on $X$ with at most normal crossings.
Let $K_X$ be a [[canonical divisor|W05VYY4HBR]] and let $A$ be an [[ample|RRK8P6TXG2]] divisor on $X$.
Let $S$ be a finite set of places of $F$.
Let $h_{K_X}$ and $h_A$ be Weil [[heights|F1FF505PWH]] for $K_X$ and $A$, and let $\lambda_{D,v}$ be a local height function for $D$ at the place $v$.
Then for every $\varepsilon > 0$ there are a proper Zariski closed subset $Z \subsetneq X$ and a constant $C$ such that
$$\sum_{v \in S} \lambda_{D,v}(P) + h_{K_X}(P) \le \varepsilon \, h_A(P) + C$$
for all $P \in X(F)$ with $P \notin Z$.

## Remarks

Vojta formulated the conjecture in 1987 by analogy with the second main theorem of Nevanlinna theory, through a dictionary between Diophantine approximation and value distribution.
For $X = \mathbb{P}^1$ and $D$ a sum of distinct points, the conjecture is Roth's theorem, which is known.
For $X = \mathbb{P}^n$ and $D$ a sum of hyperplanes in general position, it is Schmidt's subspace theorem, which is also known.
Let $X$ be of general type and $D = 0$.
Outside a proper closed subset, the canonical height is at least $\delta h_A - C'$ for some $\delta > 0$.
Taking $\varepsilon < \delta$ then forces $X(F)$ into a proper closed subset, which is the [[Bombieri–Lang conjecture|TQ1QDAK2BR]].
Generalized forms for algebraic points, with truncated local heights, are higher-dimensional analogues of the [[abc conjecture|G7JH2NXPC0]].
The conjecture is open in general.

## Explanations

### L1 human

Heights measure how complicated a rational point is.
Vojta's conjecture is a single inequality between heights that predicts how close rational points can come to a fixed divisor, given the curvature of the variety.
It unifies many famous results and conjectures.
Roth's theorem on approximating algebraic numbers, Faltings's theorem on curves and the Bombieri–Lang conjecture appear as special cases.
Its generalizations are related to the abc conjecture.
