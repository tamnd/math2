---
tag: BM6P0C2AC2
kind: statement
role: lemma
name: Gödel's β-function lemma
aliases: [beta-function-lemma, godel-beta-function]
msc: ["03F30", "03D20"]
topics: [QHCRN4JVG0]
audience: grad
uses: [0FNN9B4W64, Y0JTZXBRT5, 329ZG1Z0G5, 5NVA2JRHPV]
sources:
  - wikipedia: en:8371092@r1355768245
    locator: Gödel numbering for sequences, section Accessing members > Gödel's β-function lemma
    note: adopted
    mention: wikipedia://en/8371092#TT9T
    sections: [Statement]
  - book: isbn:9780521857840
  - book: isbn:9781482237726
inventory: [2MKMSGKP7Z]
---

## Statement

For $c, d, i \in \N$, let $\beta(c, d, i)$ be the remainder of $c$ on division by $1 + (i + 1) d$.

For every $n \in \N$ and every finite sequence $a_0, a_1, \ldots, a_n$ of natural numbers, there are $c, d \in \N$ such that
$$\beta(c, d, i) = a_i \quad \text{for } i = 0, 1, \ldots, n.$$

The graph of $\beta$ is defined by a $\Delta_0$ formula, which even represents $\beta$ in Robinson arithmetic; [[this lemma|2X3BHXYR6D]] gives the formula.

## Remarks

### Why each hypothesis is needed

- The modulus $1 + (i + 1) d$ depends on $i$ through the factor $i + 1$; a modulus that does not depend on $i$ would give the same remainder for every $i$.
- The proof chooses $d$ divisible by $1, 2, \ldots, n$ and at least every $a_i$. If $d$ is too small, the moduli need not be coprime: for $d = 1$ they are $2, 3, 4, \ldots$, and $2$ and $4$ are not coprime.

### Consequences

- A finite sequence of any length is coded by two numbers, with a $\Delta_0$ decoding. This replaces coding by prime powers, whose decoding needs exponentiation, which is not in $L_A$.
- Exponentiation is $\Sigma_1$-definable in $\mathfrak{N}$: $y = x^z$ holds exactly when there are $c, d$ with $\beta(c, d, 0) = 1$, $\beta(c, d, i + 1) = \beta(c, d, i) \cdot x$ for all $i < z$, and $\beta(c, d, z) = y$. Since $\beta(c, d, i) \le c$, these clauses are $\Delta_0$ in $c, d, x, y, z$ once written with the $\Delta_0$ formula for $\beta$ and quantifiers bounded by $c$.
- The same pattern makes the graph of every [[primitive recursive function|5NVA2JRHPV]] $\Sigma_1$, and it is the main lemma of the [[representability theorem|BJF29XET83]].

### Generalizations

The lemma is provable in [[Peano arithmetic|HACXBCM7SS]] in a formalized form: for every sequence coded by $c, d$ and every $a$, there is a code $c', d'$ of the sequence extended by $a$.
Other $\Delta_0$-decodable codings of sequences exist, but the β function is the classical one that works in the language $\set{0, S, +, \cdot, <}$ without exponentiation.

## History

Gödel introduced the β function in his 1931 paper on incompleteness, to show that relations defined by primitive recursion are definable from addition and multiplication.

## Explanations

### L1 human

The lemma says that any finite list of numbers can be packed into just two numbers $c$ and $d$.
To read the $i$-th entry back, divide $c$ by $1 + (i + 1) d$ and take the remainder.
The point is that the reading uses only addition, multiplication and bounded search, so arithmetic can talk about finite lists, and hence about computations.

### L2 human

We code the sequence $2, 0, 2, 1$, with $n = 3$.

1. Put $s = \max(3, 2, 0, 2, 1) = 3$ and $d = s! = 6$. The moduli are $7$, $13$, $19$ and $25$.
2. These are pairwise coprime, and each entry is smaller than its modulus.
3. The Chinese remainder theorem gives $c = 27001$: indeed $27001 = 3857 \cdot 7 + 2 = 2077 \cdot 13 + 0 = 1421 \cdot 19 + 2 = 1080 \cdot 25 + 1$.
4. So $\beta(27001, 6, i)$ for $i = 0, 1, 2, 3$ is $2, 0, 2, 1$.

The pair $c = 3412752$, $d = 24$ also codes this sequence; [[the Δ0 lemma for β|2X3BHXYR6D]] checks one of its entries.
The typical use is to replace "there is a finite sequence with these properties" by "there are $c$ and $d$ with these properties".
A trap is to expect uniqueness: many pairs $(c, d)$ code the same sequence, and every $c$ that agrees modulo the product of the moduli works.
