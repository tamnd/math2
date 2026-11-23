---
tag: ND17WYDNA5
kind: statement
role: theorem
name: Strong Kleene logic has no tautologies
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
about: [SZHA10A9X7]
uses: [74R8A41V6M, TFDYXS3K1N]
proofs: [VT9D8SA2AX]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: "2.2 From two to three truth values: gaps and gluts"
---

## Statement

Give $p$ and $q$ the value $\tfrac12$ in $(p \land q) \to p$, which abbreviates $\neg(p \land q) \lor p$.
Then $p \land q = \tfrac12$, its negation is $\tfrac12$, and the whole formula is $\max(\tfrac12, \tfrac12) = \tfrac12$.
The same happens to every formula, so strong Kleene logic has no laws at all.

Let $\varphi$ be a [[formula|TFDYXS3K1N]] built from variables with $\neg$, $\land$, $\lor$ and $\to$, where $\varphi \to \psi$ abbreviates $\neg \varphi \lor \psi$.
Evaluate $\varphi$ in the [[strong Kleene matrix|74R8A41V6M]].

**Theorem.**

1. The valuation that gives every variable the value $\tfrac12$ gives $\varphi$ the value $\tfrac12$.
2. So no formula is a tautology of $\mathsf{K}_3$: $\not\models_{\mathsf{K}_3} \varphi$ for every $\varphi$.
3. More generally, $\Gamma \models_{\mathsf{K}_3} \varphi$ implies that $\Gamma$ is nonempty.

The proof is [[by structural induction|VT9D8SA2AX]].

## Remarks

### Why each hypothesis is needed

The language has no constants.
If the constant $1$, often written $\top$, is a formula, then $\top$ is a tautology and the theorem fails.
The designated set is $\{1\}$.
With the designated set $\{\tfrac12, 1\}$, the logic $\mathsf{LP}$ has the tautology $p \lor \neg p$.
The connectives matter too.
With Łukasiewicz implication, $p \to p$ always has the value $1$, and [[no Kleene formula can replace it|729J1FD1GZ]].

### What it gives you

Every classical tautology fails in $\mathsf{K}_3$; for a concrete case see [[the example of p → p|MBVRGSV45Y]].
The deduction theorem fails: $p \models_{\mathsf{K}_3} p$ holds, while $p \to p$ is not a tautology.
A sound Hilbert-style system for $\mathsf{K}_3$ can have no axioms, because each axiom would be a tautology, so it consists of rules only.

### The converse direction

Every valid inference of $\mathsf{K}_3$ is classically valid, because valuations into $\{0, 1\}$ are $\mathsf{K}_3$ valuations.
The converse fails, also with premises.
The inference $q \models p \lor \neg p$ holds classically, but $q = 1$ and $p = \tfrac12$ refute it in $\mathsf{K}_3$.

### Generalizations

The same argument works for every connective $f$ with $f(\tfrac12, \dots, \tfrac12) = \tfrac12$, for example the weak Kleene connectives.
In algebraic terms, $\{\tfrac12\}$ is a subuniverse of the strong Kleene algebra, so it is closed under every term operation.
So any matrix without constants that has a one-element subalgebra outside the designated set has no tautologies.
[[First-degree entailment|KXTP4P3GHT]] has no tautologies for this reason, with the value "neither" as the subalgebra.

## History

Kleene introduced the strong tables in 1938, for predicates defined by partial recursive functions.
His 1952 book *Introduction to Metamathematics* presented them again, with the middle value read as "undefined".

## Explanations

### L1 human

Put "undefined" into every variable.
"Not undefined" is undefined, and "undefined and undefined" is undefined.
So the whole formula is undefined, never true.
This means no formula is true in every case.

### L2 human

To use the theorem, evaluate a formula at the all-$\tfrac12$ valuation, from the inside out.
Every step is $1 - \tfrac12$, $\min(\tfrac12, \tfrac12)$ or $\max(\tfrac12, \tfrac12)$, and each gives $\tfrac12$.
The typical use is to show that an inference needs premises, or that a classical law is lost.
Watch out: "no tautologies" does not mean "no valid inferences", since $p \land q \models p$ still holds.
