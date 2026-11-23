---
tag: ZTVBX14AV0
kind: proof
name: Proof of the equivalence of game and Tarski semantics by truth-preserving strategies
msc: ["03B10"]
topics: [NJDME6F845]
audience: grad
proves: G6MKG8YQ6M
uses: [D45Z7HETDA, 1WTCZB4DVB, 0HTGB13FE2]
methods: [0WCP0PVET6, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Game_semantics
    locator: lead section
---

## Proof

We show that each player can keep the game in positions that are good for that player, and that a good final position is a win.

We use the positions $(\psi, s', \rho)$ of the [[evaluation game|D45Z7HETDA]], with $\rho = +$ when Eloise is the current verifier and $\rho = -$ when Abelard is.
Call a position good for Eloise when either $\rho = +$ and $\mathcal{M} \models \psi[s']$, or $\rho = -$ and $\mathcal{M} \not\models \psi[s']$.
Otherwise call it good for Abelard.
Here $\models$ is [[satisfaction|1WTCZB4DVB]].

Claim: at a position that is good for Eloise and not final, every move of Abelard leads to a position good for Eloise, and some move of Eloise does.
We prove the claim by [[cases|0WCP0PVET6]] on the form of $\psi$, first for $\rho = +$.

1. If $\psi = \neg \chi$, the next position is $(\chi, s', -)$.
   Since $\mathcal{M} \models \neg \chi[s']$, we have $\mathcal{M} \not\models \chi[s']$, so the next position is good for Eloise.
2. If $\psi = \chi_1 \vee \chi_2$, Eloise moves.
   By the clause for $\vee$, some $\chi_i$ is satisfied under $s'$, and the move to $(\chi_i, s', +)$ is good for her.
3. If $\psi = \chi_1 \wedge \chi_2$, Abelard moves.
   By the clause for $\wedge$, both $\chi_i$ are satisfied, so both moves give good positions for Eloise.
4. If $\psi = \exists x \, \chi$, Eloise moves.
   By the clause for $\exists$, some $a \in M$ gives $\mathcal{M} \models \chi[s'[x \mapsto a]]$, and the move $a$ is good for her.
5. If $\psi = \forall x \, \chi$, Abelard moves.
   By the clause for $\forall$, every $a \in M$ gives $\mathcal{M} \models \chi[s'[x \mapsto a]]$, so every move is good for Eloise.
6. If $\rho = -$, the position is good for Eloise when $\psi$ fails under $s'$, and Abelard is the verifier.
   The cases are steps 1 to 5 with the roles and the words "satisfied" and "not satisfied" exchanged; for example, at $\chi_1 \vee \chi_2$ Abelard moves, and both disjuncts fail.

The same argument, with the players exchanged, proves the claim for positions good for Abelard.
Now we build the strategy and prove part 1.

7. By the [[axiom of choice|0HTGB13FE2]], fix a function $C$ that picks an element from each nonempty subset of $M$.
8. Define Eloise's strategy $\sigma$ at a position good for her where she moves.
   At a connective, she chooses the first subformula that gives a good position.
9. At a quantifier, she chooses $C$ of the set of elements that give a good position, which is nonempty by the claim.
   At all other positions, she chooses any legal move.
10. Suppose $\mathcal{M} \models \varphi[s]$.
    Then the start position $(\varphi, s, +)$ is good for Eloise.
11. By the claim and [[induction|0ASJVEFA9J]] on the number of moves, every position of a play in which Eloise follows $\sigma$ is good for her.
12. Every play is finite, because each move passes to a proper subformula.
    So the play reaches an atomic position $(\alpha, s'', \rho)$ that is good for Eloise.
13. At such a position either $\rho = +$ and $\alpha$ is satisfied, or $\rho = -$ and $\alpha$ fails, and in both cases Eloise wins by the winning rule.
    So $\sigma$ is a winning strategy.
14. In the same way, if $\mathcal{M} \not\models \varphi[s]$, then the start position is good for Abelard, and he has a winning strategy that keeps the positions good for him.
15. The two players cannot both have winning strategies.
    If each followed one, the single resulting play would be won by both, and the rules give each play exactly one winner.
16. Suppose Eloise has a winning strategy.
    By step 15 Abelard has none, so by step 14 we cannot have $\mathcal{M} \not\models \varphi[s]$, that is, $\mathcal{M} \models \varphi[s]$.
    With steps 10 to 13, this proves part 1.
17. Part 2 follows in the same way with the players exchanged, and together the two parts show that the game is determined.

## Idea

Tarski's clauses say that at a true position the verifier has a move to a true position, and every move of the falsifier keeps the truth.
So the verifier can play to preserve truth, and truth at the end of the play means winning.
Choice enters only in step 7, to turn "a good move exists" into a single strategy that picks one for every position at once.

## Variants

Another proof goes by induction on $\varphi$, combining winning strategies for the subformulas into a strategy for $\varphi$.
At $\forall x \, \chi$, this needs a winning strategy for each $a \in M$, chosen all at once, which again uses the axiom of choice.
For a finite structure, the winner can also be computed by backward induction on the finite game tree.
