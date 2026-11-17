---
tag: ME9J33BFNC
kind: statement
role: theorem
name: Prenex normal form theorem
aliases: [prenex-normal-form-theorem]
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
about: [CS82V969DE]
uses: [CS82V969DE, HYJ10AF6RT, 9CNGDRAMGC, 0JMR2HM2N2, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
    locator: Conversion to prenex form
  - url: https://en.wikipedia.org/wiki/Prenex_normal_form
    locator: Intuitionistic logic
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Statement

Let $\sigma$ be a signature, and let the domains of all $\sigma$-structures be nonempty.
For every $\sigma$-[[formula|HYJ10AF6RT]] $\varphi$ there is a $\sigma$-formula $\psi$ in [[prenex normal form|CS82V969DE]] with the following properties.

1. $\psi$ is [[logically equivalent|0JMR2HM2N2]] to $\varphi$: in every [[structure|983GZBQYT4]] and under every assignment, $\psi$ is true exactly when $\varphi$ is true.
2. $\psi$ has the same [[free variables|9CNGDRAMGC]] as $\varphi$, that is, $\operatorname{FV}(\psi) = \operatorname{FV}(\varphi)$.
3. $\psi$ is computed from $\varphi$ by an algorithm.

## Remarks

### Why each hypothesis is needed

1. Nonempty domains. The proof uses the rule $(\forall x \, \varphi) \to \chi \equiv \exists x \, (\varphi \to \chi)$ for $x \notin \operatorname{FV}(\chi)$. In the empty structure, $(\forall x \, P(x)) \to \forall y \, (y = y)$ is true, but $\exists x \, (P(x) \to \forall y \, (y = y))$ is false.
2. Classical logic. The proof uses $\neg \forall x \, \varphi \equiv \exists x \, \neg \varphi$, which fails in [[intuitionistic logic|Q11N8X99FK]]. There, not every formula is equivalent to a prenex formula.
3. Equivalence is taken under every assignment, not only for sentences. This makes the theorem usable inside larger formulas, by the replacement of equivalent subformulas.

### Consequences

1. Every formula has a prefix type, such as $\forall \exists \forall$. This gives the classes $\Sigma_n$ and $\Pi_n$ of the [[arithmetical hierarchy|7CVJCQKY41]].
2. Every sentence has a [[Skolem normal form|GCPQGMJYEV]], by the [[Skolem normal form theorem|Q5H7C57VNH]] applied to a prenex form.
3. The matrix of $\psi$ is quantifier-free, so it can be put in [[conjunctive normal form|0B3D4C8YF2]] by propositional rules. This is the input format of resolution provers.

### Converse

Every formula in prenex normal form is a formula, so the converse is trivial.
The prenex form is not unique.
For example, $\forall x \, P(x) \land \exists y \, Q(y)$ is equivalent to $\forall x \, \exists y \, (P(x) \land Q(y))$ and to $\exists y \, \forall x \, (P(x) \land Q(y))$.

### Generalizations

1. The theorem holds in [[many-sorted logic|7TDHDN8P96]], with the same proof, when every sort has a nonempty domain.
2. Modulo a theory $T$ with quantifier elimination, every formula is $T$-equivalent to a prenex formula with an empty prefix.
3. The proof gives a prenex form whose prefix variables are pairwise distinct and differ from the free variables.

## History

Skolem used prenex forms in his papers of 1920 and 1922 on the Löwenheim-Skolem theorem.
Hilbert and Ackermann's book of 1928 presented the conversion to prenex form as a standard tool of the predicate calculus.

## Explanations

### L1 human

Every formula can be rewritten so that all quantifiers stand at the front.
The new formula means the same thing in every situation.
For example, "if everyone is happy, then Ann is happy" becomes "there is someone such that if that person is happy, then Ann is happy".
Both sentences are true in every situation with at least one person.

### L2 human

We put $\varphi = \neg \forall x \, P(x) \lor \exists x \, Q(x)$ in prenex form.

1. By $\neg \forall x \, P(x) \equiv \exists x \, \neg P(x)$, the formula is equivalent to $\exists x \, \neg P(x) \lor \exists x \, Q(x)$.
2. The second $x$ clashes with the first one, so we rename it: $\exists x \, Q(x) \equiv \exists y \, Q(y)$.
3. Now $x$ is not free in $\exists y \, Q(y)$, so the first quantifier moves out: $\exists x \, (\neg P(x) \lor \exists y \, Q(y))$.
4. Then $y$ is not free in $\neg P(x)$, so the second one moves out: $\exists x \, \exists y \, (\neg P(x) \lor Q(y))$.

The typical use is to read off the quantifier type, here $\exists \exists$.
A trap: merging the two quantifiers gives $\exists x \, (\neg P(x) \lor Q(x))$.
This is correct here, because $\exists$ distributes over $\lor$.
With $\land$ in place of $\lor$, the same shortcut changes the meaning.

### L3 human

The theorem shows that classical first-order formulas are, up to equivalence, words in a quantifier prefix over a propositional matrix.
The prefix is a game: the $\forall$ player and the $\exists$ player choose elements in turn, and the matrix decides the winner.
Skolem functions are the strategies of the $\exists$ player.
The number of quantifier alternations is the measure behind the arithmetical and the polynomial hierarchies.
The prenex form given by the proof can be exponentially longer than $\varphi$, because each $\leftrightarrow$ doubles its arguments.
Intuitionistically, the equivalences that move a quantifier out of an antecedent or a negation fail, so constructive logic has no prenex theorem.
