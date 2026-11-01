---
tag: RBDJBK63HX
kind: statement
role: theorem
name: Dugundji extension theorem
msc: [54C20, 54C55]
uses: [0VKD1TP7F3, 0ZCK8DQYN1, 0VGFHTM75Y, 0FQSDC2EQ2]
about: [0VGFHTM75Y, 0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Dugundji_extension_theorem
same_as:
  wikidata: Q974873
  wikipedia: Dugundji extension theorem
---

## Statement

Let $X$ be a [[metric space|0VKD1TP7F3]], let $A \subseteq X$ be a [[closed|0ZCK8DQYN1]] subset, and let $L$ be a locally convex topological vector space over $\R$.
Let $f \colon A \to L$ be a [[continuous|0VGFHTM75Y]] map.
Then there is a continuous map $F \colon X \to L$ with $F(a) = f(a)$ for all $a \in A$.
Moreover, $F$ can be chosen with $F(X)$ contained in the [[convex hull|0FQSDC2EQ2]] of $f(A)$.

## Remarks

The proof covers $X \setminus A$ by small open balls whose radii are comparable to the distance to $A$.
It then takes a locally finite open refinement, which exists because metric spaces are paracompact.
For each set $W$ of the refinement, pick a point $a_W \in A$ close to $W$, and let $(\varphi_W)$ be a partition of unity subordinate to the refinement.
Set $F(x) = \sum_W \varphi_W(x) f(a_W)$ for $x \notin A$ and $F = f$ on $A$.
Continuity at points of $A$ uses that $a_W$ is near $x$ when $W$ is near $x$, together with the local convexity of $L$.

Example: with $L = \R$, the theorem gives the [[Tietze extension theorem|0X52TNMTCJ]] for metric spaces, with the bound $\inf f \le F \le \sup f$.

The hypothesis that $A$ is closed is necessary.
On $X = [0, 1]$, the map $f(x) = \sin(1/x)$ is continuous on $A = (0, 1]$, but it has no continuous extension to $X$, because $f$ has no limit at $0$.

## Explanations

### L1 human

If a continuous function is known on a closed part of a metric space, one can always fill in its values on the rest of the space continuously.
This holds not only for real values, but for values in any space where one can form averages in a controlled way.
The filled-in values are averages of known values, so they stay inside the convex hull of the original values.

### L2 human

The theorem extends the Tietze extension theorem from real-valued to vector-valued maps, at the price of assuming that $X$ is metric.
Its main consequence is that every convex subset of a locally convex metrizable topological vector space is an [[absolute retract|DK3MT3HYX5]].
The proof is a model use of partitions of unity on paracompact spaces, and the same technique appears in the [[Michael selection theorem|3RJ1K36A9A]].
