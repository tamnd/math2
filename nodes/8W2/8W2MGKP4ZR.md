---
tag: 8W2MGKP4ZR
kind: definition
name: Polynomial hierarchy
msc: [68Q15, 03D15]
defines: TDQ7AXGM6P
uses: [GVT2NKN37K, QQRA9GBW51, 5HWR2NK8N1, Z5CCVBME2V]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_hierarchy
---

## Definition

Let $k \ge 1$.
Let $q$ be a polynomial, and let $R$ be a language in [[P|GVT2NKN37K]] whose elements are $(k+1)$-tuples of strings.
A language $L \subseteq \set{0,1}^*$ is in $\Sigma_k^p$ if, for some such $q$ and $R$ and for all $x$,
$$x \in L \iff \exists y_1 \, \forall y_2 \, \exists y_3 \cdots Q_k y_k \; (x, y_1, \ldots, y_k) \in R.$$
Here each $y_i$ ranges over strings of length at most $q(\abs{x})$.
The quantifiers alternate, so $Q_k$ is $\exists$ for odd $k$ and $\forall$ for even $k$.
The class $\Pi_k^p$ is the class of complements of languages in $\Sigma_k^p$.
Set $\Sigma_0^p = \Pi_0^p = \mathrm{P}$.
The *polynomial hierarchy* is
$$\mathrm{PH} = \bigcup_{k \ge 0} \Sigma_k^p.$$

## Remarks

The first level is $\Sigma_1^p = \mathrm{NP}$ and $\Pi_1^p = \text{co-NP}$.
Example: the set of propositional formulas $\varphi(u, v)$ such that some assignment of $u$ makes $\varphi$ true for every assignment of $v$ is in $\Sigma_2^p$.
Take $y_1 = u$, $y_2 = v$, and let $R$ be the set of triples $(\varphi, u, v)$ with $\varphi(u, v)$ true, which is in P.

Non-example: the number $k$ of quantifier blocks is fixed for each language in PH.
The [[true quantified Boolean formula|WV2N01B4YV]] problem allows any number of alternations, and it is not known to be in PH.
If it were in $\Sigma_k^p$, then PSPACE would equal $\Sigma_k^p$ and the hierarchy would collapse to level $k$.

With [[oracle machines|Z5CCVBME2V]] the levels can also be written $\Sigma_{k+1}^p = \mathrm{NP}^{\Sigma_k^p}$, and one sets $\Delta_{k+1}^p = \mathrm{P}^{\Sigma_k^p}$.
Then $\Sigma_k^p \cup \Pi_k^p \subseteq \Delta_{k+1}^p \subseteq \Sigma_{k+1}^p \cap \Pi_{k+1}^p$.
If $\Sigma_k^p = \Pi_k^p$ for some $k$, then $\mathrm{PH} = \Sigma_k^p$.
