---
tag: JH11GE8MBY
kind: definition
name: Double-couple source
msc: [86A15, 74J05]
defines: S5TXH6MZ05
uses: [ZNN5WAT301, 88YRH7XQDX, 0BQAA2BK3Q, 9636MFFSGC]
sources:
  - url: https://en.wikipedia.org/wiki/Focal_mechanism
---

## Definition

Let $M_0 > 0$ and let $n, d \in \R^3$ be orthogonal unit vectors.
A point seismic source is a *double-couple source* if its [[moment tensor|ZNN5WAT301]] has the form
$$M = M_0\,(n d^T + d n^T).$$
Then $M_0$ is its [[seismic moment|88YRH7XQDX]].
Equivalently, $M$ is a real symmetric matrix with [[eigenvalues|0BQAA2BK3Q]] $M_0$, $0$, $-M_0$.

## Remarks

The two couples are a couple of forces along $d$ separated along $n$ and a couple along $n$ separated along $d$; their [[torques|9636MFFSGC]] cancel.
Example: $M(n + d) = M_0(n + d)$ and $M(n - d) = -M_0 (n - d)$, since $d \cdot n = 0$ and $\abs{n} = \abs{d} = 1$; also $M(n \times d) = 0$.
So the tension axis is $T = (n + d)/\sqrt2$, the pressure axis is $P = (n - d)/\sqrt2$, and the null axis is $n \times d$.
Conversely, a symmetric matrix with eigenvalues $M_0, 0, -M_0$ and unit eigenvectors $T, B, P$ equals $M_0(n d^T + d n^T)$ with $n = (T + P)/\sqrt2$ and $d = (T - P)/\sqrt2$.
Non-example: $M = M_0\,\mathrm{diag}(2, -1, -1)$, a compensated linear vector dipole, has trace zero like a double couple, but its eigenvalues are not of the form $M_0, 0, -M_0$, so it is not a double couple.
The roles of $n$ and $d$ can be exchanged, which is the fault-plane ambiguity of the focal mechanism.
