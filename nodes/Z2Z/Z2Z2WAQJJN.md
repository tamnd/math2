---
tag: Z2Z2WAQJJN
kind: statement
role: theorem
name: Suslin rigidity theorem
msc: [19D50, "19E20"]
uses: [ANJ5719F7F, 04C5ZBG1WT, 0X6AB5P3G1, CJSGE7JSGH, 5GVFZWMWC8]
about: [ANJ5719F7F]
sources:
  - url: https://en.wikipedia.org/wiki/Rigidity_(K-theory)
---

## Statement

Let $k \subseteq L$ be an extension of algebraically closed [[fields|04C5ZBG1WT]], and let $\ell \ge 2$ be an integer that is invertible in $k$.
Then for every $n \ge 0$ the map
$$K_n(k; \Z/\ell) \to K_n(L; \Z/\ell)$$
of [[K-groups with coefficients in $\Z/\ell$|ANJ5719F7F]] is an isomorphism.

## Remarks

The idea of the proof starts with a smooth curve $C$ over $k$ and two $k$-points $x, y$ of $C$.
The two specialization maps from the mod $\ell$ K-theory of $C$ to that of $k$ agree, because the relevant part of the Picard group of $C$ is $\ell$-divisible.
The field $L$ is a union of finitely generated $k$-algebras, each of which has $k$-points.
Specialization at such points shows that the map is injective, and a further use of the same rigidity property shows that it is surjective.

At work: let $k = \overline{\F}_p$ and $\ell$ prime to $p$.
Passing to the colimit in Quillen's [[computation for finite fields|CJSGE7JSGH]] gives $K_n(\overline{\F}_p; \Z/\ell) \cong \Z/\ell$ for even $n \ge 0$ and $0$ for odd $n$.
By the theorem, the same holds for every algebraically closed field of characteristic $p$.
Suslin also showed that the same answer holds in characteristic $0$, where it agrees with the mod $\ell$ homotopy of the space $\Z \times BU$ of topological K-theory.

The hypothesis that both fields are algebraically closed is necessary.
For $\Q \subseteq \C$ and $\ell = 2$, $K_1(\Q; \Z/2) = \Q^\times/(\Q^\times)^2$ is infinite, while $K_1(\C; \Z/2) = 0$ because every complex number is a square.
The coefficients are also needed: $K_1(\overline{\Q}) = \overline{\Q}^\times \to \C^\times = K_1(\C)$ is not surjective, since $\overline{\Q}$ is countable.

## Explanations

### L1 human

The integral K-groups of a field such as $\C$ are enormous and depend on the field.
The theorem says that modulo $\ell$, for algebraically closed fields, they do not depend on the field at all, only on its characteristic.
So the mod $\ell$ K-theory of $\C$ equals that of the algebraic numbers.

### L2 human

Rigidity is what makes mod $\ell$ K-theory computable: it reduces algebraically closed fields to the algebraic closure of the prime field.
It is the basis for comparing algebraic K-theory with étale cohomology and topological K-theory.
Gabber's rigidity theorem extends the idea from field extensions to Henselian local rings and their residue fields.
