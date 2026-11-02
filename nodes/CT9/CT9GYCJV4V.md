---
tag: CT9GYCJV4V
kind: definition
name: Derived functor
msc: [18G10, 18G15]
defines: NPMC3K6J2F
uses: [Y9CZ3MTNF1, KAN07YC9T2, S1G61TDW0K, ZW3W6FX4PW, HK2AA1YSQ2, 2J4JJJYP22]
sources:
  - url: https://en.wikipedia.org/wiki/Derived_functor
---

## Definition

Let $\mathcal{A}$ and $\mathcal{B}$ be [[abelian categories|Y9CZ3MTNF1]], and assume that every object of $\mathcal{A}$ has an [[injective resolution|ZW3W6FX4PW]].
Let $F \colon \mathcal{A} \to \mathcal{B}$ be an [[additive functor|KAN07YC9T2]] that is left [[exact|S1G61TDW0K]].
For an object $X$ of $\mathcal{A}$, choose an injective resolution $X \to I^\bullet$.
For $n \ge 0$, the $n$-th *right derived functor* of $F$ at $X$ is the [[cohomology|2J4JJJYP22]]
$$R^n F(X) = H^n(F(I^\bullet)).$$
Dually, if every object has a [[projective resolution|HK2AA1YSQ2]] $P_\bullet \to X$ and $F$ is additive and right exact, the *left derived functors* are $L_n F(X) = H_n(F(P_\bullet))$.

## Remarks

Up to a canonical isomorphism, $R^n F(X)$ does not depend on the resolution, since any two injective resolutions are chain homotopy equivalent; the same argument makes $R^n F$ a functor.
Left exactness gives $R^0 F \cong F$, and a short exact sequence in $\mathcal{A}$ gives a long exact sequence of the $R^n F$.
Example: let $F = \Hom_\Z(\Z/2\Z, -)$ on abelian groups and $X = \Z$, with the injective resolution $0 \to \Z \to \Q \to \Q/\Z \to 0$.
Then $F(\Q) = 0$ and $F(\Q/\Z) = \set{0, 1/2} \cong \Z/2\Z$, so $R^0 F(\Z) = 0$ and $R^1 F(\Z) \cong \Z/2\Z$, which is $\operatorname{Ext}^1_\Z(\Z/2\Z, \Z)$.
Non-example: the complex $0 \to \Z \xrightarrow{\id} \Z \to 0$ is exact, but $\Z$ is not injective, and using it in place of $I^\bullet$ would give $0$ in degree $1$ instead of $\Z/2\Z$.
In general $R^n \Hom_R(M, -) = \operatorname{Ext}^n_R(M, -)$ and $L_n(M \otimes_R -) = \operatorname{Tor}_n^R(M, -)$.
