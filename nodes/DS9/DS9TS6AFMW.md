---
tag: DS9TS6AFMW
kind: statement
role: theorem
name: Binomial theorem for commuting matrices
msc: ["15A99", "05A10"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [8G3X8MPG7E]
uses: [MX26N71ZD3, 076JGP6R3T, 0EHWPWGHB2]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_theorem
    locator: Generalizations
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
    locator: Characterizations and properties
---

## Statement

Let $R$ be a commutative ring, and let $A$ and $B$ be $n \times n$ matrices over $R$ that [[commute|MX26N71ZD3]].
Then, for each integer $m \ge 0$,
$$(A + B)^m = \sum_{k = 0}^{m} \binom{m}{k} A^k B^{m - k},$$
where $A^0 = B^0 = I_n$ and the powers are [[matrix products|076JGP6R3T]].

## Remarks

### Why each hypothesis is needed

- The hypothesis $AB = BA$ is needed already for $m = 2$. [[This example|60W7PZXBVB]] gives two matrices with $(A + B)^2 \neq A^2 + 2AB + B^2$.
- In fact, for $m = 2$ the formula holds if and only if $AB = BA$, because $(A + B)^2 = A^2 + AB + BA + B^2$.

### Consequences

- If $A$ and $B$ commute and are [[nilpotent|0419GJC84P]], with $A^p = 0$ and $B^q = 0$, then $(A + B)^{p + q - 1} = 0$. In each term, $k \ge p$ or $m - k \ge q$.
- For a scalar $c$ and any $A$, $(cI + A)^m = \sum_{k} \binom{m}{k} c^{m - k} A^k$, because $cI$ commutes with $A$.
- For a [[Jordan block|07PH4RX0X5]] $J = \lambda I + N$, this gives a closed formula for $J^m$.

### Generalizations

- The same statement holds for commuting elements $a$ and $b$ of any ring, with the same proof. The [[binomial theorem|0EHWPWGHB2]] for numbers is the case of a commutative ring.

## Explanations

### L1 human

The usual formula for $(a + b)^m$ still works for matrices, provided that the two matrices commute.

### L2 human

When $(A + B)^m$ is expanded, each term is a word in $A$ and $B$ of length $m$.
If $A$ and $B$ commute, a word with $k$ letters $A$ equals $A^k B^{m - k}$.
There are $\binom{m}{k}$ such words, which gives the coefficient.
