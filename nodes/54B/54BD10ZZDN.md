---
tag: 54BD10ZZDN
kind: definition
name: Saturation of approximation methods
msc: [41A40, 41A35, 41A36]
defines: 3QWJB8GHDE
uses: [06GZ956657, 03TM135G0N, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] and let $L_n \colon X \to X$, $n \ge 1$, be [[continuous linear maps|03TM135G0N]].
Let $\varphi(n) > 0$ with $\varphi(n) \to 0$.
The sequence $(L_n)$ is *saturated* with *saturation order* $\varphi(n)$ if both conditions hold.

1. If $f \in X$ and $\norm{L_n f - f} = o(\varphi(n))$, then $L_n f = f$ for all $n$.
2. Some $f \in X$ with $L_n f \ne f$ for some $n$ satisfies $\norm{L_n f - f} = O(\varphi(n))$.

The *saturation class* is the set of $f \in X$ with $\norm{L_n f - f} = O(\varphi(n))$, in [[big O notation|0TGV80E6A4]].

## Remarks

Example: the Bernstein operators $B_n$ on $C[0, 1]$ with the uniform norm are saturated with order $1/n$.
For $f(x) = x^2$ one has $B_n f(x) = x^2 + \frac{x(1 - x)}{n}$, so $\norm{B_n f - f} = \frac{1}{4n}$, which is $O(1/n)$ but not $o(1/n)$.
The only $f$ with $\norm{B_n f - f} = o(1/n)$ are the linear functions, which $B_n$ reproduces.

Non-example: the Fourier partial sum operators $S_n$ on $L^2$ of the circle are not saturated for any order.
A trigonometric polynomial $f$ of degree $k \ge 1$ has $S_n f = f$ for $n \ge k$, so $\norm{S_n f - f} = o(\varphi(n))$, but $S_0 f \ne f$, so clause 1 fails.

The Fejér means of Fourier series are saturated with order $1/n$ in $C$ of the circle, and only constants are approximated with error $o(1/n)$.
Saturation theorems typically identify the saturation class with a smoothness class, such as functions with Lipschitz first derivative for Bernstein operators.
