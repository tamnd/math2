---
tag: A79PHYDXMW
kind: definition
name: Modulus of continuity
msc: [26A16, 26A15]
defines: AXCJBSQZWF
uses: [0XHDTE5YMZ, 0BTMQ04556, 0GSZ7B0CGR, 0Q4DR37DVE, 0QNVQ4VD9T, 0WZTM0EFR6]
sources:
  - url: https://en.wikipedia.org/wiki/Modulus_of_continuity
    locator: Formal definition
---

## Definition

Let $D \subseteq \R$ and let $f \colon D \to \R$ be a [[function|0XHDTE5YMZ]].
A *modulus of continuity* is a function $\omega \colon [0, \infty) \to [0, \infty]$ that is nondecreasing, satisfies $\omega(0) = 0$, and satisfies $\omega(\delta) \to 0$ as $\delta \to 0^+$.
The function $\omega$ is a modulus of continuity *for* $f$ if
$$\abs{f(x) - f(y)} \le \omega(\abs{x - y}) \quad \text{for all } x, y \in D.$$
The *optimal modulus of continuity* of $f$ is the function $\omega_f \colon [0, \infty) \to [0, \infty]$ given by
$$\omega_f(\delta) = \sup \set{\abs{f(x) - f(y)} : x, y \in D, \ \abs{x - y} \le \delta},$$
where the [[supremum|0BTMQ04556]] is taken in the [[extended real line|0GSZ7B0CGR]].

## Remarks

The function $f$ has a modulus of continuity if and only if $f$ is [[uniformly continuous|0Q4DR37DVE]], and then $\omega_f$ is the smallest one.
The same definitions work for a map between metric spaces, with distances in place of $\abs{x - y}$ and $\abs{f(x) - f(y)}$.

Example: let $f(x) = \sqrt x$ on $D = [0, \infty)$.
For $0 \le y \le x$, one has $\sqrt x - \sqrt y \le \sqrt{x - y}$, since squaring gives $x - 2\sqrt{xy} + y \le x - y$, that is $y \le \sqrt{xy}$.
Equality holds for $y = 0$, so $\omega_f(\delta) = \sqrt \delta$, and this tends to $0$.

Non-example: let $f(x) = x^2$ on $\R$.
For $\delta > 0$, one has $f(x + \delta) - f(x) = 2x\delta + \delta^2$, which is unbounded in $x$.
So $\omega_f(\delta) = \infty$ for each $\delta > 0$, and $\omega_f$ does not tend to $0$.

The modulus $\omega(\delta) = L\delta$ gives the [[Lipschitz condition|0QNVQ4VD9T]] with constant $L$.
The modulus $\omega(\delta) = C\delta^\alpha$ with $0 < \alpha \le 1$ gives the [[Hölder condition|0WZTM0EFR6]] of exponent $\alpha$.
