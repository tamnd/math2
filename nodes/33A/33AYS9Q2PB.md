---
tag: 33AYS9Q2PB
kind: conjecture
name: Lichtenbaum's conjecture on special values
msc: ["11R70", "11R42", "19F27"]
uses: [4HXFKW55WJ, KXS5DQDFYD, MWBDFS2KJ5]
about: [4HXFKW55WJ, KXS5DQDFYD]
sources:
  - url: https://en.wikipedia.org/wiki/Special_values_of_L-functions
history:
  posed_by: Stephen Lichtenbaum
  first_stated: "1973"
---

## Statement

Let $F$ be a totally real [[number field|MWBDFS2KJ5]], that is, every embedding $F \to \C$ has image in $\R$, and let $\mathcal{O}_F$ be its ring of integers.
Let $\zeta_F$ be the [[Dedekind zeta function|KXS5DQDFYD]] of $F$, and let $n \ge 2$ be even.
Then the [[K-groups|4HXFKW55WJ]] $K_{2n-2}(\mathcal{O}_F)$ and $K_{2n-1}(\mathcal{O}_F)$ are finite, and
$$\zeta_F(1 - n) = \pm \, 2^{e} \, \frac{\abs{K_{2n-2}(\mathcal{O}_F)}}{\abs{K_{2n-1}(\mathcal{O}_F)}}$$
for some integer $e$.

## Remarks

The finiteness is known: it follows from Quillen's finite generation theorem and Borel's computation of ranks, since $r_2 = 0$, $2n - 2$ is even and $2n - 1 \equiv 3 \pmod 4$.
The value $\zeta_F(1 - n)$ is a nonzero rational number by the Siegel–Klingen theorem.
Lichtenbaum also proposed a form for all number fields, in which the leading coefficient of $\zeta_F$ at $1 - n$ is compared with the orders of K-groups and the [[Borel regulator|D22EZ3CNAF]].

In the form above, which ignores powers of $2$, the conjecture is now a theorem.
It follows from the main conjecture of Iwasawa theory for totally real fields, proved by Wiles, with the norm residue isomorphism theorem of Rost and Voevodsky.
The case $n = 2$ is the [[Birch–Tate conjecture|S2CHWAZX4V]].

Example: for $F = \Q$ and $n = 2$, $\zeta(-1) = -1/12$, $\abs{K_2(\Z)} = 2$ and $\abs{K_3(\Z)} = 48$, and indeed $-1/12 = -2/24 = -2^{1} \cdot 2/48$.

## Explanations

### L1 human

The values of the Dedekind zeta function of a totally real field at negative odd integers are rational numbers.
Lichtenbaum predicted that their numerators and denominators are explained by the sizes of finite K-groups of the ring of integers, apart from powers of $2$.
It is a higher analogue of the class number formula, in which the class number and the units explain the behaviour of the zeta function at $s = 0$ and $s = 1$.
