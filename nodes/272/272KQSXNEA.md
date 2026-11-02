---
tag: 272KQSXNEA
kind: definition
name: Classifying space
msc: [55R35, 55R15]
defines: WSZ40H5E4T
uses: [1HDH716Z24, 8E37E74XVP, R5WP8Z69Q8]
sources:
  - url: https://en.wikipedia.org/wiki/Classifying_space
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]].
A *classifying space* of $G$ is the base space $B$ of a [[universal principal $G$-bundle|1HDH716Z24]] $E \to B$.
It is written $BG$, and the total space is written $EG$.

## Remarks

Any two classifying spaces of $G$ are homotopy equivalent, so $BG$ is well defined up to homotopy.
For a CW complex $X$, isomorphism classes of [[principal $G$-bundles|8E37E74XVP]] over $X$ correspond to homotopy classes of maps $X \to BG$.
A principal $G$-bundle over a CW complex with [[contractible|R5WP8Z69Q8]] total space is universal, so its base is a $BG$.

Example: the circle group $S^1$ acts freely on the unit sphere $S^\infty$ of $\C^\infty$, with quotient $\C P^\infty$.
Since $S^\infty$ is contractible, $\C P^\infty$ is a classifying space of $S^1$.

Non-example: $\C P^1$ is not a classifying space of $S^1$.
The bundle $S^3 \to \C P^1$ is a principal $S^1$-bundle, but its total space $S^3$ is not contractible, and $\pi_3(\C P^1) \cong \Z$ while $\pi_3(\C P^\infty) = 0$.

For a discrete group $G$, a classifying space is the same as a [[classifying space of the group|WA796ZCNRX]], an Eilenberg–MacLane space $K(G, 1)$.
Other examples: $BO(n)$ and $BU(n)$ are infinite [[Grassmannians|CYPA882RB9]], and $B\Z = S^1$.
