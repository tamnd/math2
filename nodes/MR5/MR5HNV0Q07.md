---
tag: MR5HNV0Q07
kind: statement
role: theorem
name: Baer's criterion
msc: [16D50, 13C11]
uses: [85H7PRHDPZ, 0NZ8JA25WK, 096Z9MP2ME, 0NRYHJPQG2, 04RXTQA5ZA]
about: [85H7PRHDPZ]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_module
---

## Statement

Let $R$ be a ring with identity and let $E$ be a left [[$R$-module|0NZ8JA25WK]].
Then $E$ is an [[injective module|85H7PRHDPZ]] if and only if the following holds.
For every left [[ideal|096Z9MP2ME]] $I$ of $R$, every $R$-[[linear map|0NRYHJPQG2]] $f \colon I \to E$ extends to an $R$-linear map $g \colon R \to E$.

## Remarks

The condition says that for every such $f$ there is $e \in E$ with $f(a) = ae$ for all $a \in I$; take $e = g(1)$.
One direction is the definition applied to the inclusion $I \subseteq R$.
For the other, let $M \subseteq N$ and $f \colon M \to E$; by [[Zorn's lemma|04RXTQA5ZA]] there is a maximal extension $(M', f')$ of $f$ to a submodule $M' \subseteq N$.
If $x \in N$ is not in $M'$, then $I = \set{a \in R : ax \in M'}$ is a left ideal, the map $a \mapsto f'(ax)$ extends to $R$ by hypothesis, and this extends $f'$ to $M' + Rx$, a contradiction; so $M' = N$.

Example: over a [[principal ideal domain|0CMD0BCH8T]] $R$, a divisible module $E$ is injective.
A nonzero ideal is $I = (r)$ with $r \ne 0$, and a map $f \colon I \to E$ is fixed by $f(r)$; choose $e$ with $re = f(r)$, then $a \mapsto ae$ extends $f$.
For instance $\Q$ and $\Q/\Z$ are injective $\Z$-modules.

## Explanations

### L1 human

To check that a module is injective, one should extend maps from every submodule of every module, which is a lot of work.
Baer's criterion says that it is enough to extend maps defined on ideals of the ring into the whole ring.
So injectivity only has to be tested against one module, the ring itself.

### L2 human

The criterion is the main tool for proving that a given module is injective.
Over a principal ideal domain it shows that injective means divisible, which gives the injective $\Z$-modules $\Q$ and $\Q/\Z$.
From this one shows that every module embeds in an injective one, first for abelian groups and then for modules over any ring via $\Hom_\Z(R, -)$.
This existence result is what makes injective resolutions, and so right derived functors such as $\operatorname{Ext}$, available.
