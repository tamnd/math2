---
tag: J39DGKG9A7
kind: definition
name: Lipschitz class
msc: [41A25, 26A16]
defines: EHBQ295J3Q
uses: [0QNVQ4VD9T, 012PBA0FMD, AXCJBSQZWF]
sources:
  - url: https://en.wikipedia.org/wiki/Lipschitz_continuity
---

## Definition

Let $I \subseteq \R$ be an interval, let $0 < \alpha \le 1$, and let $M > 0$.
The class $\mathrm{Lip}_M \alpha$ on $I$ is the set of functions $f \colon I \to \R$ such that
$$\abs{f(x) - f(y)} \le M \abs{x - y}^\alpha \quad \text{for all } x, y \in I.$$
The *Lipschitz class* $\mathrm{Lip}\,\alpha$ on $I$ is the union of the classes $\mathrm{Lip}_M \alpha$ over all $M > 0$.

## Remarks

Example: $f(x) = \sqrt{x}$ on $[0, 1]$ lies in $\mathrm{Lip}_1 \tfrac12$.
For $0 \le y \le x$ one has $\sqrt{x} - \sqrt{y} \le \sqrt{x - y}$, since squaring gives $x + y - 2\sqrt{xy} \le x - y$, that is $y \le \sqrt{xy}$.

Non-example: the same $f$ is not in $\mathrm{Lip}\,1$, because $\abs{f(x) - f(0)} / \abs{x - 0} = x^{-1/2}$ is unbounded as $x \to 0$.

In terms of the [[modulus of continuity|AXCJBSQZWF]] $\omega(f, \delta)$, the condition $f \in \mathrm{Lip}_M \alpha$ says $\omega(f, \delta) \le M \delta^\alpha$ for all $\delta > 0$.
$\mathrm{Lip}\,1$ is the class of [[Lipschitz continuous|0QNVQ4VD9T]] functions, and $\mathrm{Lip}\,\alpha$ for $\alpha < 1$ is the class of [[Hölder continuous|012PBA0FMD]] functions of exponent $\alpha$.
The restriction $\alpha \le 1$ is natural: for $\alpha > 1$ the condition forces $f' = 0$, so only constant functions remain.
