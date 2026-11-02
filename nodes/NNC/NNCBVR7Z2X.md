---
tag: NNCBVR7Z2X
kind: statement
role: theorem
name: Eilenberg–Moore spectral sequence
msc: [55T20, 55R20]
uses: [PB9JXQ2KC3, DDQRERAQCV, 6N7BC70CX0, RDT4785M4D, 2JFF5F3EGF]
sources:
  - url: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Moore_spectral_sequence
same_as:
  wikidata: Q5349492
  wikipedia: Eilenberg–Moore spectral sequence
---

## Statement

Let $k$ be a field.
Let $\pi \colon E \to B$ be a [[Serre fibration|PB9JXQ2KC3]] and let $f \colon X \to B$ be a continuous map, where $X$, $E$ and $B$ are path-connected and $B$ is simply connected.
Assume that $H^n(X; k)$, $H^n(E; k)$ and $H^n(B; k)$ are finite-dimensional for every $n$.
Let $E_f = X \times_B E$ be the pullback fibration over $X$.
Then there is a second-quadrant spectral sequence that converges strongly to $H^*(E_f; k)$.
Its second page is
$$E_2^{-p, q} = \operatorname{Tor}^{-p, q}_{H^*(B; k)}\big(H^*(X; k), H^*(E; k)\big),$$
the bigraded [[Tor|DDQRERAQCV]] over the [[cohomology ring|RDT4785M4D]] $H^*(B; k)$, where $p$ is the homological degree and $q$ the internal degree.

## Remarks

The proof compares the cochains of $E_f$ with the derived tensor product of the cochains of $X$ and $E$ over the cochains of $B$.
The spectral sequence comes from filtering a bar construction by bar length.
Some condition on $\pi_1(B)$ is needed for convergence; for general non-simply-connected $B$ the spectral sequence may fail to converge to the cohomology of the pullback.

Taking $X$ a point gives a spectral sequence $\operatorname{Tor}_{H^*(B)}(k, H^*(E)) \Rightarrow H^*(F)$ for the fibre $F$.
Taking $X$ a point and $E$ the contractible path space gives $\operatorname{Tor}_{H^*(B)}(k, k) \Rightarrow H^*(\Omega B)$, the cohomology of the [[loop space|2JFF5F3EGF]].

Example: for $B = S^n$ with $n \ge 2$, $H^*(S^n; k)$ is an exterior algebra on a class $x$ of degree $n$.
Then $\operatorname{Tor}_{H^*(S^n)}(k, k)$ has one copy of $k$ in each bidegree $(-j, jn)$, of total degree $j(n-1)$, and the spectral sequence collapses for degree reasons.
This gives $H^i(\Omega S^n; k) \cong k$ when $n - 1$ divides $i$, and $0$ otherwise.

## Explanations

### L1 human

The Eilenberg–Moore spectral sequence computes the cohomology of a pullback, such as a fibre or a loop space, from the cohomology of the spaces it is built from.
Where the Serre spectral sequence goes from base and fibre to total space, this one goes from base and total space to the fibre.
Its starting page is an algebraic Tor group over the cohomology ring of the base.

### L2 human

The spectral sequence is a key tool for computing the cohomology of loop spaces and of homogeneous spaces $G/H$ of Lie groups.
It shows, for instance, that the cohomology of $\Omega B$ depends only on the cochain algebra of $B$ up to quasi-isomorphism when $B$ is simply connected.
It is dual in spirit to the Serre spectral sequence, and the two are often used together.
