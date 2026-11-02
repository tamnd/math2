---
tag: WDHWCQ6Y2Y
kind: statement
role: theorem
name: Birkhoff's completeness theorem
msc: [08B05, 03C05]
uses: [72S3YSQFZ7, PKD440G2XW, F1M51B4MDG]
about: [72S3YSQFZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Equational_logic
---

## Statement

Let $\sigma$ be a signature with only function symbols and let $X$ be an infinite set of variables.
Let $\Sigma$ be a set of [[identities|PKD440G2XW]] over $\sigma$ and $X$.
For every identity $s \approx t$ over $\sigma$ and $X$, the following are equivalent:

1. $\Sigma \vdash s \approx t$, that is, $s \approx t$ is derivable from $\Sigma$ in [[equational logic|72S3YSQFZ7]];
2. $\Sigma \models s \approx t$, that is, every algebra of signature $\sigma$ that satisfies all identities of $\Sigma$ satisfies $s \approx t$.

## Remarks

Soundness, from 1 to 2, holds because each rule of equational logic preserves truth in every algebra.
For completeness, let $\theta$ be the set of pairs $(u, v)$ of terms with $\Sigma \vdash u \approx v$.
The rules say that $\theta$ is a congruence of the term algebra that is invariant under substitutions, and the quotient of the term algebra by $\theta$ satisfies $\Sigma$.
Evaluating $s$ and $t$ in this quotient at the assignment $x \mapsto x/\theta$ gives $s/\theta$ and $t/\theta$, so if $\Sigma \models s \approx t$ then $(s, t) \in \theta$.
The quotient is the free algebra on $X$ of the variety defined by $\Sigma$.

Consequence: a set of identities is an [[equational theory|F1M51B4MDG]] exactly when it contains all identities $t \approx t$ and is closed under the rules of symmetry, transitivity, replacement and substitution.

## Explanations

### L1 human

The theorem says that equational reasoning is enough.
If a law follows from some given laws in every possible algebra, then it can be proved from them by plugging in, replacing equals by equals, and chaining equalities.
Nothing more powerful, such as case analysis or quantifier tricks, is ever needed for this kind of conclusion.

### L2 human

This is the equational analogue of Gödel's completeness theorem, with a much simpler set of rules.
The proof builds a canonical model: the term algebra divided by provable equality, which is the free algebra of the variety defined by $\Sigma$.
Together with Birkhoff's HSP theorem, it sets up the correspondence between varieties of algebras and equational theories.
It also justifies term rewriting: a rewriting proof of $s \approx t$ is a derivation in equational logic, and every true consequence has such a derivation, though finding it may be undecidable.
