---
tag: EBVDK5GCGV
kind: example
name: Intuitionistic propositional logic is not Post complete
msc: ["03B20", "03B05"]
topics: [H8QZY0RZXZ]
audience: grad
not_instance_of:
  - target: WK2P0E82B4
    note: the excluded middle p ∨ ¬p is not an intuitionistic theorem, yet adding it as a schema gives classical propositional logic, which is still Post consistent
uses: [WK2P0E82B4, Q11N8X99FK, NG943XNQWH, 0RYYK8PG4S, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Heyting_algebra
    locator: lead section
  - book: isbn:9781447145578
---

## Example

Let $\mathsf{IPC}$ be a Hilbert system for intuitionistic propositional logic, with the connectives $\land$, $\lor$, $\to$, $\lnot$.
We use two standard facts.

- Every axiom of $\mathsf{IPC}$ is a classical [[tautology|05006AJ7DZ]], so every theorem of $\mathsf{IPC}$ is a tautology.
- $\mathsf{IPC}$ is sound for [[Heyting algebras|NG943XNQWH]].
  If a formula is a theorem, then it takes the value $1$ under every assignment of elements of a Heyting algebra to its variables.

We show that $\mathsf{IPC}$ is not [[Post complete|WK2P0E82B4]].

1. Let $H_3 = \{ 0, \tfrac12, 1 \}$ with the usual order.
   It is a Heyting algebra with $a \land b = \min(a, b)$ and $a \lor b = \max(a, b)$.
   Implication is $a \to b = 1$ when $a \le b$ and $a \to b = b$ when $a > b$, and negation is $\lnot a = a \to 0$.
2. Assign $p \mapsto \tfrac12$.
   Then $\lnot p = \tfrac12 \to 0 = 0$, because $\tfrac12 > 0$.
3. So $p \lor \lnot p = \max(\tfrac12, 0) = \tfrac12 \neq 1$.
4. By soundness for Heyting algebras, the [[law of excluded middle|0RYYK8PG4S]] $p \lor \lnot p$ is not a theorem of $\mathsf{IPC}$.
5. Let $S = \mathsf{IPC} + (p \lor \lnot p)$, with all instances $\varphi \lor \lnot\varphi$ as new axioms.
6. Every axiom of $S$ is a tautology: the old axioms by the first fact, and $\varphi \lor \lnot\varphi$ by its truth table.
   Modus ponens keeps tautologies.
7. So every theorem of $S$ is a tautology, and the variable $p$ is not a theorem of $S$.
   Thus $S$ is Post consistent.
8. So $p \lor \lnot p$ is a non-theorem of $\mathsf{IPC}$ whose addition as a schema does not make the system trivial.
   Hence $\mathsf{IPC}$ is not Post complete.

## Remarks

The system $S$ of step 5 is a Hilbert system for classical propositional logic, and by the [[Post completeness of classical logic|R1122T076S]] it is Post complete.
So the chain $\mathsf{IPC} \subsetneq S \subsetneq$ (all formulas) cannot be refined above $S$, but it can be refined between $\mathsf{IPC}$ and $S$.
For example, adding the schema $\lnot p \lor \lnot\lnot p$ gives the [[logic of weak excluded middle|H9Z8BWRN69]], which lies strictly between them.

[[Intuitionistic logic|Q11N8X99FK]] rejects $p \lor \lnot p$ because a proof of a disjunction must give a proof of one of its parts.
The example also shows that $H_3$ is a model of $\mathsf{IPC}$ in which a classical law fails.
So the semantic method gives unprovability here just as in classical logic.

## Explanations

### L1 human

Intuitionistic logic accepts a statement only when it has a direct proof of it.
It does not accept "every statement is true or false" as a law, because for an open problem we have neither a proof nor a disproof.
If we add that law, we get ordinary classical logic, and classical logic does not prove everything.
So intuitionistic logic can be made stronger without collapse, which is exactly what Post completeness forbids.

### L2 human

We compute one more formula in $H_3$: double negation elimination under $p \mapsto \tfrac12$.

1. $\lnot p = \tfrac12 \to 0 = 0$, by step 2.
2. $\lnot\lnot p = 0 \to 0 = 1$, because $0 \le 0$.
3. So $\lnot\lnot p \to p = 1 \to \tfrac12 = \tfrac12$, because $1 > \tfrac12$.
4. So double negation elimination $\lnot\lnot p \to p$ is also not a theorem of $\mathsf{IPC}$.

The typical use of $H_3$ is to refute classical laws in intuitionistic logic by a three-row table.
A trap is to think that $H_3$ refutes every non-theorem of $\mathsf{IPC}$.
It validates $(p \to q) \lor (q \to p)$, which is not an intuitionistic theorem, so for some formulas a larger Heyting algebra or a Kripke model is needed.
