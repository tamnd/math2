---
tag: RP5BF9HK31
kind: statement
role: theorem
name: Lattice of stable matchings
msc: [91B68, 06D05]
uses: [X201T4TP0Y, CHWQVJ9F5K, WH4SFAACAS, 0HM0HQCK6N]
about: [X201T4TP0Y, 0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_of_stable_matchings
same_as:
  wikidata: Q85775934
  wikipedia: Lattice of stable matchings
---

## Statement

Consider an instance of the [[stable marriage problem|X201T4TP0Y]] with a set $M$ of men, a set $W$ of women and strict preferences.
Let $S$ be its set of stable matchings.
For $\mu, \nu \in S$, write $\mu \le \nu$ if every man likes his partner in $\nu$ at least as much as his partner in $\mu$.
Then:

1. for $\mu, \nu \in S$, sending each man $m$ to the better for him of $\mu(m)$ and $\nu(m)$ gives a stable matching, the join $\mu \vee \nu$;
2. sending each man $m$ to the worse for him of $\mu(m)$ and $\nu(m)$ gives a stable matching, the meet $\mu \wedge \nu$;
3. $(S, \le)$ is a [[distributive lattice|0HM0HQCK6N]];
4. in $\mu \vee \nu$ every woman gets the worse for her of her partners in $\mu$ and $\nu$;
5. $\mu \le \nu$ holds exactly when every woman likes her partner in $\mu$ at least as much as her partner in $\nu$.

## Remarks

The key fact is the opposition of interests.
If $\mu$ and $\nu$ are stable and a man prefers his $\nu$-partner $w$ to his $\mu$-partner, then $w$ prefers her $\mu$-partner to him, since otherwise the pair would block $\mu$.
From this one checks that the pointwise better choice for men is a bijection and has no blocking pair.
Distributivity follows because join and meet are computed partner by partner, by maxima and minima in totally ordered preference lists.
The top of the [[lattice|WH4SFAACAS]] is the man-optimal matching produced by the men-proposing [[Gale–Shapley algorithm|CHWQVJ9F5K]], and the bottom is the woman-optimal matching.
Conversely, every finite distributive lattice is isomorphic to the lattice of stable matchings of some instance.
Example: with $m_1$ ranking $w_1 > w_2$, $m_2$ ranking $w_2 > w_1$, $w_1$ ranking $m_2 > m_1$, and $w_2$ ranking $m_1 > m_2$, both matchings are stable, and the lattice is a chain with two elements.

## Explanations

### L1 human

A stable marriage instance can have many stable pairings.
What is good for the men in one of them is bad for the women.
The stable pairings can be combined: letting each man take the better of his two partners gives another stable pairing.
This makes the set of stable pairings into a well-behaved ordered structure.
The best one for the men is at the top, and the best one for the women is at the bottom.

### L2 human

The lattice structure underlies efficient algorithms for stable matchings with extra goals, such as minimising total regret or finding an egalitarian matching.
Its elements correspond to closed sets of a partial order on so-called rotations, in line with Birkhoff's representation theorem for finite distributive lattices.
