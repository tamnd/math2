---
tag: AJEJS6TFWP
kind: definition
name: Logical matrix
msc: ["03B50", "03G27"]
topics: [WZP584JQ06]
audience: grad
defines: P7E926JK13
uses: [J78Y1M4GND, TFDYXS3K1N, EJ8YJVM9BW]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 3.1 Exploiting the algebraic structure of sentences; 3.2 Logical matrices and the designation-based notion of entailment
---

## Definition

Fix a propositional language with a set $C$ of connectives, each with an arity, and let $\mathrm{Fm}$ be the algebra of [[formulas|TFDYXS3K1N]].
An *algebra of type $C$* is a nonempty set $A$ with an $n$-ary [[operation|EJ8YJVM9BW]] $c^{\mathbf{A}} \colon A^n \to A$ for each $n$-ary connective $c$.

1. A *logical matrix* is a pair $M = \langle \mathbf{A}, D \rangle$ of an algebra $\mathbf{A}$ of type $C$ and a subset $D \subseteq A$, the set of *designated values*.
2. A *valuation* in $M$ is a homomorphism $h \colon \mathrm{Fm} \to \mathbf{A}$, that is, $h(c(\varphi_1, \dots, \varphi_n)) = c^{\mathbf{A}}(h(\varphi_1), \dots, h(\varphi_n))$. It is fixed by its values on the variables.
3. *Matrix consequence*: $\Gamma \models_M \varphi$ iff every valuation $h$ with $h[\Gamma] \subseteq D$ has $h(\varphi) \in D$.
4. For a class $\mathcal{K}$ of matrices, $\Gamma \models_{\mathcal{K}} \varphi$ iff $\Gamma \models_M \varphi$ for every $M \in \mathcal{K}$.
5. A matrix $M$ is a *model* of a [[consequence relation|J78Y1M4GND]] $\vdash$ when $\Gamma \vdash \varphi$ implies $\Gamma \models_M \varphi$.
6. For a consequence relation $\vdash$ on $\mathrm{Fm}$ and a closed set $T$, the matrix $\langle \mathrm{Fm}, T \rangle$ is a *Lindenbaum matrix* of $\vdash$.

## Notation

Some authors require $\emptyset \neq D \neq A$; the matrices with $D = \emptyset$ or $D = A$ are the trivial ones.
The set of tautologies of $M$ is $\set{\varphi : \emptyset \models_M \varphi}$, also called the content of $M$.

## Remarks

1. Each $\models_{\mathcal{K}}$ satisfies reflexivity, monotonicity and cut, by the argument for one matrix applied to each member of $\mathcal{K}$.
2. Each $\models_{\mathcal{K}}$ is structural. If $\sigma$ is a substitution and $h$ a valuation, then $h \circ \sigma$ is a valuation, so $\Gamma \models_M \varphi$ gives $\sigma[\Gamma] \models_M \sigma(\varphi)$.
3. Example: $\langle \set{0, \tfrac12, 1}, \set{1} \rangle$ with Kleene's operations is the matrix of [[Strong Kleene logic|SZHA10A9X7]]; see also [[the comparison with the logic of paradox|BJMXHXJ7QQ]].
4. Example: $\langle \mathrm{Fm}, \mathrm{Cn}(\emptyset) \rangle$ is a [[Lindenbaum matrix|ZV4GTXRRCV]], and its tautologies are the theorems of $\vdash$.
5. Non-example: a probability function on formulas is not a valuation in any matrix, because it is not a homomorphism; see [[the example|EVW7FAWM68]].
6. A *many-valued matrix* in the sense of [[the definition of many-valued logic|66NMTCQNQV]] is a logical matrix with at least three values and $\emptyset \neq D \neq A$.

## Explanations

### L1 human

A logical matrix has two parts.
The first part is a set of values with a table for each connective.
The second part is the set of values that count as true.
With these, one can compute the value of any formula and decide whether it counts as true.

### L2 human

We check the structurality of $\models_M$ on an instance.

1. In classical logic, $p \models p \lor q$.
2. Substitute $p \mapsto r \land s$ and $q \mapsto \neg r$.
3. Any valuation $h$ with $h(r \land s) = 1$ gives $h((r \land s) \lor \neg r) = 1$, since a disjunction with a true disjunct is true.
4. So $r \land s \models (r \land s) \lor \neg r$, as Remark 2 predicts.

The typical use of the definition is to define a logic by a matrix, or to test an inference by a search for a counter-valuation.
A trap: a matrix consequence is always structural, so a non-structural relation, such as one with a special axiom about one variable, has no matrix semantics.
