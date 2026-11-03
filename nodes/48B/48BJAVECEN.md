---
tag: 48BJAVECEN
kind: definition
name: Canonical coordinates
msc: [70H15, 53D05, 70G10]
defines: XKDVF07R1Q
uses: [CAN490EPRT, 0QHTX7WQEY, 2S0MXDT4YH]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_coordinates
---

## Definition

Let $(M, \omega)$ be a [[symplectic manifold|CAN490EPRT]] of dimension $2n$, and let $V \subseteq M$ be open.
A chart $(q_1, \ldots, q_n, p_1, \ldots, p_n) \colon V \to \R^{2n}$ is a system of *canonical coordinates* on $V$ when the symplectic [[form|0QHTX7WQEY]] is
$$\omega = \sum_{i=1}^n dp_i \wedge dq_i \quad \text{on } V.$$
The functions $q_i$ are the *canonical positions* and the $p_i$ are the *canonical momenta*.

## Remarks

Equivalently, the [[Poisson brackets|2S0MXDT4YH]] of the coordinate functions are
$$\{q_i, q_j\} = 0, \qquad \{p_i, p_j\} = 0, \qquad \{q_i, p_j\} = \delta_{ij}.$$
Some authors use the opposite sign convention $\omega = \sum_i dq_i \wedge dp_i$; the notion of canonical coordinates is the same up to this convention.

Example: on $M = \R \times (0, \infty)$ with $\omega = dp \wedge dq$, put $Q = \log p$ and $P = -q p$.
Then $dP \wedge dQ = (-p \, dq - q \, dp) \wedge \frac{dp}{p} = -dq \wedge dp = dp \wedge dq$, so $(Q, P)$ are canonical coordinates.

Non-example: on $\R^2$ with $\omega = dp \wedge dq$, the chart $(Q, P) = (2q, p)$ gives $dP \wedge dQ = 2 \, dp \wedge dq \ne \omega$, so it is not canonical, although it is a valid chart.

Darboux's theorem states that every point of a symplectic manifold has a neighbourhood with canonical coordinates.
