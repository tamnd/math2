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

Let $K$ be a commutative ring and let $n \ge 1$.
View an $n \times n$ matrix $A = (a_{ij})$ over $K$ as the family of its $n$ rows in $K^n$.
Define $L \colon M_n(K) \to K$ by
$$L(A) = \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)} \cdots a_{n \sigma(n)},$$
where $S_n$ is the [[symmetric group|0515A6D2Y1]] and $\sgn$ is the [[sign|0SK90238BH]].

1. $L$ is multilinear and [[alternating|0MSWYWHYF5]] in the rows, and $L(I_n) = 1$ for the [[identity matrix|06DW9BAWB1]] $I_n$.
2. Let $D \colon M_n(K) \to K$ be multilinear and alternating in the rows. Then $D(A) = D(I_n)\, L(A)$ for every $A \in M_n(K)$.
3. So there is exactly one function $M_n(K) \to K$ that is multilinear and alternating in the rows and has value $1$ on $I_n$, namely $L$.
4. The alternating $n$-linear forms on $K^n$ form a [[free|02E1T12PP4]] $K$-module of rank $1$, with basis $L$.

## Remarks

### Why each hypothesis is needed

The number of arguments must equal $n$, the size of the rows.
For $k < n$ the alternating $k$-linear forms on $K^n$ form a free module of rank $\binom{n}{k}$, so part 3 fails: for $n = 2$, $k = 1$, both $x \mapsto x_1$ and $x \mapsto x_2$ are alternating $1$-linear forms.
For $k > n$ over a field, the only alternating $k$-linear form on $K^n$ is $0$, so no form takes the value $1$.
Commutativity of $K$ is used to write the products $a_{1 \sigma(1)} \cdots a_{n \sigma(n)}$ in any order.

### Consequences

- The [[determinant|00KDZRW4C0]] is well defined as the unique such function, and it is given by the [[Leibniz formula|016PE4VZ8Q]].
- Each function of the rows that is multilinear and alternating is a multiple of the determinant. This gives a short proof of [[multiplicativity|04CPJ6AF00]].
- The same holds for columns in place of rows, by the [[determinant of the transpose|0ZZQ2E1MTE]].
- On a free module $V$ of rank $n$ with basis $B$, the alternating $n$-linear forms are the multiples of the [[determinant in the basis|05CJSSXPR3]] $B$.

### Converse

Part 2 has a converse: for each $c \in K$ the function $c L$ is multilinear and alternating with value $c$ on $I_n$, by part 1.

### Generalizations

The alternating $n$-linear maps $(K^n)^n \to N$ into any $K$-module $N$ are the maps $A \mapsto L(A)\, y$ with $y \in N$, by the same proof.
In the language of exterior powers, $\Lambda^n K^n$ is free of rank $1$.

## Explanations

### L1 human

Ask for a rule that gives one number for each square table of numbers.
Ask that the rule grows in proportion with each row, that it gives zero when two rows are equal, and that it gives $1$ for the identity table.
The theorem says that exactly one rule has these three properties.
That rule is the determinant.
For $2 \times 2$ tables it is $ad - bc$.

### L2 human

We find all bilinear alternating forms $D$ on rows of length $2$.

1. Write the rows as $(a, b) = a e_1 + b e_2$ and $(c, d) = c e_1 + d e_2$.
2. Bilinearity gives $D = ac\, D(e_1, e_1) + ad\, D(e_1, e_2) + bc\, D(e_2, e_1) + bd\, D(e_2, e_2)$.
3. The alternating property gives $D(e_1, e_1) = D(e_2, e_2) = 0$ and $D(e_2, e_1) = -D(e_1, e_2)$.
4. So $D = (ad - bc)\, D(e_1, e_2) = D(I_2)\, L(A)$, as part 2 says.

The typical use is to show that a function equals the determinant without computing it.
A trap: part 2 needs the alternating property, not only multilinearity; the permanent $ad + bc$ is multilinear with value $1$ on $I_2$.

### L3 human

The theorem says that $\operatorname{Alt}^n(K^n) \cong K$, that is, $\Lambda^n K^n$ is free of rank $1$ with generator $e_1 \wedge \dots \wedge e_n$.
The determinant of an endomorphism $T$ is then the scalar by which $\Lambda^n T$ acts on this line.
The proof is the same as the computation of $\Lambda^n$ of a free module, and it works over any commutative ring.
