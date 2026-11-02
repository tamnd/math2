---
tag: 8FVWYEZWTK
kind: statement
role: theorem
name: Borel determinacy theorem
msc: ["03E60", "03E15", "91A44"]
uses: [QXECDPAYTN, 0WQXY32Q8D, 0HE5WDQ9FJ]
about: [QXECDPAYTN]
sources:
  - url: https://en.wikipedia.org/wiki/Borel_determinacy_theorem
same_as:
  wikidata: Q4944906
  wikipedia: Borel determinacy theorem
---

## Statement

Let $A$ be a nonempty set with the discrete topology, and give $A^{\N}$ the product topology.
Let $X \subseteq A^{\N}$ be a Borel set, that is, a member of the [[Borel sigma-algebra|0WQXY32Q8D]] of $A^{\N}$.
Then the game $G(A, X)$ is [[determined|QXECDPAYTN]]: one of the two players has a winning strategy.

## Remarks

The theorem was proved by Donald A. Martin in [[ZFC|0HE5WDQ9FJ]].
The base case is the Gale–Stewart theorem: games with an open or a closed payoff set are determined.
Martin's proof "unravels" a Borel game: it builds an auxiliary game on a larger set of moves in which the payoff set becomes clopen.
Winning strategies of the auxiliary game then give winning strategies of the original game.
The induction runs along the levels of the Borel hierarchy, and each step uses power sets of the sets of moves of the previous step.

The hypothesis that $X$ is Borel cannot simply be dropped: with the axiom of choice one can build a set $X \subseteq \set{0, 1}^{\N}$ that is not determined.
Harvey Friedman showed that the theorem cannot be proved in second-order arithmetic, so the use of large sets in the proof is unavoidable.

## Explanations

### L1 human

Imagine an infinite game where two players take turns choosing numbers, and the winner is decided by whether the infinite sequence of moves lands in a set $X$.
Suppose $X$ can be built from simple sets by countable unions, countable intersections and complements.
Then one of the two players has a strategy that always wins.

### L2 human

The theorem is a basic tool of descriptive set theory.
From it one gets, for instance, Wadge's lemma for Borel subsets $B$ and $C$ of the Baire space $\N^{\N}$.
It says that $B = f^{-1}(C)$ for some continuous map $f$, or $C = g^{-1}(\N^{\N} \setminus B)$ for some continuous map $g$.
Going beyond Borel sets needs more than ZFC: determinacy of analytic games follows from a measurable cardinal, and projective determinacy follows from infinitely many Woodin cardinals.
The theorem is also a famous example of a statement about countable objects whose proof requires uncountably many iterations of the power set operation.
