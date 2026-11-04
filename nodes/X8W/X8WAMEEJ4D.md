---
tag: X8WAMEEJ4D
kind: proof
name: Proof of Dirac's theorem on Hamiltonian cycles from Ore's theorem
msc: [05C45]
proves: 0TC99BRSSB
uses: [0JD5C82QMB, 0T0F6CCS9W, 090WPKFABX, 0NACHJYPKW]
sources:
  - url: https://en.wikipedia.org/wiki/Ore's_theorem
    locator: Related results
---

## Proof

We deduce the theorem from Ore's theorem.

1. Let $G$ be a finite simple [[graph|0JD5C82QMB]] with $n \ge 3$ vertices, and suppose that $\deg(w) \ge n/2$ for every vertex $w$, where $\deg$ is the [[degree|0T0F6CCS9W]].
2. Let $u$ and $v$ be two distinct vertices of $G$ that are not adjacent.
3. By Step 1, $\deg(u) + \deg(v) \ge n/2 + n/2 = n$.
4. So $G$ satisfies the hypothesis of [[Ore's theorem|0NACHJYPKW]]: it has $n \ge 3$ vertices, and every pair of distinct nonadjacent vertices has degree sum at least $n$.
5. By Ore's theorem, $G$ is [[Hamiltonian|090WPKFABX]].

## Idea

Dirac's condition bounds each degree from below by $n/2$. Adding two such bounds gives Ore's condition on pairs of nonadjacent vertices. So Dirac's theorem is the special case of Ore's theorem where every vertex is "rich" on its own.
