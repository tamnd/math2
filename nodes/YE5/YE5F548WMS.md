---
tag: YE5F548WMS
kind: statement
role: theorem
name: Arnold's classification of simple singularities
msc: [32S05, 58K40, 14B05]
uses: [VTGYEES3VS, EVPZ7ZG1HB, 1ZE51P7GRQ]
about: [VTGYEES3VS, 42V5XGZS4F]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Statement

Let $n \ge 1$ and let $\mathcal{O}_{n+1} = \C\{x, y, z_2, \dots, z_n\}$ be the [[ring of convergent power series|EVPZ7ZG1HB]] in $n + 1$ variables.
Two germs $f, g \in \mathcal{O}_{n+1}$ are *right equivalent* if $g = f \circ \phi$ for a biholomorphic germ $\phi$ of $(\C^{n+1}, 0)$.
Let $f$ be a germ with $f(0) = 0$ and an [[isolated singularity|VTGYEES3VS]] at $0$.
It is *simple* if, for $k$ large, a neighbourhood of its $k$-jet in the space of $k$-jets meets only finitely many right equivalence classes.
Write $Q = z_2^2 + \cdots + z_n^2$.
Then $f$ is simple if and only if it is right equivalent to exactly one germ of the following list:

1. $A_k$: $x^{k+1} + y^2 + Q$, for $k \ge 1$;
2. $D_k$: $x^2 y + y^{k-1} + Q$, for $k \ge 4$;
3. $E_6$: $x^3 + y^4 + Q$;
4. $E_7$: $x^3 + x y^3 + Q$;
5. $E_8$: $x^3 + y^5 + Q$.

## Remarks

Vladimir Arnold proved the classification in 1972.
In each case the index is the [[Milnor number|1ZE51P7GRQ]]: $\mu(A_k) = \mu(D_k) = k$ and $\mu(E_k) = k$.
The proof uses finite determinacy to reduce to polynomials and the splitting lemma to remove the nondegenerate quadratic part $Q$.
Then a case analysis of the low-degree terms of the remaining function of one or two variables finishes it.
A function of two variables whose $3$-jet is zero is never simple: it lies near the family $x^4 + t x^2 y^2 + y^4$, whose cross-ratio of the four lines is a continuous modulus.

Example: $f = x^3 + y^3$ has $\mu = 4$ and is right equivalent to $D_4$, since its cubic part has three distinct linear factors, as does $x^2 y + y^3 = y(x^2 + y^2)$.

## Explanations

### L1 human

Most critical points of functions are simple, like the bottom of a bowl.
Arnold asked which singular functions cannot be continuously deformed into infinitely many inequivalent nearby types.
The answer is a short list, labelled by letters $A$, $D$, $E$ and an index.
The same letters label the simply-laced Dynkin diagrams of Lie theory, and this is no accident.

### L2 human

The simple singularities appear in many guises.
For $n = 2$, they are the [[ADE singularities|HQNXQBZ6C7]], the surface singularities $\C^2 / G$ for finite subgroups $G$ of $\mathrm{SL}_2(\C)$, also called Kleinian or Du Val singularities.
For $n = 2$, the intersection form on $H_2$ of the Milnor fibre is, up to sign, the Cartan matrix of the Dynkin diagram of the same name.
Arnold continued with the unimodal and bimodal singularities, which include the $14$ exceptional unimodal singularities.
The elementary catastrophes of [[catastrophe theory|6FKJ6SXP3G]] are real forms of simple singularities of small Milnor number.
