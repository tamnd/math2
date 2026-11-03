---
tag: SBDQH0TJ5X
kind: definition
name: NP
msc: [68Q15]
defines: QQRA9GBW51
uses: [ESPYW94XGR, M7SDX137WE, T00W8RQT8E, 5MFZ4VNY6D, GVT2NKN37K]
sources:
  - url: https://en.wikipedia.org/wiki/NP_(complexity)
---

## Definition

Let $\Sigma$ be a finite alphabet.
Let $t \colon \N \to \N$ be a function.
The class $\mathrm{NTIME}(t)$ is the set of [[languages|5MFZ4VNY6D]] $L \subseteq \Sigma^*$ decided by some [[nondeterministic Turing machine|M7SDX137WE]] $M$ with the following property.
On every input of length $n$, every computation branch of $M$ halts within $O(t(n))$ steps.
The [[complexity class|ESPYW94XGR]] *NP* is
$$\mathrm{NP} = \bigcup_{k \in \N} \mathrm{NTIME}(n^k).$$
Here a nondeterministic machine decides $L$ when an input $w$ lies in $L$ exactly when at least one branch accepts $w$.

## Remarks

Equivalent form with certificates: $L \in \mathrm{NP}$ exactly when there are a polynomial $p$ and a language $V \in$ [[P|GVT2NKN37K]] of pairs such that
$$w \in L \iff \text{there is } c \in \Sigma^* \text{ with } \abs{c} \le p(\abs{w}) \text{ and } (w, c) \in V.$$
The string $c$ is a certificate for $w$, and a machine deciding $V$ is a verifier.

Example: the set of composite numbers, written in binary, is in NP.
A certificate for $m$ is a factor $d$ with $1 < d < m$, which has at most as many digits as $m$.
The verifier checks that $d$ divides $m$ by one division, in polynomial time.

Non-example: a certificate whose length grows like $2^{\abs{w}}$ is not allowed, because the definition bounds $\abs{c}$ by a polynomial in $\abs{w}$.

Every language in P is in NP, with the empty certificate, so $\mathrm{P} \subseteq \mathrm{NP}$.
The name stands for "nondeterministic polynomial time".
