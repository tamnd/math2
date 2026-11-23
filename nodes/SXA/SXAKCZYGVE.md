---
tag: SXAKCZYGVE
kind: example
name: The Ackermann function is provably total in PA but not in IΣ1
msc: ["03F30", "03D20"]
topics: [T6FK1E7GJ1]
audience: grad
instance_of: [Z742YPHPNS]
uses: [Z742YPHPNS, N470JF7ZJX, 97QF3KHSBY, MPSCREYC3M, 1QD0KDDGYJ, 5NVA2JRHPV]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_function
    locator: Relationship to recursive functions
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_function
    locator: Limitations
---

## Example

The Ackermann function is the standard case of a function whose totality needs more induction than $\mathrm{I}\Sigma_1$ has, but no more than $\mathsf{PA}$ has.
Let $A$ be the [[Ackermann function|N470JF7ZJX]], given by three equations:
$$A(0, n) = n + 1, \qquad A(m + 1, 0) = A(m, 1), \qquad A(m + 1, n + 1) = A(m, A(m + 1, n)).$$

**First values.**
Row $0$ adds one, so $A(1, 0) = A(0, 1) = 2$ and $A(1, 1) = A(0, A(1, 0)) = A(0, 2) = 3$.
In general $A(1, n) = n + 2$.
Row $2$ starts with $A(2, 0) = A(1, 1) = 3$, and each step applies $A(1, \cdot)$:
$$A(2, 1) = A(1, 3) = 5, \qquad A(2, 2) = A(1, 5) = 7, \qquad A(2, n) = 2n + 3.$$
Row $3$ starts with $A(3, 0) = A(2, 1) = 5$, and each step applies $n \mapsto 2n + 3$:
$$A(3, 1) = A(2, 5) = 13, \qquad A(3, 2) = A(2, 13) = 29, \qquad A(3, 3) = A(2, 29) = 61.$$
So $A(3, n) = 2^{n+3} - 3$; check: $2^5 - 3 = 29$.
Row $4$ starts with $A(4, 0) = A(3, 1) = 13$ and $A(4, 1) = A(3, 13) = 2^{16} - 3 = 65533$.

Let $\varphi(m, n, y)$ be the $\Sigma_1$ formula "there is a finite table of values that contains $A(m, n) = y$, in which each entry follows from one of the three equations and earlier entries".

**$A$ is [[provably total|Z742YPHPNS]] in $\mathsf{PA}$.**

1. Let $\psi(m)$ be $\forall n\, \exists y\, \varphi(m, n, y)$.
   We prove $\forall m\, \psi(m)$ by induction on $m$ in $\mathsf{PA}$.
2. $\psi(0)$ holds, because the table with the single entry $A(0, n) = n + 1$ is correct by the first equation.
3. Assume $\psi(m)$.
   We prove $\forall n\, \exists y\, \varphi(m + 1, n, y)$ by an inner induction on $n$.
4. For $n = 0$, $\psi(m)$ gives a table with $A(m, 1) = y$, and we add the entry $A(m + 1, 0) = y$ by the second equation.
5. For $n + 1$, the inner hypothesis gives a table with $A(m + 1, n) = z$, and $\psi(m)$ gives a table with $A(m, z) = y$.
6. We join the two tables and add $A(m + 1, n + 1) = y$, which follows from the third equation.
   So $\exists y\, \varphi(m + 1, n + 1, y)$ holds.
7. So $\psi(m + 1)$ holds, and by induction $\mathsf{PA} \vdash \forall m\, \psi(m)$.
8. The formula $\psi(m)$ is $\Pi_2$, so the outer induction is an induction on a $\Pi_2$ formula.
   The full induction schema of $\mathsf{PA}$ allows it.

**$A$ is not provably total in $\mathrm{I}\Sigma_1$.**

1. The diagonal $g(n) = A(n, n)$ is not [[primitive recursive|5NVA2JRHPV]], by the [[theorem on the Ackermann function|97QF3KHSBY]].
2. **Cited theorem** (Parsons; Mints).
   Every function that is provably total in $\mathrm{I}\Sigma_1$ is primitive recursive.
3. If $A$ were provably total in $\mathrm{I}\Sigma_1$ through some $\Sigma_1$ formula, then $g$ would be provably total too, through the same formula with $m = n$.
4. Then $g$ would be primitive recursive by step 2, which contradicts step 1.

## Remarks

The example shows that the strength of a theory of arithmetic depends on the complexity of the formulas that induction may use.
The inner induction in step 3 is on a $\Sigma_1$ formula, and $\mathrm{I}\Sigma_1$ could do it for each fixed $m$.
What fails is the outer induction on the $\Pi_2$ formula $\psi(m)$.
$\mathrm{I}\Sigma_1$ proves the same theorems as $\mathrm{I}\Pi_1$, and neither has induction for $\Pi_2$ formulas.

Raise the theory by one level and the picture changes.
$\mathrm{I}\Sigma_2$ proves that $A$ is total, since it proves induction for $\Pi_2$ formulas.
Fix the first argument instead, and each row $n \mapsto A(m, n)$ is primitive recursive, so $\mathrm{I}\Sigma_1$ proves each single row total.
In the [[fast-growing hierarchy|R6ZC4BJGXV]] row $m$ grows at about the rate of $f_{m-1}$.
Row $2$ is $2n + 3$, close to $f_1(n) = 2n$, and row $3$ is $2^{n+3} - 3$, close to $f_2(n) = n \cdot 2^n$.
So the diagonal $g$ grows like $f_\omega$.

## Explanations

### L1 human

The Ackermann function is built in rows, and each row repeats the row before it.
Row $1$ adds two, row $2$ roughly doubles, row $3$ takes powers of two, and row $4$ already sends $1$ to $65533$.
Ordinary arithmetic with full induction can prove that every row gives an answer for every input.
The weaker system $\mathrm{I}\Sigma_1$ can prove this for each row separately, but not for all rows at once.

### L2 human

We find $A(2, 3)$ with a table, as the formula $\varphi$ asks.
The table needs $A(2, 2) = 7$, then the third equation gives $A(2, 3) = A(1, A(2, 2)) = A(1, 7)$.
Row $1$ gives $A(1, 7) = 9$, so $A(2, 3) = 9$, which matches $2 \cdot 3 + 3$.
To find $A(3, 1) = A(2, A(3, 0)) = A(2, 5)$, the table needs row $2$ up to $n = 5$, and row $2$ needs row $1$ up to $n = 11$.
Each new row needs many entries of the row below, and this is exactly the outer induction on $m$.
The example shows the typical use: it separates $\mathrm{I}\Sigma_1$ from $\mathrm{I}\Sigma_2$ and $\mathsf{PA}$ by one concrete function.
