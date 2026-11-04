---
tag: KJSQAAXP54
kind: statement
role: theorem
name: Grushko decomposition theorem
sources:
  - wikipedia: en:18715724@r1354577450
    locator: Grushko theorem, section Grushko decomposition theorem
    note: adopted
    mention: wikipedia://en/18715724#FD4K
    sections: [Statement]
inventory: [H6AM49KD42]
---

## Statement

A useful consequence of the original Grushko theorem is the so-called **Grushko decomposition theorem.** It asserts that any nontrivial [[finitely generated group|082DWWXMRJ]] *G* can be decomposed as a free product

*G* = *A*<sub>1</sub>∗*A*<sub>2</sub>∗...∗*A*<sub>*r*</sub>∗*F*<sub>*s*</sub>, where *s* ≥ 0, *r* ≥ 0,

where each of the groups *A*<sub>*i*</sub> is nontrivial, freely indecomposable (that is, it cannot be decomposed as a free product) and not infinite cyclic, and where *F<sub>s</sub>* is a [[free group|020Z5SEN27]] of rank *s*; moreover, for a given *G*, the groups *A*<sub>1</sub>, ..., *A*<sub>*r*</sub> are unique up to a permutation of their [[conjugacy classes|0DEBXAJ5SA]] in *G* (and, in particular, the sequence of isomorphism types of these groups is unique up to a permutation) and the numbers *s* and *r* are unique as well.

More precisely, if *G* = *B*<sub>1</sub>∗...∗*B*<sub>*k*</sub>∗*F*<sub>*t*</sub> is another such decomposition then *k* = *r*, *s* = *t*, and there exists a permutation σ∈*S*<sub>*r*</sub> such that for each *i*=1,...,*r* the subgroups *A*<sub>*i*</sub> and *B*<sub>σ(*i*)</sub> are [[conjugate|0DEBXAJ5SA]] in *G*.

The existence of the above decomposition, called the **Grushko decomposition** of *G*, is an immediate corollary of the original Grushko theorem, while the uniqueness statement requires additional arguments (see, for example).

Algorithmically computing the Grushko decomposition for specific classes of groups is a difficult problem which primarily requires being able to determine if a given group is freely decomposable. Positive results are available for some classes of groups such as torsion-free word-hyperbolic groups, certain classes of relatively hyperbolic groups, fundamental groups of finite graphs of finitely generated free groups and others.

Grushko decomposition theorem is a group-theoretic analog of the Kneser prime decomposition theorem for 3-manifolds which says that a closed 3-manifold can be uniquely decomposed as a connected sum of irreducible 3-manifolds.
