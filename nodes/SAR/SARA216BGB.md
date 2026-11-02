---
tag: SARA216BGB
kind: definition
name: Variety of algebras
msc: [08B99, 03C05]
defines: AJNZJD8442
uses: [PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
    locator: Definition
---

## Definition

Let $\sigma$ be a signature of function symbols, and let $\Sigma$ be a set of [[identities|PKD440G2XW]] $s \approx t$ in the language of $\sigma$.
An algebra $A$ of signature $\sigma$ *satisfies* $s \approx t$ if $s$ and $t$ take the same value in $A$ for every assignment of the variables.
The class $\operatorname{Mod}(\Sigma)$ is the class of all algebras of signature $\sigma$ that satisfy every identity in $\Sigma$.
A *variety* (or *equational class*) of signature $\sigma$ is a class $\mathcal{V}$ of algebras of signature $\sigma$ with $\mathcal{V} = \operatorname{Mod}(\Sigma)$ for some $\Sigma$.

## Remarks

Example: abelian groups, in the signature $(+, -, 0)$, form a variety.
It is $\operatorname{Mod}(\Sigma)$ for $\Sigma$ the identities $(x + y) + z \approx x + (y + z)$, $x + 0 \approx x$, $x + (-x) \approx 0$ and $x + y \approx y + x$.
Non-example: fields do not form a variety of signature $(+, \cdot, -, 0, 1)$.
Every variety is closed under direct products, but the product $\F_2 \times \F_2$ of two fields is not a field, since $(1, 0) \cdot (0, 1) = (0, 0)$.
By Birkhoff's theorem, a class is a variety if and only if it is closed under homomorphic images, subalgebras and direct products.
Some authors write $\operatorname{Mod}(\Sigma)$ as $V(\Sigma)$.
