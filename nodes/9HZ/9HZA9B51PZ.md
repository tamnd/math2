---
tag: 9HZA9B51PZ
kind: definition
name: Spectral sequence
msc: [18G40, 55T05]
defines: GG8AYV847V
uses: [Y9CZ3MTNF1, 2J4JJJYP22, HNK1Y62G7V]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_sequence
---

## Definition

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]] and let $a \ge 0$ be an integer.
A *cohomological spectral sequence* in $\mathcal{A}$ starting at page $a$ consists of:

1. for every $r \ge a$ and all integers $p, q$, an object $E_r^{p,q}$ of $\mathcal{A}$;
2. for every $r \ge a$ and all $p, q$, a morphism $d_r^{p,q} \colon E_r^{p,q} \to E_r^{p+r, q-r+1}$ such that $d_r^{p+r, q-r+1} \circ d_r^{p,q} = 0$;
3. for every $r \ge a$ and all $p, q$, an isomorphism of $E_{r+1}^{p,q}$ with the [[homology|2J4JJJYP22]] $\ker d_r^{p,q} / \im d_r^{p-r, q+r-1}$.

The family $(E_r^{p,q})_{p,q}$ is the *$r$-th page*.

## Remarks

A spectral sequence is *first quadrant* if $E_a^{p,q} = 0$ unless $p \ge 0$ and $q \ge 0$.
Then for fixed $(p, q)$ the differentials into and out of $E_r^{p,q}$ vanish for $r$ large, so $E_r^{p,q}$ is eventually constant; its value is $E_\infty^{p,q}$.
The sequence *converges* to objects $H^n$, written $E_a^{p,q} \Rightarrow H^{p+q}$, if each $H^n$ has a finite [[filtration|HNK1Y62G7V]] $H^n = F^0 H^n \supseteq F^1 H^n \supseteq \cdots \supseteq F^{n+1} H^n = 0$ with $F^p H^n / F^{p+1} H^n \cong E_\infty^{p, n-p}$.
Example: if $E_2^{p,q} = 0$ for $q \ne 0$, then every $d_r$ with $r \ge 2$ starts or ends at a zero object, because it changes $q$ by $1 - r \ne 0$; so $E_2 = E_\infty$ and $H^n \cong E_2^{n,0}$.
Non-example: let $E_2^{0,1} = E_2^{2,0} = \Z/2\Z$, all other $E_2^{p,q} = 0$, let $d_2^{0,1}$ be the identity of $\Z/2\Z$, and put $E_3 = E_2$.
Clause 3 fails, since the homology of $d_2$ is zero at $(0,1)$ and at $(2,0)$, while $E_3^{0,1} = \Z/2\Z$.
Homological spectral sequences are defined in the same way with $d^r \colon E^r_{p,q} \to E^r_{p-r, q+r-1}$.
