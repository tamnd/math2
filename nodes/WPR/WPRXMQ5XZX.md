---
tag: WPRXMQ5XZX
kind: proof
name: Proof that Lipschitz maps are uniformly continuous
msc: [26A16]
proves: 07DCKDXRBP
uses: [063W5JMY85, 0TMZ21WKCN, 0FHSDCQACY]
sources:
  - url: https://en.wikipedia.org/wiki/Lipschitz_continuity
    locator: Properties
---

## Proof

We give an explicit $\delta$ for each $\varepsilon$.

1. Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]]. Let $f \colon X \to Y$ be [[Lipschitz|0TMZ21WKCN]] with a constant $K \ge 0$.
2. So $d_Y(f(x), f(y)) \le K \, d_X(x, y)$ for all $x, y \in X$.
3. Let $\varepsilon > 0$ be real, and put $\delta = \varepsilon / (K + 1)$. Then $\delta > 0$, because $K + 1 \ge 1$.
4. Let $x, y \in X$ with $d_X(x, y) < \delta$.
5. By step 2 and $K \ge 0$, we get $d_Y(f(x), f(y)) \le K \, d_X(x, y) \le K \delta = \varepsilon K / (K + 1)$.
6. Since $K / (K + 1) < 1$ and $\varepsilon > 0$, we get $\varepsilon K / (K + 1) < \varepsilon$. So $d_Y(f(x), f(y)) < \varepsilon$.
7. The number $\delta$ depends only on $\varepsilon$ and $K$, not on $x$ or $y$.
8. So condition 1 of [[uniform continuity|0FHSDCQACY]] holds, and $f$ is uniformly continuous.

## Idea

The Lipschitz inequality turns a bound on the input distance into a bound on the output distance, with the same factor everywhere.
Dividing $\varepsilon$ by $K + 1$ instead of $K$ avoids a special case when $K = 0$.
