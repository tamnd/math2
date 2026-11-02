---
tag: VFRJ0P2P15
kind: statement
role: theorem
name: Hyers' theorem
msc: [39B82, 39B52]
uses: [J6GPWAX3X2, KF719SZD5T, 03J5RAKB30, 06GZ956657, 0NRYHJPQG2]
about: [TPYXQTYND6, J6GPWAX3X2]
sources:
  - url: https://en.wikipedia.org/wiki/Hyers%E2%80%93Ulam%E2%80%93Rassias_stability
---

## Statement

Let $E_1$ be a real [[normed vector space|03J5RAKB30]], let $E_2$ be a real [[Banach space|06GZ956657]], and let $\delta \ge 0$.
Let $f \colon E_1 \to E_2$ be [[$\delta$-additive|J6GPWAX3X2]], that is, $\norm{f(x + y) - f(x) - f(y)} \le \delta$ for all $x, y \in E_1$.
Then:

1. For each $x \in E_1$ the limit $A(x) = \lim_{n \to \infty} 2^{-n} f(2^n x)$ exists in $E_2$.
2. The map $A \colon E_1 \to E_2$ is [[additive|KF719SZD5T]] and satisfies $\norm{f(x) - A(x)} \le \delta$ for all $x \in E_1$.
3. $A$ is the only additive map $E_1 \to E_2$ such that $f - A$ is bounded.
4. If moreover, for each $x \in E_1$, the map $t \mapsto f(tx)$ from $\R$ to $E_2$ is continuous, then $A$ is [[linear|0NRYHJPQG2]].

## Remarks

Setting $x = y$ gives $\norm{f(2x) - 2f(x)} \le \delta$, so consecutive terms of the sequence $2^{-n} f(2^n x)$ differ by at most $2^{-n-1}\delta$.
The sequence is therefore Cauchy, it converges by completeness of $E_2$, and summing the geometric bounds gives $\norm{f(x) - A(x)} \le \delta$.
Additivity follows from $\norm{2^{-n}(f(2^n(x + y)) - f(2^n x) - f(2^n y))} \le 2^{-n}\delta$.
For uniqueness, the difference $D$ of two such additive maps is additive and bounded, and $D(x) = D(nx)/n \to 0$.
Example: $f(x) = x + \sin x$ on $\R$ is $3$-additive, and the theorem gives $A(x) = x$ with $\abs{f(x) - x} \le 1$.
Completeness of $E_2$ is used to make the limit exist.
D. H. Hyers proved the theorem in 1941, answering [[Ulam's stability problem|CBYB39FTFG]] for the Cauchy equation.

## Explanations

### L1 human

If a map between normed spaces adds vectors correctly up to a fixed error, then it is close to a map that adds them exactly.
The exact map is found by scaling up, applying $f$, and scaling back down, so the fixed error becomes negligible.
The distance between the two maps is at most the error itself.

### L2 human

The theorem shows that the Cauchy equation $f(x + y) = f(x) + f(y)$ is [[Hyers–Ulam stable|TPYXQTYND6]] with constant $1$.
The method, now called the direct method, works for many other equations, such as the Jensen and quadratic equations, after a suitable rescaling.
Replacing the constant $\delta$ by a bound that grows with $\norm{x}$ and $\norm{y}$ leads to the [[Aoki–Rassias theorem|93WX6PZC8R]].
