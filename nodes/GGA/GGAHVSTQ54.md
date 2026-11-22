---
tag: GGAHVSTQ54
kind: proof
name: Proof that the trace of a linear map does not depend on the basis
msc: ["15A04", "15A15"]
topics: [S6559D61BP]
audience: ug1
proves: 0WCPH5Z7FA
uses: [0KZDNGA561, 0XC1RDBY7A, 0YQSGNYE3K, 0MKRHZB3WS, 0MQXVZEBMT, 0Y4NF1DRKD, 073E4XC016, 0EB9N0S33C]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a linear operator
---

## Proof

The [[trace of $T$|0KZDNGA561]] is defined as $\tr [T]_{B_0}$ for some basis $B_0$ of $V$, and we show that every basis gives the same number.

1. Let $B$ and $B'$ be two bases of $V$, and let $n = \dim V$.
   Let $M = [T]_B$ and $M' = [T]_{B'}$ be the [[matrices of $T$|0YQSGNYE3K]].
2. Let $P$ be the [[change of basis matrix|0MKRHZB3WS]] from $B$ to $B'$.
   It is [[invertible|0EB9N0S33C]], and the [[change of basis formula|0MQXVZEBMT]] gives $M' = P^{-1} M P$.
3. By [[associativity|073E4XC016]], $M' = P^{-1} (MP)$.
4. The [[cyclic property of the trace|0Y4NF1DRKD]], applied to the $n \times n$ matrices $P^{-1}$ and $MP$, gives
   $$\tr\bigl(P^{-1}(MP)\bigr) = \tr\bigl((MP)P^{-1}\bigr).$$
5. By associativity again, $(MP)P^{-1} = M(PP^{-1}) = M I_n = M$.
6. Steps 3 to 5 give $\tr M' = \tr M$ for the [[trace of a matrix|0XC1RDBY7A]].
   So $\tr [T]_{B'} = \tr [T]_B$ for any two bases $B$ and $B'$.
7. Taking $B' = B_0$, we get $\tr T = \tr [T]_{B_0} = \tr [T]_B$ for the given basis $B$.

## Idea

Changing the basis replaces the matrix $M$ by $P^{-1} M P$.
The trace of a product of two matrices does not depend on their order, so the factors $P^{-1}$ and $P$ meet and cancel inside the trace.
This makes the trace a property of the map and not of the chosen basis.

## Variants

One can use the [[theorem on similarity invariants|191HBJ7PVZ]] in place of steps 3 to 5, since $M$ and $M'$ are similar.
Without matrices, the trace can be defined as the evaluation map on $V^* \otimes V \cong \End(V)$, which needs no basis.
Then one checks that this map gives $\tr [T]_B$ in every basis $B$, and the statement follows at once.
