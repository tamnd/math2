---
tag: ESR34XYZVZ
kind: statement
role: proposition
name: Weak sunflower conjecture
sources:
  - wikipedia: en:8208248@r1372848827
    locator: Sunflower (mathematics), section Weak sunflower conjecture
    note: adopted
    mention: wikipedia://en/8208248#P463
    sections: [Statement]
inventory: [HXGKSE638C]
---

## Statement

Another version of the problem, sometimes called the **weak sunflower conjecture** or the **Erdős–Szemerédi sunflower conjecture**, deals with the case where the family of sets is a subset of the [[power set|00E0YZCERH]] of an *n*-element set. In this version, the size of the individual sets is not restricted. The conjecture states that if $\mathcal{F}$ is a family of subsets of ${1, 2, \ldots, n}$ and $|\mathcal{F}| > c^n$ for some constant $c<2$, then $\mathcal{F}$ must contain a sunflower of size 3 (the case where $r=3$).

This conjecture was resolved as a consequence of a breakthrough on the cap set problem. Alon, Shpilka, and Umans had previously shown that an exponential upper bound for the cap set problem would imply a solution to the weak sunflower conjecture for $r=3$. In 2016, Ellenberg and Gijswijt, building on the work of Croot, Lev, and Pach, used polynomial methods to prove a tight exponential upper bound on the size of cap sets.

Following this, Eric Naslund and Will Sawin adapted these methods to provide an explicit proof for the weak sunflower conjecture. They proved that the size of any family of subsets of ${1, 2, \ldots, n}$ without a 3-sunflower is at most $3n \sum_{k \le n/3} \tbinom{n}{k}$, which is bounded by $(1.89)^n$ for large $n$. This confirmed the conjecture that such families have a size of at most $c^n$ for a constant $c<2$.
