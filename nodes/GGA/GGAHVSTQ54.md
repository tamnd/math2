---
tag: GGAHVSTQ54
kind: proof
name: Proof that the trace of a linear map does not depend on the basis
msc: [15A04, 15A15]
proves: 0WCPH5Z7FA
uses: [0KZDNGA561, 0XC1RDBY7A, 0YQSGNYE3K, 0MKRHZB3WS, 0MQXVZEBMT, 0Y4NF1DRKD, 073E4XC016, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a linear operator
---

## Proof

The [[trace of $T$|0KZDNGA561]] is defined as $\tr [T]_{B_0}$ for some basis $B_0$ of $V$. We show that every basis gives the same number.

1. Let $B$ and $B'$ be two bases of $V$. Let $M = [T]_B$ and $M' = [T]_{B'}$ be the [[matrices of $T$|0YQSGNYE3K]], and let $n = \dim V$.
2. Let $P$ be the [[change of basis matrix|0MKRHZB3WS]] from $B$ to $B'$. By the [[change of basis formula|0MQXVZEBMT]], $P$ is [[invertible|0EB9N0S33C]] and $M' = P^{-1} M P$.
3. By [[associativity|073E4XC016]], $M' = P^{-1} (MP)$.
4. By the [[symmetry of the trace of a product|0Y4NF1DRKD]], applied to the $n \times n$ matrices $P^{-1}$ and $MP$, we get $\tr\left(P^{-1}(MP)\right) = \tr\left((MP)P^{-1}\right)$.
5. By associativity again, $(MP)P^{-1} = M(PP^{-1}) = M I_n = M$.
6. By steps 3 to 5, $\tr M' = \tr M$, with the [[trace of a matrix|0XC1RDBY7A]]. So $\tr [T]_{B'} = \tr [T]_B$ for any two bases $B$ and $B'$.
7. In particular, taking $B' = B_0$, we get $\tr T = \tr [T]_{B_0} = \tr [T]_B$ for the given basis $B$.

## Idea

Changing the basis replaces the matrix $M$ by $P^{-1} M P$. The trace does not see the order of the factors in a product, so the factors $P^{-1}$ and $P$ cancel inside the trace. This makes the trace a property of the map and not of the chosen basis.
