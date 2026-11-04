---
tag: BVFDYD1X1S
kind: proof
name: Proof that Lipschitz functions are uniformly continuous
msc: [26A16]
proves: 0K1EWAR6AF
uses: [0QNVQ4VD9T, 0Q4DR37DVE]
sources:
  - url: https://www.jirka.org/ra/html/sec_unifcont.html
    locator: Proposition 3.4.8
---

## Proof

1. Since $f$ is [[Lipschitz|0QNVQ4VD9T]], there is a real $K \ge 0$ with $\abs{f(x) - f(y)} \le K \abs{x - y}$ for all $x, y \in D$.
2. Let $\varepsilon > 0$. Put $\delta = \frac{\varepsilon}{K + 1}$. Then $\delta > 0$, since $K + 1 > 0$.
3. Let $x, y \in D$ with $\abs{x - y} < \delta$. By step 1, $\abs{f(x) - f(y)} \le K \abs{x - y} \le K \delta$.
4. Since $K < K + 1$ and $\delta > 0$, we have $K \delta < (K + 1) \delta = \varepsilon$. So $\abs{f(x) - f(y)} < \varepsilon$.
5. The number $\delta$ depends only on $\varepsilon$, not on $x$ or $y$. So $f$ is [[uniformly continuous|0Q4DR37DVE]].

## Idea

The Lipschitz bound controls the change of $f$ by a fixed multiple of the change of $x$. So one $\delta$, a fixed fraction of $\varepsilon$, works at every point. Using $K + 1$ instead of $K$ avoids division by zero when $K = 0$.
