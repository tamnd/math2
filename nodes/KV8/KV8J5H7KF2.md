---
tag: KV8J5H7KF2
kind: statement
role: theorem
name: Representation of AGM revision by total preorders
msc: ["03B42", "68T27"]
topics: [CQM9SRN8PM]
audience: research
uses: [Y05YQN7HGQ, 0VABYWJWH9, 09K9MWD2QQ]
about: [Y05YQN7HGQ]
proofs: [E5T2PT5Z1P]
history:
  first_stated: "Grove, 1988 (systems of spheres); Katsuno and Mendelzon, 1991 (total preorders on valuations)"
  notes: "Grove proved the representation for arbitrary propositional languages with systems of spheres of maximal consistent sets; Katsuno and Mendelzon stated the finite version with faithful total preorders."
sources:
  - url: https://en.wikipedia.org/wiki/Belief_revision
    locator: Conditions equivalent to the AGM postulates
  - book: isbn:9780262071093
    locator: Gärdenfors, Knowledge in Flux
---

## Statement

Every rational revision ranks the possible worlds and believes what holds in the most plausible worlds of the news, and every such ranking gives a rational revision.

Let $L$ be the language of [[propositional logic|09K9MWD2QQ]] over finitely many atoms, and let $\Omega$ be the finite set of its valuations.
For a set $\Gamma$ of formulas, $\mathrm{Mod}(\Gamma) \subseteq \Omega$ is the set of valuations that satisfy every formula of $\Gamma$.
Fix a belief set $K$, and let $*$ map each formula $\varphi$ to a belief set $K * \varphi$.
A total [[preorder|0VABYWJWH9]] $\le$ on $\Omega$ is faithful to $K$ when, for all $x \in \mathrm{Mod}(K)$ and all $y \in \Omega$, two conditions hold.
If $y \in \mathrm{Mod}(K)$, then $x \le y$ and $y \le x$.
If $y \notin \mathrm{Mod}(K)$, then $x < y$, that is, $x \le y$ and not $y \le x$.
For $A \subseteq \Omega$ put $\min(A, \le) := \{ x \in A : x \le y \text{ for all } y \in A \}$.

The operator $*$ satisfies the eight [[AGM postulates|Y05YQN7HGQ]] for $K$ if and only if there is a total preorder $\le$ on $\Omega$, faithful to $K$, such that the following holds for every formula $\varphi$.
$$\mathrm{Mod}(K * \varphi) = \min(\mathrm{Mod}(\varphi), \le)$$

## Remarks

### Why each hypothesis is needed

Finiteness of the language makes $\Omega$ finite.
Then every nonempty set of valuations has minimal elements, and every set of valuations is $\mathrm{Mod}$ of one formula.
For an infinite language the statement needs Grove's spheres of maximal consistent sets, with a limit assumption in place of finiteness.

Totality of $\le$ is needed for postulate 8.
Take a partial order with $a < b$ and $c$ incomparable to both, and let revision select the minimal elements.
Revision by the formula with models $\{a, b, c\}$ keeps $\{a, c\}$, and adding the formula with models $\{b, c\}$ leaves $\{c\}$.
But revision by the formula with models $\{b, c\}$ keeps both $b$ and $c$, and $\{b, c\} \not\subseteq \{c\}$, against postulate 8.

Faithfulness is needed for postulates 3 and 4.
Without it, revision by a formula consistent with $K$ could select models outside $\mathrm{Mod}(K)$, and then it would not be expansion.

### What it gives you

Every AGM revision of $K$ is a ranking of the valuations in levels, with the models of $K$ at the bottom.
Revision by a formula $\varphi$ consistent with $K$ is expansion, since the minimal models of $\varphi$ are then the models in $\mathrm{Mod}(K) \cap \mathrm{Mod}(\varphi)$.
Postulates 1 to 6 alone give selection functions that need not come from one preorder, so postulates 7 and 8 are exactly what forces a ranking.

### The converse and uniqueness

The theorem is an equivalence, and the preorder is unique.
We have $x \le y$ exactly when $x \in \mathrm{Mod}(K * \varphi)$ for a formula $\varphi$ with $\mathrm{Mod}(\varphi) = \{x, y\}$.
So the ranking can be read off from revisions by two-world formulas.

### Generalizations

Grove's theorem covers an arbitrary propositional language: AGM revisions correspond to systems of spheres on the maximal consistent sets, centered on those that contain $K$.
The same preorders represent AGM contraction through the Harper identity, as follows.
$$\mathrm{Mod}(K \div \varphi) = \mathrm{Mod}(K) \cup \min(\mathrm{Mod}(\neg\varphi), \le)$$
Katsuno and Mendelzon gave a similar representation of update, with one preorder for each valuation.

## History

Grove gave the representation by systems of spheres in 1988.
Katsuno and Mendelzon stated the finite version with faithful total preorders in 1991.

## Explanations

### L1 human

Imagine that you rank all the ways the world could be, from most believable to least believable.
Your current beliefs are what is true in the top-ranked ways.
When you learn something new, you look at the top-ranked ways in which the news is true, and believe what holds there.
The theorem says that every rational way of revising beliefs works like this, for some ranking.

### L2 human

We read off the preorder from a revision operator on two atoms, with $K = \mathrm{Cn}(p \wedge q)$ and valuations $11, 10, 01, 00$.
Suppose that $K * \neg p = \mathrm{Cn}(\neg p \wedge q)$.
The formula $\neg p$ has the models $01$ and $00$, and the result keeps $01$ only, so $01 < 00$.
Suppose that $K * \neg q = \mathrm{Cn}(p \wedge \neg q)$, and in the same way $10 < 00$.
Suppose that $K * (p \leftrightarrow \neg q) = \mathrm{Cn}(p \leftrightarrow \neg q)$, so both models $10$ and $01$ are kept, and $10 \approx 01$.
Faithfulness puts $11$ at the bottom, and the ranking is $11 < 10 \approx 01 < 00$.
The typical use is to build revision operators for knowledge bases by assigning ranks to valuations.
Watch out that the preorder belongs to one belief set $K$, and the postulates do not supply a new preorder after the revision.

### L3 human

The theorem is a completeness theorem: the postulates are the logic of minimal-model selection with respect to total preorders.
The same structure appears in Lewis's sphere semantics for counterfactuals and in the ranked models of rational nonmonotonic consequence, and the three representation theorems are close relatives.
In dynamic epistemic logic, plausibility models put such a preorder at every world, and revision becomes an operation on models.
