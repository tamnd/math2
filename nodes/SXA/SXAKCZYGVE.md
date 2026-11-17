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

Let $A$ be the [[Ackermann function|N470JF7ZJX]]: $A(0, n) = n + 1$, $A(m + 1, 0) = A(m, 1)$ and $A(m + 1, n + 1) = A(m, A(m + 1, n))$.
Then $A(1, n) = n + 2$, $A(2, n) = 2n + 3$ and $A(3, n) = 2^{n+3} - 3$, so $A(3, 2) = 29$.
Let $\varphi(m, n, y)$ be the $\Sigma_1$ formula "there is a finite table of values that contains $A(m, n) = y$, in which each entry follows from one of the three equations and other entries".

**$A$ is [[provably total|Z742YPHPNS]] in $\mathsf{PA}$.**

1. Let $\psi(m)$ be $\forall n\, \exists y\, \varphi(m, n, y)$. We prove $\forall m\, \psi(m)$ by induction on $m$ in $\mathsf{PA}$.
2. $\psi(0)$ holds, because the table with the single entry $A(0, n) = n + 1$ is correct by the first equation.
3. Assume $\psi(m)$. We prove $\exists y\, \varphi(m + 1, n, y)$ by an inner induction on $n$.
4. For $n = 0$: $\psi(m)$ gives a table with $A(m, 1) = y$. Add the entry $A(m + 1, 0) = y$.
5. For $n + 1$: the inner hypothesis gives a table with $A(m + 1, n) = z$, and $\psi(m)$ gives a table with $A(m, z) = y$.
6. Join the two tables and add $A(m + 1, n + 1) = y$, which follows from the third equation. So $\varphi(m + 1, n + 1, y)$ holds.
7. So $\psi(m + 1)$ holds, and by induction $\mathsf{PA} \vdash \forall m\, \psi(m)$.
8. The formula $\psi(m)$ is $\Pi_2$, so this proof uses induction beyond $\Sigma_1$. Full induction in $\mathsf{PA}$ allows it.

**$A$ is not provably total in $\mathrm{I}\Sigma_1$.**

1. The diagonal $g(n) = A(n, n)$ is not [[primitive recursive|5NVA2JRHPV]], by the [[theorem on the Ackermann function|97QF3KHSBY]].
2. **Cited theorem** (Parsons; Mints). Every function that is provably total in $\mathrm{I}\Sigma_1$ is primitive recursive.
3. If $A$ were provably total in $\mathrm{I}\Sigma_1$, then $g$ would be too, through the formula $\varphi(n, n, y)$.
4. Then $g$ would be primitive recursive by step 2, which contradicts step 1.

## Remarks

The outer induction in step 1 is on a $\Pi_2$ formula, and $\mathrm{I}\Sigma_1$ proves the same as $\mathrm{I}\Pi_1$ but has no $\Pi_2$ induction.
In fact $\mathrm{I}\Sigma_2$ proves that $A$ is total, since $\Pi_2$ induction is available there.
In the [[fast-growing hierarchy|R6ZC4BJGXV]] the diagonal $g$ grows like $f_\omega$.

## Explanations

### L1 human

The Ackermann function is defined by a double recursion, and each level grows much faster than the one before.
Ordinary arithmetic with full induction can prove that it always gives a value.
The weaker system $\mathrm{I}\Sigma_1$ cannot, because it can prove only primitive recursive functions total.

### L2 human

The proof of totality is a double induction: on $m$ outside and on $n$ inside.
The typical use of this example is to show that the strength of a theory depends on the complexity of the formulas allowed in induction.
The trap: the outer induction formula has the form "for all $n$ there is $y$", which is $\Pi_2$, and this is exactly what $\mathrm{I}\Sigma_1$ lacks.
