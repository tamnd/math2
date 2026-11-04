---
tag: BVDCFVVCJ8
kind: proof
name: Proof that the integers are countable
msc: ["03E10"]
proves: 066RJJVWH9
uses: [0SEZ3JGZP7, 0SNQEF7Z53, 0PVG1CRAJN, 0XKH881BZ7, 0CHQKZFK5S]
sources:
  - url: https://en.wikipedia.org/wiki/Countable_set
    locator: Introduction
---

## Proof

We check that the given map is injective and surjective.

1. Each $n \in \N$ is either $2k$ or $2k + 1$ for exactly one $k \in \N$, by the [[division algorithm|0CHQKZFK5S]] with divisor $2$. So $f(2k) = k$ and $f(2k+1) = -(k+1)$ define a function $f \colon \N \to \Z$.
2. For even $n = 2k$, $f(n) = k \ge 0$. For odd $n = 2k + 1$, $f(n) = -(k + 1) \le -1$.
3. The map $f$ is [[injective|0PVG1CRAJN]]. Let $f(n) = f(n')$. By step 2, $n$ and $n'$ are both even or both odd.
4. If $n = 2k$ and $n' = 2k'$, then $k = k'$, so $n = n'$. If $n = 2k + 1$ and $n' = 2k' + 1$, then $-(k+1) = -(k'+1)$, so $k = k'$ and $n = n'$.
5. The map $f$ is [[surjective|0XKH881BZ7]]. Let $m \in \Z$. If $m \ge 0$, then $f(2m) = m$.
6. If $m < 0$, put $k = -m - 1$. Then $k \in \N$, and $f(2k + 1) = -(k + 1) = m$.
7. So $f$ is a [[bijection|0SNQEF7Z53]] from $\N$ to $\Z$, and $\Z$ is [[countably infinite|0SEZ3JGZP7]].

## Idea

List the integers as $0, -1, 1, -2, 2, \dots$. The even positions hold the nonnegative integers and the odd positions hold the negative ones. Each integer appears exactly once in this list.
