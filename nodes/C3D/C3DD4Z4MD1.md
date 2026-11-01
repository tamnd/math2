---
tag: C3DD4Z4MD1
kind: statement
role: theorem
name: Landau–Kolmogorov inequality
msc: [26D10]
uses: [084NGSTWM7, 0BTMQ04556]
about: [04TKTF8KDK]
sources:
  - url: https://en.wikipedia.org/wiki/Landau–Kolmogorov_inequality
same_as:
  wikidata: Q5638668
  wikipedia: Landau–Kolmogorov inequality
---

## Statement

Let $n \ge 2$ and $1 \le k < n$ be integers.
There is a constant $C(n, k)$, depending only on $n$ and $k$, with the following property.
Let $f \colon \R \to \R$ be $n$ times differentiable, with $f$ and its $n$-th [[derivative|084NGSTWM7]] $f^{(n)}$ bounded on $\R$.
Then $f^{(k)}$ is bounded on $\R$ and
$$\norm{f^{(k)}}_\infty \le C(n, k) \, \norm{f}_\infty^{1 - k/n} \, \norm{f^{(n)}}_\infty^{k/n},$$
where $\norm{g}_\infty = \sup_{x \in \R} \abs{g(x)}$ is the [[supremum|0BTMQ04556]] of $\abs{g}$.

## Remarks

Proof idea for $n = 2$ and $k = 1$: let $M_0 = \norm{f}_\infty$ and $M_2 = \norm{f''}_\infty$.
By [[Taylor's theorem|03QHBVW4TT]], $f(x \pm h) = f(x) \pm h f'(x) + \frac{h^2}{2} f''(\xi_\pm)$ for some $\xi_\pm$.
Subtracting gives $\abs{f'(x)} \le \frac{M_0}{h} + \frac{h M_2}{2}$ for every $h > 0$, and the choice $h = \sqrt{2 M_0 / M_2}$ gives $\norm{f'}_\infty^2 \le 2 M_0 M_2$.
The constant $2$ here is the best possible on $\R$.
On the half-line $[0, \infty)$ the same kind of bound holds with the best constant $4$ in place of $2$.

The exponents are forced by scaling: replacing $f(x)$ by $f(\lambda x)$ multiplies $\norm{f^{(j)}}_\infty$ by $\lambda^j$.

## Explanations

### L1 human

If a function stays small and its $n$-th derivative also stays small, then every derivative in between must stay small too.
A function cannot wiggle fast without either growing large or having a large high-order derivative.
The inequality gives the precise trade-off.

### L2 human

These are interpolation inequalities: the middle derivative is controlled by a weighted geometric mean of the two ends.
They are a model for the Gagliardo–Nirenberg inequalities for Sobolev norms.
The best constants $C(n, k)$ on $\R$ are known for all $n$ and $k$, and they are attained by functions related to Euler splines.
For $n = 2$ and $k = 1$ the best constant is $\sqrt{2}$.
