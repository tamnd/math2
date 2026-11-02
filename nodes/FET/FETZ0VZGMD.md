---
tag: FETZ0VZGMD
kind: statement
role: theorem
name: Beck's monadicity theorem
msc: [18C15, 18C20]
uses: [DNTDCKZBKK, TZHF6ZM92S, DVSTWGVCSZ, FEPRJR3MND]
about: [DNTDCKZBKK]
sources:
  - url: https://en.wikipedia.org/wiki/Beck%27s_monadicity_theorem
same_as:
  wikidata: Q4878586
  wikipedia: Beck's monadicity theorem
---

## Statement

Let $U \colon \mathcal{D} \to \mathcal{C}$ be a functor.
A pair of morphisms $f, g \colon d \to d'$ in $\mathcal{D}$ is *$U$-split* if $U(f), U(g)$ have a split coequalizer in $\mathcal{C}$.
A split coequalizer of $p, q \colon x \to y$ is a morphism $e \colon y \to z$ with $s \colon z \to y$ and $t \colon y \to x$ such that $e p = e q$, $e s = \id_z$, $p t = \id_y$ and $q t = s e$.
Then $U$ is [[monadic|DNTDCKZBKK]] if and only if these three conditions hold.

1. $U$ has a [[left adjoint|TZHF6ZM92S]].
2. $U$ reflects isomorphisms: if $U(h)$ is an isomorphism, then $h$ is an isomorphism.
3. Every $U$-split pair in $\mathcal{D}$ has a [[coequalizer|DVSTWGVCSZ]] in $\mathcal{D}$, and $U$ preserves these coequalizers.

## Remarks

A split coequalizer is a coequalizer, and every functor preserves it, because the equations that define it are preserved.
For the proof, let $T = U F$ and let $(A, a)$ be an algebra in the [[Eilenberg–Moore category|FEPRJR3MND]].
The pair $F(a), \varepsilon_{F(A)} \colon F U F (A) \to F(A)$ is $U$-split, and its coequalizer defines a left adjoint of the comparison functor.
Conditions 2 and 3 then make the unit and counit of this adjunction isomorphisms.

Example: the forgetful functor from groups to sets satisfies all three conditions, so it is monadic.
The same holds for rings, modules over a ring, and every variety of universal algebras.

Without condition 2 the conclusion fails.
The forgetful functor from topological spaces to sets has a left adjoint, but a continuous bijection need not be a homeomorphism, and this functor is not monadic.

## Explanations

### L1 human

The theorem gives a practical test for deciding whether a category is algebraic over another one.
One checks that free objects exist, that the forgetful functor detects isomorphisms, and that certain quotients exist and are computed underneath.
When the test passes, the objects are exactly the algebras of a monad.

### L2 human

Beck's theorem is the standard tool for proving monadicity, for example of compact Hausdorff spaces over sets or of modules over a ring.
There is also a variant that uses reflexive coequalizers: a right adjoint that reflects isomorphisms and in whose domain reflexive coequalizers exist and are preserved is monadic.
The dual statement characterizes comonadic functors, and in algebraic geometry it is the basis of descent theory.
In the strict form, $U$ creates coequalizers of $U$-split pairs, and the comparison functor is then an isomorphism.
