---
tag: T6A6ENWEKC
kind: definition
name: System of imprimitivity
msc: ["22D30", "22D10"]
defines: KMDXTQTR4D
uses: [AHV05ZBCYW, 74BPYJNZTM, HM2HHE3J51, ATGT25E5FF, 0WCY42EV9V]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_imprimitivity
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] that acts on a space $X$ with a Borel structure.
Assume that each map $x \mapsto g x$ is a Borel bijection.
Let $\mathcal{H}$ be a [[Hilbert space|HM2HHE3J51]].
A *system of imprimitivity* for $G$ based on $X$ is a pair $(\pi, P)$ where:

1. $\pi$ is a [[unitary representation|74BPYJNZTM]] of $G$ on $\mathcal{H}$;
2. $P$ is a [[projection-valued measure|ATGT25E5FF]] on the Borel sets of $X$, with values projections on $\mathcal{H}$;
3. $\pi(g) P(E) \pi(g)^{-1} = P(gE)$ for every $g \in G$ and every Borel set $E \subseteq X$.

## Remarks

In most uses, $X = G/H$ for a closed subgroup $H$, with $G$ acting by left multiplication.

Example: let $G$ be a discrete group acting on a countable set $X$, let $\mathcal{H} = \ell^2(X)$ with basis $(\delta_x)$, let $\pi(g)\delta_x = \delta_{gx}$, and let $P(E)$ be multiplication by the indicator $\mathbf{1}_E$.
For $y \in X$, $\pi(g)P(E)\pi(g)^{-1}\delta_y = \pi(g)P(E)\delta_{g^{-1}y}$, which is $\delta_y$ if $g^{-1}y \in E$ and $0$ otherwise.
This is $P(gE)\delta_y$, so clause 3 holds.

Non-example: take $G = X = \Z$ acting by translation, $\mathcal{H} = \ell^2(\Z)$, the same $P$, but $\pi(g) = I$ for all $g$.
Then clause 3 would give $P(\set{0}) = P(\set{1})$, which is false.

The [[induced representation|JJP4JFH3C6]] $\operatorname{Ind}_H^G \sigma$ has a canonical system of imprimitivity based on $G/H$, in which $P(E)$ multiplies functions by $\mathbf{1}_E$.
For second countable $G$, the [[Mackey imprimitivity theorem|CTYQQWJPMB]] says that every system of imprimitivity based on $G/H$ is equivalent to one of these.
