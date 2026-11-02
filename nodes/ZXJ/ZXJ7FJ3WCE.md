---
tag: ZXJ7FJ3WCE
kind: statement
role: theorem
name: Hellinger–Toeplitz theorem
msc: [47B25, 47A05]
uses: [HM2HHE3J51, 0NRYHJPQG2, 03TM135G0N, GXM8BX8YM7, VM7B38PA87]
about: [03TM135G0N]
sources:
  - url: https://en.wikipedia.org/wiki/Hellinger%E2%80%93Toeplitz_theorem
same_as:
  wikidata: Q1472120
  wikipedia: Hellinger–Toeplitz theorem
---

## Statement

Let $H$ be a [[Hilbert space|HM2HHE3J51]] over $\R$ or $\C$ with inner product $\ip{\cdot}{\cdot}$.
Let $A \colon H \to H$ be a [[linear map|0NRYHJPQG2]] defined on all of $H$.
Assume that
$$\ip{Ax}{y} = \ip{x}{Ay} \qquad \text{for all } x, y \in H.$$
Then $A$ is bounded, that is, $A$ is a [[continuous linear map|03TM135G0N]].

## Remarks

Proof idea: by the [[closed graph theorem|GXM8BX8YM7]], it suffices to show that $A$ is [[closed|VM7B38PA87]].
If $x_n \to x$ and $A x_n \to z$, then for every $y \in H$,
$$\ip{z}{y} = \lim \ip{A x_n}{y} = \lim \ip{x_n}{Ay} = \ip{x}{Ay} = \ip{Ax}{y},$$
so $z = Ax$.

Example: if $A$ is given on $\ell^2$ by a real symmetric infinite matrix and is defined on all of $\ell^2$, the theorem says $A$ is automatically bounded.

Completeness of $H$ is needed.
On the space of finitely supported sequences with the $\ell^2$ inner product, the diagonal map $(x_n) \mapsto (n x_n)$ is defined everywhere and symmetric.
It is unbounded, since it sends the $n$-th unit vector to $n$ times itself.

## Explanations

### L1 human

In quantum mechanics, observables are represented by symmetric operators, and many of them, such as position and momentum, are unbounded.
The theorem says that such an unbounded symmetric operator can never be defined on the whole Hilbert space.
So domains are unavoidable in the theory of unbounded operators.

### L2 human

The theorem is a short application of the closed graph theorem, and it is one reason why the theory of unbounded self-adjoint operators works with dense, proper domains.
It also shows that a bounded operator is self-adjoint exactly when it is symmetric on all of $H$; no extra boundedness hypothesis is needed.
A related form: a linear map $A \colon H \to H$ that has a formal adjoint $B \colon H \to H$, with $\ip{Ax}{y} = \ip{x}{By}$ for all $x, y$, is bounded, by the same proof.
