---
tag: RJE1W5NRE3
kind: statement
role: theorem
name: Jensen's covering theorem
msc: ["03E45"]
uses: [6TF2JBTPPJ, HCTNBZZQ0W, 0YSCSX5YZC, 0EBACQFAZW]
about: [6TF2JBTPPJ, HCTNBZZQ0W]
sources:
  - url: https://en.wikipedia.org/wiki/Jensen's_covering_theorem
same_as:
  wikidata: Q6179899
  wikipedia: Jensen's covering theorem
---

## Statement

Assume ZFC, and assume that [[zero sharp|HCTNBZZQ0W]] does not exist.
Then for every uncountable set $X$ of [[ordinals|0YSCSX5YZC]] there is a set $Y$ in the [[constructible universe|6TF2JBTPPJ]] $L$ such that $X \subseteq Y$ and $\abs{Y} = \abs{X}$.

## Remarks

The proof by Jensen uses the fine structure theory of $L$; one takes an elementary substructure that contains $X$ and analyses its transitive collapse.
A consequence: if $0^\sharp$ does not exist, then every singular cardinal $\kappa$ of $V$ is singular in $L$, and $(\kappa^+)^L = \kappa^+$.
It also follows that the singular cardinals hypothesis holds when $0^\sharp$ does not exist.
The hypothesis is necessary.
If $0^\sharp$ exists, then $\aleph_\omega$ is a regular cardinal in $L$.
Then the set $X = \omega_1 \cup \set{\aleph_n : n < \omega}$ of size $\aleph_1$ cannot be covered.
Indeed, a set $Y \in L$ with $\abs{Y} = \aleph_1$ has order type less than $\omega_2$.
So $Y \cap \aleph_\omega$ has $L$-cardinality less than $\aleph_\omega$, and it is bounded in $\aleph_\omega$.

## Explanations

### L1 human

The theorem says that, unless zero sharp exists, the constructible universe is a good approximation of the full universe.
Every uncountable set of ordinals sits inside a constructible set of the same size.
So the constructible universe cannot miss much: it has the same large singular cardinals and the same successors of them.
This gives a dichotomy: either the constructible universe is close to everything, or it is very thin.

### L2 human

The theorem is the model for many covering results for larger inner models, such as the Dodd–Jensen core model and the [[core model|A6ZJ8MSCAY]] in general.
It turns the nonexistence of a large cardinal object into strong combinatorial consequences, such as the singular cardinals hypothesis.
Read the other way, it gives lower bounds for consistency strength.
If the singular cardinals hypothesis fails, then $0^\sharp$ exists, and in fact much stronger large cardinal hypotheses hold in inner models.
