---
tag: CPC8ZMF1SD
kind: definition
name: Bedford–Taylor theory
msc: [32W20, 32U40]
defines: EEHQSWFHSB
uses: [FF2P7ER3QT, MXRC891TQS, BYJHP6A906, 360H7MD9RD]
sources:
  - url: https://en.wikipedia.org/wiki/Plurisubharmonic_function
---

## Definition

Let $\Omega \subseteq \C^n$ be open, and let $d^c = i(\bar\partial - \partial)$.
Let $u$ be a locally bounded [[plurisubharmonic function|FF2P7ER3QT]] on $\Omega$, and let $T$ be a closed [[positive current|BYJHP6A906]] of bidegree $(p, p)$ on $\Omega$, with $p \le n - 1$.
The coefficients of $T$ are measures and $u$ is locally bounded and Borel, so $uT$ is a well defined [[current|360H7MD9RD]].
The *Bedford–Taylor product* is the current
$$dd^c u \wedge T = dd^c (u T),$$
where $dd^c$ is taken in the sense of currents.
For locally bounded plurisubharmonic functions $u_1, \dots, u_k$ on $\Omega$, with $k \le n$, the product is defined by induction:
$$dd^c u_1 \wedge dd^c u_2 \wedge \cdots \wedge dd^c u_k = dd^c \left( u_1 \, dd^c u_2 \wedge \cdots \wedge dd^c u_k \right).$$
In particular $(dd^c u)^n$ is the *Monge–Ampère measure* of $u$.

## Remarks

The main facts of the theory are these.
The product $dd^c u \wedge T$ is again a closed positive current, which makes the induction possible.
When the $u_j$ are of class $C^2$ the product agrees with the wedge product of smooth forms, so $(dd^c u)^n$ agrees with the [[complex Monge–Ampère operator|MXRC891TQS]].
If $u_j^{(m)}$ decreases to $u_j$ as $m \to \infty$, for each $j$, then the products of the $u_j^{(m)}$ converge weakly to the product of the $u_j$.
The product is symmetric in $u_1, \dots, u_k$.
Example: for $n = 1$ and $T = 1$, $dd^c u = \Delta u$ is the Riesz measure of the subharmonic function $u$, which is defined for every subharmonic $u$.
Non-example: the definition does not apply to $u = \log\abs{z_1}$ on $\C^2$, which is not locally bounded.
For unbounded plurisubharmonic functions in general, $(dd^c u)^n$ cannot be defined as a measure with good continuity properties.
