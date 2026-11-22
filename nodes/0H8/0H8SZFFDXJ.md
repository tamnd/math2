---
tag: 0H8SZFFDXJ
kind: statement
role: proposition
name: Rule of Sarrus
msc: [15A15]
topics: [DTBK11SR77]
audience: school
uses: [0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Rule_of_Sarrus
    locator: lead section
same_as:
  wikidata: Q913837
  wikipedia: Rule of Sarrus
---

## Statement

The rule of Sarrus computes a $3 \times 3$ determinant as three products along diagonals minus three products along the opposite diagonals.
Let $K$ be a commutative ring and let $a, b, c, d, e, f, g, h, i \in K$.
Then the [[determinant|00KDZRW4C0]] of the $3 \times 3$ matrix with these entries is
$$\det \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = aei + bfg + cdh - ceg - afh - bdi.$$
Write the first two columns again to the right of the matrix, which gives the scheme
$$\begin{matrix} a & b & c & a & b \\ d & e & f & d & e \\ g & h & i & g & h \end{matrix}.$$
In this scheme the three positive terms are the products along the diagonals that go down to the right.
The three negative terms are the products along the diagonals that go up to the right.

## Remarks

### A first computation

Take the matrix
$$A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 2 \end{pmatrix}.$$
The three diagonals that go down to the right start at the entries $2$, $0$ and $1$ of the first row:
$$2 \cdot 3 \cdot 2 + 0 \cdot 2 \cdot 1 + 1 \cdot 1 \cdot 1 = 12 + 0 + 1 = 13.$$
The three diagonals that go up to the right start at the entries $1$, $1$ and $2$ of the last row:
$$1 \cdot 3 \cdot 1 + 1 \cdot 2 \cdot 2 + 2 \cdot 1 \cdot 0 = 3 + 4 + 0 = 7.$$
So $\det A = 13 - 7 = 6$.
Check by the [[Laplace expansion|0C08BQ3M05]] along the first row: $2 (3 \cdot 2 - 2 \cdot 1) - 0 + 1 (1 \cdot 1 - 3 \cdot 1) = 8 - 2 = 6$.
The [[rule of Sarrus as a method|7H2P40X0MV]] gives more examples, among them a [[matrix with negative entries|8XBS7KHJXK]].

### Why the rule is true

The [[Leibniz formula|016PE4VZ8Q]] writes a $3 \times 3$ determinant as a sum over the six permutations $\sigma$ of $\{1, 2, 3\}$:
$$\det A = \sum_{\sigma} \operatorname{sgn}(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)} a_{3 \sigma(3)}.$$
A diagonal that goes down to the right moves one column to the right in each row, so it uses a cyclic shift $\sigma(r) = r + k$, counted modulo $3$.
The three shifts are the identity and the two $3$-cycles, and each has [[sign|0SK90238BH]] $+1$.
A diagonal that goes up to the right uses a map $\sigma(r) = k - r$, counted modulo $3$, and the three such maps are the three transpositions, each with sign $-1$.
So the six diagonals give the six terms of the Leibniz formula, each once and with its correct sign.
For the term $bfg$, for example, the permutation is $1 \mapsto 2$, $2 \mapsto 3$, $3 \mapsto 1$, a $3$-cycle, so its sign is $+1$.

### Why the size must be three

The size is the hypothesis that matters, and a count shows why.
A $3 \times 3$ determinant has $3! = 6$ terms, and the scheme has exactly $6$ diagonals, so nothing is missed.
A $4 \times 4$ determinant has $4! = 24$ terms.
The same scheme for a $4 \times 4$ matrix, with three columns copied, has $4$ diagonals in each direction, so it lists only $8$ products, and $16$ terms of the determinant are lost.

A single matrix makes the failure concrete.
Let $P$ be the $4 \times 4$ [[permutation matrix|08SP3DF8NB]] that swaps the first two coordinates, with entries $p_{12} = p_{21} = p_{33} = p_{44} = 1$ and $0$ elsewhere.
Its determinant is $-1$, because it is the identity with two rows swapped.
Its only nonzero product of the Leibniz type is $p_{12} p_{21} p_{33} p_{44}$, and this product lies on none of the $8$ diagonals, since $1 \mapsto 2, 2 \mapsto 1, 3 \mapsto 3, 4 \mapsto 4$ is neither a cyclic shift nor of the form $r \mapsto k - r$.
So every diagonal product contains a zero, and the false scheme gives $0$ instead of $-1$.

### The commutative ring

The entries must commute, because the order of the three factors in a product is not fixed by the picture.
For quaternion entries, $ij = k$ but $ji = -k$, so the products along one diagonal can depend on the order in which we multiply.
Over every commutative ring, such as $\mathbb{Z}$, $\mathbb{R}$, $\mathbb{C}$ or a polynomial ring, the rule holds, because the Leibniz formula holds there.

### What it gives you

The rule turns every $3 \times 3$ determinant into twelve multiplications and five additions or subtractions.
For an upper triangular matrix, each diagonal except the main one meets a zero below the main diagonal, so the rule gives the product $a e i$ of the diagonal entries.
With entries in a polynomial ring, the rule gives the characteristic polynomial of a $3 \times 3$ matrix, and with the symbols $\mathbf{i}, \mathbf{j}, \mathbf{k}$ in the first row it gives the [[cross product|0N5N15HWZ7]].

### Watch out

An up diagonal is subtracted with its own sign.
If an up product is $(-2) \cdot 3 \cdot 1 = -6$, then subtracting it adds $6$ to the result.
A second slip is to copy the columns in the wrong order, for example column $2$ before column $1$, which changes the six products.

### Try it

First, compute $\det \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$.
The down products are $0$, $40$ and $0$, the up products are $15$, $24$ and $0$, so the determinant is $40 - 39 = 1$.

Second, explain why the same scheme for $2 \times 2$ matrices, with one column copied, always gives $0$.
The down products are $a_{11} a_{22}$ and $a_{12} a_{21}$, the up products are $a_{21} a_{12}$ and $a_{22} a_{11}$, and the two sums cancel.

## History

The rule is named after the French mathematician Pierre Frédéric Sarrus.

## Explanations

### L1 human

The rule of Sarrus is a quick way to compute a $3 \times 3$ determinant by hand.
Copy the first two columns again to the right of the matrix, so that you see five columns.
Multiply the three numbers on each of the three lines that go down to the right, and add the three results.
Do the same on the three lines that go up to the right, and subtract those three results.
For the identity matrix only the main diagonal has no zero, so the answer is $1$.

### L2 human

Here is a typical problem: for which $t$ is the matrix $\begin{pmatrix} 1 & 1 & 1 \\ 1 & t & 1 \\ 1 & 1 & t \end{pmatrix}$ not invertible?
The down products are $t^2$, $1$ and $1$, and the up products are $t$, $1$ and $t$.
Subtract the second sum from the first:
$$\det = t^2 + 2 - (2t + 1) = t^2 - 2t + 1 = (t - 1)^2.$$
So the matrix is singular exactly for $t = 1$.
Check: for $t = 1$ all three rows are $(1, 1, 1)$, so the rows are dependent and the determinant is $0$.
This is the typical use of the rule: a $3 \times 3$ determinant with a parameter, written out as a polynomial in one step.
The trap is to use the same picture for a $4 \times 4$ matrix, where it lists only $8$ of the $24$ terms.

### L3 human

The six diagonals are the six symmetries of a triangle with corners $1, 2, 3$: three rotations and three reflections, the dihedral group of order $6$.
For $n = 3$ this group is all of the symmetric group $S_3$, and its rotations are exactly the even permutations, so the picture is the Leibniz formula.
For $n \ge 4$ the dihedral group of order $2n$ is much smaller than $S_n$, which has $n!$ elements.
Its signs are also wrong in general, since the cyclic shift by one place is an $n$-cycle, which is odd when $n$ is even.
The general tools are the [[Laplace expansion|0C08BQ3M05]] and row reduction to a [[triangular matrix|0K1KKMFHYH]], which need about $n^3$ operations instead of the roughly $n! \cdot n$ of the Leibniz formula.
