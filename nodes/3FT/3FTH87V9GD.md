---
tag: 3FTH87V9GD
kind: definition
name: Mikusiński field of operators
msc: [44A40]
defines: 82YAXZMMQ1
uses: [FCKX8KFVGN, E9QNNPQD2P, 0F2PTGX1A2]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Definition

Let $\mathcal{C}$ be the set of continuous functions $[0, \infty) \to \C$, with pointwise addition and the [[convolution on the half-line|FCKX8KFVGN]] $(f * g)(t) = \int_0^t f(\tau) g(t - \tau) \, d\tau$ as multiplication.
This is a commutative ring without unit and [[without zero divisors|E9QNNPQD2P]].
The *Mikusiński field of operators* $\mathcal{M}$ is its [[field of fractions|0F2PTGX1A2]]:

1. its elements are the classes $f/g$ of pairs $(f, g) \in \mathcal{C} \times (\mathcal{C} \setminus \set{0})$, where $(f, g)$ and $(f_1, g_1)$ are identified when $f * g_1 = f_1 * g$;
2. addition is $f/g + f_1/g_1 = (f * g_1 + f_1 * g)/(g * g_1)$;
3. multiplication is $(f/g)(f_1/g_1) = (f * f_1)/(g * g_1)$.

The elements of $\mathcal{M}$ are called *operators*.

## Remarks

The construction works without a unit in $\mathcal{C}$.
The identification is an equivalence relation because $\mathcal{C}$ has no zero divisors, and $\mathcal{M}$ is a field with unit $g/g$ for any $g \ne 0$.
Each $f \in \mathcal{C}$ is identified with $(f * g)/g$, which does not depend on $g$, and this embeds $\mathcal{C}$ as a subring.
Let $l \in \mathcal{C}$ be the constant function $1$, so that $l * f$ is the integral $\int_0^t f$.
A complex number $\alpha$ is identified with $(\alpha l)/l$; then the product of $\alpha$ and $f$ in $\mathcal{M}$ is the ordinary multiple $\alpha f$.
The operator $s = l/(l * l) = 1/l$ satisfies $s f = f' + f(0)$ for every continuously differentiable $f$, because $l * f' = f - f(0) l$.

Example: the function $t$ equals $l * l$, so its image in $\mathcal{M}$ is $(l * l * l)/l$, and $s \cdot t = \frac{l}{l * l} \cdot \frac{l * l * l}{l} = \frac{l * l * l * l}{l * l * l} = l$.
So $s t = l$, the constant function $1$, in line with $s f = f' + f(0)$ for $f(t) = t$.

Non-example: the pair $(l, 0)$ does not define an element of $\mathcal{M}$, since clause 1 requires a nonzero denominator.
Allowing the denominator $0$ would make every pair $(f, 0)$ equivalent to every $(f_1, 0)$, since $f * 0 = f_1 * 0 = 0$, and the division rules would fail.
