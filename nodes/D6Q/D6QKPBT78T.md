---
tag: D6QKPBT78T
kind: definition
name: Extension and contraction of ideals
msc: [13A15, 13B02]
defines: 5AFH94P4S3
uses: [0GYGHKX834, 0GGE0Z0JQ1, 0MYSA6MYNA, 030TZ0DQWT]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_(ring_theory)
---

## Definition

Let $A$ and $B$ be [[commutative rings|0GYGHKX834]] and let $f \colon A \to B$ be a [[ring homomorphism|0GGE0Z0JQ1]].

1. For an [[ideal|0MYSA6MYNA]] $I$ of $A$, the *extension* of $I$ is the [[ideal generated|030TZ0DQWT]] by $f(I)$ in $B$:
$$I^e = f(I) B = \set{\textstyle\sum_{k=1}^{n} b_k f(a_k) : n \ge 0,\ a_k \in I,\ b_k \in B}.$$
2. For an ideal $J$ of $B$, the *contraction* of $J$ is the preimage $J^c = f^{-1}(J)$, an ideal of $A$.

## Remarks

The relations $I \subseteq I^{ec}$, $J^{ce} \subseteq J$, $I^{e} = I^{ece}$ and $J^{c} = J^{cec}$ hold.
If $J$ is a [[prime ideal|06HC6HK0Z8]] of $B$, then $J^c$ is a prime ideal of $A$, because $A/J^c$ embeds into the integral domain $B/J$.
Example: for the inclusion $\Z \to \Z[i]$, $(2 + i)^c = 5\Z$, since $(2 + i) \cap \Z$ contains $5 = (2+i)(2-i)$ and is a proper ideal containing $5\Z$.
Non-example of the analogous property for extension: $2\Z$ is prime in $\Z$, but $(2\Z)^e = 2\Z[i]$ is not prime, since $(1 + i)^2 = 2i$ lies in it while $1 + i$ does not.
The image $f(I)$ itself need not be an ideal of $B$; for $\Z \subseteq \Q$, the image of $2\Z$ is not an ideal of $\Q$, and its extension is all of $\Q$.
