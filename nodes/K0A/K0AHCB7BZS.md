---
tag: K0AHCB7BZS
kind: statement
role: proposition
name: Quillen's excess-intersection formula
sources:
  - wikipedia: en:54145380@r1348461149
    locator: Residual intersection, section Formulae > Quillen's excess-intersection formula
    note: adopted
    mention: wikipedia://en/54145380#E8YU
    sections: [Statement]
inventory: [P718MCFS5C]
---

## Statement

The formula in the topological setting is due to (Quillen 1971).

Now, suppose we are given *Y{{*}}*→*Y*' and suppose*i'*:*X*' =*X*×<sub>*Y*</sub>*Y*' →*Y*' is regular of codimension*d'*so that one can define*i'*<sup>!</sup> as before. Let*F*be the excess bundle of*i*and*i<sup>'</sup>*; that is, it is the pullback to*X{{*}}* of the quotient of *N* by the normal bundle of *i'*. Let *e*(*F*) be the Euler class (top Chern class) of *F*, which we view as a homomorphism from *A*<sub>*k*−*d'*</sub> (*X{{*}}*) to*A*<sub>*k*−*d*</sub>(*X{{*}}*). Then

where *i*<sup>!</sup> is determined by the morphism *Y{{*}}*→*Y'*→*Y*.*

Finally, it is possible to generalize the above construction and formula to complete intersection morphisms; this extension is discussed in § 6.6. as well as Ch. 17 of loc. cit.

*Proof*: One can deduce the intersection formula from the rather explicit form of a Gysin homomorphism. Let *E* be a vector bundle on *X* of rank *r* and *q*: **P**(*E* ⊕ 1) → *X* the projective bundle (here 1 means the trivial line bundle). As usual, we identity **P**(*E* ⊕ 1) as a disjoint union of **P**(*E*) and *E*. Then there is the tautological exact sequence

$$0 \to \mathcal{O}(-1) \to q^*E \oplus 1 \to \xi \to 0$$

on **P**(*E* ⊕ 1). We claim the Gysin homomorphism is given as

$$A_k(E) \to A_{k-r}(X), \, x \mapsto q_*(e(\xi) \overline{x})$$

where *e*(*ξ*) = *c*<sub>*r*</sub>(*ξ*) is the Euler class of ξ and $\overline{x}$ is an element of *A*<sub>*k*</sub>(**P**(*E* ⊕ 1)) that restricts to *x*. Since the injection *q*<sup>\*</sup>: *A*<sub>*k*−*r*</sub>(*X*) → *A*<sub>*k*</sub>(**P**(*E* ⊕ 1)) splits, we can write

$$\overline{x} = q^* y + z$$

where *z* is a class of a cycle supported on **P**(*E*). By the Whitney sum formula, we have: *c*(*q*<sup>\*</sup>*E*) = (1 − *c*<sub>1</sub>(*O*(1)))*c*(*ξ*) and so

$$e(\xi) = \sum_0^r c_1(\mathcal{O}(1))^i c_{r-i}(q^* E).$$

Then we get:

$$q_*(e(\xi) q^* y) = \sum_{i=0}^r s_{i-r}(E \oplus 1) c_{r-i}(E) y$$

where *s*<sub>*I*</sub>(*E* ⊕ 1) is the *i*-th Segre class. Since the zeroth term of a Segre class is the identity and its negative terms are zero, the above expression equals *y*. Next, since the restriction of ξ to **P**(*E*) has a nowhere-vanishing section and *z* is a class of a cycle supported on **P**(*E*), it follows that *e*(ξ)*z* = 0. Hence, writing π for the projection map of *E* and *j* for the inclusion *E* to **P**(*E*⊕1), we get:

$$\pi^* q_*(e(\xi) \overline{x}) = \pi^*(y) = j^* q^* y = j^*(\overline{x} - z) = j^*(\overline{x}) = x$$

where the second-to-last equality is because of the support reason as before. This completes the proof of the explicit form of the Gysin homomorphism.

The rest is formal and straightforward. We use the exact sequence

$$0 \to \xi' \to \xi \to r^* F \to 0$$

where *r* is the projection map for . Writing *P* for the closure of the specialization of *V*, by the Whitney sum formula and the projection formula, we have:

$$i^!(V) = r_*(e(\xi) P) = r_*(e(r^*F) e(\xi') P) = e(F) r_*(e(\xi') P) = e(F) {i'}^!(V).$$

$$\square$$

One special case of the formula is the self-intersection formula, which says: given a regular embedding *i*: *X* → *Y* with normal bundle *N*,

$$i^*i_* = e(N).$$

(To get this, take *Y'* = *Y{{*}}*\=*X*.) For example, from this and the projection formula, when*X*,*Y*are smooth, one can deduce the formula:*

$$i_*(x) i_*(y) = i_*(e(N) xy).$$

in the Chow ring of *Y*.

Let $f: \widetilde{Y} \to Y$ be the blow-up along a closed subscheme *X*, $\widetilde{X}$ the exceptional divisor and $g: \widetilde{g}: \widetilde{X} \to X$ the restriction of *f*. Assume *f* can be written as a closed immersion followed by a smooth morphism (for example, *Y* is quasi-projective). Then, from $f^* i_* = i^! g^*$, one gets:
