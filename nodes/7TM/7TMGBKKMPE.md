---
tag: 7TMGBKKMPE
kind: example
name: A polynomial of degree d has at most d roots, by induction on d
msc: ["12E05"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [B2D8PTFNN1]
uses: [B2D8PTFNN1, 0K3MWA7DMC, 0DPF6WRZW6, 00EHX6FWC0, 0QA8CHH8MG, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Factor_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Polynomial
    locator: Solving equations
---

## Example

Let $F$ be a [[field|0QA8CHH8MG]].
We prove that a nonzero polynomial $f \in F[x]$ of [[degree|0DPF6WRZW6]] $d$ has at most $d$ [[roots|00EHX6FWC0]] in $F$.
The proof is an [[induction on size|B2D8PTFNN1]], with the degree as the size.
Let $P(d)$ be the statement "every nonzero polynomial of degree $d$ over $F$ has at most $d$ roots in $F$".

1. Base case $d = 0$: a nonzero polynomial of degree $0$ is a constant $f = a$ with $a \neq 0$.
   Then $f(r) = a \neq 0$ for each $r \in F$, so $f$ has $0$ roots.
2. Induction step: let $d \ge 0$, assume $P(d)$, and let $f$ be an arbitrary nonzero polynomial of degree $d + 1$.
3. If $f$ has no root in $F$, then it has $0 \le d + 1$ roots, and $P(d + 1)$ holds for $f$.
4. Otherwise let $c \in F$ be a root of $f$.
   By the [[factor theorem|0K3MWA7DMC]], $f = (x - c)\, q$ for some $q \in F[x]$.
5. The factor $x - c$ has leading coefficient $1$, so the leading coefficient of $(x - c)\, q$ equals that of $q$, and $\deg f = 1 + \deg q$.
   Thus $q \neq 0$ and $\deg q = d$.
6. Let $r \in F$ be a root of $f$.
   Then $(r - c)\, q(r) = f(r) = 0$.
7. A field has no zero divisors: if $ab = 0$ and $a \neq 0$, then $b = a^{-1} a b = 0$.
   So $r - c = 0$ or $q(r) = 0$.
8. So each root of $f$ is $c$ or a root of $q$, and $q$ has at most $d$ roots by $P(d)$.
9. So $f$ has at most $1 + d$ roots, and $P(d + 1)$ holds.
10. By induction, $P(d)$ holds for every $d \ge 0$.

The bound can be reached.
Over $\mathbb{Q}$ the polynomial
$$x^3 - x = x(x - 1)(x + 1)$$
has degree $3$ and the $3$ roots $0$, $1$ and $-1$.

## Remarks

The reduction "factor out one root" lowers the degree by exactly $1$ and keeps the hypothesis "nonzero polynomial over $F$".
That is why the degree is the right size here.
Step 3 matters too: a polynomial with no root has no reduction, and the proof handles it directly.

The hypothesis "field" is used only in step 7, and it cannot be dropped.
Over the ring $\mathbb{Z}/8\mathbb{Z}$, the polynomial $x^2 - 1$ of degree $2$ has the $4$ roots $1$, $3$, $5$ and $7$, because $1$, $9$, $25$ and $49$ all leave the remainder $1$ on division by $8$.
At the root $3$ the product $(3 - 1)(3 + 1) = 8$ is $0$ in $\mathbb{Z}/8\mathbb{Z}$, but neither factor is $0$.
The same proof works over every integral domain, because step 7 uses only the absence of zero divisors.
The hypothesis "nonzero" is needed as well, since every element of $F$ is a root of the zero polynomial.

A consequence follows at once.
Two polynomials of degree at most $d$ over a field that agree at $d + 1$ distinct points are equal, since otherwise their difference is a nonzero polynomial of degree at most $d$ with $d + 1$ roots.

## Explanations

### L1 human

A polynomial of degree $2$, such as $x^2 - 5x + 6$, can be zero at no more than $2$ numbers.
Here these numbers are $2$ and $3$.
The reason is that each zero lets us split off a factor, here $x^2 - 5x + 6 = (x - 2)(x - 3)$.
Each factor uses up one degree.
When all the degree is used up, nothing is left that could be zero, so there are no more zeros.

### L2 human

We follow the proof for $f = x^3 - 2x^2 - x + 2$ over $\mathbb{Q}$.
Test $c = 1$: $f(1) = 1 - 2 - 1 + 2 = 0$, so $1$ is a root.
Division by $x - 1$ gives the factorization
$$f = (x - 1)(x^2 - x - 2).$$
The quotient $q = x^2 - x - 2$ has degree $2$, so the induction hypothesis says that it has at most $2$ roots.
Indeed $q = (x - 2)(x + 1)$, with the roots $2$ and $-1$.
So the roots of $f$ are among $1$, $2$ and $-1$, and all three are roots.

Check: $(x - 1)(x^2 - x - 2) = x^3 - x^2 - 2x - x^2 + x + 2 = x^3 - 2x^2 - x + 2$.
The typical use of the result is the uniqueness of polynomial interpolation, and the bound of $n$ on the number of $n$th roots of unity in a field.
Watch out: over a ring with zero divisors, such as $\mathbb{Z}/8\mathbb{Z}$, the bound fails.
