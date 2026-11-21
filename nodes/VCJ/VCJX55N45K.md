---
tag: VCJX55N45K
kind: statement
role: theorem
name: Characterization of universal Horn classes
aliases: [characterization-of-universal-horn-classes, universal-horn-classes-substructures-reduced-products]
msc: ["03C52", "03C20", "08C15"]
topics: [JYJHB4YBAH]
audience: grad
about: [9A4CYWXPEA]
uses: [9A4CYWXPEA, PGZSNWS5VN, 676H7EGTKJ, F4WRD396PB, 15PF73BKY6, WDVVEYD6AT, 983GZBQYT4]
sources:
  - book: isbn:9780521587136
---

## Statement

Let $L$ be a [[signature|WDVVEYD6AT]], and let $\mathcal{K}$ be a class of [[$L$-structures|983GZBQYT4]] with nonempty domains that is closed under isomorphism.
Write $\mathbf{P}_R(\mathcal{K})$ for the class of [[reduced products|F4WRD396PB]] $\prod_{i \in I} \mathcal{B}_i / F$ with $I$ nonempty, each $\mathcal{B}_i \in \mathcal{K}$, and $F$ a [[filter|15PF73BKY6]] on $I$.
Let $\mathbf{1}_L$ be the one-element $L$-structure in which every relation symbol holds of the unique tuple.

1. $\mathcal{K}$ is a [[universal Horn class|9A4CYWXPEA]] if and only if $\mathcal{K}$ is closed under [[substructures|676H7EGTKJ]] and $\mathbf{P}_R(\mathcal{K}) \subseteq \mathcal{K}$.
2. For every class $\mathcal{K}$, an $L$-structure satisfies all universal Horn sentences true in $\mathcal{K}$ if and only if it is isomorphic to a substructure of a member of $\mathbf{P}_R(\mathcal{K})$. In short, the models of the universal Horn theory of $\mathcal{K}$ form $\mathbf{I}\mathbf{S}\mathbf{P}_R(\mathcal{K})$.
3. $\mathcal{K}$ is axiomatized by strict universal Horn sentences $\forall \bar x \, (\alpha_1 \wedge \cdots \wedge \alpha_n \rightarrow \beta)$ if and only if $\mathcal{K}$ is closed under substructures and reduced products and contains a copy of $\mathbf{1}_L$.

## Remarks

### Why each hypothesis is needed

- Substructures: [[divisible abelian groups|ZXVBEPMTCN]] are closed under reduced products, since their axioms are Horn sentences, but $\mathbb{Z}$ is a subgroup of $\mathbb{Q}$ that is not divisible.
- Reduced products: [[total orders|GTBBMP1K56]] are closed under substructures and ultraproducts, but the square of a $2$-element chain is not total.
- Direct products alone do not suffice. The [[residually finite groups|HEE922EHQ8]] are closed under subgroups and direct products, but an ultrapower $\mathbb{Z}^{\mathbb{N}} / \mathcal{U}$ by a nonprincipal ultrafilter is not residually finite. The class of $(n!)_n$ is nonzero and divisible by every $k \ge 1$, so it lies in every subgroup of finite index.
- The one-element structure in part 3: [[strict partial orders|60FNZ35H6R]] are a universal Horn class, but $\mathbf{1}_L$ violates $\forall x \, \neg (x < x)$, so no strict axioms define them.

### Consequences

- In an algebraic signature, part 3 says that the [[quasivarieties|WRXEKT4NQS]] are the classes of algebras closed under subalgebras and reduced products that contain a trivial algebra. [[Mal'cev's characterization|DFNM3BGMAY]] gives the same classes with direct products and ultraproducts in place of reduced products.
- [[Partial orders|S4EM1MDMJG]] and [[torsion-free groups|WYKXBD3GFE]] are universal Horn classes, and total orders are not.
- The smallest universal Horn class containing $\mathcal{K}$ is $\mathbf{I}\mathbf{S}\mathbf{P}_R(\mathcal{K})$, by part 2.

### Converse

Each part is an equivalence.
The direction from axioms to closure properties uses only that universal sentences pass to substructures and that [[Horn sentences pass to reduced products|8RRECJJM3G]].

### Generalizations

- Without the Horn condition, closure under substructures and ultraproducts characterizes [[universal classes|JPGDSW2TAP]].
- Arbitrary Horn sentences, with quantifier prefixes of any shape, are the sentences preserved under reduced products; see [[this theorem|1FF2GRE6VX]].

## History

Horn sentences are named after Alfred Horn, who showed in 1951 that they are preserved under direct products.
The characterization of quasivarieties by closure properties is due to Mal'cev.

## Explanations

### L1 human

Some families of structures are described by rules of the form "if these basic facts hold, then that one holds".
The theorem says how to recognize such families without seeing the rules.
A family is of this kind exactly when it is closed under two operations: taking a part of a structure, and taking a kind of product of many structures.

### L2 human

We test part 1 on the class of [[equivalence relations|0G8VEZ3WTK]] and on a class that fails.

1. An equivalence relation is reflexive, symmetric and transitive, and these are strict universal Horn sentences.
2. A coordinatewise product of equivalence relations relates two tuples when every coordinate is related; this is again an equivalence relation.
3. A substructure of an equivalence relation is the restriction to a subset, which is again an equivalence relation.
4. The class of equivalence relations with at most two classes is closed under substructures, but the square of a two-class relation has four classes. So that class is not universal Horn.

### L3 human

Part 2 is a completeness theorem for universal Horn logic.
Its proof maps a model $\mathcal{A}$ of the universal Horn theory into a reduced product indexed by pairs: a finite set of atomic facts true in $\mathcal{A}$, and one atomic fact false in $\mathcal{A}$.
The filter makes every true fact hold almost everywhere, while each false fact fails on a set that meets every filter set.
This is the Horn analogue of the ultraproduct argument for universal classes, and it needs no ultrafilter, because Horn sentences never force a choice between two atoms.
