---
tag: ~593aaada
kind: example
name: The three-element MV-algebra
msc: ["06D35", "03B50"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [8T4M7RN9AC]
uses: [QVWHWDJ5X1, ~bd015994]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Examples of MV-algebras
---

## Example

Let $L_2 = \set{0, \tfrac12, 1}$ with $x \oplus y = \min(1, x + y)$ and $\neg x = 1 - x$.
It is a subalgebra of $[0, 1]$, so it is an [[MV-algebra|QVWHWDJ5X1]] by [[the standard MV-algebra theorem|~bd015994]].
Rows give $x$ and columns give $y$, in the order $0, \tfrac12, 1$.

| $x \oplus y$ | $0$ | $\tfrac12$ | $1$ |
|---|---|---|---|
| $0$ | $0$ | $\tfrac12$ | $1$ |
| $\tfrac12$ | $\tfrac12$ | $1$ | $1$ |
| $1$ | $1$ | $1$ | $1$ |

| $x \odot y$ | $0$ | $\tfrac12$ | $1$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $0$ |
| $\tfrac12$ | $0$ | $0$ | $\tfrac12$ |
| $1$ | $0$ | $\tfrac12$ | $1$ |

| $x \to y$ | $0$ | $\tfrac12$ | $1$ |
|---|---|---|---|
| $0$ | $1$ | $1$ | $1$ |
| $\tfrac12$ | $\tfrac12$ | $1$ | $1$ |
| $1$ | $0$ | $\tfrac12$ | $1$ |

The negation is $\neg 0 = 1$, $\neg \tfrac12 = \tfrac12$, $\neg 1 = 0$.

## Remarks

1. $\tfrac12 \oplus \tfrac12 = 1 \ne \tfrac12$, so the algebra is not Boolean.
2. It satisfies $x \oplus x \oplus x = x \oplus x$; the law fails in $[0, 1]$ at $x = \tfrac13$.
3. It is the algebra of three-valued Łukasiewicz logic: $p \lor \neg p$ takes the value $\tfrac12$ at $p = \tfrac12$.

## Explanations

### L1 human

There are three truth values: false, half true and true.
"Not half true" is half true.
Two half truths, joined by the strong "or", make a full truth.

### L2 human

1. Compute $\tfrac12 \odot \tfrac12 = \neg(\tfrac12 \oplus \tfrac12) = \neg 1 = 0$.
2. So the strong "and" of a half truth with itself is false.
3. Compute $\tfrac12 \to 0 = \neg \tfrac12 \oplus 0 = \tfrac12$.
4. Check residuation: $\tfrac12$ is the largest $z$ with $z \odot \tfrac12 \le 0$.

The typical use: the smallest MV-algebra that is not Boolean, for quick counterexamples.
The trap: it is not the three-element Heyting chain; there, $\neg \tfrac12 = 0$.
