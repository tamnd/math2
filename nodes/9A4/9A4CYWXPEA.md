---
tag: 9A4CYWXPEA
kind: concept
name: Universal Horn class
aliases: [universal-horn-class, horn-class, universal-horn-axiomatizable-class]
msc: ["03C52", "08C15"]
topics: [JYJHB4YBAH]
audience: grad
specializes: [ZSTEZ3PRT9]
uses: [ZSTEZ3PRT9, QR92EZDTKF, MCZRXR3SVB, 676H7EGTKJ, F4WRD396PB, WRXEKT4NQS]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
    locator: Definition
  - book: isbn:9780521587136
---

## Summary

A *universal Horn sentence* is a sentence $\forall \bar x \, \theta$ in which $\theta$ is a disjunction of [[atomic formulas|MCZRXR3SVB]] and their negations with at most one unnegated atom, that is, a [[Horn clause|QR92EZDTKF]] of first-order atoms.
A *universal Horn class* is the class of models of a set of universal Horn sentences.
Every universal Horn class is a [[universal class|ZSTEZ3PRT9]], and it is closed under [[reduced products|F4WRD396PB]], in particular under direct products of nonempty families.
By [[this theorem|VCJX55N45K]], closure under isomorphisms, [[substructures|676H7EGTKJ]] and reduced products characterizes universal Horn classes.
In an algebraic signature, the classes axiomatized by universal Horn sentences that each have an unnegated atom are the [[quasivarieties|WRXEKT4NQS]].
The formal definition is [[this definition|PGZSNWS5VN]].

## Motivation

Many axioms in algebra say: if some equations or relations hold among elements, then one more holds.
Transitivity of an order and cancellation in a group are of this kind.
Such an axiom can be checked one coordinate at a time, so it survives products, and it survives passing to a subset closed under the operations.
Disjunctive axioms such as totality of an order are different: in a product, one coordinate may choose one disjunct and another coordinate the other.
Universal Horn classes isolate exactly the axioms that never force such a choice.
They are the model-theoretic setting of quasivarieties, of logic programming over first-order structures, and of the classes that have free or initial models.

## Notation

A universal Horn sentence has one of two shapes, with all $\alpha_i$ and $\beta$ atomic:

$$\forall \bar x \, (\alpha_1 \wedge \cdots \wedge \alpha_n \rightarrow \beta) \qquad \text{or} \qquad \forall \bar x \, \neg (\alpha_1 \wedge \cdots \wedge \alpha_n).$$

Sentences of the first shape are *strict*; for $n = 0$ the first shape is $\forall \bar x \, \beta$.
For a class $\mathcal{K}$ of structures, $\mathbf{I}$, $\mathbf{S}$ and $\mathbf{P}_R$ denote closure under isomorphic copies, substructures and reduced products of nonempty families.
The smallest universal Horn class containing $\mathcal{K}$ is $\mathbf{I}\mathbf{S}\mathbf{P}_R(\mathcal{K})$.

## Remarks

### Examples

- [[Partial orders|S4EM1MDMJG]] are a universal Horn class: reflexivity, antisymmetry and transitivity are strict universal Horn sentences.
- [[Torsion-free groups|WYKXBD3GFE]] are a universal Horn class, axiomatized by the group laws and $\forall x \, (x^n = e \rightarrow x = e)$ for each $n \ge 1$.
- Every [[variety of algebras|AJNZJD8442]] is a universal Horn class, since identities are strict universal Horn sentences with $n = 0$.
- [[Strict partial orders|60FNZ35H6R]] are a universal Horn class through the axiom $\forall x \, \neg (x < x)$ and transitivity.

### Non-examples

- [[Total orders|GTBBMP1K56]] form a universal class that is not universal Horn: the square of a $2$-element chain has incomparable elements.
- Fields are not even a universal class, since $\mathbb{Z}$ is a substructure of $\mathbb{Q}$; see [[this example|ZJ4WWQWVG6]].
- [[Divisible abelian groups|ZXVBEPMTCN]] are closed under reduced products but not under substructures, so they form no universal Horn class.

### Basic properties

- A universal Horn class is closed under isomorphisms, substructures, reduced products, ultraproducts and direct products of nonempty families.
- The intersection of universal Horn classes is universal Horn; take the union of the axiom sets.
- The union of two universal Horn classes need not be universal Horn. With one unary symbol $P$, take the structures with at most one element and the structures with $\forall x \, P(x)$. The product of a point outside $P$ with a two-element model of $\forall x \, P(x)$ has two elements and empty $P$.
- A universal Horn class axiomatized by strict sentences contains the one-element structure in which every relation holds.

### History

Horn sentences are named after Alfred Horn, who showed in 1951 that they are preserved under direct products.
The characterization of quasivarieties by closure under subalgebras, products and ultraproducts is [[Mal'cev's theorem|DFNM3BGMAY]].

### Common errors

- A universal Horn class is closed under products of nonempty families only, unless all axioms are strict: the empty product is the one-element structure, and $\forall x \, \neg(x < x)$ fails there.
- Closure under products and substructures alone does not give a universal Horn class; the [[residually finite groups|HEE922EHQ8]] are closed under both and are not closed under ultrapowers.
- The lexicographic product of two chains is a chain, but it is not the direct product, whose order is coordinatewise.

## Explanations

### L1 human

A universal Horn rule says: for all elements, if these basic facts hold, then that basic fact holds too, or else these facts never hold together.
Partial orders obey such rules, since reflexivity, antisymmetry and transitivity all have this shape.
Total orders need "$x \le y$ or $y \le x$", which offers a choice between two facts.
In the product of two $2$-element chains, the corners $(0, 1)$ and $(1, 0)$ are incomparable, so the choice breaks.

### L2 human

We check that a strict universal Horn sentence holds in a product $A \times B$ when it holds in $A$ and $B$.

1. Take transitivity $\forall x \forall y \forall z \, (x \le y \wedge y \le z \rightarrow x \le z)$ and the coordinatewise order.
2. Let $(a_1, b_1) \le (a_2, b_2) \le (a_3, b_3)$; then $a_1 \le a_2 \le a_3$ in $A$ and $b_1 \le b_2 \le b_3$ in $B$.
3. Transitivity in each factor gives $a_1 \le a_3$ and $b_1 \le b_3$, so $(a_1, b_1) \le (a_3, b_3)$.

The same steps work for any reduced product, with "in every coordinate" replaced by "on a set in the filter".
A trap is the disjunction $x \le y \vee y \le x$: the coordinates of a pair may satisfy different disjuncts, and then the product satisfies neither.

### L3 human

The theory of universal Horn classes is the first-order shadow of equational logic.
When the signature has a constant symbol, a strict universal Horn theory has an initial model.
Its elements are the closed terms modulo the equations that the theory proves, its relations are the atomic facts that the theory proves, and it maps into every other model by a unique homomorphism.
This is the reason why logic programming and term rewriting use Horn clauses.
On the semantic side, $\mathbf{I}\mathbf{S}\mathbf{P}_R$ is a closure operator whose closed classes are the universal Horn classes, as $\mathbf{I}\mathbf{S}\mathbf{P}_U$ is for universal classes and $\mathbf{H}\mathbf{S}\mathbf{P}$ is for varieties by [[Birkhoff's theorem|5083DHSK82]].
The step from universal Horn sentences to arbitrary Horn sentences, with quantifiers in any order, is the subject of [[Horn sentences and reduced products|1FF2GRE6VX]].
