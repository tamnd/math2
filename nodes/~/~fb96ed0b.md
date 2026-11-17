---
tag: ~fb96ed0b
kind: example
name: The trivial solution of a homogeneous linear system
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [~f4ece120]
uses: [~f4ece120, 04KGXJG1A2, 0VD9ZSWWJG, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Triviality_(mathematics)
    locator: Examples
---

## Example

A [[homogeneous linear system|04KGXJG1A2]] is a system $A\mathbf{x} = \mathbf{0}$, where $A$ is a [[matrix|0VD9ZSWWJG]] and $\mathbf{0}$ is the zero vector.
Every such system has the solution $\mathbf{x} = \mathbf{0}$, because $A\mathbf{0} = \mathbf{0}$.
This solution is called the [[trivial|~f4ece120]] solution, and every other solution is called nontrivial.
Here "trivial" has an exact meaning, and we compare two systems.

1. Take the system $x + 2y = 0$ and $2x + 4y = 0$.
2. The second equation is $2$ times the first, so the system has the same solutions as $x + 2y = 0$ alone.
3. The pair $(x, y) = (0, 0)$ is the trivial solution.
4. The pair $(x, y) = (2, -1)$ is a nontrivial solution: $2 + 2 \cdot (-1) = 0$ and $2 \cdot 2 + 4 \cdot (-1) = 0$.
5. Now take the system $x + 2y = 0$ and $3x + 4y = 0$.
6. The first equation gives $x = -2y$. We put this into the second equation: $3(-2y) + 4y = -2y = 0$, so $y = 0$, and then $x = -2 \cdot 0 = 0$.
7. So the second system has only the trivial solution.

## Remarks

The example shows that "trivial" names one definite solution, and that the real question is whether a nontrivial solution exists.
For a square matrix $A$, the system $A\mathbf{x} = \mathbf{0}$ has a nontrivial solution exactly when the [[determinant|00KDZRW4C0]] of $A$ is $0$.
For the first system, $\det \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} = 4 - 4 = 0$.
For the second system, $\det \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = 4 - 6 = -2 \neq 0$.
The same language is used for differential equations: $y = 0$ is the trivial solution of $y' = y$, and $y = e^x$ is a nontrivial one.

## Explanations

### L1 human

The equations "$x + 2y = 0$" and "$2x + 4y = 0$" are both true when $x = 0$ and $y = 0$.
Any equations of this kind, with $0$ on the right, are true when every unknown is $0$.
Mathematicians call this answer the trivial solution, because it is always there and needs no work.
The interesting question is whether there is another answer, such as $x = 2$ and $y = -1$.

### L2 human

We decide whether $x - y = 0$ and $2x - 2y = 0$ has a nontrivial solution.

1. The second equation is $2$ times the first.
2. So every pair with $x = y$ is a solution, for example $(1, 1)$.
3. Since $(1, 1) \neq (0, 0)$, the system has a nontrivial solution.
4. The determinant check agrees: $\det \begin{pmatrix} 1 & -1 \\ 2 & -2 \end{pmatrix} = -2 + 2 = 0$.

The typical use of the trivial solution is in the definition of linear independence: vectors are independent when a linear combination equal to $\mathbf{0}$ has only the trivial solution.
A trap: "the system has a solution" is always true for a homogeneous system, so a proof must ask for a nontrivial solution.
