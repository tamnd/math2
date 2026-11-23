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
Let $\mathbb{N} = \{0, 1, 2, \ldots\}$ be the set of [[natural numbers|0MWKJ44V5A]].
We define $\mathfrak{N}$ by the domain $\mathbb{N}$ and the school meaning of each symbol, and we check that $\mathfrak{N}$ is an $L_A$-[[structure|983GZBQYT4]].

1. The domain is nonempty, because $0 \in \mathbb{N}$.
2. The constant symbol $0$ gets the number $0^{\mathfrak{N}} = 0$, which lies in $\mathbb{N}$.
3. The symbol $S$ gets the successor map $S^{\mathfrak{N}}(n) = n + 1$.
   For each $n \in \mathbb{N}$ the number $n + 1$ is again in $\mathbb{N}$, so $S^{\mathfrak{N}} \colon \mathbb{N} \to \mathbb{N}$ is a function.
4. The symbol $+$ gets addition, and a sum of natural numbers is a natural number, so $+^{\mathfrak{N}} \colon \mathbb{N}^2 \to \mathbb{N}$ is a function.
5. The symbol $\cdot$ gets multiplication, and a product of natural numbers is a natural number, so $\cdot^{\mathfrak{N}} \colon \mathbb{N}^2 \to \mathbb{N}$ is a function.
6. The symbol $<$ gets the set $<^{\mathfrak{N}} = \{ (m, n) \in \mathbb{N}^2 : m < n \}$, which is a subset of $\mathbb{N}^2$.

Each symbol has an interpretation of the right type, so $\mathfrak{N}$ is an $L_A$-structure, called the standard model of arithmetic.

Now we evaluate the closed [[term|6D3WA7N2W4]] $S(S(0)) + S(0)$ from the inside out:
$$0 \mapsto 0, \qquad S(0) \mapsto 1, \qquad S(S(0)) \mapsto 2, \qquad S(S(0)) + S(0) \mapsto 2 + 1 = 3.$$

## Remarks

A structure for $L_A$ needs only a domain and operations and a relation of the right arities.
The axioms of [[Peano arithmetic|0QFT7Z76N5]] play no role in the definition, and $\mathfrak{N}$ happens to satisfy them.

Small changes show which conditions matter.
With the domain $\mathbb{Z}$ and the same operations we get another $L_A$-structure, because the integers are closed under $n \mapsto n + 1$, addition and multiplication.
With the domain $\{0, 1, \ldots, 9\}$ and ordinary addition we do not get a structure, because $9 + 1 = 10$ lies outside the domain.
With the same domain and every operation taken modulo $10$ we get a structure again, because each remainder modulo $10$ lies in the domain.
A structure in which $<$ means "greater than" is also an $L_A$-structure, though not the intended one.

## Explanations

### L1 human

The language of arithmetic has the symbols $0$, $S$ (for "the next number"), $+$, $\cdot$ and $<$.
To make a structure, we choose the numbers $0, 1, 2, \ldots$ and give each symbol its school meaning.
The only thing to check is that each operation gives an answer inside the chosen set.
Adding or multiplying two whole numbers gives again a whole number, so the check passes.
The expression $S(S(0)) + S(0)$ means "two plus one", and its value is $3$.

### L2 human

Terms with variables need a value for each variable.
Give $x$ the value $4$ and evaluate $S(x) \cdot (x + S(0))$ in $\mathfrak{N}$:
$$S(x) \mapsto 5, \qquad x + S(0) \mapsto 4 + 1 = 5, \qquad S(x) \cdot (x + S(0)) \mapsto 5 \cdot 5 = 25.$$
Check: $(4 + 1)(4 + 1) = 25$.
The typical use of $\mathfrak{N}$ is as the intended structure of arithmetic, against which theories such as Peano arithmetic are measured.
Watch out: $L_A$ does not fix the meaning of its symbols, and [[nonstandard models of arithmetic|1QWN5CV4CG]] interpret the same symbols differently.
