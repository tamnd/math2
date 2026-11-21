---
tag: ~00cd7ceb
kind: concept
name: Preservation theorems
aliases: [preservation-theorems-model-theory, preservation-theorem]
msc: ["03C40", "03C52"]
topics: [JYJHB4YBAH]
audience: grad
uses: [92SWXST1ZM, MVCH6N9SNW, 1NR3HAWG9D, EP5E317TNW, 676H7EGTKJ, KBXSZC6BV1, F4WRD396PB, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Łoś–Tarski_preservation_theorem
    locator: lead section
  - book: isbn:9780521587136
---

## Summary

Let $\mathsf{C}$ be a construction that makes new $L$-structures from old ones, such as taking a [[substructure|676H7EGTKJ]] or a [[homomorphic|KBXSZC6BV1]] image, and let $\Phi$ be a syntactic class of first-order [[formulas|HYJ10AF6RT]].
A *preservation theorem* for $(\mathsf{C}, \Phi)$ says that a first-order [[theory|92SWXST1ZM]] $T$ has a class of [[models|MVCH6N9SNW]] closed under $\mathsf{C}$ if and only if $T$ is equivalent to a set of sentences in $\Phi$.
The sentence form says that a sentence $\varphi$ is preserved by $\mathsf{C}$ if and only if $\varphi$ is logically equivalent to a sentence in $\Phi$.
One direction is always an induction on formulas: sentences in $\Phi$ survive $\mathsf{C}$.
The other direction is the content, and it uses the [[compactness theorem|1NR3HAWG9D]].
Preservation theorems turn a question about how models behave into a question about the shape of the axioms.

## Motivation

The group axioms in the signature $\set{\cdot, {}^{-1}, e}$ are universal, and subgroups are again groups.
Field axioms need "there exists an inverse", and the subring $\mathbb{Z}$ of the field $\mathbb{Q}$ is not a field.
This suggests a rule: universal axioms go down to substructures and existential axioms may fail to.
One then asks whether the rule is sharp.
If a class of models is closed under substructures, can one always rewrite its axioms as universal sentences?
The Łoś-Tarski theorem says yes, and the same pattern repeats for other constructions.
So the syntax of the axioms is not an accident of presentation; it is forced by the closure properties of the class.

## Notation

- A formula is *universal* ($\forall_1$, or $\Pi_1$) if it has the form $\forall \bar x \, \theta$ with $\theta$ quantifier-free, and *existential* ($\exists_1$, or $\Sigma_1$) if it has the form $\exists \bar x \, \theta$.
- A formula is $\forall\exists$ ($\forall_2$, or $\Pi_2$) if it has the form $\forall \bar x \, \exists \bar y \, \theta$ with $\theta$ quantifier-free. Every formula is equivalent to a [[prenex|CS82V969DE]] one, so these classes are taken up to equivalence.
- A formula is *positive* if it is built from atomic formulas, $\top$ and $\bot$ with $\wedge$, $\vee$, $\forall$ and $\exists$ only. It is *existential-positive* if it uses no $\forall$.
- "$\varphi$ is preserved by $\mathsf{C}$" means: if the input structures satisfy $\varphi$, then the output structure satisfies $\varphi$.

## Remarks

### Examples

The classical preservation theorems are the following.

| Construction | Syntactic form | Theorem |
|---|---|---|
| substructures | universal | [[Łoś-Tarski|9RN0KYXNT1]] |
| extensions | existential | [[Łoś-Tarski|9RN0KYXNT1]], dual form |
| unions of chains | $\forall\exists$ | [[Chang-Łoś-Suszko|~99a892b2]] |
| surjective homomorphic images | positive | [[Lyndon|~79a402be]] |
| homomorphic images | existential-positive | homomorphism preservation theorem |
| reduced products | Horn | [[Keisler and Galvin|~a403cb4d]] |
| substructures and ultraproducts, for classes | universal | [[universal classes|~f72a8819]] |
| substructures and reduced products, for classes | universal Horn | [[universal Horn classes|~b2077580]] |
| ultraproducts and elementary equivalence, for classes | first-order | [[elementary classes|4HNAJQQ8Z0]] |

The definability theorems of [[Beth|RJBDSA2ETP]], [[Svenonius|~8495e2be]] and [[Chang and Makkai|~09dc0606]] follow the same pattern for a new relation symbol, with automorphisms as the construction.

### Non-examples

- Direct products. Horn sentences are preserved by direct products, but Chang and Morel showed that an elementary class closed under direct products need not be axiomatized by Horn sentences. So the pair (direct products, Horn) is not a preservation theorem.
- Finite structures. The Łoś-Tarski theorem fails when one considers only finite structures; the counterexample is in [[Łoś-Tarski|9RN0KYXNT1]]. Lyndon's theorem also fails in the finite.

### Basic properties

- The easy direction holds in every case by induction on formulas, and it holds for finite structures too.
- The hard direction proves more than the existence of axioms: the axioms can be taken to be the consequences of $T$ in $\Phi$.
- A sentence version follows from a theory version by compactness when $\Phi$ is closed under finite conjunctions.
- Each theorem has a relative form: a formula is preserved between models of $T$ if and only if it is equivalent modulo $T$ to a formula in $\Phi$.

### History

The Łoś-Tarski theorem, Lyndon's theorem and the homomorphism preservation theorem date from the 1950s.
Alfred Horn studied the sentences preserved by direct products in 1951, and Roger Lyndon published his theorem on homomorphisms in 1959.
Keisler proved the characterization of Horn sentences in 1965 under the continuum hypothesis, and Fred Galvin removed this hypothesis.
In 1959 William Tait showed that the Łoś-Tarski theorem fails over finite structures.
Benjamin Rossman showed in 2008 that the homomorphism preservation theorem survives over finite structures.

### Common errors

- To think that the theorem gives one universal sentence for one preserved sentence by a short syntactic trick. The proof only shows that a universal sentence exists, by compactness.
- To use the finite case without care. A sentence preserved by substructures of finite structures need not be equivalent on finite structures to a universal sentence.
- To confuse "preserved by surjective homomorphisms" with "preserved by all homomorphisms". The first gives positive sentences; the second gives existential-positive ones.

## Explanations

### L1 human

Some rules about a structure only forbid patterns, like "no point is linked to itself".
If a big structure follows such a rule, every part of it follows the rule too.
Other rules ask for something to exist, like "every number has a half".
Every fraction has a half among the fractions, but the whole number $1$ has no half among the whole numbers.
So this rule holds for the fractions and fails for a part of them.
A preservation theorem says that the way a family of structures reacts to an operation tells exactly which type of rule describes it.

### L2 human

We use the table to decide whether the class of groups in the signature $\set{\cdot}$ has universal axioms.

1. The positive integers under addition are a substructure of the group $(\mathbb{Z}, +)$ in the signature $\set{+}$.
2. The positive integers have no neutral element for $+$, so they do not form a group.
3. So the class of groups in this signature is not closed under substructures.
4. By the easy direction of Łoś-Tarski, no set of universal axioms in $\set{\cdot}$ describes the groups.

The typical use is negative: one closure failure rules out a whole syntactic form.
A trap is to forget the signature: with $e$ and ${}^{-1}$ in the signature, the class of groups is universal.

### L3 human

All the classical proofs follow one plan.
Let $T_\Phi$ be the set of consequences of $T$ in $\Phi$, and let $A \models T_\Phi$.
One uses compactness and the method of [[diagrams|EP5E317TNW]] to find a model $B$ of $T$ that is related to $A$ by a chain of the constructions, often together with elementary extensions.
Closure under the construction then gives $A \models T$.
For unions of chains and for surjective homomorphisms, the chain is infinite, and the elementary chain theorem holds it together.

Without compactness the plan breaks, and finite model theory shows this: Łoś-Tarski and Lyndon fail, while Rossman's homomorphism preservation theorem for finite structures needs a new combinatorial proof.
In abstract model theory, [[Lindström's theorem|FYZ3CJGZYV]] explains why compactness is special to first-order logic.
The same pattern appears in universal algebra, where [[Birkhoff's HSP theorem|5083DHSK82]] matches closure under homomorphic images, subalgebras and products with equational axioms.
