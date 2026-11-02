---
tag: NX9X1A5EKY
kind: definition
name: Universal class
msc: ["03C52", "03C40"]
defines: ZSTEZ3PRT9
uses: [WDVVEYD6AT, 983GZBQYT4, DKFGQTRYZE, 0GHS47PDAQ]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
---

## Definition

Let $\sigma$ be a first-order [[signature|WDVVEYD6AT]].
A *universal sentence* of $\sigma$ is a [[sentence|DKFGQTRYZE]] of the form $\forall x_1 \cdots \forall x_n \, \varphi$, with $n \ge 0$ [[universal quantifiers|0GHS47PDAQ]].
Here $\varphi$ is a quantifier-free formula whose free variables are among $x_1, \ldots, x_n$.
Let $K$ be a class of [[$\sigma$-structures|983GZBQYT4]].
Then $K$ is a *universal class* if there is a set $\Sigma$ of universal sentences of $\sigma$ whose models are exactly the members of $K$.

## Remarks

Example: simple graphs, in the signature with one binary relation $E$, form a universal class with the axioms $\forall x \, \neg E(x, x)$ and $\forall x \forall y \, (E(x, y) \rightarrow E(y, x))$.

Non-example: fields, in the signature $(+, -, \cdot, 0, 1)$, do not form a universal class.
A universal sentence true in a structure is true in each [[substructure|676H7EGTKJ]], because it only speaks about tuples of elements and the operations on them.
The ring $\Z$ is a substructure of the field $\Q$ in this signature, and it is not a field.

Every universal class is an [[elementary class|MEC3ZMC4F1]].
The [[Łoś–Tarski preservation theorem|9RN0KYXNT1]] gives the converse characterization: an elementary class is universal exactly when it is closed under substructures.
