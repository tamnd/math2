---
tag: 72CPDNTXKT
kind: example
name: Checking one satisfying assignment is not a proof system
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
not_instance_of:
  - target: 3V24CYWDT6
    note: the map is polynomial-time, but it outputs satisfiable formulas that are not tautologies, so soundness fails
  - target: 1Q046J0AW2
    note: a satisfying assignment is evidence for satisfiability, an NP property, while proof complexity studies evidence for tautologies, a coNP property
uses: [3V24CYWDT6, 05006AJ7DZ, 3A81RHAN68, 3QKF32ZAKN]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
---

## Example

Define $g$ on strings $w = \tau \# a$, where $\tau$ is a formula and $a$ is an assignment to its variables.

1. If $a$ makes $\tau$ true, then $g(w) = \tau$.
2. In every other case, $g(w) = p \lor \neg p$.

The function $g$ is computable in polynomial time, since one evaluation of $\tau$ under $a$ is fast.
Every tautology is a value of $g$, since every assignment makes a tautology true.

But $g$ is not a [[propositional proof system|3V24CYWDT6]].
The formula $p$ is not a [[tautology|05006AJ7DZ]], and $g(p \# (p = 1)) = p$.
So the image of $g$ contains a formula outside $\mathrm{TAUT}$, and soundness fails.

The image of $g$ is the set of all satisfiable formulas.
So $g$ is a proof system for the language $\mathrm{SAT}$ of the [[satisfiability problem|3QKF32ZAKN]], in the general sense of a polynomial-time map onto a language.

## Remarks

One assignment shows that a formula is satisfiable, and it says nothing about the other assignments.
A tautology needs evidence about all $2^n$ assignments at once, and the [[truth-table proof system|67MYPBSHCJ]] writes such evidence in full.
Short evidence of this kind for every tautology exists if and only if $\mathrm{NP} = \mathrm{coNP}$, by the [[Cook-Reckhow theorem|YS1T29B00B]].

## Explanations

### L1 human

To show that a formula can be true, it is enough to give one way of making it true.
To show that a formula is always true, one way is not enough.
For example, $p \land q$ is true when $p$ and $q$ are both true, but it is false when $p$ is false, so it is not a tautology.

### L2 human

We test $g$ on two inputs.

1. $w_1 = (p \lor \neg p) \# (p = 0)$. The assignment makes $p \lor \neg p$ true, so $g(w_1) = p \lor \neg p$, a tautology.
2. $w_2 = (p \land q) \# (p = 1, q = 1)$. The assignment makes $p \land q$ true, so $g(w_2) = p \land q$.
3. $p \land q$ is false at $p = 0$, so $g(w_2)$ is not a tautology.

The typical use of the example is to show why soundness is part of the definition.
A trap: completeness and polynomial time hold for $g$, and only soundness fails.
