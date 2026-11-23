---
tag: 7RX0Z6S1KZ
kind: statement
role: lemma
name: Restriction lemma for resolution
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
uses: [6JSH907W5R, T3SXVH3ZZC]
about: [6JSH907W5R]
proofs: [Z6Z1RV7D68]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in propositional logic
---

## Statement

The restriction lemma says that fixing some variables never makes a resolution refutation longer or wider.
For example, setting $p = 1$ in the refutation $\{p\}, \{\neg p, q\}, \{q\}, \{\neg q\}, \square$ leaves the refutation $\{q\}, \{\neg q\}, \square$ of the restricted clauses.

Let $F$ be a CNF and $\rho$ a partial assignment to its variables.
For a [[clause|T3SXVH3ZZC]] $C$, write $C|_\rho = 1$ if $\rho$ makes some literal of $C$ true.
Otherwise $C|_\rho$ is $C$ with the literals made false by $\rho$ removed.
Let $F|_\rho$ be the set of the clauses $C|_\rho$ for $C \in F$ with $C|_\rho \ne 1$.

**Lemma.** Let $\pi = (C_1, \dots, C_s)$ be a [[resolution derivation|6JSH907W5R]] from $F$.
Then there is a resolution derivation $\pi'$ from $F|_\rho$ with these properties.

1. For each $i$ with $C_i|_\rho \ne 1$, the derivation $\pi'$ contains a clause $D_i \subseteq C_i|_\rho$.
2. Every clause of $\pi'$ is one of these $D_i$.
   So $\pi'$ has at most $s$ clauses, and its width is at most the width of $\pi$.
3. If $\pi$ is tree-like, then $\pi'$ is tree-like, and it has at most as many leaves as $\pi$.

In particular, if $\pi$ is a refutation of $F$, then $\pi'$ is a refutation of $F|_\rho$ of size at most $S(\pi)$ and width at most $w(\pi)$.
The measures are size in clauses and width.

## Remarks

### Why the lemma is stated with subclauses

The clauses $C_i$ with $C_i|_\rho = 1$ must be dropped, since they are true under $\rho$ and have no counterpart in $F|_\rho$.
The conclusion gives a subclause $D_i$, and not $C_i|_\rho$ itself, because some steps collapse.
In the example above, the clause $\{q\}$ came from a step on the pivot $p$, which $\rho$ sets.
That step is no longer a resolution step, so the lemma keeps the premise $\{\neg p, q\}|_\rho = \{q\}$ and skips the step.
In other cases the kept premise is strictly smaller than $C_i|_\rho$, so only "$\subseteq$" holds.

### What it gives you

The three least measures can only go down:
$$S(F|_\rho \vdash \square) \le S(F \vdash \square), \quad S_T(F|_\rho \vdash \square) \le S_T(F \vdash \square), \quad w(F|_\rho \vdash \square) \le w(F \vdash \square).$$
This is the tool behind most lower bounds for resolution.
A random restriction that makes every "large" clause true turns a small refutation of $F$ into a refutation of $F|_\rho$ with no large clause.
The [[proof of Haken's theorem|8D74S641EK]] and the [[proof of the size-width relation|9BVKW1XJZK]] both follow this plan.
Read the other way, a lower bound for $F|_\rho$ is a lower bound for $F$, and this is how bounds for the pigeonhole formula on a sparse graph transfer to the full [[pigeonhole formulas|RJ571F7FF0]].

### The converse

A refutation of $F|_\rho$ does not give a refutation of $F$ of the same size.
Add back to each axiom the literals that $\rho$ removed: the steps stay correct, and the result is a derivation from $F$ of a clause whose literals are all made false by $\rho$.
This lifting is the first step of the width lemma in the proof of the size-width relation.

### Generalizations

The same proof works for derivations of any clause, not only for refutations.
Similar restriction lemmas hold for [[bounded-depth Frege|41QJ1WEMJ3]], [[cutting planes|KKCX2HQP2K]] and the [[algebraic proof systems|ZERBQSTZB5]], since in each of them a restriction maps proofs to proofs of no larger size.

### Watch out

The lemma does not say that the restricted refutation is $\pi$ with $\rho$ applied line by line.
Applying $\rho$ line by line can break steps: the step from $\{p\}$ and $\{\neg p, q\}$ to $\{q\}$ becomes "from $1$ and $\{q\}$ infer $\{q\}$", which is no step at all.
The lemma repairs this by keeping one premise.

## History

The lemma is folklore in the study of resolution.
It is used in the lower bound proofs of Haken, of Beame and Pitassi, and of Ben-Sasson and Wigderson.

## Explanations

### L1 human

If some variables of a contradictory set of clauses are fixed, the remaining clauses are still contradictory.
The lemma says that a proof of the original contradiction can be cut down to a proof of the new one, and that it does not get longer.
For example, set $p = 1$ in the clauses "$p$", "not $p$ or $q$" and "not $q$".
The first clause becomes true, the second becomes "$q$", and one step from "$q$" and "not $q$" finishes the proof.

### L2 human

We restrict the refutation $\{p\}$, $\{\neg p, q\}$, $\{q\}$, $\{\neg q\}$, $\square$ by $\rho = \{p = 1\}$, line by line.
The axiom $\{p\}$ becomes true, so it is dropped.
The axiom $\{\neg p, q\}$ becomes $\{q\}$, an axiom of $F|_\rho$.
The clause $\{q\}$ came from a step on $p$, which $\rho$ sets, so the lemma keeps the premise that is not true under $\rho$, whose restriction is $\{q\}$.
The axiom $\{\neg q\}$ stays as it is, and $\square$ is the resolvent of $\{q\}$ and $\{\neg q\}$.
The restricted refutation has $3$ clauses, against $5$ before.
The typical use is with a random $\rho$, inside a lower bound proof.
