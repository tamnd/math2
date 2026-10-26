---
tag: 04TSHB9H8D
kind: definition
name: Little o notation
msc: [41A60]
defines: 00T5EPFQB9
uses: [0RYTGBJAGN]
sources:
  - url: https://en.wikipedia.org/wiki/Big_O_notation
    locator: Little-o notation
---

## Definition

Let $f$ and $g$ be real functions defined on an interval $[x_0, \infty)$.
We write $f(x) = o(g(x))$ as $x \to \infty$ if for each $\varepsilon > 0$ there is $x_1 \ge x_0$ with
$$|f(x)| \le \varepsilon |g(x)| \quad \text{for all } x \ge x_1.$$

## Remarks

If $g(x) \ne 0$ for large $x$, then $f = o(g)$ means that $f(x)/g(x) \to 0$.
Each $f = o(g)$ is also $f = O(g)$, in the sense of [[big O notation|0RYTGBJAGN]].
For example, $x = o(x^2)$ and $\ln x = o(x)$ as $x \to \infty$.
Mathlib defines it for filters, as `Asymptotics.IsLittleO`.

## Explanations

### L1 human

The statement $f = o(g)$ says that $f$ becomes negligible compared with $g$.
Each fixed fraction of $|g|$ eventually exceeds $|f|$.
