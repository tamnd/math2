---
tag: W91HFP63SN
kind: definition
name: Completely distributive lattice
msc: [06D10, 06B23]
defines: 5TBC06NNS1
uses: [D7A0ZGZT5S, 0HM0HQCK6N, 00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Completely_distributive_lattice
---

## Definition

Let $L$ be a [[complete lattice|D7A0ZGZT5S]].
Let $J$ be a set, let $(K_j)_{j \in J}$ be a family of sets, and let $x_{j,k} \in L$ for $j \in J$ and $k \in K_j$.
Let $F$ be the set of choice functions $f$ on $J$ with $f(j) \in K_j$ for every $j \in J$.
The lattice $L$ is *completely distributive* if for all such data
$$\bigwedge_{j \in J} \bigvee_{k \in K_j} x_{j,k} = \bigvee_{f \in F} \bigwedge_{j \in J} x_{j, f(j)}.$$

## Remarks

Example: the [[power set|00E0YZCERH]] of a set $X$.
A point $x$ lies in $\bigcap_j \bigcup_k x_{j,k}$ if and only if for each $j$ there is $k = f(j)$ with $x \in x_{j, f(j)}$.
This is membership in the right side, where the axiom of choice picks $f$.
Non-example: the lattice of open subsets of $\R$ is a frame but not completely distributive.
Take $J = \N_{\ge 1}$, $K_j = \set{1, 2}$, $x_{j,1} = (-1/j, 1/j)$ and $x_{j,2} = \R \setminus \set{0}$.
The left side is $\R$.
Each meet on the right is the interior of an intersection and never contains $0$, so the right side is $\R \setminus \set{0}$.
Complete distributivity is self-dual: the condition is equivalent to the same identity with $\bigwedge$ and $\bigvee$ exchanged.
Every completely distributive lattice is a [[distributive lattice|0HM0HQCK6N]].
