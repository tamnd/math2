---
tag: ZPJYXS4MQ9
kind: proof
name: Proof of Bernoulli's inequality by induction
msc: [26D05]
proves: 0M1MX28VXK
uses: [0ASJVEFA9J, 0QSPNASE50]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Bernoulli%27s_inequality
    locator: Proof for integer exponent
---

## Proof

We argue by [[induction|0ASJVEFA9J]] on $n$.
Let $x$ be a real number with $x \ge -1$.
For each natural number $n$, let $P(n)$ be the claim $(1 + x)^n \ge 1 + n x$.
We use the rules of the [[ordered field $\mathbb{R}$|0QSPNASE50]].

1. Base case: $(1 + x)^0 = 1$ and $1 + 0 \cdot x = 1$. So $P(0)$ holds.
2. Induction step: suppose that $P(n)$ holds, that is, $(1 + x)^n - (1 + n x) \ge 0$.
3. Since $x \ge -1$, adding $1$ to both sides gives $1 + x \ge 0$.
4. The product of two nonnegative reals is nonnegative. So $\big((1 + x)^n - (1 + n x)\big)(1 + x) \ge 0$ by steps 2 and 3.
5. Expanding step 4 gives $(1 + x)^{n+1} \ge (1 + n x)(1 + x)$.
6. We expand: $(1 + n x)(1 + x) = 1 + (n + 1) x + n x^2$.
7. If $x \ge 0$, then $x^2 = x \cdot x \ge 0$. If $x < 0$, then $-x > 0$ and $x^2 = (-x)(-x) \ge 0$. Since $n \ge 0$, also $n x^2 \ge 0$.
8. Adding $1 + (n + 1) x$ to $n x^2 \ge 0$ gives $1 + (n + 1) x + n x^2 \ge 1 + (n + 1) x$.
9. By steps 5, 6 and 8 and transitivity, $(1 + x)^{n+1} \ge 1 + (n + 1) x$. So $P(n + 1)$ holds.
10. By induction, $(1 + x)^n \ge 1 + n x$ for every natural number $n$.

## Idea

Each step multiplies by $1 + x$, which is allowed in an inequality because $1 + x \ge 0$.
The product $(1 + n x)(1 + x)$ equals $1 + (n + 1) x$ plus the extra term $n x^2$.
This extra term is never negative, so it can be dropped.
