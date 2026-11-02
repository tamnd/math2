---
tag: 6ZDSVX9GAR
kind: statement
role: theorem
name: Besicovitch covering theorem
msc: [28A75, 28A15]
uses: [0XPR1E85W0, 05DSV40EB9]
about: [05DSV40EB9]
sources:
  - url: https://en.wikipedia.org/wiki/Besicovitch_covering_theorem
same_as:
  wikidata: Q137164
  wikipedia: Besicovitch covering theorem
---

## Statement

For each integer $n \ge 1$ there is an integer $N_n$, depending only on $n$, with the following property.
Let $\mathcal{F}$ be a family of [[closed balls|05DSV40EB9]] of positive radius in [[Euclidean space|0XPR1E85W0]] $\R^n$ with $\sup \set{\operatorname{diam} B : B \in \mathcal{F}} < \infty$.
Let $A$ be the set of centres of the balls of $\mathcal{F}$.
Then there are subfamilies $\mathcal{G}_1, \dots, \mathcal{G}_{N_n} \subseteq \mathcal{F}$ such that:

1. Each $\mathcal{G}_i$ is a countable family of pairwise disjoint balls.
2. $A \subseteq \bigcup_{i=1}^{N_n} \bigcup_{B \in \mathcal{G}_i} B$.

## Remarks

The proof chooses balls greedily, each time a ball of nearly maximal radius centred at a point not yet covered.
A geometric argument in $\R^n$ shows that each chosen ball meets only a bounded number of earlier chosen balls of comparable or larger size, with a bound depending on $n$.
The chosen balls are then sorted into $N_n$ disjoint subfamilies.

Unlike the Vitali covering lemma, no enlargement of the balls is needed and no measure enters the statement.
So its consequences hold for every Radon measure on $\R^n$, doubling or not.
A consequence concerns a locally finite Borel measure $\mu$ on $\R^n$ and a set $A$.
If every point of $A$ is the centre of balls of $\mathcal{F}$ of arbitrarily small radius, then some countable disjoint subfamily of $\mathcal{F}$ covers $\mu$-almost all of $A$.

The fact that the balls are centred at points of $A$ is essential.
The theorem does not extend to general metric spaces.

## Explanations

### L1 human

Every point of a set is the centre of a ball.
One can choose some of these balls so that they still cover all the centres, and so that no point is in too many of the chosen balls.
The bound on the overlap depends only on the dimension.

### L2 human

The theorem is the covering tool for measures that are not doubling.
It gives the differentiation theorem $\lim_{r \to 0} \nu(B(x,r)) / \mu(B(x,r)) = \frac{d\nu}{d\mu}(x)$ for Radon measures $\mu, \nu$ on $\R^n$ with $\nu \ll \mu$, for $\mu$-almost every $x$.
It is a basic tool of geometric measure theory.
