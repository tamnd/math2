---
tag: KMVW45B0TT
kind: statement
role: theorem
name: Hermite–Minkowski theorem
msc: [11R29, 11R21]
uses: [MWBDFS2KJ5, E0VZTNPJXA, 1TQ2F9CFVE, H5RC67SD24, 0K387S2PKQ, WWCJ7CR2R3]
about: [E0VZTNPJXA]
sources:
  - url: https://en.wikipedia.org/wiki/Discriminant_of_an_algebraic_number_field
---

## Statement

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] of degree $n \ge 2$ with [[discriminant|E0VZTNPJXA]] $d_K$.
Let $r_2$ be the number of pairs of complex conjugate embeddings of $K$.

1. (Minkowski) The discriminant satisfies
$$\abs{d_K} \ge \left(\frac{\pi}{4}\right)^{2 r_2} \left(\frac{n^n}{n!}\right)^2 > 1.$$
In particular $\abs{d_K} \ge 3$, and some prime number [[ramifies|H5RC67SD24]] in $K$.
2. (Hermite) For each real number $D$, there are only finitely many number fields $K \subset \C$ with $\abs{d_K} \le D$.

## Remarks

Part 1 follows from the [[Minkowski bound|1TQ2F9CFVE]]: every ideal class contains a nonzero integral ideal of norm at least $1$ and at most $M_K$, so $M_K \ge 1$.
Since $2 r_2 \le n$ and $\pi/4 < 1$, the right side is at least $(\pi/4)^n (n^n/n!)^2$, which is $\pi^2/4 > 2$ for $n = 2$ and increases with $n$.
A prime $p$ ramifies in $K$ exactly when $p$ divides $d_K$, so $\abs{d_K} > 1$ gives a ramified prime.

For part 2, the bound of part 1 first bounds the degree $n$.
Then [[Minkowski's theorem|0K387S2PKQ]] on convex bodies gives a primitive element of $K$ whose conjugates are bounded in terms of $D$.
So its minimal polynomial has bounded integer coefficients, and there are finitely many such polynomials.

Example: $\Q(\sqrt{-3})$ has $\abs{d_K} = 3$, so the bound $\abs{d_K} \ge 3$ for $n = 2$ is sharp.

## Explanations

### L1 human

Every number field other than $\Q$ has a discriminant of absolute value larger than $1$.
So in every proper extension of $\Q$ some prime number breaks into repeated factors.
Also, only finitely many number fields have a discriminant below a given size.

### L2 human

Part 1 says that $\Q$ has no nontrivial extension that is unramified at all primes.
Many other number fields do have such extensions, and the abelian ones are described by the [[Hilbert class field|WWCJ7CR2R3]].
Part 2 makes tables of number fields ordered by discriminant possible, since each range contains finitely many fields.
