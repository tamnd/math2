---
tag: SXNWHN2C01
kind: statement
role: theorem
name: Resolvent as Laplace transform of a semigroup
msc: [47D06, 47A10, 44A10]
uses: [0BDTTM24DP, EVF180QJXY, 60HSWZBTK9, X0243CZD9D, 0V49JEZW06]
about: [EVF180QJXY, J5YNNKSB9P]
sources:
  - url: https://en.wikipedia.org/wiki/C0-semigroup
---

## Statement

Let $X$ be a complex [[Banach space|0BDTTM24DP]], and let $(T(t))_{t \ge 0}$ be a [[$C_0$-semigroup|EVF180QJXY]] on $X$ with [[generator|60HSWZBTK9]] $A$.
Let $M \ge 1$ and $\omega \in \R$ be constants with $\norm{T(t)} \le M e^{\omega t}$ for all $t \ge 0$.
Then every complex $\lambda$ with $\operatorname{Re} \lambda > \omega$ lies in the [[resolvent set|X0243CZD9D]] of $A$, and for every $x \in X$,
$$(\lambda I - A)^{-1} x = \int_0^\infty e^{-\lambda t} \, T(t) x \, dt = \lim_{r \to \infty} \int_0^r e^{-\lambda t} \, T(t) x \, dt.$$
Moreover $\norm{(\lambda I - A)^{-1}} \le M / (\operatorname{Re} \lambda - \omega)$.

## Remarks

Constants $M$ and $\omega$ as above exist for every $C_0$-semigroup, by the uniform boundedness principle.
Let $R(\lambda) x$ denote the integral; it converges absolutely by the bound on $\norm{T(t)}$, which also gives the norm estimate.
A direct computation with the semigroup law shows $\frac{1}{h}(T(h) - I) R(\lambda) x \to \lambda R(\lambda) x - x$ as $h \to 0^+$, so $R(\lambda) x \in D(A)$ and $(\lambda I - A) R(\lambda) x = x$.
For $x \in D(A)$, $A$ commutes with the integral, so $R(\lambda)(\lambda I - A) x = x$.
Example: for a square matrix $A$ and $T(t) = e^{t A}$, the formula reads $(\lambda I - A)^{-1} = \int_0^\infty e^{-\lambda t} e^{t A} \, dt$ when $\operatorname{Re} \lambda$ exceeds the real parts of all eigenvalues of $A$.

## Explanations

### L1 human

For a number $a$, $\int_0^\infty e^{-\lambda t} e^{a t} \, dt = 1/(\lambda - a)$.
The theorem says that the same identity holds for operators: the [[Laplace transform|0V49JEZW06]] of the semigroup $e^{t A}$ is the inverse of $\lambda - A$.

### L2 human

The formula is the bridge between semigroups and their generators.
It gives the necessity part of the [[Hille–Yosida theorem|5YR4GJKPCV]], and the norm bound $M/(\operatorname{Re} \lambda - \omega)$ is exactly the resolvent estimate in that theorem.
Conversely, one recovers $T(t)$ from the resolvent by a complex inversion integral or by $T(t) x = \lim_{n \to \infty} \left(\frac{n}{t} R(\frac{n}{t})\right)^n x$, an operator form of [[Post's inversion formula|D6QKPBS2EN]].
