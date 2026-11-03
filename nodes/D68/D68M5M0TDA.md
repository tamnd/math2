---
tag: D68M5M0TDA
kind: statement
role: theorem
name: Universal property of the Grothendieck group
msc: [19A99, 20M14, 18F30]
uses: [0N6R902FG1, 082GHNPJ53, 0JYTG5K9Y4, 5FDMY7PDYY]
about: [5FDMY7PDYY]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_group
---

## Statement

Let $M$ be a commutative [[monoid|0N6R902FG1]], written additively.
Then there are an [[abelian group|082GHNPJ53]] $K(M)$ and a monoid homomorphism $i \colon M \to K(M)$ with the following property.
For every abelian group $A$ and every monoid homomorphism $f \colon M \to A$, there is exactly one [[group homomorphism|0JYTG5K9Y4]] $g \colon K(M) \to A$ with $g \circ i = f$.
The pair $(K(M), i)$ is unique up to a unique isomorphism compatible with the maps from $M$.

## Remarks

Existence comes from an explicit construction.
On $M \times M$ put $(m, n) \sim (m', n')$ when $m + n' + p = m' + n + p$ for some $p \in M$.
This is an equivalence relation compatible with addition, and the classes form an abelian group in which the class of $(n, m)$ is the inverse of the class of $(m, n)$.
Set $i(m)$ to be the class of $(m, 0)$, so that the class of $(m, n)$ is $i(m) - i(n)$.
Given $f$, the only possible choice is $g(i(m) - i(n)) = f(m) - f(n)$, and one checks that it is well defined; uniqueness of $(K(M), i)$ is the usual argument for universal objects.

Example: for $M = \N$ under addition one gets $K(M) = \Z$, and $g(k) = k f(1)$.
The construction also shows that $i(m) = i(n)$ exactly when $m + p = n + p$ for some $p \in M$.
So $i$ is injective exactly when $M$ is cancellative.
For $M = \N \cup \set{\infty}$ with $n + \infty = \infty$, every element becomes equal to $\infty$ after adding $\infty$, so $K(M) = 0$.

## Explanations

### L1 human

Given a way to add things that cannot be subtracted, there is a best way to allow subtraction.
The result is the [[Grothendieck group|5FDMY7PDYY]], and "best" means that every other way to map the things into a group factors through it in exactly one way.
This is how the integers arise from the natural numbers.

### L2 human

The universal property is what makes K-groups functorial.
A monoid homomorphism $M \to N$ composed with $N \to K(N)$ factors through $K(M)$, which gives a group homomorphism $K(M) \to K(N)$.
For example, a ring homomorphism $R \to S$ sends projective $R$-modules to projective $S$-modules by base change, and this induces $K_0(R) \to K_0(S)$.
The universal property is also the fastest way to compute.
To define a homomorphism out of $K_0(R)$, such as the rank or the determinant, it suffices to give an additive function on modules.
