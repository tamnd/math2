---
tag: DWV9B8VTEZ
kind: definition
name: Position operator
msc: ["81Q10", "47B25"]
defines: 7XAKGQQWTP
uses: [SASP14MA1Z, DF5RN297GE, KRJX5RA0PW, 0NEGN5CRSC, 9F6B05QAWH, BMKATJ802A]
sources:
  - url: https://en.wikipedia.org/wiki/Position_operator
---

## Definition

Let [[$L^2(\R)$|SASP14MA1Z]] be the Hilbert space of a particle on the line.
The *position operator* $X$ is the operator with domain
$$D(X) = \set{\psi \in L^2(\R) : \int_\R x^2 \abs{\psi(x)}^2 \, dx < \infty}$$
given by $(X\psi)(x) = x\psi(x)$.
In $\R^n$, the position operators $X_1, \dots, X_n$ on $L^2(\R^n)$ are defined in the same way with $x_j$ in place of $x$.

## Remarks

$X$ is an [[unbounded|KRJX5RA0PW]] [[self-adjoint operator|0NEGN5CRSC]], so it is an [[observable|DF5RN297GE]].
It is the unbounded analogue of a [[multiplication operator|9F6B05QAWH]].
Its [[spectrum|BMKATJ802A]] is $\R$, and it has no eigenvalues, since $x\psi(x) = a\psi(x)$ almost everywhere forces $\psi = 0$ almost everywhere.
Its projection-valued measure is $P^X(B)\psi = \mathbf{1}_B \psi$, so the probability that the position lies in $B$ is $\int_B \abs{\psi}^2 \, dx$.

Example: $\psi(x) = \pi^{-1/4} e^{-x^2/2}$ lies in $D(X)$, since $\int x^2 \pi^{-1/2} e^{-x^2}\, dx = 1/2 < \infty$.
Its expectation value is $\ip{\psi}{X\psi} = \int x \pi^{-1/2} e^{-x^2}\, dx = 0$.

Non-example: $\psi(x) = \pi^{-1/2}(1 + x^2)^{-1/2}$ is a unit vector of $L^2(\R)$, but $\int x^2 \abs{\psi}^2 \, dx = \pi^{-1} \int x^2/(1 + x^2)\, dx = \infty$, so $\psi \notin D(X)$.
