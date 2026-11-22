---
tag: 1C8RRWHD45
kind: statement
role: theorem
name: Existence and uniqueness of the normalized alternating n-linear form
msc: ["15A15", "15A75"]
topics: [DTBK11SR77]
audience: ug2
about: [0K6CH0MT0F]
uses: [0MSWYWHYF5, 0SK90238BH, 0515A6D2Y1, 06DW9BAWB1, 02E1T12PP4]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
  - url: https://en.wikipedia.org/wiki/Leibniz_formula_for_determinants
    locator: Formal statement and proof
---

## Statement

There is exactly one function of the rows of a square matrix that is linear in each row, vanishes when two rows are equal, and gives $1$ on the identity, and every function with the first two properties is a multiple of it.
Let $K$ be a commutative ring and let $n \ge 1$.
View an $n \times n$ matrix $A = (a_{ij})$ over $K$ as the family of its $n$ rows in $K^n$.
Define $L \colon M_n(K) \to K$ by
$$L(A) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)} \cdots a_{n \sigma(n)},$$
where $S_n$ is the [[symmetric group|0515A6D2Y1]] and $\operatorname{sgn}$ is the [[sign|0SK90238BH]].

1. $L$ is multilinear and [[alternating|0MSWYWHYF5]] in the rows, and $L(I_n) = 1$ for the [[identity matrix|06DW9BAWB1]] $I_n$.
2. Let $D \colon M_n(K) \to K$ be multilinear and alternating in the rows. Then $D(A) = D(I_n)\, L(A)$ for every $A \in M_n(K)$.
3. So there is exactly one function $M_n(K) \to K$ that is multilinear and alternating in the rows and has the value $1$ on $I_n$, namely $L$.
4. The alternating $n$-linear forms on $K^n$ form a [[free|02E1T12PP4]] $K$-module of rank $1$, with basis $L$.

## Remarks

### The case of size two

For $n = 2$, write the rows as $(a, b) = a e_1 + b e_2$ and $(c, d) = c e_1 + d e_2$, and let $D$ be bilinear and alternating.
Expanding in both rows gives four terms:
$$D = ac\, D(e_1, e_1) + ad\, D(e_1, e_2) + bc\, D(e_2, e_1) + bd\, D(e_2, e_2).$$
The alternating property kills the first and last terms and gives $D(e_2, e_1) = -D(e_1, e_2)$.
So $D = (ad - bc)\, D(e_1, e_2)$, which is part 2, since $D(e_1, e_2) = D(I_2)$ and $L(A) = ad - bc$.
For $n$ rows the same expansion has $n^n$ terms, and only the $n!$ terms that use each basis vector once survive.

### Why each hypothesis is needed

The number of arguments must equal $n$, the length of the rows.
For $k < n$ the alternating $k$-linear forms on $K^n$ form a free module of rank $\binom{n}{k}$, which is larger than $1$, so no single form generates them.
For example, for $n = 2$ and $k = 1$ the condition "alternating" is empty, and both $x \mapsto x_1$ and $x \mapsto x_2$ are alternating $1$-linear forms on $K^2$, and neither is a multiple of the other.
For $k > n$ every alternating $k$-linear form on $K^n$ is $0$, because each term of the expansion in the standard basis repeats a basis vector.

Commutativity of $K$ is used twice.
The proof of part 1 reorders the factors of the products $a_{1 \sigma(1)} \cdots a_{n \sigma(n)}$, and the proof of part 2 pulls scalars out of every slot of $D$.

### What it gives you

The theorem is what makes the [[determinant|00KDZRW4C0]] well defined as the unique normalized alternating form of the rows, and the formula for $L$ is the [[Leibniz formula|016PE4VZ8Q]].
Part 2 also gives a quick proof of [[multiplicativity|04CPJ6AF00]].
For a fixed $B$, the function $A \mapsto \det(AB)$ is multilinear and alternating in the rows of $A$, so it equals $\det(I_n B) \det A = \det B \det A$.
By the [[determinant of the transpose|0ZZQ2E1MTE]], the same statements hold with columns in place of rows.
On a free module $V$ of rank $n$ with basis $B$, the alternating $n$-linear forms are exactly the multiples of the [[determinant in the basis B|05CJSSXPR3]].

### The converse

Part 2 has a converse: for each $c \in K$, the function $c L$ is multilinear and alternating with value $c$ on $I_n$, by part 1.
So the forms $D$ correspond exactly to the elements $D(I_n)$ of $K$, which is part 4.

### Generalizations

The alternating $n$-linear maps $(K^n)^n \to N$ into any $K$-module $N$ are exactly the maps $A \mapsto L(A)\, y$ with $y \in N$, by the same proof.
In the language of exterior powers, $\Lambda^n K^n$ is free of rank $1$, with generator $e_1 \wedge \dots \wedge e_n$.

## Explanations

### L1 human

Ask for a rule that gives one number for each square table of numbers.
Ask that the rule grows in proportion with each row and adds up when a row is a sum, that it gives zero when two rows are equal, and that it gives $1$ for the identity table.
The theorem says that exactly one rule has these three properties, and that rule is the determinant.
For $2 \times 2$ tables it is $ad - bc$, so the table with rows $1, 2$ and $3, 4$ gets $4 - 6 = -2$.

### L2 human

Here is a typical use: prove that the scalar triple product $u \cdot (v \times w)$ is the determinant of the matrix with rows $u$, $v$, $w$, without expanding the determinant.
The triple product is trilinear and alternating, as the [[triple product example|DT0H0YQ4H7]] checks.
By part 2 it equals its value on $(e_1, e_2, e_3)$ times the determinant.
That value is $e_1 \cdot (e_2 \times e_3) = e_1 \cdot e_1 = 1$.
So $u \cdot (v \times w) = \det(u, v, w)$, and for $u = (1, 0, 2)$, $v = (0, 1, 1)$ and $w = (1, 1, 0)$ both sides are $-3$.
Watch out: part 2 needs the alternating property and not only multilinearity.
The [[permanent|X9B1XETBPF]] $ad + bc$ is multilinear with value $1$ on $I_2$, but it is not the determinant.

### L3 human

The theorem says that $\operatorname{Alt}^n(K^n) \cong K$, that is, the top exterior power $\Lambda^n K^n$ is free of rank $1$.
The determinant of an endomorphism $T$ is then the scalar by which $\Lambda^n T$ acts on this line, which is a definition free of bases.
The proof works over any commutative ring, and it is the same computation that shows $\Lambda^k K^n$ is free of rank $\binom{n}{k}$ with the products $e_{i_1} \wedge \dots \wedge e_{i_k}$, $i_1 < \dots < i_k$, as a basis.
