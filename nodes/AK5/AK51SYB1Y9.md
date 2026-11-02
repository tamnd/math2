---
tag: AK51SYB1Y9
kind: definition
name: Infinite loop space
msc: [55P47, 55P42]
defines: A7VB2NSGJ2
uses: [2JFF5F3EGF, T9DG8DDE75, 4Q3WY1RX91, 1GHF4EKBXS, EASHTX8EG5]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_loop_space_machine
---

## Definition

Let $X$ be a [[pointed space|T9DG8DDE75]], and write $\Omega Y$ for the [[loop space|2JFF5F3EGF]] of a pointed space $Y$.
The space $X$ is an *infinite loop space* if there are pointed spaces $X_0, X_1, X_2, \ldots$ and [[weak homotopy equivalences|4Q3WY1RX91]]
$$X \simeq X_0, \qquad X_n \to \Omega X_{n+1} \quad \text{for all } n \ge 0.$$

## Remarks

The sequence $(X_n)$ with the adjoint maps $\Sigma X_n \to X_{n+1}$ is an $\Omega$-[[spectrum|1GHF4EKBXS]] $E$, and $X$ is weakly equivalent to its zeroth space $\Omega^\infty E$.
Conversely, the zeroth space of every $\Omega$-spectrum is an infinite loop space.

Example: for an abelian group $A$, the Eilenberg–MacLane spaces satisfy $K(A, n) \simeq \Omega K(A, n+1)$, so $K(A, 0) = A$ with the discrete topology is an infinite loop space with $X_n = K(A, n)$.
The check: $\pi_k \Omega K(A, n+1) = \pi_{k+1} K(A, n+1)$, which is $A$ for $k = n$ and $0$ otherwise.

Example: for a pointed CW complex $Y$, the space $QY = \operatorname{colim}_n \Omega^n \Sigma^n Y$ is an infinite loop space, with $X_n = Q \Sigma^n Y$.
By Bott periodicity, $\Z \times BU$ is an infinite loop space too.

Non-example: the sphere $S^2$ is not an infinite loop space, and not even a loop space.
A loop space is an [[H-space|EASHTX8EG5]], and $S^2$ is not one: a cup product computation in $H^*(S^2 \times S^2; \Z)$ rules out any H-space multiplication on $S^2$.
