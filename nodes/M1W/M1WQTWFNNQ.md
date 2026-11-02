---
tag: M1WQTWFNNQ
kind: statement
role: theorem
name: Cobordism hypothesis
msc: [57R56, 18N65, 81T45]
uses: [T8BVGPPSZP, DAP92B80J2, 5S7ER95XAC, 8A7YXMW727, 3A1NMGJKJ3]
about: [DAP92B80J2, T8BVGPPSZP]
sources:
  - url: https://en.wikipedia.org/wiki/Cobordism_hypothesis
same_as:
  wikidata: Q16910990
  wikipedia: Cobordism hypothesis
---

## Statement

Let $n \ge 1$ and let $\mathcal{C}$ be a [[symmetric monoidal|5S7ER95XAC]] $(\infty, n)$-category.
Let $\mathrm{Bord}_n^{\mathrm{fr}}$ be the symmetric monoidal $(\infty, n)$-category of $n$-framed [[bordisms|T8BVGPPSZP]].
Its objects are $n$-framed $0$-manifolds.
For $1 \le k \le n$, its $k$-morphisms are $n$-framed $k$-dimensional bordisms between $(k-1)$-dimensional bordisms.
Its higher morphisms are diffeomorphisms and their isotopies.
The monoidal product is disjoint union.
Let $\mathrm{Fun}^{\otimes}(\mathrm{Bord}_n^{\mathrm{fr}}, \mathcal{C})$ be the $\infty$-groupoid of symmetric monoidal functors from $\mathrm{Bord}_n^{\mathrm{fr}}$ to $\mathcal{C}$.
Let $(\mathcal{C}^{\mathrm{fd}})^{\simeq}$ be the $\infty$-groupoid of fully [[dualizable objects|8A7YXMW727]] of $\mathcal{C}$.
Then evaluation at the point with its standard $n$-framing is an equivalence
$$\mathrm{Fun}^{\otimes}\left(\mathrm{Bord}_n^{\mathrm{fr}}, \mathcal{C}\right) \simeq \left(\mathcal{C}^{\mathrm{fd}}\right)^{\simeq}.$$

## Remarks

A symmetric monoidal functor $Z \colon \mathrm{Bord}_n^{\mathrm{fr}} \to \mathcal{C}$ is a fully extended framed [[topological quantum field theory|DAP92B80J2]].
The theorem says that such a theory is determined by its value $Z(\mathrm{pt})$ on a point, and that every fully dualizable object occurs.
The point is fully dualizable in the bordism category, because bending a bordism gives the duality data; this is why $Z(\mathrm{pt})$ must be fully dualizable.
The hypothesis cannot be dropped: an object of $\mathcal{C}$ that is not fully dualizable is not the value on a point of any such theory.
Baez and Dolan proposed the hypothesis in 1995 in the language of $n$-categories.
Lurie published a detailed outline of a proof in 2009 in the language of $(\infty, n)$-categories.
For $n = 1$ and $\mathcal{C}$ the category of vector spaces over a field, the fully dualizable objects are the finite-dimensional spaces $V$.
The theory with $Z(\mathrm{pt}) = V$ assigns to a circle the number $\dim V$, the trace of the identity of $V$.
There are versions for other tangential structures, such as orientations, in which framings are replaced by the structure and the object carries a homotopy fixed point structure.

## Explanations

### L1 human

A topological field theory assigns algebraic data to manifolds and to the ways of gluing them.
The cobordism hypothesis says that, in the most local version, all the data are decided by what the theory assigns to a single point.
Everything else is built by gluing points into lines, lines into surfaces, and so on.
The only condition on the data at the point is that it be finite in a strong algebraic sense, called full dualizability.

### L2 human

Classical two-dimensional field theories are classified by commutative Frobenius algebras, which uses the decomposition of surfaces into pairs of pants.
The cobordism hypothesis extends such classifications to all dimensions by requiring the theory to be defined down to points, using higher categories.
It ties [[higher category theory|3A1NMGJKJ3]] to manifold topology: the framed bordism $(\infty, n)$-category is the free symmetric monoidal $(\infty, n)$-category with duals on one object.
Its proof outline relies on Morse theory to decompose bordisms into elementary handles.
