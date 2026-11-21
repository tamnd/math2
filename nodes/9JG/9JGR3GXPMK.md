---
tag: 9JGR3GXPMK
kind: example
name: The algebraic numbers are not saturated
msc: ["03C50", "03C60"]
topics: [Z772KEC9BY]
audience: grad
not_instance_of:
  - target: RMTZ5J64FX
    note: "the field of algebraic numbers omits the transcendental type over the empty set"
  - target: F30ZVR4AD5
    note: "the countable field of transcendence degree 1 does not embed elementarily into the algebraic numbers"
  - target: ZGEXNRHC9M
    note: "the omitted transcendental type is a computable set of formulas without parameters"
uses: [RMTZ5J64FX, F30ZVR4AD5, ZGEXNRHC9M, 6DP6ESTNYR, 0H628RSGWX, 0NQMZ89X4A, PPGD5KW8JC, S8W40PYNHX]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Example

Let $\overline{\Q}$ be the field of [[algebraic numbers|0H628RSGWX]], a countable model of $\mathrm{ACF}_0$.
Let $p_\infty(x) = \set{f(x) \ne 0 : f \in \Z[x], \, f \ne 0}$.

1. A finite subset of $p_\infty$ excludes the finitely many roots of finitely many polynomials, and $\overline{\Q}$ is infinite. So $p_\infty$ is finitely satisfiable in $\overline{\Q}$, and it is a type over $\emptyset$.
2. Every element of $\overline{\Q}$ is a root of a nonzero $f \in \Z[x]$, so it fails $f(x) \ne 0$. So $\overline{\Q}$ omits $p_\infty$.
3. The parameter set $\emptyset$ is finite, so $\overline{\Q}$ is not $\aleph_0$-saturated, and not [[saturated|RMTZ5J64FX]].
4. The set $p_\infty$ is [[computable|PPGD5KW8JC]], since the nonzero integer polynomials can be listed by a program. So $\overline{\Q}$ is not [[recursively saturated|ZGEXNRHC9M]].
5. Let $F = \Q(t)^{\mathrm{alg}}$, a countable model of $\mathrm{ACF}_0$ with a [[transcendental|0NQMZ89X4A]] element $t$.
6. An elementary embedding $F \to \overline{\Q}$ would send $t$ to an element that realizes $\operatorname{tp}(t) = p_\infty$, which does not exist by step 2.
7. So $\overline{\Q}$ is not [[universal|F30ZVR4AD5]].

## Remarks

The field $\overline{\Q}$ is the opposite of a saturated model: it is the [[prime model|S8W40PYNHX]] of $\mathrm{ACF}_0$, and it realizes only the isolated types over $\emptyset$; see [[the type space of algebraically closed fields|6DP6ESTNYR]].
It is still homogeneous: an isomorphism between finitely generated subfields extends to an automorphism of $\overline{\Q}$.
So homogeneity does not imply saturation.
Replacing $\overline{\Q}$ by a field of transcendence degree $\aleph_0$ gives the countable saturated model.

## Explanations

### L1 human

The algebraic numbers contain a root of every polynomial equation with integer coefficients, and nothing else.
A consistent wish, "a number that solves no such equation", is never met inside them.
So the algebraic numbers are as small as possible, not as rich as possible.

### L2 human

The test for failure of saturation is one consistent type over a small set that is omitted.

1. Here the set is empty, and the type is $p_\infty$.
2. The omission follows from the definition of an algebraic number.

The typical use is to compare the prime model and the saturated model of a theory.
The trap is to think that being algebraically closed is a saturation property: algebraic closure realizes the algebraic types only.
