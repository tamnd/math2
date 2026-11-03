---
tag: C9X1PYHXQ9
kind: definition
name: H-infinity norm of a system
msc: [93B36, 93C05, 30H10]
defines: QVREFP7BH7
uses: [86JKV3TRFD, 09VMDSRXWJ, PNNNFJVF6W, 0R3H5PANRQ, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy_space
---

## Definition

Let $G$ be a $p \times m$ matrix of functions that are analytic and bounded on the open right half-plane $\set{s \in \C : \operatorname{Re} s > 0}$.
The [[transfer function|86JKV3TRFD]] matrices of stable linear time-invariant systems are of this kind.
Write $\bar\sigma(M)$ for the largest [[singular value|09VMDSRXWJ]] of a complex matrix $M$.
The *H-infinity norm* of $G$ is
$$\norm{G}_\infty = \sup_{\operatorname{Re} s > 0} \bar\sigma\big(G(s)\big).$$
The set of all such $G$ with this norm is the [[Hardy space|PNNNFJVF6W]] $H^\infty$ of the right half-plane, with matrix values.

## Remarks

For $G$ real-rational, proper and with all poles in the open left half-plane, the maximum principle gives
$$\norm{G}_\infty = \sup_{\omega \in \R} \bar\sigma\big(G(i \omega)\big).$$
It is also the gain induced by the energy norm: $\norm{G}_\infty = \sup \set{\norm{y}_2 / \norm{u}_2 : u \in L^2([0, \infty); \R^m),\ u \ne 0}$.
Here $y$ is the output for the input $u$ and zero initial state, and $\norm{\cdot}_2$ is the norm of the [[L^2 space|SASP14MA1Z]].
Example: $G(s) = 1/(s + a)$ with $a > 0$ gives $\abs{G(i\omega)} = 1/\sqrt{\omega^2 + a^2}$, whose [[supremum|0R3H5PANRQ]] is $1/a$ at $\omega = 0$, so $\norm{G}_\infty = 1/a$.
Non-example: $G(s) = 1/(s - 1)$ is not in $H^\infty$, since it is unbounded near its pole $s = 1$ in the right half-plane, although $\abs{G(i\omega)} \le 1$ on the imaginary axis.
Likewise $G(s) = s$ is not bounded on the right half-plane, so an improper system has no finite H-infinity norm.
