---
tag: D8A4VEQR98
kind: statement
role: theorem
name: Ulm's theorem
msc: [20K10]
uses: [082GHNPJ53, 01826KMG2H, 01TQB88H4C, 0YSCSX5YZC, 0ZXZ82FTX2, 03GSZ8RTZJ, ZXVBEPMTCN]
about: [082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Height_(abelian_group)
---

## Statement

Let $p$ be a [[prime|01826KMG2H]].
An abelian $p$-group is an [[abelian group|082GHNPJ53]] in which every element has order a power of $p$.
It is *reduced* if its only [[divisible|ZXVBEPMTCN]] subgroup is $\set{0}$.
For an abelian $p$-group $A$, define subgroups $p^\alpha A$ for each [[ordinal|0YSCSX5YZC]] $\alpha$ by $p^0 A = A$, $p^{\alpha+1} A = p(p^\alpha A)$, and $p^\lambda A = \bigcap_{\alpha < \lambda} p^\alpha A$ for limit ordinals $\lambda$.
Let $P_\alpha = \set{x \in p^\alpha A : px = 0}$, a vector space over the [[finite field|0ZXZ82FTX2]] $\F_p$.
The *$\alpha$-th Ulm invariant* of $A$ is $u_\alpha(A) = \dim_{\F_p} (P_\alpha / P_{\alpha+1})$.

Let $A$ and $B$ be [[countable|01TQB88H4C]] reduced abelian $p$-groups.
Then $A \cong B$ if and only if $u_\alpha(A) = u_\alpha(B)$ for every ordinal $\alpha$.

## Remarks

Isomorphic groups have the same Ulm invariants, since an isomorphism carries each $P_\alpha$ onto the corresponding subgroup.
For the converse one builds an isomorphism step by step, by a back-and-forth argument over the countably many elements.
At each step one keeps a partial isomorphism between finite subgroups that preserves the heights of elements.
The equality of the Ulm invariants is what makes each extension step possible.

Example: for $A = \Z/p^k\Z$ with $k \ge 1$, $P_n$ is cyclic of order $p$ for $n < k$ and zero for $n \ge k$, so $u_{k-1}(A) = 1$ and all other invariants vanish.
For a finite abelian $p$-group, $u_n$ counts the cyclic summands of order $p^{n+1}$, and the theorem reduces to the classification of finite abelian $p$-groups.

Countability is necessary.
Let $B = \bigoplus_{n \ge 1} \Z/p^n\Z$, and let $\bar B$ be the torsion part of $\prod_{n \ge 1} \Z/p^n\Z$.
Both are reduced, both have $u_n = 1$ for every finite $n$ and $u_\alpha = 0$ for $\alpha \ge \omega$, but $B$ is countable and $\bar B$ is uncountable, so they are not isomorphic.

## Explanations

### L1 human

A countable abelian group in which every element has order a power of $p$ can be very complicated, with elements divisible by $p$ many times, infinitely many times, and beyond.
Ulm attached to such a group a list of numbers, indexed by ordinals, that measure how many independent elements of order $p$ sit at each level of divisibility.
The theorem says that, for countable groups with no divisible part, this list determines the group completely.

### L2 human

Ulm's theorem extends the classification of finite abelian $p$-groups by cyclic decompositions to all countable reduced $p$-groups, where no cyclic decomposition need exist.
A general countable abelian $p$-group is the direct sum of a [[divisible|ZXVBEPMTCN]] group and a reduced group.
The divisible part is a direct sum of [[Prüfer groups|F0XAMM2PPS]], determined by the number of summands.
So all countable abelian $p$-groups are classified.
The uncountable case has no such classification, as the example above shows.
