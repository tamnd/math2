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

Suppose an agent knows the axioms of group theory.
In a Kripke model of [[epistemic logic|EA34W4ERRE]] she then knows every theorem of group theory, including ones that nobody has proved yet.
This is logical omniscience, and it holds in every Kripke model, whatever the relation is.

Fix a [[Kripke model|NGHWZ9Y7ZV]] $M = (W, (R_a)_a, V)$ and an agent $a$.
For a world $w$ write $R_a(w) = \{v : w R_a v\}$, the worlds that $a$ cannot rule out at $w$.
We show four closure laws, with no condition on $R_a$.

1. Valid formulas are known.
   If $\varphi$ is true at every world of $M$, then it is true on $R_a(w)$, so $K_a \varphi$ is true at $w$.
   For instance, $K_a ((p \to q) \vee (q \to p))$ is true everywhere, since the inner formula is a tautology.
2. Knowledge is closed under valid implication.
   Let $\varphi \to \psi$ be true at every world of $M$, and let $K_a \varphi$ be true at $w$.
   Then $\varphi$ is true on $R_a(w)$, so $\psi$ is true on $R_a(w)$, and $K_a \psi$ is true at $w$.
3. Knowledge is closed under conjunction.
   If $K_a \varphi$ and $K_a \psi$ are true at $w$, then both formulas hold on $R_a(w)$, so $K_a (\varphi \wedge \psi)$ is true at $w$.
4. Equivalent formulas are known together.
   If $\varphi \leftrightarrow \psi$ is valid, step 2 in both directions gives $K_a \varphi \leftrightarrow K_a \psi$ at every world.

As a concrete instance of step 2, the formula $K_a (p \wedge q) \to K_a (q \vee r)$ is valid, because $p \wedge q \to q \vee r$ is a tautology.

## Remarks

Step 1 is the semantic form of the [[necessitation rule|9TPXQT9625]], and step 2 is the [[epistemic closure|H9RGWCR10W]] principle.
Every step uses one fact only: knowing $\varphi$ at $w$ means that $\varphi$ holds on the whole set $R_a(w)$.
Any law about "holds on all of a set" therefore becomes a law of knowledge.

Real agents do not satisfy step 1 for long tautologies.
Deciding whether a formula is a tautology is coNP-complete, so no known method does it quickly.
In the Kripke picture, knowledge is better read as implicit knowledge, meaning what follows from the agent's information.
Fagin, Halpern, Moses and Vardi weaken omniscience with awareness structures and with impossible worlds, in which tautologies may fail.

## Explanations

### L1 human

In a Kripke model, knowing a fact means that it holds in every situation you consider possible.
Then you know every logical truth, because a logical truth holds in every situation.
You also know everything that follows from what you know.
Real people do not: you can know the rules of chess without knowing the best first move.
So the model describes the information that an agent has, more than what she has worked out.

### L2 human

Take $W = \{w, v\}$ with $R_a(w) = \{w, v\}$, $p$ and $q$ true at both worlds, and $r$ false everywhere.
Then $K_a (p \wedge q)$ is true at $w$, and so is $K_a (q \vee r)$, since $q$ holds at $w$ and $v$.
The agent never "derived" $q \vee r$; it was known the moment $q$ held on $R_a(w)$.
Watch out: step 1 needs $\varphi$ true at every world of the model, not only at $w$.
In this model $K_a \neg r$ also holds at $w$, but only because $r$ happens to be false at $w$ and $v$.
Add a world where $r$ is true to $R_a(w)$ and $K_a \neg r$ fails, while $K_a (r \vee \neg r)$ holds in every model.

### L3 human

Logical omniscience is the price of a normal modal logic, since the rule from $\varphi$ to $K_a \varphi$ and axiom $\mathsf{K}$ already imply it.
A semantics that avoids it must leave the normal logics, as neighborhood and awareness semantics do.
The same issue appears for belief in [[doxastic logic|RTP4HTZYK3]] and for obligation in [[deontic logic|7B74J6J5JV]].
[[Justification logic|5HKWCXEFG1]] offers another way out, by tracking the reason for each piece of knowledge.
