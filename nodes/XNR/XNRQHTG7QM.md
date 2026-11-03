---
tag: XNRQHTG7QM
kind: definition
name: PSPACE
msc: [68Q15]
defines: T9NTRY93ZT
uses: [FDNFGKEEJR, ESPYW94XGR, 5MFZ4VNY6D, GVT2NKN37K, QQRA9GBW51]
sources:
  - url: https://en.wikipedia.org/wiki/PSPACE
---

## Definition

Let $\Sigma$ be a finite alphabet.
The [[complexity class|ESPYW94XGR]] *PSPACE* is
$$\mathrm{PSPACE} = \bigcup_{k \in \N} \mathrm{DSPACE}(n^k),$$
where $\mathrm{DSPACE}$ is defined through the [[space complexity|FDNFGKEEJR]] of deterministic Turing machines.
So a [[language|5MFZ4VNY6D]] $L \subseteq \Sigma^*$ lies in PSPACE when the following holds for some $k$.
Some deterministic Turing machine decides $L$ using $O(n^k)$ work-tape cells on inputs of length $n$.

## Remarks

Example: the set of propositional tautologies lies in PSPACE.
For a formula $\varphi$ with $n$ variables, a machine runs through all $2^n$ assignments, keeping only the current one, and evaluates $\varphi$ at each.
The space used is polynomial in the length of $\varphi$, though the time may be exponential.

Non-example: a machine that stores a table with one entry for each of the $2^n$ assignments uses exponential space.
It does not show that its language lies in PSPACE.

One has $\mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{PSPACE}$, where P is the class [[P|GVT2NKN37K]] and NP is the class [[NP|QQRA9GBW51]].
A machine with polynomial space has at most exponentially many configurations, so PSPACE lies in exponential time.
By Savitch's theorem, PSPACE also equals the class NPSPACE defined with nondeterministic machines.
