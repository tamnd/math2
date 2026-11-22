---
tag: KZD8TFB85C
kind: example
name: Over F₂ there are 2 × 2 matrices with AB − BA = I
msc: ["15A15", "15A27"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0PXW0BN7DW]
uses: [076JGP6R3T, E2P5TNE0G9]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a product
---

## Example

In a field where $1 + 1 = 0$ the trace argument breaks down, and the identity becomes a commutator.
Work over the field $\mathbb{F}_2 = \{0, 1\}$, where $-1 = 1$.
Let
$$A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}.$$

1. The [[product|076JGP6R3T]] in one order is
$$AB = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot 0 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}.$$
2. In the other order it is
$$BA = \begin{pmatrix} 0 & 0 \\ 1 \cdot 0 + 0 \cdot 0 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.$$
3. The difference is
$$AB - BA = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2,$$
because $-1 = 1$ in $\mathbb{F}_2$.
4. The trace check is consistent: $\operatorname{tr}(AB - BA) = 0$ and $\operatorname{tr} I_2 = 1 + 1 = 0$ in $\mathbb{F}_2$.
5. So $A$ and $B$ do not [[commute|8G3X8MPG7E]], and their [[commutator|0PXW0BN7DW]] is the identity.

## Remarks

### Where the matrices come from

Over $\mathbb{Q}$ the same matrices give $AB - BA = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \neq I_2$, in line with the [[theorem|E2P5TNE0G9]].
On $\mathbb{F}_2[x]/(x^2)$ with basis $1, x$, the derivative sends $1 \mapsto 0$ and $x \mapsto 1$, so its matrix is $A$.
Multiplication by $x$ sends $1 \mapsto x$ and $x \mapsto x^2 = 0$, so its matrix is $B$.
For a prime $p$, the same construction on $\mathbb{F}_p[x]/(x^p)$ gives $p \times p$ solutions.

### Watch out

The example does not contradict the theorem, which assumes characteristic $0$.
Over $\mathbb{F}_2$ there is still no $1 \times 1$ or $3 \times 3$ solution, since then $\operatorname{tr} I_n = n \cdot 1 = 1 \neq 0$.

## Explanations

### L1 human

In a number system where $1 + 1 = 0$, the identity matrix of size $2$ has trace $0$.
Then the trace argument does not apply, and a solution exists.

### L2 human

The theorem uses only $\operatorname{tr} I_n = n \cdot 1 \neq 0$.
When the characteristic divides $n$, this step fails, and this example shows that the conclusion fails too.
So the hypothesis on the characteristic cannot be dropped.
