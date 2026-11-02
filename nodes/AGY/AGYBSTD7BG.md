---
tag: AGYBSTD7BG
kind: statement
role: theorem
name: Łoś's theorem
msc: [03C20]
uses: [AX9Q86GB8M, J64Y3JC0RE, HYJ10AF6RT]
about: [AX9Q86GB8M]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
---

## Statement

Let $L$ be a signature, let $\mathcal{U}$ be an [[ultrafilter|J64Y3JC0RE]] on a nonempty set $I$, and let $(M_i)_{i \in I}$ be $L$-structures with nonempty domains.
Let $M = \prod_{i \in I} M_i / \mathcal{U}$ be their [[ultraproduct|AX9Q86GB8M]].
Let $\varphi(x_1, \dots, x_n)$ be a first-order [[$L$-formula|HYJ10AF6RT]], and let $a_1, \dots, a_n \in \prod_{i \in I} M_i$.
Then
$$M \models \varphi([a_1], \dots, [a_n]) \iff \set{i \in I : M_i \models \varphi(a_1(i), \dots, a_n(i))} \in \mathcal{U}.$$

## Remarks

The proof is an induction on the formula.
Atomic formulas hold by the definition of the ultraproduct, and conjunction uses that $\mathcal{U}$ is closed under finite intersections.
Negation uses that $\mathcal{U}$ contains exactly one of each set and its complement, which is where the ultrafilter property enters.
For $\exists y \, \psi$, the axiom of choice picks a witness $b(i)$ in each factor where one exists.

In particular, a sentence holds in an ultraproduct exactly when the set of factors where it holds lies in $\mathcal{U}$.
For an ultrapower $M^I / \mathcal{U}$, the diagonal map $m \mapsto [(m, m, \dots)]$ is an elementary embedding of $M$.
For example, every ultrapower of $\R$ is a real closed ordered field, since these properties are first-order.
The theorem also gives a proof of the compactness theorem.
If every finite subset of a theory $T$ has a model, an ultraproduct of these models over a suitable ultrafilter is a model of $T$.

The ultrafilter is necessary: for a filter that is not an ultrafilter, the corresponding reduced product of fields can fail to be a field.

## Explanations

### L1 human

An ultraproduct glues many structures into one, and an ultrafilter decides which sets of indices count as "most".
Łoś's theorem says that a first-order statement is true in the glued structure exactly when it is true in "most" of the pieces.
So the glued structure keeps every first-order property that most pieces share.

### L2 human

Łoś's theorem is the reason ultraproducts are useful in model theory.
It gives the compactness theorem without any proof system, and it shows that a class of structures closed under ultraproducts and elementary equivalence is axiomatisable.
With a non-principal ultrafilter on $\N$, the ultrapower of $\R$ gives the hyperreal numbers, and the theorem becomes the transfer principle of nonstandard analysis.
Ultraproducts of the finite fields $\F_p$, indexed by the primes $p$, over a non-principal ultrafilter are fields of characteristic $0$.
This links statements about large primes with statements in characteristic $0$.
