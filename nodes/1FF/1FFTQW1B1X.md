---
tag: 1FFTQW1B1X
kind: definition
name: Tutte polynomial
msc: [05C31, 05B35]
defines: C81RAXD6DV
uses: [PX31ZNYS3Z, SYRCTH853H, 4WCYBSH1P6, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Tutte_polynomial
---

## Definition

Let $M$ be a [[matroid|PX31ZNYS3Z]] on a finite ground set $E$ with [[rank function|SYRCTH853H]] $r$.
The *Tutte polynomial* of $M$ is
$$T_M(x, y) = \sum_{A \subseteq E} (x - 1)^{r(E) - r(A)} \, (y - 1)^{\abs{A} - r(A)}.$$
Let $G$ be a finite [[graph|00C0BR7D7H]], with loops and multiple edges allowed.
Its Tutte polynomial $T_G$ is the Tutte polynomial of its graphic matroid:
$$T_G(x, y) = \sum_{A \subseteq E(G)} (x - 1)^{k(A) - k(E)} \, (y - 1)^{k(A) + \abs{A} - \abs{V(G)}},$$
where $k(A)$ is the number of connected components of the graph $(V(G), A)$.

## Remarks

Let $e \in E$, and let $M \setminus e$ and $M / e$ be the [[deletion and contraction|4WCYBSH1P6]] of $e$.
If $e$ is neither a loop nor a coloop, then $T_M = T_{M \setminus e} + T_{M / e}$.
If $e$ is a coloop, then $T_M = x \, T_{M / e}$; if $e$ is a loop, then $T_M = y \, T_{M \setminus e}$.
For the dual matroid, $T_{M^*}(x, y) = T_M(y, x)$.
The value $T_M(1, 1)$ is the number of bases of $M$.
For a graph $G$, the [[chromatic polynomial|0B621RBVS9]] is $P_G(\lambda) = (-1)^{\abs{V(G)} - k(E)} \lambda^{k(E)} \, T_G(1 - \lambda, 0)$.

Example: for the triangle $K_3$, $\abs{V} = 3$ and $k(E) = 1$.
The empty set gives $(x-1)^2$, the $3$ single edges give $3(x-1)$, the $3$ pairs give $3$, and the full edge set gives $y - 1$.
The sum is $x^2 - 2x + 1 + 3x - 3 + 3 + y - 1 = x^2 + x + y$.
Then $T(1, 1) = 3$ spanning trees, and $(-1)^2 \lambda \, T(1 - \lambda, 0) = \lambda(\lambda - 1)(\lambda - 2)$ is the chromatic polynomial of $K_3$.

Non-example: the rank generating polynomial $\sum_{A} u^{r(E) - r(A)} v^{\abs{A} - r(A)}$ is not the Tutte polynomial itself; the Tutte polynomial is obtained from it by the substitution $u = x - 1$, $v = y - 1$.
