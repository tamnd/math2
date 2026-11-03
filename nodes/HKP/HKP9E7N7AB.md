---
tag: HKP9E7N7AB
kind: statement
role: proposition
name: Canonical commutation relation
msc: ["81S05", "81Q10", "47B25"]
uses: [7XAKGQQWTP, 5WG6YTAA6J, 0PXW0BN7DW, CG9JEATW3Q, SASP14MA1Z, 2S0MXDT4YH, Z877XDBMQ3]
about: [7XAKGQQWTP, 5WG6YTAA6J]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_commutation_relation
same_as:
  wikidata: Q473322
  wikipedia: Canonical commutation relation
---

## Statement

Let $\hbar > 0$, and let $X$ and $P$ be the [[position operator|7XAKGQQWTP]] and the [[momentum operator|5WG6YTAA6J]] on [[$L^2(\R)$|SASP14MA1Z]].
Let $\mathcal{S}(\R)$ be the [[Schwartz space|CG9JEATW3Q]].
Then $X$ and $P$ map $\mathcal{S}(\R)$ into itself, and for every $\psi \in \mathcal{S}(\R)$,
$$X P \psi - P X \psi = i\hbar\, \psi.$$
In [[commutator|0PXW0BN7DW]] notation, $[X, P] = i\hbar I$ on $\mathcal{S}(\R)$.

## Remarks

On $\mathcal{S}(\R)$ one has $(X\psi)(x) = x\psi(x)$ and $P\psi = -i\hbar\psi'$, and both maps preserve $\mathcal{S}(\R)$.
By the product rule, $P(X\psi) = -i\hbar(\psi + x\psi')$, while $X(P\psi) = -i\hbar x\psi'$.
The difference is $i\hbar\psi$.

In $\R^n$, with $X_j$ and $P_k = -i\hbar\, \partial/\partial x_k$, the same computation gives $[X_j, P_k] = i\hbar \delta_{jk} I$, $[X_j, X_k] = 0$ and $[P_j, P_k] = 0$ on $\mathcal{S}(\R^n)$.

No pair of bounded operators $A, B$ on a nonzero Hilbert space satisfies $AB - BA = cI$ with $c \ne 0$.
In finite dimension $n$ this follows from the trace: $\operatorname{tr}(AB - BA) = 0 \ne cn$.
So at least one of $X, P$ must be unbounded, and the relation can only hold on a subspace such as $\mathcal{S}(\R)$.

The relation mirrors the [[Poisson bracket|2S0MXDT4YH]] $\set{x, p} = 1$ of classical mechanics, with $[\cdot, \cdot]/(i\hbar)$ in place of $\set{\cdot, \cdot}$.
The [[Stone–von Neumann theorem|Z877XDBMQ3]] says that, in the exponentiated Weyl form, the relation has essentially one irreducible representation, the Schrödinger representation on $L^2(\R^n)$.

## Explanations

### L1 human

Measuring the position and then the momentum is not the same as doing it in the other order.
The commutation relation measures the difference: it is always $i\hbar$ times the identity.
This small identity is behind the uncertainty principle and behind the discreteness of energy levels in many systems.

### L2 human

The relation is the defining rule of canonical quantization: one replaces classical coordinates and momenta by operators whose commutators are $i\hbar$ times the classical Poisson brackets.
With the Robertson inequality it gives $\sigma_X \sigma_P \ge \hbar/2$ for states in $\mathcal{S}(\R)$.
Domain questions are real.
Some pairs of self-adjoint operators satisfy the relation on a dense invariant domain but are not unitarily equivalent to the Schrödinger pair.
This is why the Stone–von Neumann theorem uses the Weyl form.
