---
tag: PDMBKJV6JQ
kind: statement
role: theorem
name: Toda's theorem
msc: [68Q15]
uses: [TDQ7AXGM6P, Z5CCVBME2V, M7SDX137WE]
about: [TDQ7AXGM6P]
sources:
  - url: https://en.wikipedia.org/wiki/Toda%27s_theorem
same_as:
  wikidata: Q719966
  wikipedia: Toda's theorem
---

## Statement

Let $\#\mathrm{P}$ be the class of functions $f \colon \set{0,1}^* \to \N$ of the following form.
There is a polynomial-time [[nondeterministic Turing machine|M7SDX137WE]] whose number of accepting paths on each input $x$ is $f(x)$.
Let $\mathrm{P}^{\#\mathrm{P}}$ be the class of languages decided in polynomial time by a deterministic [[oracle machine|Z5CCVBME2V]] with an oracle for some function in $\#\mathrm{P}$.
Then the [[polynomial hierarchy|TDQ7AXGM6P]] is contained in it:
$$\mathrm{PH} \subseteq \mathrm{P}^{\#\mathrm{P}}.$$

## Remarks

The proof has two steps.
First, $\mathrm{PH} \subseteq \mathrm{BPP}^{\oplus \mathrm{P}}$, where $\oplus \mathrm{P}$ is the class of languages decided by the parity of the number of accepting paths.
This step uses the Valiant–Vazirani isolation lemma, which reduces satisfiability to unique satisfiability with random hash functions, applied level by level.
Second, $\mathrm{BPP}^{\oplus \mathrm{P}} \subseteq \mathrm{P}^{\#\mathrm{P}}$.
Here a polynomial transformation turns the parity of a count into a count modulo a large power of $2$.
Then one call to a $\#\mathrm{P}$ oracle sums over all random strings at once.

The theorem can also be written $\mathrm{PH} \subseteq \mathrm{P}^{\mathrm{PP}}$, since $\mathrm{P}^{\mathrm{PP}} = \mathrm{P}^{\#\mathrm{P}}$, where PP is probabilistic polynomial time with unbounded error.
By [[Valiant's theorem on the permanent|E21YAD8156]], an oracle for the permanent of $0$-$1$ matrices decides every problem in PH in polynomial time.

## Explanations

### L1 human

The polynomial hierarchy contains questions with any fixed number of alternations of "there is" and "for every".
Toda's theorem says that all of them can be answered in polynomial time if one can count solutions.
Counting here means asking how many accepting paths an NP machine has.
So counting is at least as powerful as any fixed number of quantifier alternations.

### L2 human

Seinosuke Toda proved the theorem in 1991.
It is surprising because a $\#\mathrm{P}$ oracle seems closely tied to a single NP machine, while PH involves many levels of NP oracles.
Since $\mathrm{P}^{\#\mathrm{P}} \subseteq \mathrm{PSPACE}$, the theorem refines the inclusion $\mathrm{PH} \subseteq \mathrm{PSPACE}$.
It also implies that if the permanent were easy, the whole polynomial hierarchy would collapse to P.
