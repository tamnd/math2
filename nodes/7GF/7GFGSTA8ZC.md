---
tag: 7GFGSTA8ZC
kind: proof
name: Proof that a bounded derivative on a convex set implies Lipschitz
msc: [26B35]
proves: 0TKG7T3K0E
uses: [02CYB184RC, 0K06X9QXDX, 0135XZZQ8M, 055VVSN00V]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Proposition 8.4.2
---

## Proof

We apply the mean value inequality to each pair of points of $C$.

1. Let $U$, $f$, $C$ and $M$ be as in the statement, and let $x, y \in C$.
2. For $0 \le t \le 1$, the point $x + t (y - x)$ equals $(1 - t) x + t y$.
3. Since $C$ is [[convex|0K06X9QXDX]], step 2 shows that the segment $[x, y] = \{x + t (y - x) : 0 \le t \le 1\}$ lies in $C$. As $C \subseteq U$, it lies in $U$.
4. By hypothesis, $\|Df(z)\| \le M$ for each $z \in C$, so in particular for each $z \in [x, y]$.
5. The map $f$ is [[differentiable|0135XZZQ8M]] on the open set $U$. By steps 3 and 4 and the [[mean value inequality|02CYB184RC]], $\|f(y) - f(x)\| \le M \, \|y - x\|$.
6. Since $x, y \in C$ were arbitrary, $f$ is [[Lipschitz on C|055VVSN00V]] with constant $M$.

## Idea

Convexity puts the whole segment between two points of $C$ inside $C$. On that segment the derivative is bounded by $M$, so the mean value inequality bounds the change of $f$ by $M$ times the distance.
