---
tag: 93WX6PZC8R
kind: statement
role: theorem
name: Aoki–Rassias theorem
msc: [39B82, 39B52]
uses: [KF719SZD5T, 03J5RAKB30, 06GZ956657, 0NRYHJPQG2, VFRJ0P2P15]
about: [TPYXQTYND6]
sources:
  - url: https://en.wikipedia.org/wiki/Hyers%E2%80%93Ulam%E2%80%93Rassias_stability
---

## Statement

Let $E_1$ be a real [[normed vector space|03J5RAKB30]] and let $E_2$ be a real [[Banach space|06GZ956657]].
Let $\theta \ge 0$ and $0 \le p < 1$.
Let $f \colon E_1 \to E_2$ satisfy
$$\norm{f(x + y) - f(x) - f(y)} \le \theta \left( \norm{x}^p + \norm{y}^p \right) \quad \text{for all } x, y \in E_1.$$
Then there is a unique [[additive map|KF719SZD5T]] $A \colon E_1 \to E_2$ such that
$$\norm{f(x) - A(x)} \le \frac{2\theta}{2 - 2^p} \norm{x}^p \quad \text{for all } x \in E_1,$$
where $\norm{0}^0$ is read as $1$.
It is given by $A(x) = \lim_{n \to \infty} 2^{-n} f(2^n x)$.
If moreover, for each $x \in E_1$, the map $t \mapsto f(tx)$ from $\R$ to $E_2$ is continuous, then $A$ is [[linear|0NRYHJPQG2]].

## Remarks

The proof follows [[Hyers' theorem|VFRJ0P2P15]].
Setting $x = y$ gives $\norm{f(2x) - 2f(x)} \le 2\theta \norm{x}^p$, so consecutive terms of $2^{-n} f(2^n x)$ differ by at most $\theta \, 2^{n(p-1)} \norm{x}^p$.
Because $p < 1$, these bounds form a convergent geometric series with sum $\frac{2\theta}{2 - 2^p}\norm{x}^p$.
For $p = 0$ the hypothesis is a constant bound $2\theta$, and the theorem gives back Hyers' theorem with $\delta = 2\theta$.
Example: $f(x) = x + \sqrt{\abs{x}}$ on $\R$ satisfies the hypothesis with $\theta = 1$ and $p = 1/2$, because $0 \le \sqrt{\abs{x}} + \sqrt{\abs{y}} - \sqrt{\abs{x + y}} \le \sqrt{\abs{x}} + \sqrt{\abs{y}}$; here $A(x) = x$.
The hypothesis $p < 1$ cannot be dropped: Z. Gajda showed that the statement fails for $p = 1$, already for maps $\R \to \R$.
T. Aoki proved the additive case in 1950, and Th. M. Rassias proved the linear case in 1978.

## Explanations

### L1 human

Hyers' theorem allows a fixed error in the rule $f(x + y) = f(x) + f(y)$.
This theorem allows an error that grows with the size of $x$ and $y$, but more slowly than linearly.
The conclusion is the same in spirit: $f$ is close to an exact additive map, with a distance that grows like $\norm{x}^p$.

### L2 human

The theorem started the study of stability with a control function, often called Hyers–Ulam–Rassias stability.
The same rescaling argument works for $p > 1$ with $A(x) = \lim_n 2^n f(2^{-n} x)$, and the excluded case $p = 1$ marks the boundary where the geometric series diverges.
Similar results hold for the Jensen, quadratic and many other [[functional equations|SRAN4EKWS0]].
