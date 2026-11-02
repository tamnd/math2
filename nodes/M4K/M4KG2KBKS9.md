---
tag: M4KG2KBKS9
kind: definition
name: Lamé function
msc: ["33E10", 34B30]
defines: KTP37HF2RZ
uses: [FF9ZPCZ59K, 0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Lam%C3%A9_function
---

## Definition

Let $k \in (0, 1)$, and let $\operatorname{sn}(z, k)$, $\operatorname{cn}(z, k)$ and $\operatorname{dn}(z, k)$ be the Jacobi [[elliptic functions|FF9ZPCZ59K]] of modulus $k$.
Let $\nu$ and $h$ be complex numbers.
*Lamé's equation* is the [[linear differential equation|0QQRP17Z7S]]
$$\frac{d^2 w}{dz^2} + \left( h - \nu(\nu + 1) k^2 \operatorname{sn}^2(z, k) \right) w = 0.$$
A *Lamé function* is a solution $w$ of Lamé's equation.
Let $\nu = n$ be a nonnegative integer.
A *Lamé polynomial* of degree $n$ is a nonzero solution of the form $\operatorname{sn}^{e_1} z\, \operatorname{cn}^{e_2} z\, \operatorname{dn}^{e_3} z \cdot P(\operatorname{sn}^2 z)$.
Here $e_1, e_2, e_3 \in \set{0, 1}$ and $P$ is a polynomial.

## Remarks

Example: for $\nu = 1$ and $h = 1 + k^2$, the function $w = \operatorname{sn} z$ is a Lamé polynomial.
Check: from $\operatorname{sn}' = \operatorname{cn} \operatorname{dn}$, $\operatorname{cn}^2 = 1 - \operatorname{sn}^2$ and $\operatorname{dn}^2 = 1 - k^2 \operatorname{sn}^2$, one gets $\operatorname{sn}'' = -(1 + k^2) \operatorname{sn} + 2k^2 \operatorname{sn}^3$, so $w'' + (1 + k^2 - 2k^2 \operatorname{sn}^2) w = 0$.
In the same way $\operatorname{cn} z$ is a solution for $h = 1$ and $\operatorname{dn} z$ for $h = k^2$.
Non-example: for $\nu = 1$ and $h = 0$, the function $\operatorname{sn} z$ is not a solution, since the left side equals $-(1 + k^2) \operatorname{sn} z$, which is not identically $0$.
For each nonnegative integer $n$ there are exactly $2n + 1$ values of $h$ that admit a Lamé polynomial of degree $n$.
This matches the dimension $2n + 1$ of the space of spherical harmonics of degree $n$.
An equivalent form of the equation uses the Weierstrass function $\wp$ in place of $k^2 \operatorname{sn}^2$, and in the variable $\operatorname{sn}^2 z$ it becomes a special case of Heun's equation.
