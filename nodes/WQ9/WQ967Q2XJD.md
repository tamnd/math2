---
tag: WQ967Q2XJD
kind: statement
role: theorem
name: Easton's theorem
msc: ["03E35", "03E10"]
uses: [ZCE333FAWC, NTE5C260S1, 0QKPNZKNEA, 0MN2MER9WN, F2DTWW9HP7]
about: [13ZV2F8JAR]
sources:
  - url: https://en.wikipedia.org/wiki/Easton's_theorem
same_as:
  wikidata: Q2226644
  wikipedia: Easton's theorem
---

## Statement

Let $M$ be a countable transitive model of ZFC in which the generalized continuum hypothesis holds.
Let $F$ be a class function, definable in $M$, from the [[regular cardinals|ZCE333FAWC]] of $M$ to the [[cardinals|0QKPNZKNEA]] of $M$.
Assume that in $M$ the function $F$ satisfies both conditions:

1. If $\kappa \le \lambda$, then $F(\kappa) \le F(\lambda)$.
2. $\operatorname{cf}(F(\kappa)) > \kappa$ for each $\kappa$, where $\operatorname{cf}$ is the [[cofinality|NTE5C260S1]].

Then there is a [[forcing|F2DTWW9HP7]] extension $N$ of $M$ with the same cardinals and the same cofinalities as $M$.
In $N$, $2^\kappa = F(\kappa)$ for every regular cardinal $\kappa$.

## Remarks

The two conditions are exactly the constraints that ZFC proves for $\kappa \mapsto 2^\kappa$ on regular cardinals.
Monotonicity is clear, and $\operatorname{cf}(2^\kappa) > \kappa$ is König's theorem.
The proof uses a class product of Cohen-style forcings, one for each regular $\kappa$, with supports chosen so that the whole product preserves cardinals.
Example: one can have $2^{\aleph_0} = \aleph_2$ and $2^{\aleph_1} = \aleph_2$, or $2^{\aleph_0} = \aleph_{\omega + 1}$.
But $2^{\aleph_0} = \aleph_\omega$ is impossible, since $\operatorname{cf}(\aleph_\omega) = \omega$.
The theorem says nothing about singular cardinals, where the situation is far more constrained, as in Silver's theorem and the singular cardinals hypothesis.

## Explanations

### L1 human

For an infinite cardinal $\kappa$, the number $2^\kappa$ counts the subsets of a set of size $\kappa$.
The usual axioms of set theory say very little about it.
Easton's theorem makes this precise for regular cardinals: apart from two simple rules, any pattern of values is possible.
For example, the axioms do not decide whether there are $\aleph_1$ or $\aleph_2$ real numbers.

### L2 human

Forcing with Cohen reals shows that $2^{\aleph_0}$ can be any cardinal of uncountable cofinality.
Easton's theorem extends this to all regular cardinals at once.
It shows that monotonicity and König's theorem are the only ZFC constraints on the function $\kappa \mapsto 2^\kappa$ on regular cardinals.
At singular cardinals the story changes: the values of $2^\kappa$ below a singular cardinal can restrict its value at that cardinal.
This is the subject of Silver's theorem, of the singular cardinals hypothesis and of Shelah's pcf theory.
