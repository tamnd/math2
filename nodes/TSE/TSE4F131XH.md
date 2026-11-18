---
tag: TSE4F131XH
kind: example
name: Logical omniscience in Kripke models of knowledge
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [EA34W4ERRE]
uses: [NGHWZ9Y7ZV, H9RGWCR10W, 9TPXQT9625, ERG3KAQWYF]
sources:
  - url: https://en.wikipedia.org/wiki/Epistemic_modal_logic
    locator: section Problems with the possible world model and modal model of knowledge
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 9
---

## Example

Fix any [[Kripke model|NGHWZ9Y7ZV]] $M = (W, (R_a)_{a}, V)$ and an agent $a$.
For a world $w$ write $R_a(w) = \set{v : w R_a v}$, the worlds that $a$ cannot rule out at $w$.
We show three closure laws, with no condition on $R_a$.

1. Valid formulas are known. Let $\varphi$ be true at every world of $M$. Then $\varphi$ is true on $R_a(w)$, so $K_a\varphi$ is true at $w$.
2. For instance, $K_a((p \to q) \vee (q \to p))$ is true at every world of every model, since the inner formula is a tautology.
3. Knowledge is closed under valid implication. Let $\varphi \to \psi$ be true at every world of $M$, and let $K_a\varphi$ be true at $w$.
4. Then $\varphi$ is true on $R_a(w)$, so $\psi$ is true on $R_a(w)$, and $K_a\psi$ is true at $w$.
5. For instance, $K_a(p \wedge q) \to K_a(q \vee r)$ is valid, since $p \wedge q \to q \vee r$ is a tautology.
6. Knowledge is closed under conjunction. If $K_a\varphi$ and $K_a\psi$ are true at $w$, both formulas hold on $R_a(w)$, so $K_a(\varphi \wedge \psi)$ is true at $w$.
7. Equivalent formulas are known together: if $\varphi \leftrightarrow \psi$ is valid, step 4 applied in both directions gives $K_a\varphi \leftrightarrow K_a\psi$.

These laws together are called logical omniscience.
The agent of a Kripke model knows every tautology, and every consequence of what she knows.

## Remarks

Step 1 is the semantic form of the [[necessitation rule|9TPXQT9625]], and steps 3 and 4 give the [[epistemic closure|H9RGWCR10W]] principle.
Real agents do not satisfy step 1 for long tautologies.
Recognizing tautologies is coNP-complete, and no efficient method for it is known.
So in the Kripke picture, knowledge is better read as "implicit knowledge", or as what follows from the agent's information.
Fagin, Halpern, Moses and Vardi weaken omniscience with awareness structures and with impossible worlds, where tautologies may fail.
In first-order epistemic logic the same argument shows that an agent who knows the axioms of a theory knows all its theorems.

## Explanations

### L1 human

In a Kripke model, "knowing" a fact means it holds in every situation you consider possible.
Then you automatically know every logical truth, since it holds everywhere.
You also know everything that follows from what you know.
Real people do not: you can know the rules of chess without knowing the best first move.
So the model describes the information an agent has, more than what she has worked out.

### L2 human

The proofs above use one idea: knowing $\varphi$ is a fact about the set $R_a(w)$, namely that $\varphi$ holds on all of it.
Any law about "holds on all of a set" becomes a law of knowledge.

1. Truth on a set is closed under logical consequence, which gives steps 3 and 4.
2. Truth on a set is closed under intersection of truth sets, which gives step 6.

The typical use is to check whether a proposed axiom of knowledge is forced by the semantics.
A trap: step 1 needs $\varphi$ true at every world of the model, not only at $w$; a fact true at $w$ alone need not be known.

### L3 human

Logical omniscience is the price of a normal modal logic: the rule $\varphi / K_a\varphi$ and axiom $\mathsf{K}$ already imply it.
Any semantics that avoids it must leave the class of normal logics, as neighbourhood or awareness semantics do.
The same issue appears for belief in [[doxastic logic|RTP4HTZYK3]], and for obligation in deontic logic.
