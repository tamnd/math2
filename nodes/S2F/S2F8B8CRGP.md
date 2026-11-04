---
tag: S2F8B8CRGP
kind: proof
name: Proof that limits are unique in Hausdorff spaces
msc: [54D10]
proves: 0D8T984XEE
uses: [0MXB4CKHFW, 09CJ00H3NW]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_space
    locator: Equivalences
---

## Proof

We argue by contradiction.

1. Suppose $(x_n)$ converges to $x$ and to $y$, and $x \neq y$.
2. Since $X$ is [[Hausdorff|0MXB4CKHFW]], there are open sets $U$ and $V$ with $x \in U$, $y \in V$ and $U \cap V = \varnothing$.
3. The open set $U$ satisfies $x \in U \subseteq U$, so $U$ is a [[neighbourhood|09CJ00H3NW]] of $x$. In the same way, $V$ is a neighbourhood of $y$.
4. By convergence to $x$, there is $n_0$ with $x_n \in U$ for all $n \ge n_0$. By convergence to $y$, there is $n_1$ with $x_n \in V$ for all $n \ge n_1$.
5. Let $n = \max(n_0, n_1)$. Then $x_n \in U \cap V$, which contradicts $U \cap V = \varnothing$.
6. Hence $x = y$.

## Idea

Two different limits could be separated by disjoint open sets. A convergent sequence eventually stays in each of them, so from some index on it would lie in both at once, which is impossible.
