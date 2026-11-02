---
tag: XQMNJF241J
kind: statement
role: theorem
name: Goodstein's theorem
msc: [03F30, 03F15]
uses: [0QFT7Z76N5, 0YSCSX5YZC]
about: [0QFT7Z76N5]
sources:
  - url: https://en.wikipedia.org/wiki/Goodstein's_theorem
same_as:
  wikidata: Q1149185
  wikipedia: Goodstein's theorem
---

## Statement

Let $b \ge 2$ be an integer.
The *hereditary base-$b$ notation* of $n \ge 1$ writes $n$ as a sum $b^{e_1} c_1 + \cdots + b^{e_r} c_r$ with $e_1 > \cdots > e_r$ and $0 < c_i < b$.
Then it writes each exponent $e_i$ in hereditary base-$b$ notation again.
Let $B_b(n)$ be the number obtained by replacing every $b$ in this notation by $b + 1$, with $B_b(0) = 0$.
The *Goodstein sequence* of $m \in \N$ is $G_1 = m$ and $G_{k+1} = B_{k+1}(G_k) - 1$ while $G_k > 0$.

1. For every $m \in \N$ the Goodstein sequence of $m$ reaches $0$.
2. Statement 1, written as a sentence of first-order arithmetic, is not provable in [[Peano arithmetic|0QFT7Z76N5]] $\mathsf{PA}$.

## Remarks

Proof idea for 1: replace each base in the hereditary notation of $G_k$ by the [[ordinal|0YSCSX5YZC]] $\omega$.
This gives an ordinal $o_k < \varepsilon_0$, and the change of base does not change it while subtracting $1$ makes it strictly smaller.
A strictly decreasing sequence of ordinals is finite, so the sequence reaches $0$.
Goodstein proved part 1 in 1944; Kirby and Paris proved part 2 in 1982, by showing that $\mathsf{PA}$ plus statement 1 proves the consistency of $\mathsf{PA}$.

Example: for $m = 3$, the sequence is $3 = 2 + 1$, then $3 + 1 - 1 = 3$, then in base $3$, $3 = 3^1$ becomes $4 - 1 = 3$, then $2$, $1$, $0$.
For $m = 4$ the sequence also reaches $0$, but only after more than $10^{100{,}000{,}000}$ steps.

## Explanations

### L1 human

Start with a number and write it in base $2$, using only $2$s even in the exponents.
Change all $2$s to $3$s and subtract $1$; then repeat with bases $3$ and $4$, and so on.
The numbers first grow enormously, yet the theorem says they always come back to $0$.
The proof uses infinite ordinals, and in fact the theorem cannot be proved with the usual axioms of arithmetic alone.

### L2 human

The theorem shows how ordinals below $\varepsilon_0$ measure the strength of $\mathsf{PA}$: transfinite induction up to [[epsilon nought|KT50SMH3EC]] proves it, while $\mathsf{PA}$ does not.
This ties it to [[Gentzen's consistency proof|QPV0HNP22S]] and to [[ordinal analysis|C5E5TG8PGP]].
Like the [[Paris–Harrington theorem|509ZWA0R26]], it is a natural true statement independent of $\mathsf{PA}$.
