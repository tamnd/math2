---
tag: BR6KJEJD1C
kind: definition
name: Hölder space
msc: ["46E15", 35B65]
defines: P101AX1ZSC
uses: [012PBA0FMD, 09EGC6F8PT, 06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/H%C3%B6lder_condition
---

## Definition

Let $U \subseteq \R^n$ be open, let $k \ge 0$ be an integer, and let $0 < \alpha \le 1$.
For a function $v \colon U \to \R$, its Hölder seminorm of exponent $\alpha$ is
$$[v]_{\alpha, U} = \sup_{x, y \in U, \; x \ne y} \frac{\abs{v(x) - v(y)}}{\abs{x - y}^{\alpha}}.$$
The *Hölder space* $C^{k,\alpha}(\overline{U})$ is the set of functions $u \colon U \to \R$ such that:

1. $u$ is $k$ times continuously differentiable on $U$;
2. every [[partial derivative|09EGC6F8PT]] $\partial^\beta u$ with $\abs{\beta} \le k$ is bounded on $U$;
3. every partial derivative $\partial^\beta u$ with $\abs{\beta} = k$ satisfies $[\partial^\beta u]_{\alpha, U} < \infty$.

Its norm is
$$\norm{u}_{C^{k,\alpha}(\overline{U})} = \sum_{\abs{\beta} \le k} \sup_{U} \abs{\partial^\beta u} + \sum_{\abs{\beta} = k} [\partial^\beta u]_{\alpha, U}.$$

## Remarks

With this norm, $C^{k,\alpha}(\overline{U})$ is a [[Banach space|06GZ956657]].
Condition 3 says that the derivatives of order $k$ are [[Hölder continuous|012PBA0FMD]] with exponent $\alpha$ on $U$, so they extend continuously to the closure $\overline{U}$.
The space $C^{0,1}(\overline{U})$ is the space of bounded Lipschitz functions.
On a bounded set $U$, $C^{k,\beta}(\overline{U}) \subseteq C^{k,\alpha}(\overline{U})$ for $0 < \alpha < \beta \le 1$.
The local space $C^{k,\alpha}(U)$ is the set of $u$ with $u \in C^{k,\alpha}(\overline{V})$ for every open $V$ with compact closure in $U$.

Example: $u(x) = \sqrt{\abs{x}}$ lies in $C^{0,1/2}([-1, 1])$.
It is continuous and bounded by $1$, and $\abs{\sqrt{\abs{x}} - \sqrt{\abs{y}}} \le \sqrt{\abs{\abs{x} - \abs{y}}} \le \abs{x - y}^{1/2}$.

Non-example: the same $u$ is not in $C^{0,1}([-1, 1])$, so it fails condition 3 for $\alpha = 1$.
Indeed $\abs{u(x) - u(0)} / \abs{x - 0} = \abs{x}^{-1/2}$ is unbounded as $x \to 0$.
