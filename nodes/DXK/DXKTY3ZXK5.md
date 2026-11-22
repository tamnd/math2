---
tag: DXKTY3ZXK5
kind: example
name: The 2 × 3 zero matrix as the identity for addition
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0ZTKJJDGR7]
uses: [4KY5AWGMW5, 0BVXADM10P, 0K28YXMS7Q]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_matrix
    locator: Properties
---

## Example

We check, with one concrete matrix, that the zero matrix of the right size behaves like the number $0$ for addition.
Let
$$A = \begin{pmatrix} 1 & -2 & 0 \\ 3 & 5 & -1 \end{pmatrix}, \qquad 0 = 0_{2 \times 3} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$

1. By the rule for [[matrix addition|0BVXADM10P]], we add matching entries:
$$A + 0 = \begin{pmatrix} 1 + 0 & -2 + 0 & 0 + 0 \\ 3 + 0 & 5 + 0 & -1 + 0 \end{pmatrix} = A.$$
2. Addition of numbers is commutative, so each entry of $0 + A$ is $0 + a_{ij} = a_{ij}$, and $0 + A = A$.
3. The negative of $A$ has the entries $-a_{ij}$:
$$-A = \begin{pmatrix} -1 & 2 & 0 \\ -3 & -5 & 1 \end{pmatrix}, \qquad A + (-A) = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = 0.$$
4. By the rule for [[scalar multiplication|0K28YXMS7Q]], the scalar $0$ times $A$ has the entries $0 \cdot a_{ij} = 0$, so $0 \cdot A = 0_{2 \times 3}$.
5. The $2 \times 2$ zero matrix does not work here. The sum $A + 0_{2 \times 2}$ is not defined, because $A$ has 3 columns and $0_{2 \times 2}$ has 2.

## Remarks

Steps 1 to 3 are the vector space rules for the zero vector and for negatives, checked entry by entry.
So the [[zero matrix|4KY5AWGMW5]] $0_{2 \times 3}$ is the zero vector of the [[space of 2 × 3 matrices|0RE6X3BGPN]].
Step 5 shows that this zero vector depends on the size: each space $M_{m \times n}(R)$ has its own.

In step 4 the symbol $0$ appears twice with two meanings.
On the left it is the scalar $0$, and on the right it is the matrix $0_{2 \times 3}$.
If we replace the scalar $0$ by any other number $c$, the product $cA$ is the zero matrix only when $c = 0$, because the entry $a_{11} = 1$ becomes $c$.

## Explanations

### L1 human

Adding a table of zeros to a table of the same size changes nothing.
Every matrix also has a negative, made by changing the sign of each entry.
A matrix plus its negative is the table of zeros.

### L2 human

The rules in steps 1 to 3 hold for every size, and the proof is always the same one line: each entry is a sum of numbers, and $a + 0 = a$ and $a + (-a) = 0$ for numbers.
The typical use is in solving matrix equations, as with numbers.
From $X + A = B$ we add $-A$ to both sides and get $X = B - A$.
The trap is to write a zero matrix of the wrong size, which makes the sum undefined.
