---
tag: PGMNNRN5YN
kind: statement
role: theorem
name: Nörlund–Rice integral
msc: [39A70, "30E20"]
uses: [E38801KVJ1, 00FWNP9TXY, 032HKYS329, 092GEF38YD]
about: [3039GWNHWS]
sources:
  - url: https://en.wikipedia.org/wiki/N%C3%B8rlund%E2%80%93Rice_integral
same_as:
  wikidata: Q3333616
  wikipedia: Nørlund–Rice integral
---

## Statement

Let $n \ge 1$ and $0 \le \alpha \le n$ be integers.
Let $\gamma$ be a positively oriented simple closed curve in $\C$ that passes through none of the integers $0, \dots, n$.
Assume that its interior contains $\alpha, \alpha + 1, \dots, n$ and none of $0, 1, \dots, \alpha - 1$.
Let $f$ be holomorphic on an open set that contains $\gamma$ and its interior.
Then
$$\sum_{k=\alpha}^{n} \binom{n}{k} (-1)^k f(k) = \frac{(-1)^n}{2\pi i} \oint_\gamma f(z)\, \frac{n!}{z(z-1)(z-2)\cdots(z-n)}\, dz,$$
where the integral is a [[contour integral|00FWNP9TXY]] and $\binom{n}{k}$ is the [[binomial coefficient|092GEF38YD]].

## Remarks

The proof is the [[residue theorem|032HKYS329]].
Inside $\gamma$ the integrand has simple poles only at $z = k$ with $\alpha \le k \le n$, and the residue there is $f(k)\, n! / \prod_{j \ne k} (k - j) = (-1)^{n-k} \binom{n}{k} f(k)$.
Multiplying by $(-1)^n$ gives the terms $(-1)^k \binom{n}{k} f(k)$.
For $\alpha = 0$ the left side is $(-1)^n \Delta^n f(0)$, an [[$n$-th forward difference|E38801KVJ1]], so the formula turns a high-order difference into a contour integral.
Example: for $f = 1$ and $\alpha = 0$, the left side is $(1 - 1)^n = 0$.
On the right, the integrand is $O(\abs{z}^{-2})$, and the integral over a circle does not depend on its radius once $\gamma$ encloses $0, \dots, n$.
So it equals its limit as the radius grows, which is $0$.

## Explanations

### L1 human

Alternating sums with binomial coefficients, such as $\sum_k \binom{n}{k} (-1)^k f(k)$, involve huge cancellations and are hard to estimate term by term.
The Nörlund–Rice integral rewrites such a sum as one complex integral.
The integral can then be estimated by moving the contour, which often gives precise asymptotics as $n$ grows.

### L2 human

The integrand is $f(z)$ times the kernel $n!/(z(z-1)\cdots(z-n)) = \Gamma(n+1)\Gamma(z-n)/\Gamma(z+1)$, so its size away from the integers is controlled by the gamma function.
To get asymptotics one extends $f$ meromorphically, enlarges the contour, and collects the residues at the poles of $f$ that are crossed.
This method is a standard tool in the analysis of algorithms, for example for digital trees and related recursive structures.
It is closely related to the Mellin transform method for harmonic sums.
