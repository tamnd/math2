---
tag: ~aee599ed
kind: example
name: A definable Skolem function for square roots in the real field
msc: ["03C07", "03C64"]
topics: [2RE7GWWXM5]
audience: ug2
instance_of: [~71af893e]
uses: [~71af893e, CY1TXHF6KQ, 8WZF9SBP39, DDY3Q3PJ6W]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: Skolem theories
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Example

Let $L = \set{+, -, \cdot, 0, 1}$ be the signature of rings, and let $\mathcal{R} = (\R, +, -, \cdot, 0, 1)$.
Let $\varphi(x, y)$ be the formula $y \cdot y = x$.
Let $\psi(x, y)$ be the formula
$$(y \cdot y = x \land \exists z \, (y = z \cdot z)) \lor (\neg \exists z \, (z \cdot z = x) \land y = 0).$$
We check that $\psi$ defines a function $f \colon \R \to \R$, and that $f$ is a [[Skolem function|~71af893e]] for $\varphi$.

1. In $\R$ an element $y$ is a square exactly when $y \ge 0$. So $\exists z \, (y = z \cdot z)$ says $y \ge 0$, and $\exists z \, (z \cdot z = x)$ says $x \ge 0$.
2. Let $x \ge 0$. The second disjunct is false, and the first says $y^2 = x$ and $y \ge 0$. Its only solution is $y = \sqrt{x}$.
3. Let $x < 0$. The first disjunct is false, because $y^2 \ge 0 > x$. The second says $y = 0$.
4. So for each $x$ there is exactly one $y$ with $\mathcal{R} \models \psi(x, y)$, namely $f(x) = \sqrt{x}$ for $x \ge 0$ and $f(x) = 0$ for $x < 0$.
5. If $\mathcal{R} \models \exists y \, \varphi(x, y)$, then $x \ge 0$ by step 1, and $\varphi(x, f(x))$ holds since $(\sqrt{x})^2 = x$.
6. So $f$ is a Skolem function for $\varphi$, and it is [[definable|CY1TXHF6KQ]] without parameters.

## Remarks

The example shows a Skolem function that needs no choice: the formula $\psi$ selects one of the two square roots.
The selection uses the order, which the ring language defines through squares.
Every [[elementary substructure|8WZF9SBP39]] of $\mathcal{R}$ is closed under $f$.
Indeed, if $a$ lies in it, then $\exists y \, \psi(a, y)$ holds in $\R$, so some element $b$ of the substructure satisfies $\psi(a, b)$, and $b = f(a)$.
The same choice of the nonnegative root works in every [[real closed field|DDY3Q3PJ6W]].
More generally, a nonzero polynomial in $y$ has finitely many real roots, so "the least root" defines a Skolem function of the coefficients without parameters.
In the complex field no formula selects one square root of $-1$; see [[this non-example|~ad253bd2]].

## Explanations

### L1 human

Every positive number has two square roots, for example $3$ and $-3$ for $9$.
To make a rule that gives one answer, we can say "take the root that is not negative".
This rule can be written with only addition and multiplication, because the numbers that are not negative are exactly the squares.
For negative numbers there is no real square root, and the rule gives $0$ by convention.

### L2 human

We evaluate $\psi$ at two points.

1. At $x = 9$: $y = 3$ satisfies $3 \cdot 3 = 9$, and $3 = (\sqrt{3})^2$ is a square. So $\psi(9, 3)$ holds.
2. At $x = 9$: $y = -3$ satisfies $(-3)(-3) = 9$, but $-3$ is not a square of a real number. So $\psi(9, -3)$ fails.
3. At $x = -4$: no $z$ has $z^2 = -4$, so the second disjunct gives $\psi(-4, 0)$.
4. So $f(9) = 3$ and $f(-4) = 0$.

The typical use is to show that a class of substructures is closed under a function without the axiom of choice.
A trap is to drop the condition "$y$ is a square" in the first disjunct: then $\psi$ defines a relation with two values at each $x > 0$, not a function.
