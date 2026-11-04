---
tag: J27P3HT2BH
kind: proof
name: Proof that a zero derivative on a connected open set implies constant
msc: [26B05]
proves: 0BYZTFM0DJ
uses: [02CYB184RC, 0135XZZQ8M, 0R37DFJKFW, 0D939CMME7, 01ZQQDCERP, 0DC3MPR7C9]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Corollary 8.4.4
---

## Proof

We show that $f$ is constant near each point, and then use connectedness.

1. Let $U$ and $f$ be as in the statement. If $U$ is empty, there is nothing to prove. So fix $a \in U$, and put $c = f(a)$.
2. Let $z \in U$. Since $U$ is [[open|01ZQQDCERP]], there is $\rho > 0$ such that the [[open ball|0DC3MPR7C9]] $B(z, \rho)$ lies in $U$.
3. Let $y \in B(z, \rho)$ and $0 \le t \le 1$. Then $\|z + t (y - z) - z\| = t \|y - z\| < \rho$. So the segment from $z$ to $y$ lies in $B(z, \rho) \subseteq U$.
4. On this segment $Df = 0$, so $\|Df\| \le 0$ there. The map $f$ is [[differentiable|0135XZZQ8M]] on $U$. By the [[mean value inequality|02CYB184RC]] with $M = 0$, $\|f(y) - f(z)\| \le 0$. So $f(y) = f(z)$.
5. Thus $f$ is constant on the ball $B(z, \rho)$, for each $z \in U$ and its $\rho$ from step 2.
6. Put $S = \{x \in U : f(x) = c\}$ and $T = U \setminus S$. Then $S \cap T = \varnothing$, $S \cup T = U$, and $a \in S$.
7. The set $S$ is open. If $z \in S$, then by step 5 each $y \in B(z, \rho)$ has $f(y) = f(z) = c$. So $B(z, \rho) \subseteq S$.
8. The set $T$ is open. If $z \in T$, then by step 5 each $y \in B(z, \rho)$ has $f(y) = f(z) \ne c$. So $B(z, \rho) \subseteq T$.
9. The sets $S$ and $T$ are open in $\mathbb{R}^n$ and lie in $U$, so they are open in $U$ with the subspace topology.
10. The set $U$ is [[connected|0R37DFJKFW]], so $U$ is not the union of two disjoint nonempty open subsets. This is the definition of a [[connected space|0D939CMME7]]. Since $S \ne \varnothing$ by step 6, steps 6 to 9 force $T = \varnothing$.
11. So $S = U$, that is, $f(x) = c$ for each $x \in U$. Hence $f$ is constant on $U$.

## Idea

A zero derivative makes $f$ constant on each small ball, by the mean value inequality. So the set where $f$ takes the value $f(a)$ and the set where it does not are both open. A connected set cannot be split into two disjoint nonempty open pieces, so the second set is empty.
