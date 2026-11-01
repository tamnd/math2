---
tag: YBAE5QCH1A
kind: example
name: Voter model
msc: [60K35, 82C22]
instance_of: [GR49AM3PSZ]
sources:
  - url: https://en.wikipedia.org/wiki/Voter_model
same_as:
  wikidata: Q7942158
  wikipedia: Voter model
---

## Example

Let $d \ge 1$.
The *voter model* on $\Z^d$ is the spin system on $\set{0, 1}^{\Z^d}$ with flip rates
$$c(x, \eta) = \frac{1}{2d} \, \#\set{y \in \Z^d : \abs{y - x} = 1, \ \eta(y) \ne \eta(x)}.$$
Here $\eta(x)$ is the opinion of the voter at site $x$.
At rate $1$, each voter picks one of its $2d$ neighbours uniformly at random and adopts that neighbour's opinion.
The rates lie in $[0, 1]$ and depend on $2d + 1$ sites, so it is an [[interacting particle system|GR49AM3PSZ]].

## Remarks

The two constant configurations, all $0$ and all $1$, are absorbing.
The model is dual to a system of coalescing [[random walks|04VZE3FZXF]].
Tracing back whose opinion a voter holds gives a random walk path, and two such paths merge when they meet.
Because of this duality, the long-time behaviour depends on whether simple random walk on $\Z^d$ is recurrent, which by [[Pólya's recurrence theorem|BEQH6AZPYM]] holds exactly for $d \le 2$.
Started from independent opinions with density $\rho \in (0, 1)$, for $d \le 2$ any two sites tend to agree, $P(\eta_t(x) \ne \eta_t(y)) \to 0$ as $t \to \infty$.
For $d \ge 3$ there is a one-parameter family of invariant measures in which both opinions keep a positive density.

## Explanations

### L1 human

Each person on a grid holds one of two opinions.
From time to time a person asks a random neighbour and copies their opinion.
Nobody is persuaded by arguments; opinions simply spread by imitation.
On a line or in the plane, large regions of agreement form and grow, while in three or more dimensions disagreement can persist forever.
