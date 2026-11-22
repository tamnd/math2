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

### Why the hypothesis is needed

The theorem says that the formula from school algebra survives for matrices, provided the two summands commute.
Without that hypothesis it fails already for $m = 2$, because
$$(A + B)^2 = A^2 + AB + BA + B^2,$$
and this equals $A^2 + 2AB + B^2$ exactly when $BA = AB$.
[[The binomial formula does not generalize to matrices|60W7PZXBVB]] gives two shears for which the two sides differ.
The [[proof|KCD79MKQ16]] uses $AB = BA$ at one place only, to move $B$ past powers of $A$.

### Powers of a scalar plus a nilpotent

For a scalar $c$ and any $A$, the matrix $cI$ commutes with $A$, so
$$(cI + A)^m = \sum_{k = 0}^{m} \binom{m}{k} c^{m - k} A^k.$$
If $A$ is [[nilpotent|0419GJC84P]], the sum stops early, and for a [[Jordan block|07PH4RX0X5]] this gives a closed formula.
For example, $J = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = 2I + N$ with $N = E_{12}$ and $N^2 = 0$, so
$$J^m = 2^m I + m \, 2^{m - 1} N = \begin{pmatrix} 2^m & m \, 2^{m - 1} \\ 0 & 2^m \end{pmatrix}.$$
Check for $m = 3$: $J^2 = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix}$ and $J^3 = \begin{pmatrix} 8 & 4 + 8 \\ 0 & 8 \end{pmatrix}$, and indeed $3 \cdot 2^2 = 12$.

### Sums of commuting nilpotents

If $A$ and $B$ commute, with $A^p = 0$ and $B^q = 0$, then $(A + B)^{p + q - 1} = 0$.
In each term of the sum, $k < p$ forces $m - k \ge (p + q - 1) - (p - 1) = q$, so either $A^k = 0$ or $B^{m - k} = 0$.

### Generalizations

The same statement holds for commuting elements $a$ and $b$ of any ring, with the same proof.
The [[binomial theorem|0EHWPWGHB2]] for numbers is the case of a commutative ring, where every two elements commute.

## History

The coefficients $\binom{m}{k}$ form the arithmetic triangle that Pascal studied in a treatise written in 1654.
The version for matrices adds only the hypothesis that the two summands commute.

## Explanations

### L1 human

The usual formula for $(a + b)^m$ still works for matrices, provided that the two matrices commute.
For example, $(A + B)^2 = A^2 + 2AB + B^2$ holds for commuting $A$ and $B$, but it can fail when $AB \ne BA$.

### L2 human

When we expand $(A + B)^m$ without collecting terms, we get $2^m$ words in $A$ and $B$ of length $m$, such as $ABBA$ for $m = 4$.
If $A$ and $B$ commute, we can sort the letters, and a word with $k$ letters $A$ equals $A^k B^{m - k}$; for example $ABBA = A^2 B^2$.
There are $\binom{m}{k}$ such words, which gives the coefficient.
Watch out: the sorting step is exactly where commuting is used, and for matrices that do not commute, $ABBA$ and $A^2 B^2$ are in general different.
