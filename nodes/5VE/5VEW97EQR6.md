---
tag: 5VEW97EQR6
kind: example
name: An idempotent matrix whose powers never reach the identity
msc: [20A05, 20M99]
topics: [BAZT8JJ70S, Y1ESNQ2V52]
audience: ug1
instance_of: [0KCE8CG86P]
not_instance_of:
  - target: 0WE2NHZJ7B
    note: the matrix E with entries 1, 0, 0, 0 satisfies E^n = E for each positive n, but it is not invertible, so it is not an element of a group of matrices with the identity matrix as identity, and it has no order
uses: [0N5NJZKKN3, 0JXZKX526R, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: lead section
---

## Example

Let
$$E = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$
in the set $M_2(\mathbb{R})$ of real $2 \times 2$ [[square matrices|0JXZKX526R]].
We show that no power of $E$ equals $I$, and that $E$ has no [[order|0WE2NHZJ7B]] in the sense of group theory.

1. Multiply row by column:
$$E^2 = \begin{pmatrix} 1 \cdot 1 + 0 \cdot 0 & 1 \cdot 0 + 0 \cdot 0 \\ 0 \cdot 1 + 0 \cdot 0 & 0 \cdot 0 + 0 \cdot 0 \end{pmatrix} = E.$$
So $E$ is an [[idempotent element|0N5NJZKKN3]] of $M_2(\mathbb{R})$.
2. By [[induction|0ASJVEFA9J]], $E^n = E$ for each $n \ge 1$: the case $n = 1$ holds, and $E^n = E$ gives $E^{n+1} = E^n E = E E = E$ by step 1.
3. The entry $(2, 2)$ of $E$ is $0$ and that of $I$ is $1$, so $E \ne I$, and by step 2 also $E^n \ne I$ for every $n \ge 1$.
4. The [[determinant|00KDZRW4C0]] of $E$ is $1 \cdot 0 - 0 \cdot 0 = 0$, so $E$ is not invertible. Hence $E$ lies in no group of matrices whose identity element is $I$.
5. The order of an element is defined only for elements of a group. So $E$ has neither finite nor infinite order: the concept does not apply.

## Remarks

The set $\{E\}$ is a group under matrix multiplication, because $E E = E$.
In this tiny group the identity element is $E$, not $I$, and $E$ has order $1$.
So the order of an element depends on the group, and in particular on its identity element.

The example shows how a [[monoid|0N6R902FG1]] such as $M_2(\mathbb{R})$ differs from a group.
In a monoid, powers can repeat without ever reaching the identity, as $E^2 = E^1$ here.
In a group this cannot happen: if $g^a = g^b$ with $a < b$, cancelling $g^a$ gives $g^{b - a} = e$.
If we replace $E$ by $\operatorname{diag}(1, -1)$, which is invertible, the powers alternate between it and $I$, and the order is $2$.

## Explanations

### L1 human

Take the matrix $E$ and multiply it by itself.
The result is $E$ again, and it stays $E$ at every further step.
So the powers of $E$ never reach the identity matrix $I$.
This does not mean that $E$ has infinite order, because $E$ has no inverse, and order is defined only inside a group.

### L2 human

Compare $E$ with an element of a group whose powers repeat.
In the group $\{1, i, -1, -i\}$ of complex numbers, the powers of $i$ are $i, -1, -i, 1, i, \dots$, so $i^5 = i^1$.
Cancelling $i$ from $i \cdot i^4 = i \cdot 1$ gives $i^4 = 1$, so the repeat leads back to the identity.
For $E$ we also have a repeat, $E \cdot E = E \cdot I$, but we cannot cancel $E$, because $E$ has no inverse, and indeed $E \ne I$.
The typical use of the example is to show why the definition of order asks for a group.
Watch out: calling $E$ an element of infinite order is wrong, since $E$ is not in the group $\mathrm{GL}_2(\mathbb{R})$ at all.
