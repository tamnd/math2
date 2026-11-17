---
tag: WP27CABPA4
kind: example
name: The natural numbers as a structure for the language of arithmetic
msc: ["03C07", "03B10"]
topics: [NJDME6F845]
audience: ug2
instance_of: [983GZBQYT4]
uses: [983GZBQYT4, WDVVEYD6AT, 0MWKJ44V5A, 6D3WA7N2W4]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
    locator: Examples
  - book: isbn:9780122384523
    locator: Section 2.2
---

## Example

Let $L_A$ be the signature of arithmetic: a constant symbol $0$, a unary function symbol $S$, binary function symbols $+$ and $\cdot$, and a binary relation symbol $<$.
Let $\N = \set{0, 1, 2, \ldots}$ be the set of [[natural numbers|0MWKJ44V5A]], with $0 \in \N$.
We define $\mathfrak{N}$ by the domain $\N$ and the following interpretations, and we check that $\mathfrak{N}$ is an $L_A$-[[structure|983GZBQYT4]].

1. The domain is nonempty, because $0 \in \N$.
2. The constant symbol $0$ gets the number $0^{\mathfrak{N}} = 0$, which lies in $\N$.
3. The symbol $S$ gets the successor map $S^{\mathfrak{N}}(n) = n + 1$. For each $n \in \N$ the number $n + 1$ is again in $\N$, so $S^{\mathfrak{N}} \colon \N \to \N$ is a function.
4. The symbol $+$ gets addition. The sum of two natural numbers is a natural number, so $+^{\mathfrak{N}} \colon \N^2 \to \N$ is a function.
5. The symbol $\cdot$ gets multiplication. The product of two natural numbers is a natural number, so $\cdot^{\mathfrak{N}} \colon \N^2 \to \N$ is a function.
6. The symbol $<$ gets the set $<^{\mathfrak{N}} = \set{(m, n) \in \N^2 : m < n}$, which is a subset of $\N^2$.

Each symbol has an interpretation of the right type, so $\mathfrak{N}$ is an $L_A$-structure.
It is called the standard model of arithmetic.

We compute the value of the closed [[term|6D3WA7N2W4]] $S(S(0)) + S(0)$ in $\mathfrak{N}$.

1. The value of $0$ is $0$.
2. The value of $S(0)$ is $S^{\mathfrak{N}}(0) = 1$.
3. The value of $S(S(0))$ is $S^{\mathfrak{N}}(1) = 2$.
4. The value of $S(S(0)) + S(0)$ is $2 +^{\mathfrak{N}} 1 = 3$.

## Remarks

The example shows that a structure for $L_A$ only needs functions and a relation of the right arities on one domain.
The axioms of [[Peano arithmetic|0QFT7Z76N5]] play no role in the definition; $\mathfrak{N}$ happens to satisfy them.

The example changes as follows when one part changes.

- With the domain $\Z$ and the same interpretations, we get another $L_A$-structure, because the integers are closed under $n \mapsto n + 1$, addition and multiplication.
- With the domain $\set{0, 1, \ldots, 9}$ and ordinary addition, we do not get a structure, because $9 + 1 = 10$ lies outside the domain.
- With the domain $\set{0, 1, \ldots, 9}$ and all operations taken modulo $10$, we get a structure again, because each remainder modulo $10$ lies in the domain.
- A structure for $L_A$ in which $<$ means "greater than" is also a structure; it is just not the intended one.

## Explanations

### L1 human

The language of arithmetic has the symbols $0$, $S$ (for "the next number"), $+$, $\cdot$ and $<$.
To make a structure we choose the numbers $0, 1, 2, \ldots$ and give each symbol its school meaning.
The only thing to check is that each operation gives an answer inside the chosen set.
Adding or multiplying two whole numbers that are $0$ or more gives again such a number, so all is fine.
For example, the expression $S(S(0)) + S(0)$ means "two plus one", and its value is $3$.

### L2 human

We check the term clause on a term with a variable.
Give $x$ the value $4$ and compute the value of $S(x) \cdot (x + S(0))$ in $\mathfrak{N}$.

1. The value of $x$ is $4$, and the value of $S(x)$ is $5$.
2. The value of $S(0)$ is $1$, so the value of $x + S(0)$ is $4 + 1 = 5$.
3. The value of the whole term is $5 \cdot 5 = 25$.

The typical use of $\mathfrak{N}$ is as the intended structure of arithmetic, against which theories such as Peano arithmetic are measured.
A trap is to think that $L_A$ fixes the meaning of its symbols: other $L_A$-structures, such as [[non-standard models of arithmetic|1QWN5CV4CG]], interpret the same symbols differently.
