---
tag: N5JCKN50NE
kind: definition
name: Degenerate kernel
msc: [45B05, 45P05]
defines: 6Y1RY5767R
uses: [GSMBXT7FPK, 0CRMGPAH83]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_integral_equation
---

## Definition

Let $a < b$.
A *degenerate kernel* on $[a, b]$ is a [[kernel|GSMBXT7FPK]] $K \colon [a, b] \times [a, b] \to \C$ for which there are an integer $n \ge 1$ and functions $a_1, \ldots, a_n, b_1, \ldots, b_n \colon [a, b] \to \C$ such that
$$K(x, s) = \sum_{i=1}^{n} a_i(x) \, b_i(s) \quad \text{for all } x, s \in [a, b].$$

## Remarks

Example: $K(x, s) = \cos(x - s) = \cos x \cos s + \sin x \sin s$, with $n = 2$, $a_1 = b_1 = \cos$ and $a_2 = b_2 = \sin$.

Non-example: $K(x, s) = e^{x s}$ on $[0, 1]$.
If $e^{x s} = \sum_{i=1}^{n} a_i(x) b_i(s)$, then each function $x \mapsto e^{x s}$ would lie in the span of $a_1, \ldots, a_n$.
But the functions $e^{s_1 x}, \ldots, e^{s_{n+1} x}$ for distinct $s_j$ are [[linearly independent|0CRMGPAH83]], which gives $n + 1$ independent functions in a space of dimension at most $n$.

The names *separable kernel* and *kernel of finite rank* are also used.
One usually asks that $a_i$ and $b_i$ be continuous, or square-integrable, and one may take $a_1, \ldots, a_n$ and $b_1, \ldots, b_n$ linearly independent.
For $\varphi(x) = f(x) + \lambda \int_a^b K(x, s) \varphi(s) \, ds$ with a degenerate $K$, every solution has the form $\varphi = f + \lambda \sum_i c_i a_i$ with $c_i = \int_a^b b_i \varphi \, ds$, and the $c_i$ solve an $n \times n$ linear system.
