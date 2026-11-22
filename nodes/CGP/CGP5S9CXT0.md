---
tag: CGP5S9CXT0
kind: example
name: The products of the 2 × 2 matrix units
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [A4HTT7JFD1]
illustrates: [E66YRYVWQ3]
uses: [4H93XF4RVH, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: Properties
---

## Example

The $2 \times 2$ [[matrix units|4H93XF4RVH]] are
$$E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad E_{21} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad E_{22} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.$$
We compute five products directly and compare each with the rule $E_{ij} E_{kl} = \delta_{jk} E_{il}$.

1. First,
$$E_{12} E_{21} = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot 0 + 1 \cdot 0 \\ 0 \cdot 0 + 0 \cdot 1 & 0 \cdot 0 + 0 \cdot 0 \end{pmatrix} = E_{11},$$
and the rule gives $\delta_{22} E_{11} = E_{11}$.
2. In the other order,
$$E_{21} E_{12} = \begin{pmatrix} 0 \cdot 0 + 0 \cdot 0 & 0 \cdot 1 + 0 \cdot 0 \\ 1 \cdot 0 + 0 \cdot 0 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = E_{22},$$
and the rule gives $\delta_{11} E_{22} = E_{22}$.
3. A square:
$$E_{12} E_{12} = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = 0,$$
and the rule gives $\delta_{21} E_{12} = 0$.
4. Next,
$$E_{11} E_{12} = \begin{pmatrix} 1 \cdot 0 + 0 \cdot 0 & 1 \cdot 1 + 0 \cdot 0 \\ 0 & 0 \end{pmatrix} = E_{12},$$
and the rule gives $\delta_{11} E_{12} = E_{12}$.
5. In the other order,
$$E_{12} E_{11} = \begin{pmatrix} 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = 0,$$
and the rule gives $\delta_{21} E_{11} = 0$.

## Remarks

The [[product rule|E66YRYVWQ3]] gives all $16$ products of two $2 \times 2$ matrix units without computation.
Steps 1 and 2 show that $E_{12}$ and $E_{21}$ do not commute, and steps 4 and 5 show that $E_{11}$ and $E_{12}$ do not commute either.
Step 3 shows a nonzero matrix whose square is $0$, so $E_{12}$ is nilpotent.
In contrast, $E_{11} E_{11} = \delta_{11} E_{11} = E_{11}$, so $E_{11}$ is idempotent.

## Explanations

### L1 human

Two matrix units multiply to a matrix unit when the inner indices match, and to zero otherwise.
In step 1 the inner indices are $2$ and $2$, so the product is the matrix unit with the outer indices, $E_{11}$.

### L2 human

Steps 1 and 2 give the commutator
$$E_{12} E_{21} - E_{21} E_{12} = E_{11} - E_{22} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$
Its trace is $1 - 1 = 0$, as for every commutator, since $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
Watch out: the rule only reads the inner indices $j$ and $k$; in step 5 the outer indices $1$ and $1$ agree, but the inner ones, $2$ and $1$, do not, so the product is $0$.
