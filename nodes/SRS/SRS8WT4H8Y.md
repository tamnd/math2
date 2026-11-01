---
tag: SRS8WT4H8Y
kind: definition
name: Braid group
msc: ["20F36", "57K10"]
defines: BNR4H5GCTP
uses: [G5S1M9, 0JGEQXQ4AC, SAWBDBHE41, 0515A6D2Y1]
sources:
  - url: https://en.wikipedia.org/wiki/Braid_group
---

## Definition

Let $n \ge 1$ be an integer.
The *braid group on $n$ strands* is the [[group|G5S1M9]] $B_n$ with the [[presentation|0JGEQXQ4AC]] with generators $\sigma_1, \ldots, \sigma_{n-1}$ and the relations

1. $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $1 \le i, j \le n - 1$ with $\abs{i - j} \ge 2$;
2. $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ for $1 \le i \le n - 2$.

## Remarks

Geometrically, $\sigma_i$ is the braid in which strand $i$ crosses over strand $i + 1$ and the other strands go straight down.
By a theorem of Artin, this presentation gives the group of isotopy classes of geometric braids on $n$ strands.
It is the [[Artin group|SAWBDBHE41]] of the Coxeter matrix of $S_n$.

Example: $B_1$ is trivial and $B_2 = \langle \sigma_1 \mid \ \rangle \cong \Z$.
The group $B_3 = \langle \sigma_1, \sigma_2 \mid \sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2 \rangle$ is not abelian.
The map $\sigma_i \mapsto (i \ i{+}1)$ respects both relations, so it gives a surjective homomorphism $B_n \to S_n$ onto the [[symmetric group|0515A6D2Y1]], and $S_3$ is not abelian.
The kernel of $B_n \to S_n$ is the pure braid group.

Non-example: the symmetric group $S_n$ with the transpositions $(i \ i{+}1)$ satisfies relations 1 and 2, but it is not $B_n$ for $n \ge 2$.
In $S_n$ the generators also satisfy $(i \ i{+}1)^2 = 1$, while in $B_n$ each $\sigma_i$ has infinite order, since the map $B_n \to \Z$ with $\sigma_i \mapsto 1$ respects the relations and sends $\sigma_i^k$ to $k$.
