---
tag: NBSD5FG7NY
kind: definition
name: co-NP
msc: [68Q15]
defines: 5HWR2NK8N1
uses: [QQRA9GBW51, ESPYW94XGR, 5MFZ4VNY6D, GVT2NKN37K, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Co-NP
---

## Definition

Let $\Sigma$ be a finite alphabet.
For a [[language|5MFZ4VNY6D]] $L \subseteq \Sigma^*$, its complement is $\overline{L} = \Sigma^* \setminus L$.
The [[complexity class|ESPYW94XGR]] *co-NP* is
$$\text{co-NP} = \set{L \subseteq \Sigma^* : \overline{L} \in \mathrm{NP}},$$
where NP is the class [[NP|QQRA9GBW51]].

## Remarks

Equivalent form: $L \in \text{co-NP}$ exactly when there are a polynomial $p$ and a language $V \in$ [[P|GVT2NKN37K]] of pairs with
$$w \in L \iff (w, c) \in V \text{ for every } c \in \Sigma^* \text{ with } \abs{c} \le p(\abs{w}).$$

Example: the set TAUT of encodings of propositional [[tautologies|05006AJ7DZ]] is in co-NP.
Its complement consists of the formulas that are not tautologies, together with strings that encode no formula.
A formula is not a tautology when some assignment makes it false, and such an assignment is a certificate that can be checked in polynomial time.

Non-example: co-NP is not the complement of NP as a set of languages.
The language $\Sigma^*$ lies in both NP and co-NP.

Since P is closed under complement, $\mathrm{P} \subseteq \mathrm{NP} \cap \text{co-NP}$.
