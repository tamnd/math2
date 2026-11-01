---
tag: FKF9YGBKHF
kind: object
name: Complex p-adic numbers
msc: [12J25, 11S80]
instance_of: [0PF6TM8TWT]
uses: [BT6T702C28, 0MCXX29HWY, KFYW0WN9AD, 1H5F1BP6XS]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_number
---

## Description

Let $p$ be a prime and let $\Q_p$ be the field of [[p-adic numbers|BT6T702C28]] with the $p$-adic absolute value $\abs{\cdot}_p$.
Let $\overline{\Q}_p$ be an [[algebraic closure|0MCXX29HWY]] of $\Q_p$.
Because $\Q_p$ is complete, $\abs{\cdot}_p$ extends in exactly one way to an absolute value on $\overline{\Q}_p$, and this extension is a [[non-Archimedean absolute value|1H5F1BP6XS]].
The field $\overline{\Q}_p$ is not complete for it.
The field $\C_p$ of *complex $p$-adic numbers* is the [[completion|KFYW0WN9AD]] of $\overline{\Q}_p$ for this absolute value.

The field $\C_p$ is an [[algebraically closed field|0PF6TM8TWT]] and it is complete.
The algebraic closedness follows from [[Krasner's lemma|G8PGN0WQHW]].
One approximates a monic polynomial over $\C_p$ by monic polynomials over $\overline{\Q}_p$, whose roots lie in $\overline{\Q}_p$.
The roots of these approximations can be chosen to form a Cauchy sequence, and its limit in $\C_p$ is a root of the original polynomial.

## Remarks

The set of values $\abs{x}_p$ for $x \in \C_p^\times$ is $p^{\Q} = \set{p^r : r \in \Q}$, the same as for $\overline{\Q}_p$.
The residue field of $\C_p$ is an algebraic closure of the finite field $\F_p$.
The field $\C_p$ plays for $\Q_p$ the role that $\C$ plays for $\R$, but $\C_p$ has infinite degree over $\Q_p$.

## Explanations

### L1 human

To do analysis with $p$-adic numbers one wants a field where every polynomial has a root and every Cauchy sequence has a limit.
Adding all roots of polynomials to $\Q_p$ gives algebraic closedness but loses completeness.
Completing once more gives $\C_p$, and the surprise is that no new polynomial roots are needed after that.
