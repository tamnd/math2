---
tag: 6K90GWZJ7K
kind: statement
role: theorem
name: Characters of a finite abelian group form a basis
msc: [43A40, 20K01]
uses: [082GHNPJ53, FPRA2KEHFF, 000AYPA9AJ, 0KCQ9Y3QKA, S6ARZ7M1YE, KF2QQ1GJGB]
about: [FPRA2KEHFF]
sources:
  - url: https://en.wikipedia.org/wiki/Character_group
---

## Statement

Let $G$ be a finite [[abelian group|082GHNPJ53]], let $\widehat{G}$ be its [[character group|FPRA2KEHFF]], and let $\C^G$ be the complex [[vector space|000AYPA9AJ]] of all functions $G \to \C$.
Give $\C^G$ the inner product $\ip{f}{g} = \frac{1}{\abs{G}}\sum_{x \in G} f(x)\overline{g(x)}$.
Then $\widehat{G}$ is an orthonormal [[basis|0KCQ9Y3QKA]] of $\C^G$.
In particular, every $f \colon G \to \C$ can be written uniquely as
$$f = \sum_{\chi \in \widehat{G}} \ip{f}{\chi}\, \chi.$$

## Remarks

Proof idea: by the [[orthogonality of characters|S6ARZ7M1YE]], the characters are orthonormal, hence linearly independent.
By the [[number of characters|KF2QQ1GJGB]], there are $\abs{G}$ of them, which is the dimension of $\C^G$.

Example: for $G = \Z/2\Z$ the characters are $\chi_0 = (1, 1)$ and $\chi_1 = (1, -1)$, listing values at $0$ and $1$.
The function $f = (3, 1)$ has $\ip{f}{\chi_0} = 2$ and $\ip{f}{\chi_1} = 1$, and indeed $f = 2\chi_0 + \chi_1$.

The hypothesis that $G$ is abelian is necessary.
For $G = S_3$ there are only two homomorphisms to $\C^\times$, which cannot span the $6$-dimensional space $\C^{S_3}$; one needs the matrix entries of all irreducible representations instead.

## Explanations

### L1 human

Every function on a finite abelian group is a unique combination of characters.
This is Fourier analysis in its simplest form: the characters play the role of sines and cosines, and the coefficients are found by inner products.

### L2 human

The coefficients $\ip{f}{\chi}$ are, up to the factor $\frac{1}{\abs{G}}$ and the choice of $\chi$ or $\overline{\chi}$, the Fourier transform of $f$ on $G$.
The expansion gives the Plancherel identity $\ip{f}{f} = \sum_\chi \abs{\ip{f}{\chi}}^2$.
In Mathlib this basis appears as `AddChar.complexBasis`.
For nonabelian finite groups, the characters of irreducible representations form a basis only of the class functions.
