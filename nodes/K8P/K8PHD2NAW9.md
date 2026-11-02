---
tag: K8PHD2NAW9
kind: definition
name: q-Pochhammer symbol
msc: [05A30, 33D15]
defines: Y1X8ZZQ7VM
uses: [09FTAET5Z4, H1Z2TKY3EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Q-Pochhammer_symbol
---

## Definition

Let $a$ and $q$ be [[complex numbers|09FTAET5Z4]], and let $n \ge 0$ be an integer.
The $q$-Pochhammer symbol is
$$(a; q)_n = \prod_{k=0}^{n-1} (1 - a q^k),$$
with $(a; q)_0 = 1$.
If $\abs{q} < 1$, the infinite $q$-Pochhammer symbol is the infinite product
$$(a; q)_\infty = \prod_{k=0}^{\infty} (1 - a q^k).$$

## Remarks

For $\abs{q} < 1$ the product defining $(a; q)_\infty$ converges, since $\sum_k \abs{a q^k} = \abs{a} / (1 - \abs{q}) < \infty$; it is zero exactly when some factor is zero.
Example: $(q; q)_2 = (1 - q)(1 - q^2) = 1 - q - q^2 + q^3$, by the definition with $a = q$ and $n = 2$.
Non-example: for $\abs{q} > 1$ and $a \ne 0$, the factors $1 - a q^k$ do not tend to $1$, so the infinite product does not [[converge|H1Z2TKY3EQ]] and $(a; q)_\infty$ is not defined.
The name comes from the limit $\frac{(q^x; q)_n}{(1 - q)^n} \to x(x+1)\cdots(x+n-1)$ as $q \to 1$, the rising factorial or Pochhammer symbol.
The [[generating function for partitions|0578PA53VA]] reads $\sum_{n \ge 0} p(n) q^n = 1/(q; q)_\infty$ for $\abs{q} < 1$.

## Explanations

### L1 human

The symbol $(a; q)_n$ is shorthand for the product of $n$ factors $1 - a$, $1 - aq$, up to $1 - aq^{n-1}$.
