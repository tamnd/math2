---
tag: N37SPDWYGS
kind: definition
name: Localization at a prime ideal
msc: [13B30, 13H99]
defines: X6JD4AG973
uses: [4C1AE84N5N, 00MHHZ9SNE, AN9SKEZ3VY, MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Localization_(commutative_algebra)
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $\mathfrak p$ be a [[prime ideal|00MHHZ9SNE]] of $R$.
The set $S = R \setminus \mathfrak p$ is a [[multiplicative set|AN9SKEZ3VY]].
The *localization of $R$ at $\mathfrak p$* is the [[localization|4C1AE84N5N]]
$$R_{\mathfrak p} = S^{-1}R = \set{a/s : a \in R, \ s \in R \setminus \mathfrak p}.$$

## Remarks

The ring $R_{\mathfrak p}$ is a [[local ring|MZ02BKPHJA]].
Its unique maximal ideal is $\mathfrak p R_{\mathfrak p} = \set{a/s : a \in \mathfrak p, \ s \notin \mathfrak p}$.
Indeed, an element $a/s$ with $a \notin \mathfrak p$ has the inverse $s/a$, so every element outside $\mathfrak p R_{\mathfrak p}$ is a unit.
The [[residue field|NJ3APQ8BHH]] $R_{\mathfrak p} / \mathfrak p R_{\mathfrak p}$ is called the residue field of $R$ at $\mathfrak p$.

Example: for $R = \Z$ and $\mathfrak p = p\Z$ with $p$ prime, $\Z_{(p)}$ is the ring of rationals $a/b$ in lowest terms with $p \nmid b$.
Its maximal ideal is $p \Z_{(p)}$ and its residue field is $\Z/p\Z$.
For $\mathfrak p = (0)$ in an [[integral domain|0QVD7WBFGN]] $R$, the localization $R_{(0)}$ is the [[field of fractions|0F2PTGX1A2]] of $R$.

Non-example: the construction needs $\mathfrak p$ to be prime.
For the ideal $6\Z$ of $\Z$, the complement $\Z \setminus 6\Z$ contains $2$ and $3$ but not $6$, so it is not a multiplicative set.

Notation: for an element $f \in R$, the ring $R_f$ is the localization at the powers of $f$, which differs from $R_{\mathfrak p}$.
