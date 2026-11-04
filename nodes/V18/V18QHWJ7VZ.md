---
tag: V18QHWJ7VZ
kind: proof
name: Proof of the characterization of the floor
msc: [26A09]
proves: 0R9B0B5458
uses: [0YVRNEDSVG, 0C4JS9RF5M, 0QSPNASE50]
sources:
  - url: https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
    locator: Equivalences
---

## Proof

1. Let $x$ be a real number. By definition, the [[floor|0YVRNEDSVG]] $\floor{x}$ is the greatest [[integer|0C4JS9RF5M]] $k$ with $k \le x$.
2. Let $n = \floor{x}$. Then $n \le x$.
3. The integer $n + 1$ is larger than $n$. Since $n$ is the greatest integer at most $x$, $n + 1 \le x$ fails. The order of $\R$ is [[total|0QSPNASE50]], so $x < n + 1$.
4. Conversely, let $n$ be an integer with $n \le x < n + 1$.
5. Let $m$ be an integer with $m \le x$. Then $m \le x < n + 1$, so $m - n < 1$.
6. The number $m - n$ is an integer less than $1$, so $m - n \le 0$. Thus $m \le n$.
7. By steps 4 and 6, $n$ is an integer at most $x$ and is at least every such integer. So $n$ is the greatest one, that is, $n = \floor{x}$.
8. Steps 2, 3 and 4 to 7 prove the equivalence. Taking $n = \floor{x}$ in steps 2 and 3 gives $\floor{x} \le x < \floor{x} + 1$.

## Idea

The integer $n + 1$ is the next integer after $n$. So $n$ is the greatest integer below $x$ exactly when $n$ is at most $x$ and $n + 1$ is not.
