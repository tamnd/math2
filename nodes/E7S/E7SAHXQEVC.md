---
tag: E7SAHXQEVC
kind: statement
role: proposition
name: Linear systems as vector equations
msc: [15A06]
topics: [DXSXFVDMXQ]
audience: school
uses: [0PDVQEP0ZC, 0V8F3E48E6, 0T6MWGZSXA, 0GT4WWGWH2, 0DTY8B9HMS]
proofs: [8A7X3ZSNHB]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-2.xml#L901
    locator: src/section2-2.xml:901
  - book: isbn:9780321982384
    locator: Section 1.4
---

## Statement

A linear system can be read across its rows as equations or down its columns as one vector equation, and both readings ask the same question.
Let $F$ be a field, and let $A$ be an $m \times n$ matrix over $F$ with columns $v_1, \dots, v_n$.
Let $x = (x_1, \dots, x_n)^{\mathsf{T}}$ be a column vector with $n$ entries, and let $b$ be a column vector with $m$ entries.

Then the following three statements are equivalent.

1. The vector $x$ satisfies the equation $Ax = b$, using the [[matrix-vector product|0PDVQEP0ZC]].
2. The vector $b$ is the [[linear combination|0V8F3E48E6]] $x_1 v_1 + \dots + x_n v_n$ of the columns of $A$, with the entries of $x$ as weights.
3. The entries $x_1, \dots, x_n$ form a solution of the [[linear system|0GT4WWGWH2]] whose [[augmented matrix|0T6MWGZSXA]] is $[v_1 \; \dots \; v_n \mid b]$.

So the system with augmented matrix $[A \mid b]$ is consistent if and only if $b$ is in the [[span|0DTY8B9HMS]] of the columns of $A$, that is, in the column space of $A$.

## Remarks

### A small case

The system $x + 2y = 5$, $3x + 4y = 11$ asks for $x$ and $y$ with $x(1, 3) + y(2, 4) = (5, 11)$.
The answer $x = 1$, $y = 2$ gives $(1, 3) + (4, 8) = (5, 11)$, and also $1 + 4 = 5$ and $3 + 8 = 11$ in the row reading.

### Why each hypothesis is needed

The number of entries of $x$ must equal the number $n$ of columns of $A$, since otherwise $Ax$ is not defined.
The vector $b$ must have $m$ entries, one for each equation, since otherwise $Ax = b$ compares vectors of different sizes.
The field can be any field, and the proof uses only the rules of addition and multiplication in $F$, so the result holds over any commutative ring in the same way.

### What follows

The equation $Ax = b$ has a solution for every $b \in F^m$ if and only if the columns of $A$ span $F^m$.
The homogeneous equation $Ax = 0$ has only the solution $x = 0$ if and only if the columns of $A$ are linearly independent.
So every linear system has three equivalent forms: a list of equations, a vector equation, and a matrix equation.
The consistency criterion works in both directions: if $b$ is a combination of the columns, its weights solve the system.

### Many right sides

For an $m \times n$ matrix $A$ and an $n \times p$ matrix $X$, column $j$ of $AX$ is $A$ times column $j$ of $X$.
So the matrix equation $AX = B$ is $p$ systems with the same coefficient matrix, one for each column of $B$.

### Names for the forms

Lay calls the form $x_1 v_1 + \dots + x_n v_n = b$ a vector equation and $Ax = b$ a matrix equation.

## Explanations

### L1 human

A system of equations can be read row by row, one equation at a time.
It can also be read column by column: we look for numbers that combine the columns into the right side.
For example, $x + 2y = 5$ and $3x + 4y = 11$ ask for $x$ and $y$ with $x(1, 3) + y(2, 4) = (5, 11)$.

### L2 human

We test whether $b = (3, 5, 1)$ is a combination of $v_1 = (1, 2, 0)$ and $v_2 = (1, 1, 1)$.

1. By the statement, this is the question whether the system $x_1 + x_2 = 3$, $2x_1 + x_2 = 5$, $x_2 = 1$ is consistent.
2. The third equation gives $x_2 = 1$.
3. The first equation then gives $x_1 = 2$.
4. The second equation reads $4 + 1 = 5$, which is true.
5. So $b = 2v_1 + v_2$, and indeed $(2, 4, 0) + (1, 1, 1) = (3, 5, 1)$.

The typical use is to turn a question about spans into a linear system that row reduction can answer.
Watch out: the weights are the unknowns, and the vectors are the columns of the matrix, not its rows.

### L3 human

The statement says that the map $x \mapsto Ax$ is the [[linear map|0NRYHJPQG2]] $F^n \to F^m$ that sends $e_j$ to $v_j$.
So its image is the column space, and the solution set of $Ax = b$ is the preimage of $b$.
Questions about systems become questions about linear maps, and conversely.
