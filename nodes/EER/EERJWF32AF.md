---
tag: EERJWF32AF
kind: statement
role: proposition
name: Distributivity laws for complete lattices
sources:
  - wikipedia: en:616019@r1291705765
    locator: Distributivity (order theory), section Distributivity laws for complete lattices
    note: adopted
    mention: wikipedia://en/616019#PQ26
    sections: [Statement]
inventory: [YN2ZTAHKWX]
---

## Statement

For a complete lattice, arbitrary subsets have both infima and suprema and thus infinitary meet and join operations are available. Several extended notions of distributivity can thus be described. For example, for the **infinite distributive law**, finite meets may distribute over arbitrary joins, i.e.

$$x \wedge \bigvee S = \bigvee \{ x \wedge s \mid s \in S \}$$

may hold for all elements *x* and all subsets *S* of the lattice. Complete lattices with this property are called **frames**, **locales** or **complete Heyting algebras**. They arise in connection with pointless topology and Stone duality. This distributive law *is not equivalent* to its dual statement

$$x \vee \bigwedge S = \bigwedge \{ x \vee s \mid s \in S \}$$

which defines the class of dual frames or complete co-Heyting algebras.

Now one can go even further and define orders where arbitrary joins distribute over arbitrary meets. Such structures are called completely distributive lattices. However, expressing this requires formulations that are a little more technical. Consider a doubly indexed family {*x*<sub>*j*,*k*</sub> | *j* in *J*, *k* in *K*(*j*)} of elements of a complete lattice, and let *F* be the set of choice functions *f* choosing for each index *j* of *J* some index *f*(*j*) in *K*(*j*). A complete lattice is **completely distributive** if for all such data the following statement holds:

$$\bigwedge_{j\in J}\bigvee_{k\in K(j)} x_{j,k} = \bigvee_{f\in F}\bigwedge_{j\in J} x_{j,f(j)}$$

Complete distributivity is again a self-dual property, i.e. dualizing the above statement yields the same class of complete lattices. Completely distributive complete lattices (also called *completely distributive lattices* for short) are indeed highly special structures. See the article on completely distributive lattices.
