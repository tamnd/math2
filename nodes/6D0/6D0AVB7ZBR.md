---
tag: 6D0AVB7ZBR
kind: definition
name: Almost everywhere
msc: [28A12, 28A20]
defines: RARTMA0ZEC
uses: [P15VQS5DJ9, VQQM4Y550T, 0ST21PGDAP]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_everywhere
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]], and let $P(x)$ be a statement about the points $x \in X$.
The statement $P$ holds *$\mu$-almost everywhere* if there is a [[null set|VQQM4Y550T]] $N \in \Sigma$ such that $P(x)$ is true for every $x \in X \setminus N$.

## Remarks

Let $\lambda$ be Lebesgue measure on $\R$ and let $f(x) = 1$ for rational $x$ and $f(x) = 0$ otherwise.
Then $f = 0$ holds $\lambda$-almost everywhere: take $N = \Q$, a countable set, so $\lambda(\Q) = 0$.
The statement $x \ne 0 \Rightarrow x < 0$ does not hold $\lambda$-almost everywhere, since it fails on $(0, \infty)$, and every measurable set containing $(0, \infty)$ has measure $\infty$.
The set where $P$ fails is only required to lie inside a null set; it need not be measurable itself.
The usual abbreviation is a.e., or $\mu$-a.e.
On a probability space, almost everywhere is called [[almost surely|0ST21PGDAP]].
