---
tag: HFTBG5PMXC
kind: concept
name: Model theory
msc: ["03C07", "03C98"]
topics: [AY09KYSW81]
audience: ug2
uses: [983GZBQYT4, 92SWXST1ZM, MVCH6N9SNW, K7XDVK5854, 086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Model_theory
    locator: lead section; Basic model-theoretic concepts
  - book: isbn:9780387987606
    locator: Chapter 1
  - book: isbn:9780521587136
    locator: Chapter 1
same_as:
  wikidata: Q467606
  wikipedia: Model theory
---

## Summary

*Model theory* is the branch of mathematical logic that studies the relation between formal [[theories|92SWXST1ZM]] and the [[structures|983GZBQYT4]] in which they are true.
Its basic objects are a [[signature|WDVVEYD6AT]] $L$, the first-order $L$-sentences, the $L$-structures, and the relation $\mathcal{M} \models \sigma$ of [[truth|K7XDVK5854]] between them.
A [[model|MVCH6N9SNW]] of a theory $T$ is a structure in which every sentence of $T$ is true.
Model theory asks which classes of structures a theory describes, which structures a theory cannot tell apart, and which sets a formula can define inside a structure.
The subject matters because its general theorems, such as the [[compactness theorem|1NR3HAWG9D]], give new results in algebra, number theory and geometry.

## Motivation

Many proofs in algebra use only a few axioms of the objects that they study.
A result about all fields of characteristic $0$ that follows from the field axioms holds in $\Q$, in $\R$ and in $\C$ at the same time.
So it is natural to study the axioms and the class of their models as mathematical objects.
Two questions then appear.
How much does a list of axioms determine its models?
And which sets and functions can the axioms see inside one model?
Model theory answers these questions with exact theorems, and the answers often show hidden structure in familiar objects.

## Notation

We write $\mathcal{M}, \mathcal{N}$ for structures and $M, N$ for their domains.
We write $\mathcal{M} \models \sigma$ when the sentence $\sigma$ is true in $\mathcal{M}$, and $\mathcal{M} \models \varphi(\bar{a})$ when the formula $\varphi(\bar{x})$ is satisfied by the tuple $\bar{a}$.
Some books write $\mathcal{M} \models \varphi[\bar{a}]$ instead of $\mathcal{M} \models \varphi(\bar{a})$.
The words "structure", "model" and "algebra" are used for the same object in different books; in math2 a model is a structure together with a theory that it satisfies.
$\operatorname{Th}(\mathcal{M})$ is the [[theory of the structure|~305c87e7]] $\mathcal{M}$, and $\operatorname{Mod}(T)$ is the class of models of $T$.

## Remarks

### Examples

- The ordered sets $(\Q, <)$ and $(\R, <)$ satisfy exactly the same first-order sentences, so first-order logic cannot see the difference between countable and uncountable here; see [[this example|~aba9d1ce]].
- The field $\C$ and the field of algebraic numbers satisfy the same sentences, because the theory of algebraically closed fields of characteristic $0$ is [[complete|655K8Y7VS8]]; see [[this example|~81e191f1]].
- In the field $\R$, the formula $\exists y \, (y \cdot y = x)$ defines the set $[0, \infty)$, so the order of $\R$ is [[definable|CY1TXHF6KQ]] from the field operations.
- The [[compactness theorem|1NR3HAWG9D]] shows that the class of torsion groups is not an [[elementary class|MEC3ZMC4F1]]; see [[properties that are not first-order|~941125b4]].
- [[Nonstandard analysis|WM62GKCBWN]] builds an ordered field with infinitesimals that satisfies the same first-order sentences as $\R$ in a large language.

### Non-examples

- The computation of the homology groups of a sphere is not model theory: it uses no formal language and no relation of truth.
- The study of formal proofs as finite objects is [[proof theory|N4EDJNMTEF]], not model theory, although the [[completeness theorem|WQ1ZE255SF]] joins the two.

### Basic properties

- Two slogans describe the subject: "model theory = universal algebra + logic" (Chang and Keisler) and "model theory = algebraic geometry minus fields" (Hodges).
- The first slogan stresses structures and their maps: [[substructures|676H7EGTKJ]], [[embeddings|SCRB74SWQN]] and [[reducts and expansions|~ad0fa7f2]].
- The second slogan stresses [[definable sets|CY1TXHF6KQ]], which behave like the algebraic sets of algebraic geometry in many structures.
- [[Elementary equivalence|P3B1V182N4]] is weaker than isomorphism: by the [[Löwenheim-Skolem theorem|484M0TZ1S7]], an infinite structure in a countable signature is elementarily equivalent to structures of every infinite size.
- Pure model theory classifies complete theories by the behavior of their models ([[stable theories|T7JW5QY6KR]], [[NIP theories|74VCDYQDGP]]); tame geometry studies structures whose definable sets are simple, such as [[o-minimal|DTWHAW1N0V]] structures.

### History

Löwenheim (1915) and Skolem (1920) proved the first theorems about the sizes of models.
Gödel proved the completeness theorem in 1929, and Tarski gave the definition of truth in a structure in 1933.
Tarski and Abraham Robinson made model theory a separate branch of logic in the 1950s.
The [[history of model theory|~f440592a]] gives a longer account.

### Common errors

- To think that a theory with one model up to isomorphism is usual: an infinite structure always has non-isomorphic elementarily equivalent structures.
- To confuse $\models$ (truth in structures) with $\vdash$ (provability); the completeness theorem says that they agree for first-order logic, but they are different definitions.
- To think that model theory is only about logic: most of its present work concerns groups, fields and geometry.

## Explanations

### L1 human

Model theory looks at mathematics from two sides at once: the sentences that we write and the objects that make them true.
For example, the sentence "for all $x$ and $y$, $x \cdot y = y \cdot x$" is true in the integers with multiplication.
It is false in the group of symmetries of a triangle.
A typical question is: if two objects make the same sentences true, how alike must they be?
The answer is unexpected: the fractions and the real numbers, with their usual order, make the same sentences true, although there are many more real numbers.
Another question is: which sets of points can a sentence with variables describe inside one object?

### L2 human

We check that the sentence "the order is dense" separates $(\Z, <)$ from $(\Q, <)$.

1. The sentence is $\delta = \forall x \, \forall y \, (x < y \to \exists z \, (x < z \land z < y))$.
2. In $(\Q, <)$, for $x < y$ take $z = (x + y)/2$; then $x < z < y$, so $(\Q, <) \models \delta$.
3. In $(\Z, <)$, take $x = 0$ and $y = 1$; no integer $z$ satisfies $0 < z < 1$, so $(\Z, <) \models \neg\delta$.
4. So the two orders are not [[elementarily equivalent|P3B1V182N4]], and no [[isomorphism|PZMGQMDN25]] exists between them.

The typical use of model theory is the reverse step: to show that a statement holds in one structure, we show that it holds in another structure with the same theory.
A trap is to expect that every property of a structure is first-order: completeness of the order of $\R$ is not, because $(\Q, <)$ and $(\R, <)$ have the same theory.

### L3 human

A structure is a set with functions and relations, so model theory sits above universal algebra, and its maps are the [[embeddings|SCRB74SWQN]] and the [[elementary embeddings|CGH8C8EA9N]].
The definable sets of a structure form a family closed under Boolean operations and projections, and in many structures this family behaves like the constructible sets of algebraic geometry.
This view leads to the main branches of the area: [[ultraproducts|HZG1YP26AB]] and [[back-and-forth methods|N64R1MGDBN]] for elementary equivalence, [[types and saturation|Z772KEC9BY]] and [[categoricity|6XEXRME4C1]] for the classification of models.
It also leads to [[quantifier elimination|1A9JSC5YG8]] for the description of definable sets, and to [[stability|2T8HMVV8SB]], [[NIP|RS09CRTDRA]] and [[o-minimality|QS8ZBPAFJN]] for the classification of theories.
Applications go through the [[model theory of fields|Q3S2YF9BCR]] to [[Diophantine geometry|VYT6EX1HH1]].
Outside first-order logic, [[infinitary logics|VBYC17XY83]] and [[finite model theory|CBPS8B13S4]] ask the same questions for other logics and other classes of structures.
