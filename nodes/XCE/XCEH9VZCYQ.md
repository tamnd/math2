---
tag: XCEH9VZCYQ
kind: example
name: Equations between ring terms are atomic formulas
msc: ["03B10", "08B05"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [MCZRXR3SVB]
uses: [MCZRXR3SVB, BP6WW7H5CC, 6D3WA7N2W4, 0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Atomic_formula
    locator: lead section
---

## Example

An algebraic identity such as the distributive law is, in logic, one atomic formula, however long its two sides are.
Let $\sigma = \{ +, \cdot, -, 0, 1 \}$ be the signature of [[rings|0B1261B5ED]], and let $\varphi$ be the string
$$x \cdot (y + 1) = x \cdot y + x.$$
We check that $\varphi$ is an [[atomic formula|MCZRXR3SVB]] and find where it is true.

1. The strings $x \cdot (y + 1)$ and $x \cdot y + x$ are [[terms|6D3WA7N2W4]] of $\sigma$, built from $x$, $y$ and $1$ by $+$ and $\cdot$.
2. The string $\varphi$ is $t_1 = t_2$ for these two terms, so it is atomic by form 1 of the [[definition|BP6WW7H5CC]].
3. The variables of $\varphi$ are $x$ and $y$, and both are free, so $\varphi$ is a formula with two free variables and not a sentence.
4. In the ring $\mathbb{Z}$, the distributive law gives, for all integers $x$ and $y$,
   $$x \cdot (y + 1) = x \cdot y + x \cdot 1 = x \cdot y + x.$$
5. So $\varphi$ holds in $\mathbb{Z}$ under every assignment of values to $x$ and $y$.
   Check: at $x = 2$ and $y = 5$ both sides are $12$.

So an equation between terms is atomic, and its truth depends on the structure and on the values of the variables.

## Remarks

Some atomic equations hold in one ring and fail in another.
The formula $x \cdot y = y \cdot x$ holds in $\mathbb{Z}$ under every assignment, but it fails in the ring of $2 \times 2$ real matrices for some pairs, as the L2 explanation shows.
By contrast $\varphi$ holds in every ring, because it follows from distributivity and the axiom $x \cdot 1 = x$.

The universal closure $\forall x \, \forall y \, \varphi$ is a sentence, and it is true in every ring.
Identities of this kind are the subject of equational logic, and a class of structures defined by universal closures of equations is a variety, such as the class of rings or of groups.
The negation $\neg (x \cdot y = y \cdot x)$ is not atomic, but it is a literal and quantifier-free.

## Explanations

### L1 human

An equation between two expressions, such as $x \cdot (y + 1) = x \cdot y + x$, is an atomic formula.
It has no "and", "not" or "for all" in it.
In the integers it is true for every choice of $x$ and $y$.
For $x = 2$ and $y = 5$ both sides are $12$.

### L2 human

We show that $x \cdot y = y \cdot x$ fails in the ring of $2 \times 2$ real matrices.
Take
$$A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}.$$
Multiply rows by columns:
$$A B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad B A = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.$$
So the atomic formula fails with $x = A$ and $y = B$.
The typical use of atomic equations is to state algebraic identities, such as the ring axioms.
Watch out: an atomic formula with free variables is neither true nor false until the variables have values.
