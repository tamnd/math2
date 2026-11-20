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

Let $F$ be a field.

1. Let $U$, $V$, $W$ be vector spaces over $F$, and let $S \colon U \to V$ and $T \colon V \to W$ be [[linear maps|0RJF668P1T]]. Then the [[composite|05YBKMRVAR]] $T \circ S \colon U \to W$ is linear.
2. Let $A$ be an $m \times n$ matrix and $B$ an $n \times p$ matrix over $F$. Let $T_A(y) = Ay$ and $T_B(x) = Bx$. Then $T_A \circ T_B = T_{AB}$, where $AB$ is the [[matrix product|076JGP6R3T]].

## Remarks

### Why each hypothesis is needed

- Part 1 needs both maps linear. For $S(x) = x + 1$ and $T(x) = 2x$ on $\R$, $T \circ S$ sends $0$ to $2$, so it is not linear.
- The composite of two non-linear maps can still be linear: for $S(x) = x^3$ and $T(x) = \sqrt[3]{x}$ on $\R$, $T \circ S$ is the identity.
- Part 2 needs the sizes to match: the number of columns of $A$ must equal the number of rows of $B$.

### Consequences

- Linear maps can be composed in any number, and the result is linear.
- The powers $T^k$ of a linear map $T \colon V \to V$ are linear.
- Part 2 and associativity of composition give associativity of matrix multiplication, as in the [[proof by composition|KC9SCPKS2G]].

### Converse

The converse of part 1 is false, by the cube and cube-root example above.

### Generalizations

- For any bases, the [[matrix of a composite is the product of the matrices|05Q1B7MH0M]].
- The same statement holds for homomorphisms of modules over a ring, and for [[group homomorphisms|0JYTG5K9Y4]].

## History

Cayley defined the product of matrices in 1858 so that part 2 holds.
His aim was to describe two linear substitutions of variables done one after the other.

## Explanations

### L1 human

If two maps each respect sums and scalar multiples, then doing one after the other also respects them.
For matrix maps, doing $B$ and then $A$ is the same as multiplying by the single matrix $AB$.

### L2 human

Let $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, the rotation by a right angle, and $B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, the reflection in the $x$-axis.

1. $AB = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the reflection in the line $y = x$.
2. Check on $e_1$: $B e_1 = (1, 0)$ and $A(1, 0) = (0, 1)$, which is the first column of $AB$.

The trap is the order: $T_A \circ T_B$ is $T_{AB}$ and not $T_{BA}$.
