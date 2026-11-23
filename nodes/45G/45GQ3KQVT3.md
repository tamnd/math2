---
tag: 45GQ3KQVT3
kind: definition
name: Theories of iterated inductive definitions
msc: ["03F15", "03F35"]
topics: [XTTKZTYDSD]
audience: research
defines: 5VNT564Y2W
uses: [0QFT7Z76N5, 5NVA2JRHPV, 0ZHQMQ2C1N, DBD64TH52D, CK8ZQRN183]
sources:
  - url: https://en.wikipedia.org/wiki/Theories_of_iterated_inductive_definitions
    locator: Original definition
  - url: https://en.wikipedia.org/wiki/Theories_of_iterated_inductive_definitions
    locator: Explanation / alternate definition
---

## Definition

These theories add to arithmetic a predicate for the least fixed point of each positive operator, once or along a well-ordering.

Let $\mathcal{L}$ be the language of [[Peano arithmetic|0QFT7Z76N5]], and let $X$ be a new unary predicate symbol.
A formula $A(X, x)$ is $X$-positive if no occurrence of $X$ is negated in its negation normal form.

### The theory ID₁

For each $X$-positive formula $A(X, x)$ of $\mathcal{L} \cup \{ X \}$ with no other free variables, add a unary predicate symbol $I_A$.
The axioms of $\mathrm{ID}_1$ are those of PA, with induction for all formulas of the extended language, and for each $A$ the two schemes below.
$$(\mathrm{ID}^1_A) \quad \forall x \, \big( A(I_A, x) \to I_A(x) \big)$$
$$(\mathrm{ID}^2_A) \quad \forall x \, \big( A(F, x) \to F(x) \big) \to \forall x \, \big( I_A(x) \to F(x) \big) \quad \text{for every formula } F(x)$$
Here $A(F, x)$ replaces each atom $X(t)$ by $F(t)$.

### The theory ID_ν

Let $\prec$ be a [[primitive recursive|5NVA2JRHPV]] well-ordering of type $\nu$ on a set of numbers, and let $Y$ be a binary predicate symbol.
For each $X$-positive formula $A(X, Y, \mu, x)$, in which $Y$ may also occur negatively, add a binary predicate symbol $P_A$.
Write $P^\mu_A(x)$ for $P_A(\mu, x)$, and $P^{\prec \mu}_A$ for $(\lambda, y) \mapsto \lambda \prec \mu \wedge P_A(\lambda, y)$.
The axioms of $\mathrm{ID}_\nu$ are PA with full induction and, for each $A$, the three schemes below.
$$(\mathrm{ID}^1_\nu) \quad \forall \mu \, \forall x \, \big( A(P^\mu_A, P^{\prec\mu}_A, \mu, x) \to P^\mu_A(x) \big)$$
$$(\mathrm{ID}^2_\nu) \quad \forall \mu \, \Big[ \forall x \, \big( A(F, P^{\prec\mu}_A, \mu, x) \to F(x) \big) \to \forall x \, \big( P^\mu_A(x) \to F(x) \big) \Big] \quad \text{for every formula } F$$
$$(\mathrm{TI}_\nu) \quad \forall \mu \, \big( \forall \lambda \, (\lambda \prec \mu \to G(\lambda)) \to G(\mu) \big) \to \forall \mu \, G(\mu) \quad \text{for every formula } G$$

## Notation

In $\mathrm{ID}_\nu$, stage $\mu$ is the least fixed point of the operator $A(\cdot, P^{\prec \mu}_A, \mu, \cdot)$, which may use the earlier stages in any way.
The scheme $(\mathrm{TI}_\nu)$ is [[transfinite induction|0ZHQMQ2C1N]] along $\prec$ for all formulas.
The theory $\mathrm{ID}_{<\nu}$ is the union of the theories $\mathrm{ID}_\mu$ for $\mu < \nu$, and $\mathrm{ID}^i_\nu$ is the same theory over [[Heyting arithmetic|CK8ZQRN183]].
Strictly, the theory depends on the ordering $\prec$ and not only on its type $\nu$, and one uses a standard ordering of each type.
Many sources write $J_A$ or $I^\mu_A$ instead of $P^\mu_A$.
The fixed-point variants replace $(\mathrm{ID}^2)$ by the converse of $(\mathrm{ID}^1)$, and much of the literature writes them $\widehat{\mathrm{ID}}_\nu$.

## Remarks

Each part of the definition has a job.
Positivity makes the operator monotone, so in the standard model the least fixed point exists, and $(\mathrm{ID}^1)$ with $(\mathrm{ID}^2)$ prove that $I_A$ is a fixed point.
Without it the axioms can hold for a set that is not a fixed point, as [[the operator ¬X|VF1N6N8ECC]] shows: there $I = \mathbb{N}$ satisfies both schemes, but $\neg \mathbb{N} \ne \mathbb{N}$.

The scheme $(\mathrm{ID}^2)$ is stated for every formula $F$, not only for sets, and this gives the strength of the theory.
Applied to the [[accessible part of an order|CRP7Z3M9XD]], it yields transfinite induction along the order on the accessible part, for every formula.
The scheme $(\mathrm{TI}_\nu)$ makes the stages well-ordered inside the theory, so a property of all stages can be proved by induction on $\mu$.

In $\mathrm{ID}_\nu$ the earlier stages may occur negatively, because they are already fixed when stage $\mu$ is defined.
The [[tree classes O₁ and O₂|PDVPG1SN9X]] are the standard instance in $\mathrm{ID}_2$: $\mathcal{O}_2$ branches over $\mathcal{O}_1$, and $\mathcal{O}_1$ stands negatively in its operator.
The ordinals of these theories, and their place in proof theory, are in the account of [[iterated inductive definitions|5VNT564Y2W]].

## Explanations

### L1 human

The definition gives a name to the smallest set that follows a rule.
Two axioms say what "smallest set that follows the rule" means: the named set follows the rule, and it is inside every other set that follows the rule.
In the iterated version there is a list of rules, indexed by a well-ordered list of stages.
The rule of a stage may talk freely about the sets of earlier stages.

### L2 human

We write out $\mathrm{ID}_1$ for the even numbers.
The operator is
$$A(X, x) = (x = 0) \vee \exists y \, (x = y + 2 \wedge X(y)),$$
and it is $X$-positive.
The axiom $(\mathrm{ID}^1_A)$ says $I_A(0)$, and $I_A(y) \to I_A(y + 2)$.
Take $F(x) = \exists z \, (x = 2z)$; then $A(F, x) \to F(x)$, so $(\mathrm{ID}^2_A)$ shows that every member of $I_A$ is even.
Induction on $z$ with the closure axiom puts every even number in $I_A$, so $\mathrm{ID}_1$ proves $I_A(x) \leftrightarrow \exists z \, (x = 2z)$.

This set is arithmetical, so $\mathrm{ID}_1$ adds nothing new here, and the strength comes from operators like accessible parts.
Watch out: $F$ may be any formula, including formulas that mention $I_A$ itself.
