---
tag: G1ST9Y1DEP
kind: proof
name: Proof of the recurrence for derangements by the image of the last point
msc: [05A05]
proves: 0QRRYXG7V7
uses: [0TH61JR04G, 0BQMWCNS8S, 0EE2V3CHFK, 0GV2573FP4]
sources:
  - url: https://en.wikipedia.org/wiki/Derangement
    locator: Counting derangements
---

## Proof

We sort the derangements by the image of the last point and count each class by a bijection.

1. Conjugating by a bijection between two sets with $m$ elements matches their [[derangements|0TH61JR04G]]. So by the [[bijection principle|0GV2573FP4]], $D_m$ depends only on $m$.
2. Let $n$ be a natural number, let $X = \set{1, \dots, n + 2}$, let $z = n + 2$, and let $Y = X \setminus \set{z}$. So $|Y| = n + 1$.
3. Let $\sigma$ be a derangement of $X$. Then $\sigma(z) \ne z$, so $\sigma(z) \in Y$.
4. Fix $i \in Y$. Let $E_i$ be the set of derangements $\sigma$ of $X$ with $\sigma(z) = i$. Split $E_i$ into $E_i'$, where $\sigma(i) = z$, and $E_i''$, where $\sigma(i) \ne z$.
5. Count $E_i'$. Let $Z = X \setminus \set{i, z}$, a set with $n$ elements. For $\sigma \in E_i'$, $\sigma$ maps $\set{i, z}$ onto itself, so its restriction to $Z$ is a [[permutation|0BQMWCNS8S]] of $Z$.
6. This restriction has no fixed point, since $\sigma$ has none. Conversely, a derangement of $Z$ extended by $i \mapsto z$ and $z \mapsto i$ lies in $E_i'$.
7. These two maps are inverse to each other. So $|E_i'| = D_n$.
8. Count $E_i''$. For $\sigma \in E_i''$, let $j = \sigma^{-1}(z)$. Then $j \ne z$ because $\sigma(z) = i \ne z$, and $j \ne i$ because $\sigma(i) \ne z$.
9. Define $\tau : Y \to Y$ by $\tau(j) = i$ and $\tau(x) = \sigma(x)$ for $x \in Y \setminus \set{j}$. These values lie in $Y$, since only $j$ is sent to $z$ by $\sigma$.
10. The map $\tau$ is a bijection of $Y$. Indeed, $\sigma$ maps $Y \setminus \set{j}$ onto $X \setminus \set{z, i}$, since $\sigma(j) = z$ and $\sigma(z) = i$. Adding $\tau(j) = i$ gives all of $Y$.
11. The map $\tau$ has no fixed point. For $x \ne j$, $\tau(x) = \sigma(x) \ne x$. Also $\tau(j) = i \ne j$ by step 8.
12. Conversely, let $\tau$ be a derangement of $Y$, and let $j = \tau^{-1}(i)$. Define $\sigma$ on $X$ by $\sigma(z) = i$, $\sigma(j) = z$, and $\sigma(x) = \tau(x)$ for the other $x$.
13. This $\sigma$ is a permutation of $X$, because $\tau$ maps $Y \setminus \set{j}$ onto $Y \setminus \set{i}$, and $\sigma$ adds $j \mapsto z$ and $z \mapsto i$. It has no fixed point: $\sigma(z) = i \ne z$, $\sigma(j) = z \ne j$, and $\sigma(x) = \tau(x) \ne x$ otherwise.
14. Moreover $\sigma(i) \ne z$. Otherwise $i = j$, so $\tau(i) = i$, which is false for a derangement. Thus $\sigma \in E_i''$.
15. The constructions of steps 9 and 12 are inverse to each other. Starting from $\sigma$, we get $\tau(j) = i$, so step 12 recovers the same $j$ and then $\sigma$. Starting from $\tau$, we get $\sigma^{-1}(z) = j$, so step 9 recovers $\tau$. Hence $|E_i''| = D_{n+1}$.
16. By the [[rule of sum|0EE2V3CHFK]], $|E_i| = |E_i'| + |E_i''| = D_n + D_{n+1}$.
17. By step 3, the derangements of $X$ are the disjoint union of the sets $E_i$ for the $n + 1$ elements $i \in Y$.
18. By the rule of sum, $D_{n+2} = (n + 1)(D_{n+1} + D_n)$.

## Idea

Look at where the last point $z$ goes, say to $i$. If $\sigma$ also sends $i$ back to $z$, removing the swap leaves a derangement of $n$ points. Otherwise, short-circuiting $z$ out of $\sigma$ leaves a derangement of $n + 1$ points.
