---
tag: 13HTANHBNW
kind: example
name: A star interpreted too large violates the PDL axioms
msc: ["03B45", "68Q60"]
topics: [SPQVNPZDTB]
audience: research
not_instance_of:
  - target: VJ78A0Q22R
    note: the structure gives the program a* the relation W x W, which is larger than the reflexive transitive closure of R_a, so it is not a model of propositional dynamic logic, and the star axioms fail in it
uses: [VJ78A0Q22R, 05J9NWX07X]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_logic_(modal_logic)
    locator: Axioms
---

## Example

Suppose we treat each program term as an independent box, as in a multimodal Kripke model, and give $a^*$ any relation we like.
Let $W = \{0, 1\}$, $R_a = \emptyset$, $V(p) = \{0\}$, and let the relation for $a^*$ be $S = W \times W$.
We show that this structure is not a model of [[propositional dynamic logic|VJ78A0Q22R]], and that two star axioms fail in it.

1. The reflexive [[transitive closure|05J9NWX07X]] of $R_a = \emptyset$ is the identity $\{(0, 0), (1, 1)\}$.
2. The relation $S$ contains $(0, 1)$, which is not in the identity, so $S$ is not the relation of $a^*$ in a $\mathsf{PDL}$ model.
3. Read with $S$, $[a^*] p$ is false at $0$, since $0 S 1$ and $1 \notin V(p)$.
4. Every box $[a] \psi$ is true at every world, because $R_a$ is empty.
5. Take the unfolding axiom $[a^*] p \leftrightarrow p \wedge [a][a^*] p$ at $0$.
   The right side is true, since $p$ holds at $0$ and $[a][a^*] p$ holds by step 4.
   The left side is false by step 3, so the axiom fails at $0$.
6. Take the induction axiom $[a^*](p \to [a] p) \to (p \to [a^*] p)$ at $0$.
   By step 4, $p \to [a] p$ is true everywhere, so the first antecedent holds, and $p$ holds at $0$.
   The consequent $[a^*] p$ fails by step 3, so the axiom fails at $0$.

## Remarks

The star axioms carry the meaning of the star, and here they reject the extra pair $(0, 1)$.
If we replace $S$ by the identity, both axioms hold at both worlds, since then $[a^*] p$ says the same as $p$.

A relation that is too small fails too.
With $S = \emptyset$, the formula $[a^*] p$ is true at $1$ because there is nothing to check, while $p$ is false at $1$.
So $[a^*] p \to p$ fails at $1$, and that formula follows from the unfolding axiom.

In general the two axioms, valid for every valuation, pin $S$ down exactly.
The unfolding axiom makes $S$ reflexive and closed under a further $a$-step, so $S$ contains the closure of $R_a$.
The induction axiom, with $p$ true exactly at the worlds that $w$ reaches by $R_a$-chains, puts every $S$-successor of $w$ among those worlds.
So $S$ is the reflexive transitive closure of $R_a$, no more and no less.

## Explanations

### L1 human

The star of a program means "repeat it zero or more times".
Here the step $a$ can never be taken, so "repeat $a$" can only mean "do nothing".
The structure pretends that "repeat $a$" can move from world $0$ to world $1$.
The axioms of $\mathsf{PDL}$ notice this mistake, because they describe the star exactly.

### L2 human

We check the claim about the empty relation $S = \emptyset$ in detail.
At world $1$, $[a^*] p$ has no successors to look at, so it is true.
But $p$ is false at $1$, because $V(p) = \{0\}$.
So $[a^*] p \to p$ fails at $1$.
In $\mathsf{PDL}$ this formula is a theorem, by the unfolding axiom and propositional logic, so the structure with $S = \emptyset$ is no model either.
The typical use of such structures is to find out which axioms pin down a program operation.
Watch out: an axiom is a scheme over all formulas, so a structure may pass an instance for one $p$ and fail it for another.
