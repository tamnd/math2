---
tag: 52QT0EK3GJ
kind: definition
name: Analytic set
msc: ["03E15", "28A05", "54H05"]
defines: 3RWWZYPAFV
uses: [584GXXY73M, P2WS16HKD7, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_set
---

## Definition

Let $X$ be a [[Polish space|584GXXY73M]], and let $\mathcal{N} = \N^\N$ be the [[Baire space|P2WS16HKD7]].
A subset $A \subseteq X$ is *analytic* if $A = \emptyset$ or there is a [[continuous map|0VGFHTM75Y]] $f \colon \mathcal{N} \to X$ with $f(\mathcal{N}) = A$.
The class of analytic subsets of $X$ is written $\Sigma^1_1$.

## Remarks

Every closed subset $F$ of $X$ is analytic: if $F$ is nonempty, it is a Polish space, and every nonempty Polish space is a continuous image of $\mathcal{N}$.
More generally every Borel subset of $X$ is analytic.
Non-example by counting: in $X = \R$ there are only $2^{\aleph_0}$ analytic sets.
Indeed, each nonempty one is the image of a continuous map on $\mathcal{N}$, and such a map is determined by its values on a countable dense set.
Since $\R$ has $2^{2^{\aleph_0}}$ subsets, some subset of $\R$ is not analytic.
The following are equivalent forms of the definition.
$A$ is the projection to $X$ of a closed subset of $X \times \mathcal{N}$.
$A$ is the projection to $X$ of a Borel subset of $X \times Y$ for some Polish space $Y$.
$A$ is empty or a continuous image of a Polish space.
Complements of analytic sets are called coanalytic, and they form the class $\Pi^1_1$.
