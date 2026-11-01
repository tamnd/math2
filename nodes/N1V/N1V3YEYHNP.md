---
tag: N1V3YEYHNP
kind: statement
role: theorem
name: Hilbert's irreducibility theorem
msc: ["12E25", 11R09]
uses: [00X2A9G9W3, 0CES91M79A]
about: [00X2A9G9W3, SFPKB3NC0E]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_irreducibility_theorem
same_as:
  wikidata: Q5761142
  wikipedia: Hilbert's irreducibility theorem
---

## Statement

Let $r, s \ge 1$ and let $f_1, \dots, f_k$ be [[irreducible|00X2A9G9W3]] elements of the [[polynomial ring|0CES91M79A]] $\Q[t_1, \dots, t_r, x_1, \dots, x_s]$, each of positive degree in the variables $x_1, \dots, x_s$.
Then there is $a = (a_1, \dots, a_r) \in \Q^r$ such that each $f_i(a, x_1, \dots, x_s)$ is irreducible in $\Q[x_1, \dots, x_s]$.

## Remarks

The set of good $a$ is large: one may take $a \in \Z^r$, and there are infinitely many such $a$.
Classical proofs expand the roots of $f$ as series in $t$ near infinity and show that rational specialisations giving a factor are rare.
Example: $x^2 - t$ is irreducible in $\Q[t, x]$; the value $t = 2$ gives the irreducible $x^2 - 2$, while $t = 4$ gives $(x - 2)(x + 2)$.
So irreducibility can fail at some values, and the theorem only says that it survives at many.
A stronger form preserves the Galois group: if an irreducible $f \in \Q(t)[x]$ has Galois group $G$ over $\Q(t)$, then $f(a, x)$ has Galois group $G$ over $\Q$ for infinitely many $a \in \Q$.
The analogue fails over $\R$: $x^2 - t^2 - 1$ is irreducible in $\R[t, x]$, but for every $a \in \R$ the polynomial $x^2 - a^2 - 1$ has the real roots $\pm \sqrt{a^2 + 1}$.

## Explanations

### L1 human

A polynomial in several letters that cannot be factored usually stays unfactorable after you replace some letters by numbers.
Hilbert's theorem says that, over the rationals, you can always choose such numbers.

### L2 human

Fields with this property are called [[Hilbertian fields|SFPKB3NC0E]]; number fields are Hilbertian, while finite fields and algebraically closed fields are not.
The theorem is the main tool to pass from Galois groups over $\Q(t)$ to Galois groups over $\Q$.
For example, the generic polynomial with Galois group the full symmetric group $S_n$ over $\Q(t_1, \dots, t_n)$ specialises to polynomials over $\Q$ with Galois group $S_n$.
This is the starting point of many attacks on the [[inverse Galois problem|YJS6X8JN7D]].
