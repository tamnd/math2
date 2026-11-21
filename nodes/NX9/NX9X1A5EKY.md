---
tag: NX9X1A5EKY
kind: definition
name: Universal class
aliases: [universal-class-definition]
msc: ["03C52", "03C40"]
topics: [JYJHB4YBAH]
audience: grad
defines: ZSTEZ3PRT9
uses: [WDVVEYD6AT, 983GZBQYT4, DKFGQTRYZE, 0GHS47PDAQ, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: Definition
  - book: isbn:9780521587136
---

## Definition

Let $L$ be a first-order [[signature|WDVVEYD6AT]].
A *universal sentence* of $L$ is a [[sentence|DKFGQTRYZE]] of the form $\forall x_1 \cdots \forall x_n \, \theta$, with $n \ge 0$ [[universal quantifiers|0GHS47PDAQ]].
Here $\theta$ is a quantifier-free formula whose free variables are among $x_1, \ldots, x_n$.
Let $\mathcal{K}$ be a class of [[$L$-structures|983GZBQYT4]].
Then $\mathcal{K}$ is a *universal class* if there is a set $\Sigma$ of universal sentences of $L$ whose [[models|MVCH6N9SNW]] are exactly the members of $\mathcal{K}$.
A theory is *universal* if all its sentences are universal.

## Notation

Some authors write $\forall_1$-axiomatizable or $\Pi_1$-axiomatizable class.
The universal theory $\mathrm{Th}_\forall(\mathcal{K})$ is the set of universal sentences true in all members of $\mathcal{K}$, and $\mathcal{K}$ is universal exactly when it is the class of models of $\mathrm{Th}_\forall(\mathcal{K})$.

## Remarks

- Replacing an axiom by a logically equivalent sentence does not change the class. So it is enough that each axiom be equivalent to a universal sentence, for example through a [[prenex normal form|CS82V969DE]].
- Example: simple graphs form a universal class, with the axioms $\forall x \, \neg E(x, x)$ and $\forall x \forall y \, (E(x, y) \rightarrow E(y, x))$.
- Non-example: fields in the signature $\set{+, -, \cdot, 0, 1}$. A universal sentence true in a structure is true in each [[substructure|676H7EGTKJ]], and the subring $\mathbb{Z}$ of the field $\mathbb{Q}$ is not a field.
- Every universal class is an [[elementary class|MEC3ZMC4F1]]. The [[Łoś-Tarski theorem|9RN0KYXNT1]] shows that an elementary class is universal exactly when it is closed under substructures.
- The concept page is [[universal class|ZSTEZ3PRT9]], and the characterization by closure properties is [[this theorem|JPGDSW2TAP]].

## Explanations

### L1 human

A universal axiom begins with "for all" and then states a condition with no further "there exists".
A class is universal when such axioms describe it exactly.
For example, "for all $x$, $x$ is not linked to itself" is universal.

### L2 human

We write the class of graphs without a vertex of degree at least $3$ as a universal class.

1. Use the graph axioms $\forall x \, \neg E(x, x)$ and $\forall x \forall y \, (E(x, y) \rightarrow E(y, x))$.
2. Add $\forall x \forall y_1 \forall y_2 \forall y_3 \, \neg(E(x, y_1) \wedge E(x, y_2) \wedge E(x, y_3) \wedge y_1 \ne y_2 \wedge y_1 \ne y_3 \wedge y_2 \ne y_3)$.
3. A graph satisfies the new axiom exactly when no vertex has three distinct neighbors.
4. All three axioms are universal, so the class is universal.

The typical use is to read off a universal axiom from a forbidden pattern.
A trap is the class of graphs with every degree at least $1$: the axiom $\forall x \, \exists y \, E(x, y)$ is not universal, and an isolated vertex is a substructure of an edge.
