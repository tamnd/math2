---
tag: 665BTJVKK1
kind: statement
role: theorem
name: Grothendieck's comparison theorem
sources:
  - wikipedia: en:603916@r1312289985
    locator: Kähler differential, section Higher differential forms and algebraic de Rham cohomology > Grothendieck's comparison theorem
    note: adopted
    mention: wikipedia://en/603916#3JUT
    sections: [Statement]
inventory: [Z1ZWV3115Y]
---

## Statement

If $X$ is a smooth complex algebraic variety, there is a natural comparison map of complexes of sheaves

$$\Omega^{\bullet}_{X/\mathbb{C}}(-) \to \Omega^{\bullet}_{X^\text{an}}((-)^\text{an})$$

between the algebraic de Rham complex and the [[smooth|0BE3QDH73A]] de Rham complex defined in terms of (complex-valued) differential forms on $X^\text{an}$, the complex manifold associated to *X*. Here, $(-)^{\text{an}}$ denotes the complex analytification functor. This map is far from being an isomorphism. Nonetheless, (Grothendieck 1966a) showed that the comparison map induces an isomorphism

$$H^\ast_\text{dR}(X/\mathbb{C}) \cong H^\ast_\text{dR}(X^\text{an})$$

from algebraic to smooth de Rham cohomology (and thus to singular cohomology $H^*_{\text{sing}}(X^{\text{an}}; \mathbb{C})$ by de Rham's theorem). In particular, if *X* is a smooth affine algebraic variety embedded in $\mathbb{C}^n$, then the inclusion of the subcomplex of algebraic differential forms into that of all smooth forms on *X* is a quasi-isomorphism. For example, if

$$X = \{ (w,z) \in \mathbb{C}^2: w z =1 \},$$

then as shown above, the computation of algebraic de Rham cohomology gives explicit generators $\{ 1, z^{-1} dz \}$ for $H^0_{\text{dR}}(X/\mathbb{C})$ and $H^1_{\text{dR}}(X/ \mathbb{C})$, respectively, while all other cohomology groups vanish. Since *X* is homotopy equivalent to a [[circle|060W5CBZP6]], this is as predicted by Grothendieck's theorem.

Counter-examples in the singular case can be found with non-Du Bois singularities such as the graded ring $k[x,y]/(y^2-x^3)$ with $y$ where $\deg(y)=3$ and $\deg(x)=2$. Other counterexamples can be found in algebraic plane curves with isolated singularities whose Milnor and Tjurina numbers are non-equal.

A proof of Grothendieck's theorem using the concept of a mixed Weil cohomology theory was given by (Cisinski Déglise 2013).
