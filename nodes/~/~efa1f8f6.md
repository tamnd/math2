---
tag: ~efa1f8f6
kind: statement
role: theorem
name: Tautologies and duality of LP and K3
aliases: [lp-k3-duality]
msc: ["03B53", "03B50"]
topics: [NJB94B39QK]
audience: ug2
about: [~26a0362d, SZHA10A9X7]
uses: [~655488d6, 05006AJ7DZ, SZHA10A9X7, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
  - book: isbn:9780521670265
---

## Statement

Let $\vDash_{\mathrm{LP}}$ and $\vDash_{\mathrm{K3}}$ be the consequence relations of the [[logic of paradox|~655488d6]] and of [[strong Kleene logic|SZHA10A9X7]].

1. A formula is an LP tautology if and only if it is a classical [[tautology|05006AJ7DZ]].
2. K3 has no tautologies: for every formula $\varphi$ there is a valuation $v$ with $v(\varphi) \neq 1$.
3. For formulas $\gamma_1, \ldots, \gamma_n$ with $n \geq 1$ and $\varphi$,
$$\gamma_1, \ldots, \gamma_n \vDash_{\mathrm{LP}} \varphi \quad\text{if and only if}\quad \neg\varphi \vDash_{\mathrm{K3}} \neg\gamma_1 \lor \cdots \lor \neg\gamma_n.$$

In particular $\gamma \vDash_{\mathrm{LP}} \varphi$ if and only if $\neg\varphi \vDash_{\mathrm{K3}} \neg\gamma$.

## Remarks

### Why each hypothesis is needed

- Part 1 needs the designated set $\set{1, \tfrac12}$. With only $1$ designated, part 2 shows that no formula is a tautology.
- Part 3 needs $n \geq 1$, because the empty disjunction is not a formula. For $n = 0$ the right analogue is: $\varphi$ is an LP tautology if and only if no K3 valuation designates $\neg\varphi$.
- Part 3 uses that [[negation|029JBBF693]] is $a \mapsto 1 - a$. For a negation that does not swap $\set{1}$ with $\set{0}$, the duality fails.

### Consequences

- LP and classical logic have the same theorems but different inferences: explosion and modus ponens fail in LP.
- Every LP-invalid inference gives a K3-invalid inference by part 3. For example, $p, \neg p \nvDash_{\mathrm{LP}} q$ gives $\neg q \nvDash_{\mathrm{K3}} \neg p \lor \neg\neg p$, a failure of excluded middle in K3.
- Since LP is paraconsistent, K3 is paracomplete, and the converse also holds by part 3.

### Converse

The two directions of part 3 are each other's converse, and both hold.
Part 1 is also an equivalence; the direction from LP tautology to classical tautology is the easy one.

### Generalizations

- In multiple-conclusion form, $\Gamma \vDash_{\mathrm{LP}} \Delta$ if and only if $\neg\Delta \vDash_{\mathrm{K3}} \neg\Gamma$. Here $\Gamma \vDash \Delta$ means that every valuation that designates all of $\Gamma$ designates some member of $\Delta$, and $\neg\Gamma = \set{\neg\gamma : \gamma \in \Gamma}$. The same proof applies, and it also covers empty $\Gamma$ and infinite sets.
- For four-valued FDE, the same argument shows that FDE is self-dual: $\gamma \vDash_{\mathrm{FDE}} \varphi$ if and only if $\neg\varphi \vDash_{\mathrm{FDE}} \neg\gamma$.

## History

Kleene introduced the strong three-valued tables, and Priest introduced LP in 1979.
Wikipedia states part 2 with the valuation that gives every atom the middle value.
The [[proof|~8088dd79]] uses the monotonicity of the strong Kleene tables in the information order.

## Explanations

### L1 human

LP and K3 share their tables but differ in what counts as accepted.
LP accepts "true" and "both"; K3 accepts only "true".
The theorem says three things.
LP accepts exactly the classical laws of logic.
K3 accepts no law at all, since a formula whose letters are all unknown is unknown.
And a valid LP argument, turned around and negated, is a valid K3 argument.

### L2 human

We test part 3 with $\gamma = p$ and $\varphi = p \lor q$.

1. $p \vDash_{\mathrm{LP}} p \lor q$, since $\max(v(p), v(q)) \geq v(p) > 0$ when $v(p) > 0$.
2. Part 3 predicts $\neg(p \lor q) \vDash_{\mathrm{K3}} \neg p$.
3. If $v(\neg(p \lor q)) = 1$, then $\max(v(p), v(q)) = 0$, so $v(p) = 0$ and $v(\neg p) = 1$.

So the prediction holds.
A trap is to apply part 3 with $\vDash_{\mathrm{LP}}$ on both sides; the logics swap.

### L3 human

Let $\sqsubseteq$ be the information order with $\tfrac12$ below $0$ and $1$.
The K3 designated set $\set{1}$ is the image of the LP undesignated set $\set{0}$ under $a \mapsto 1 - a$.
This makes $\neg$ an isomorphism between the LP matrix and the dual of the K3 matrix, which is the abstract form of part 3.
Part 1 is a form of the fact that a three-valued valuation is a partial classical valuation, so every refinement to a classical valuation agrees where the value is classical.
