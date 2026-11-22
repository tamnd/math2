---
tag: FSXBBV9C76
kind: statement
role: theorem
name: The composite of linear maps is linear
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [00BKRZKMSS]
uses: [05YBKMRVAR, 0RJF668P1T, 0CCQV3884B, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
  - book: isbn:9780134860244
    locator: Section 2.3
  - book: isbn:9780321982384
    locator: Section 2.1
---

## Statement

The theorem says that doing two linear maps in a row gives a linear map, and that for matrix maps the result is multiplication by the product matrix.
Let $F$ be a field.

1. Let $U$, $V$ and $W$ be vector spaces over $F$, and let $S \colon U \to V$ and $T \colon V \to W$ be [[linear maps|0RJF668P1T]]. Then the [[composite|05YBKMRVAR]] $T \circ S \colon U \to W$ is linear.
2. Let $A$ be an $m \times n$ matrix and $B$ an $n \times p$ matrix over $F$, with $T_A(y) = Ay$ and $T_B(x) = Bx$. Then $T_A \circ T_B = T_{AB}$, where $AB$ is the [[matrix product|076JGP6R3T]].

## Remarks

### Why the hypotheses are needed

Part 1 needs both maps to be linear.
For $S(x) = x + 1$ and $T(x) = 2x$ on $\R$, the composite sends $0$ to $T(1) = 2$, so it is not linear.
On the other hand, two non-linear maps can still have a linear composite: for $S(x) = x^3$ and $T(x) = \sqrt[3]{x}$ on $\R$, the composite $T \circ S$ is the identity.
So the converse of part 1 is false.
Part 2 needs the sizes to match, with as many columns in $A$ as rows in $B$, since $T_A$ must accept the outputs of $T_B$.

### A worked use

Let $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, the rotation by a right angle, and $B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, the reflection in the $x$-axis.
Part 2 says that "reflect, then rotate" is multiplication by
$$AB = \begin{pmatrix} 0 \cdot 1 + (-1) \cdot 0 & 0 \cdot 0 + (-1)(-1) \\ 1 \cdot 1 + 0 \cdot 0 & 1 \cdot 0 + 0 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},$$
which is the reflection in the line $y = x$.
Check on $e_1$: $B e_1 = (1, 0)$ and $A(1, 0) = (0, 1)$, which is the first column of $AB$.
The [[rotation and reflection example|W9GA3QFG24]] also works out the other order.

### What it gives you

Linear maps can be composed in any number, and the result is linear, so the powers $T^k$ of a linear map $T \colon V \to V$ are linear.
Part 2, together with the associativity of composition of functions, gives the associativity of matrix multiplication, as in the [[proof by composition|KC9SCPKS2G]].
For any bases of finite-dimensional spaces, the [[matrix of a composite is the product of the matrices|05Q1B7MH0M]].
The same statement holds for homomorphisms of modules over a ring and for [[group homomorphisms|0JYTG5K9Y4]], with the same proof.

## History

Cayley defined the product of matrices in his memoir of 1858 so that part 2 holds, as a way to describe two linear substitutions of variables done one after the other.

## Explanations

### L1 human

If two maps each respect sums and scalar multiples, then doing one after the other also respects them.
For matrix maps, doing $B$ and then $A$ is the same as multiplying by the single matrix $AB$.
For example, stretching by $2$ and then by $3$ is the same as stretching by $6$.

### L2 human

Here is a typical use: show that $x \mapsto A(Bx + Cx)$ is linear, for matrices of matching sizes.
The map $x \mapsto Bx + Cx$ is $T_{B + C}$, which is linear by the [[theorem on matrix transformations|W6KB0J3SZZ]].
Part 1 then shows that $T_A \circ T_{B + C}$ is linear, and part 2 identifies it as $T_{A(B + C)}$.
So no new check of the two conditions is needed.
Watch out for the order: $T_A \circ T_B$ is $T_{AB}$ and not $T_{BA}$.
