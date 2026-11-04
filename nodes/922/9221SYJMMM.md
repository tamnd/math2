---
tag: 9221SYJMMM
kind: proof
name: Proof that a linear map between normed spaces is continuous if and only if it is bounded
msc: [47B01]
proves: 0F3K4C7XYW
uses: [0S3SMRH0Z5, 0TMZ21WKCN, 0YF82GBTND, 0B2305GNAZ, 0A26X79RTB]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_operator
    locator: Equivalence of boundedness and continuity
---

## Proof

We prove both directions. The metrics are $\|x - y\|_V$ and $\|x - y\|_W$.

1. Suppose $T$ is bounded, with $\|Tx\|_W \le C \|x\|_V$ for all $x$. By linearity, $\|Tx - Ty\|_W = \|T(x - y)\|_W \le C \|x - y\|_V$. So $T$ is [[Lipschitz|0TMZ21WKCN]] with constant $C$.
2. Let $a \in V$ and $\varepsilon > 0$, and let $\delta = \varepsilon / (C + 1)$. If $\|x - a\|_V < \delta$, then $\|Tx - Ta\|_W \le C \delta < \varepsilon$.
3. By [[continuity via open sets|0YF82GBTND]], $T$ is continuous. So $T$ is a [[continuous linear map|0S3SMRH0Z5]].
4. Conversely, suppose $T$ is continuous. The open ball $B = \{w \in W : \|w\|_W < 1\}$ is [[open|0B2305GNAZ]], so $T^{-1}(B)$ is open in $V$.
5. Since $T0 = 0 \in B$, we have $0 \in T^{-1}(B)$. By [[the ball criterion|0A26X79RTB]], there is $\eta > 0$ with $\|Tx\|_W < 1$ whenever $\|x\|_V < \eta$.
6. Let $\delta = \eta / 2$, and let $x \in V$ with $x \neq 0$. Put $y = \delta x / \|x\|_V$. Then $\|y\|_V = \delta < \eta$, so $\|Ty\|_W < 1$.
7. By linearity, $Ty = (\delta / \|x\|_V) \, Tx$. So $\|Tx\|_W = (\|x\|_V / \delta) \|Ty\|_W < \|x\|_V / \delta$.
8. For $x = 0$, $Tx = 0$. So $\|Tx\|_W \le C \|x\|_V$ for all $x \in V$, with $C = 1 / \delta$, and $T$ is bounded.

## Idea

A bound $\|Tx\| \le C \|x\|$ makes $T$ Lipschitz, hence continuous. Conversely, continuity at $0$ gives a small ball that $T$ maps into the unit ball. Linearity lets us rescale any vector into that small ball, which yields the bound.
