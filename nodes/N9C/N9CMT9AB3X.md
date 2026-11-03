---
tag: N9CMT9AB3X
kind: statement
role: theorem
name: Sipser–Lautemann theorem
msc: [68Q15, 68Q10]
uses: [PTD7E1PKV4, TDQ7AXGM6P]
about: [PTD7E1PKV4, TDQ7AXGM6P]
sources:
  - url: https://en.wikipedia.org/wiki/Sipser–Lautemann_theorem
same_as:
  wikidata: Q7525845
  wikipedia: Sipser–Lautemann theorem
---

## Statement

The class [[BPP|PTD7E1PKV4]] is contained in the second level of the [[polynomial hierarchy|TDQ7AXGM6P]]:
$$\mathrm{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p.$$

## Remarks

The proof below is Lautemann's.
Let $L \in \mathrm{BPP}$ and $x$ of length $n$.
After amplification there is a polynomial-time machine $V$ using $m = m(n)$ random bits, with $m$ polynomial in $n$, such that the set $A_x = \set{r \in \set{0,1}^m : V(x, r) = 1}$ has $\abs{A_x} \ge (1 - 2^{-n}) 2^m$ if $x \in L$ and $\abs{A_x} \le 2^{-n} 2^m$ if $x \notin L$.
Take $n$ large enough that $m 2^{-n} < 1$.
If $x \in L$, a counting argument shows that there are shifts $t_1, \ldots, t_m \in \set{0,1}^m$ with $\bigcup_i (A_x \oplus t_i) = \set{0,1}^m$, where $\oplus$ is bitwise exclusive or.
If $x \notin L$, any $m$ shifts of $A_x$ cover at most $m 2^{-n} 2^m < 2^m$ strings.
Hence
$$x \in L \iff \exists t_1, \ldots, t_m \ \forall r \ \bigvee_{i=1}^m V(x, r \oplus t_i) = 1,$$
which is a $\Sigma_2^p$ condition.
Since BPP is closed under complement, also $\mathrm{BPP} \subseteq \Pi_2^p$.

## Explanations

### L1 human

Randomised polynomial-time algorithms can be replaced by a two-round game of "there is" and "for every" over polynomial-size strings.
So randomness gives at most the power of two alternating quantifiers.
In particular, if $\mathrm{P} = \mathrm{NP}$, then the whole polynomial hierarchy equals P, and then BPP equals P as well.

### L2 human

Michael Sipser and Péter Gács proved the inclusion in 1983, and Clemens Lautemann gave the short proof with random shifts in the same year.
The shifting argument is a basic tool of derandomization: a few shifts of a large set cover the whole cube.
Together with the closure of BPP under complement, it places randomised computation low in the [[polynomial hierarchy|TDQ7AXGM6P]].
It is not known whether BPP is contained in NP.
