---
tag: B75H4VEARE
kind: definition
name: Triangulated category
msc: [18G80]
defines: T2V7GJJ2EN
uses: [B2VP96NJSK, KAN07YC9T2, P8PFMNCB8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Triangulated_category
---

## Definition

Let $\mathcal{T}$ be an [[additive category|B2VP96NJSK]] and let $\Sigma \colon \mathcal{T} \to \mathcal{T}$ be an [[additive functor|KAN07YC9T2]] that is an automorphism, the *shift*, also written $X \mapsto X[1]$.
A *triangle* is a diagram $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$.
A morphism of triangles is a triple of morphisms $(f, g, h)$ between the first, second and third objects.
It must make the three squares commute, the last one with $\Sigma f$.
A *triangulated category* is such a pair $(\mathcal{T}, \Sigma)$ with a class of triangles, the *distinguished triangles*, such that:

1. (TR1) for each object $X$, the triangle $X \xrightarrow{\id} X \to 0 \to \Sigma X$ is distinguished. Each triangle isomorphic to a distinguished triangle is distinguished. Each morphism $u \colon X \to Y$ is the first morphism of a distinguished triangle $X \xrightarrow{u} Y \to Z \to \Sigma X$;
2. (TR2) a triangle $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ is distinguished if and only if $Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X \xrightarrow{-\Sigma u} \Sigma Y$ is distinguished;
3. (TR3) for distinguished triangles $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ and $X' \xrightarrow{u'} Y' \xrightarrow{v'} Z' \xrightarrow{w'} \Sigma X'$ and morphisms $f \colon X \to X'$, $g \colon Y \to Y'$ with $g u = u' f$, there is $h \colon Z \to Z'$ such that $(f, g, h)$ is a morphism of triangles;
4. (TR4) the [[octahedral axiom|P8PFMNCB8Y]] holds.

## Remarks

Example: for an additive category $\mathcal{A}$, the homotopy category $K(\mathcal{A})$ with the shift of complexes is triangulated, the distinguished triangles being those isomorphic to $X \xrightarrow{f} Y \to \operatorname{Cone}(f) \to X[1]$ for chain maps $f$.
For a distinguished triangle and an object $W$, the sequences obtained by applying $\Hom(W, -)$ and $\Hom(-, W)$ are long exact.
Non-example: the category of abelian groups has no triangulated structure, for any shift and any class of triangles.
In a triangulated category every monomorphism $u$ is split, since in a triangle $\Sigma^{-1} Z \xrightarrow{t} X \xrightarrow{u} Y \to Z$ one has $u t = 0$, so $t = 0$, and a triangle with a zero map splits.
But the monomorphism $\Z \xrightarrow{\cdot 2} \Z$ does not split.
A category satisfying TR1 to TR3 only is called *pretriangulated*.
