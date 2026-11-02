---
tag: 3QB691PFPB
kind: definition
name: Nonparametric statistics
msc: [62G05, 62G10]
defines: VFAJ1EG3X5
uses: [K3AMMSY8DD, MSC0MR8VMH]
sources:
  - url: https://en.wikipedia.org/wiki/Nonparametric_statistics
---

## Definition

Let $\mathcal{P}$ be a [[statistical model|K3AMMSY8DD]], a set of probability distributions on a sample space.
The model $\mathcal{P}$ is *nonparametric* if it is not a [[parametric model|MSC0MR8VMH]].
That is, it cannot be indexed in a natural way by a parameter in a subset of $\R^k$ for a fixed $k$.
*Nonparametric statistics* is the study of inference in nonparametric models.
It also covers *distribution-free* procedures: tests or intervals whose law under the null hypothesis is the same for all distributions in a nonparametric class.

## Remarks

"Natural" means that the indexing map has the regularity required of a parametric model.
Any set of the size of $\R$ is in bijection with $\R$, so a bare bijection does not count.
Example: the set of all distributions on $\R$ with a continuous distribution function is nonparametric.
Example: the sign test of $H_0 \colon$ the median is $0$ is distribution-free.
Under $H_0$, the number of positive observations is binomial with parameters $n$ and $1/2$, for every continuous law with median $0$.
Non-example: the family $\set{\mathcal{N}(\mu, \sigma^2) : \mu \in \R, \sigma > 0}$ is parametric, with $k = 2$.
Semiparametric models mix both kinds, with a finite-dimensional parameter of interest and an infinite-dimensional nuisance part.
