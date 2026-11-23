---
tag: GHTK3M7JPZ
kind: example
name: A(Fp) ∧ Gq is a path formula, not a state formula
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
not_instance_of:
  - target: Y4XZ94GRXV
    note: A(Fp) ∧ Gq is a CTL* path formula, not a state formula, so it has no truth value at a state and is not a CTL* formula in the sense of the definition
uses: [5MH8WSAWXT]
sources:
  - url: https://en.wikipedia.org/wiki/CTL*
    locator: section Syntax
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
---

## Example

Consider the expression $\chi = A(Fp) \wedge Gq$ in the grammar of [[CTL*|5MH8WSAWXT]].
We sort its parts from the inside out.

1. $Fp$ is a path formula, so $A(Fp)$ is a state formula.
2. $Gq$ is a path formula, and it is not a state formula, because the state grammar has no clause for $G$.
3. A conjunction is a state formula only when both parts are state formulas, so $\chi$ is not a state formula.
4. Every state formula is also a path formula, so $A(Fp)$ is a path formula, and $\chi$ is a path formula.
5. A CTL* formula is by definition a state formula.
   So $\chi$ has a truth value on a path, but not at a state.

A concrete structure makes the difference visible.
Let $M$ have one state $s$ with $s \to s$ and $L(s) = \{q\}$.
On the only path $s s s \cdots$, $Gq$ holds and $Fp$ fails, so $A(Fp)$ fails at $s$, and $\chi$ fails on the path.
The question "does $s$ satisfy $\chi$?" has no answer in the definition, because $Gq$ needs a path.

## Remarks

The fix is to add a quantifier: $A(Fp) \wedge AGq$ and $A\chi = A(A(Fp) \wedge Gq)$ are state formulas.
They are equivalent, because $A$ distributes over conjunction, and $A\,A(Fp)$ is equivalent to $A(Fp)$, since a state formula on a path is read at its first state.
Both are equivalent to $A(Fp \wedge Gq)$, again by distribution.
Model checkers reject $\chi$ as ill-formed for the same reason.
If the structure had two paths from $s$, one with $Gq$ and one without, the choice between $A$ and $E$ in front of $Gq$ would change the answer, which is why no default quantifier is safe.

## Explanations

### L1 human

"Every run eventually turns the light on, and always the door is closed" is unclear.
The second half needs a run to talk about.
Say "on every run the door is always closed", and the sentence becomes a statement about the state.

### L2 human

Mark each subformula as a state formula or a path formula, from the inside out.
A temporal operator makes a path formula, and a path quantifier makes a state formula.
A Boolean combination is a state formula only if all its parts are.
Watch out: some textbooks blur the two sorts and silently insert $A$, and this hides the error rather than fixing it.
