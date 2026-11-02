---
tag: EFFC7688KR
kind: counterexample
name: Lebesgue spine
msc: [31B25, 31B20]
uses: [B7948M365K, STMT1K1865, 4YZVFGJVSZ, 0YE5868HZB]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_spine
same_as:
  wikidata: Q6511322
  wikipedia: Lebesgue spine
---

## Counterexample

In $\R^3$, write points as $x = (x_1, x_2, x_3)$ and consider the closed thin spike
$$K = \set{x \in \R^3 : 0 < x_1 \le 1, \; x_2^2 + x_3^2 \le e^{-2/x_1}} \cup \set{0}.$$
Its cross-section at distance $x_1$ from the origin is a disc of radius $e^{-1/x_1}$.
Let $\Omega = B \setminus K$, where $B$ is the [[open ball|0YE5868HZB]] of radius $2$ centred at $0$.
The origin $0$ is a boundary point of $\Omega$, the tip of the spike, and it is not a [[regular boundary point|B7948M365K]].
Check with [[Wiener's criterion|STMT1K1865]], using the part $E_k$ of the complement in the shell $2^{-k-1} \le \abs{x} \le 2^{-k}$.
For large $k$, $E_k$ lies in a thin cylinder of length about $2^{-k-1}$ and radius at most $e^{-2^k}$.
A cylinder of length $\ell$ and radius $r \le \ell/2$ has Newtonian [[capacity|4YZVFGJVSZ]] at most a constant times $\ell / \log(\ell / r)$.
So $\operatorname{cap}(E_k)$ is at most a constant times $2^{-k} / 2^k = 4^{-k}$, and $\sum_k 2^k \operatorname{cap}(E_k)$ converges.
Hence $0$ is irregular.

## Remarks

The example is due to Lebesgue.
The spike is connected and has interior points, so a boundary point can be irregular even when the complement of $\Omega$ near it is a connected set of positive volume.
Suppose the spike is less sharp, for example with radius $x_1^m$ for some $m > 1$.
Then $E_k$ contains a cylinder whose capacity is at least a constant times $2^{-k}/k$.
The terms of Wiener's series are then at least a constant times $1/k$, the series diverges, and the tip is regular.
In the plane no such example exists: a boundary point that lies in a connected component of the complement with more than one point is always regular.

## Explanations

### L1 human

Push a very sharp needle into a ball from the inside, so that the needle tip is a point of the boundary.
If the needle gets thin fast enough near its tip, the solution of the Dirichlet problem does not feel the tip.
Then a prescribed boundary value at the tip can be ignored by the solution.
