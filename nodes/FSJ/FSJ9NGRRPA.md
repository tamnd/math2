---
tag: FSJ9NGRRPA
kind: statement
role: theorem
name: Quantifier elimination for real closed fields
msc: [03C10, 12L12, 12D15]
uses: [0P3VCBDEE2]
sources:
  - url: https://en.wikipedia.org/wiki/Real_closed_field
---

## Statement

Let $\mathcal{L} = \set{+, -, \cdot, 0, 1, <}$ be the language of ordered rings.
Let $\mathrm{RCF}$ be the $\mathcal{L}$-theory of real closed fields with their unique field ordering.
Its axioms are those of an [[ordered field|0P3VCBDEE2]], together with two more.
One axiom says that every positive element has a square root.
One scheme says that every polynomial of odd degree has a root.
Then $\mathrm{RCF}$ admits quantifier elimination: for every $\mathcal{L}$-formula $\varphi(x_1, \dots, x_n)$ there is a quantifier-free $\mathcal{L}$-formula $\psi(x_1, \dots, x_n)$ such that
$$\mathrm{RCF} \vdash \forall x_1 \cdots \forall x_n \, \bigl(\varphi(x_1, \dots, x_n) \leftrightarrow \psi(x_1, \dots, x_n)\bigr).$$

## Remarks

The theorem is due to Tarski.
It suffices to eliminate one existential quantifier in front of a conjunction of polynomial equations and inequalities in one variable $x$.
Such a conjunction has a solution exactly when certain sign conditions on the coefficients hold.
These conditions can be computed, for instance with Sturm sequences and the intermediate value property of polynomials over a real closed field.

Example: for real closed fields,
$$\exists x \, (x^2 + b x + c = 0) \quad \leftrightarrow \quad b^2 - 4c > 0 \ \lor \ b^2 - 4c = 0.$$

Consequences: $\mathrm{RCF}$ is complete, so every real closed field satisfies the same first-order sentences as $\R$; and $\mathrm{RCF}$ is decidable.
Geometrically, the projection of a semialgebraic set is semialgebraic, which is the Tarski–Seidenberg theorem.

The symbol $<$ is necessary.
In the language of rings alone, the set $\set{x \in \R : \exists y \, (x = y^2)} = [0, \infty)$ is definable, but every quantifier-free definable subset of $\R$ in that language is finite or cofinite.

## Explanations

### L1 human

A statement about real numbers that uses "there exists" and "for all", together with addition, multiplication and order, can be rewritten without "there exists" and "for all".
What remains is a combination of polynomial equations and inequalities in the free variables.
For example, "the quadratic $x^2 + bx + c$ has a real root" is the same as "$b^2 - 4c \ge 0$".
So every such question about the real numbers can, in principle, be decided by a computation.

### L2 human

Quantifier elimination is the model-theoretic core of real algebraic geometry.
It shows that the sets definable in $\R$ with $+$, $\cdot$ and $<$ are exactly the semialgebraic sets, and that projections and images under polynomial maps stay in this class.
It gives the completeness of the theory of real closed fields, which transfers results from $\R$ to every real closed field.
This transfer gives a short modern proof of Artin's solution of [[Hilbert's seventeenth problem|J45F4F13VB]].
It also shows that the theory of $\R$ is o-minimal: every definable subset of the line is a finite union of points and intervals.
The analogous result for [[algebraically closed fields|MT8TDVPBXB]] uses only the language of rings.
