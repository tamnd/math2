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

Take the formula $p \land q$ and the assignment $p = 1$, $q = 1$.
The assignment makes the formula true, and you can check that in one evaluation.
So the pair is short, fast evidence, but it is evidence that $p \land q$ *can* be true, and $p \land q$ is not a tautology.

Turn this into a map $g$ on strings $w = \tau \# a$, where $\tau$ is a formula and $a$ is an assignment to its variables.

1. If $a$ makes $\tau$ true, then $g(w) = \tau$.
2. In every other case, $g(w) = p \lor \neg p$.

We check the conditions of a [[propositional proof system|3V24CYWDT6]] one by one.

1. *Polynomial time holds.*
   One evaluation of $\tau$ under $a$ takes time polynomial in $\lvert w \rvert$.
2. *Completeness holds.*
   A [[tautology|05006AJ7DZ]] $\tau$ is true under every assignment, so $g(\tau \# a) = \tau$ for any $a$.
3. *Soundness fails.*
   The formula $p$ is not a tautology, and $g(p \# (p = 1)) = p$.
   So the image of $g$ contains a formula outside $\mathrm{TAUT}$.

The image of $g$ is exactly the set of satisfiable formulas.
So $g$ is a proof system for the language $\mathrm{SAT}$ of the [[satisfiability problem|3QKF32ZAKN]], in the general sense of a polynomial-time map onto a language, but not for $\mathrm{TAUT}$.

## Remarks

One assignment shows that one row of the truth table is true, and it says nothing about the other rows.
A tautology needs evidence about all $2^n$ rows at once, and the [[truth-table proof system|67MYPBSHCJ]] writes such evidence in full.
Short evidence of that kind for every tautology exists if and only if $\mathrm{NP} = \mathrm{coNP}$, by the [[Cook-Reckhow theorem|YS1T29B00B]].

What changes if you ask for every assignment instead of one?
Then $w$ must list all $2^n$ assignments, soundness holds, and you get the truth-table system back, with its exponential size.
Watch out: polynomial time and completeness both hold for $g$, so a check of only those two conditions would wrongly accept it.

## Explanations

### L1 human

To show that a formula can be true, it is enough to give one way of making it true.
To show that a formula is always true, one way is not enough.
For example, "$p$ and $q$" is true when $p$ and $q$ are both true, but it is false when $p$ is false.

### L2 human

We run $g$ on two inputs.

1. Let $w_1 = (p \lor \neg p) \# (p = 0)$.
   The assignment makes $p \lor \neg p$ true, so $g(w_1) = p \lor \neg p$, a tautology.
2. Let $w_2 = (p \land q) \# (p = 1, q = 1)$.
   The assignment makes $p \land q$ true, so $g(w_2) = p \land q$.
3. The formula $p \land q$ is false at $p = 0$, so $g(w_2)$ is not a tautology.

So one bad output is enough to break soundness.
The typical use of the example is to show why the definition asks for the image to be exactly $\mathrm{TAUT}$.
