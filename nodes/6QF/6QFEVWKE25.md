---
tag: 6QFEVWKE25
kind: definition
name: Veblen function
msc: ["03E10", "03F15"]
defines: JQFAE9S2F4
uses: [0RDJK7EQYY, PXTF18X433, 2C7MBG93AZ, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Veblen_function
---

## Definition

The functions $\varphi_\gamma$, for ordinals $\gamma$, map [[ordinals|0RDJK7EQYY]] to ordinals.
They are defined by [[transfinite recursion|0ZHQMQ2C1N]] on $\gamma$:

1. $\varphi_0(\alpha) = \omega^\alpha$, with ordinal exponentiation from [[ordinal arithmetic|2C7MBG93AZ]].
2. $\varphi_{\gamma + 1}$ lists in increasing order the fixed points of $\varphi_\gamma$, the ordinals $\alpha$ with $\varphi_\gamma(\alpha) = \alpha$.
3. For a nonzero limit ordinal $\gamma$, $\varphi_\gamma$ lists in increasing order the common fixed points of all $\varphi_\delta$ with $\delta < \gamma$.

The two-variable function $(\gamma, \alpha) \mapsto \varphi_\gamma(\alpha)$, also written $\varphi(\gamma, \alpha)$, is the Veblen function.

## Remarks

Each $\varphi_\gamma$ is a [[normal function|PXTF18X433]], and this makes clauses 2 and 3 meaningful, since the fixed points of normal functions form a closed unbounded class.
Example: $\varphi_1(\alpha) = \varepsilon_\alpha$, the $\alpha$-th epsilon number, so $\varphi_1(0) = \varepsilon_0$ is the least $\alpha$ with $\omega^\alpha = \alpha$.
Check: $\varphi_1$ lists the fixed points of $\varphi_0$, and these are by definition the epsilon numbers.
Non-example: the function $\alpha \mapsto \omega^\alpha + 1$ cannot start the hierarchy, since it is not normal and has no fixed points.
The least ordinal $\alpha$ with $\varphi_\alpha(0) = \alpha$ is the Feferman–Schütte ordinal $\Gamma_0$.
More generally, one may start from any normal function $f$ in place of $\alpha \mapsto \omega^\alpha$.
