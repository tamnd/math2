---
tag: ESRDNKF6WJ
kind: definition
name: Smash product
msc: [16S40, 16T05]
defines: 2ZJ2G308QV
uses: [04C5ZBG1WT, 7XFYP0N84H, 3CTW1P4HBP, 0NZ8JA25WK, NC26CE0Y8B, PCKK4SFZEK]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_smash_product
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $H$ be a [[Hopf algebra|7XFYP0N84H]] over $k$ with comultiplication $\Delta$ and counit $\varepsilon$.
Write $\Delta(h) = \sum h_{(1)} \otimes h_{(2)}$ in [[Sweedler notation|NC26CE0Y8B]].
A *left $H$-module algebra* is an [[associative algebra|3CTW1P4HBP]] $A$ over $k$ with identity that is also a left $H$-[[module|0NZ8JA25WK]], written $h \cdot a$, such that:

1. $h \cdot (ab) = \sum (h_{(1)} \cdot a)(h_{(2)} \cdot b)$ for all $h \in H$ and $a, b \in A$.
2. $h \cdot 1_A = \varepsilon(h) 1_A$ for all $h \in H$.

The *smash product* $A \# H$ is the vector space $A \otimes_k H$, with $a \otimes h$ written $a \# h$, and with the multiplication
$$(a \# h)(b \# g) = \sum a \, (h_{(1)} \cdot b) \# h_{(2)} g.$$

## Remarks

With this product $A \# H$ is an associative algebra with identity $1 \# 1$, and $a \mapsto a \# 1$ and $h \mapsto 1 \# h$ embed $A$ and $H$ as subalgebras.
Example: let $G$ be a group acting on $A$ by algebra automorphisms and let $H = kG$, with $\Delta(g) = g \otimes g$ and $\varepsilon(g) = 1$.
Then clause 1 reads $g \cdot (ab) = (g \cdot a)(g \cdot b)$, clause 2 reads $g \cdot 1 = 1$, and the product is $(a \# g)(b \# h) = a (g \cdot b) \# gh$, so $A \# kG$ is the [[skew group ring|PCKK4SFZEK]] $A * G$.
Example: if $H = U(\mathfrak g)$ for a Lie algebra $\mathfrak g$, with $\Delta(x) = x \otimes 1 + 1 \otimes x$ for $x \in \mathfrak g$, clause 1 says that each $x$ acts by a derivation of $A$.
Non-example: let $G = \set{e, g}$ have order $2$, $A = k[x]$, and let $g$ act linearly by $g \cdot 1 = 1$ and $g \cdot x^n = -x^n$ for $n \ge 1$.
This is a $kG$-module with clause 2, but $g \cdot (x \cdot x) = -x^2$ while $(g \cdot x)(g \cdot x) = x^2$, so clause 1 fails when the characteristic of $k$ is not $2$.
