---
tag: 5ZJDCNSGHJ
kind: definition
name: Singular cohomology
msc: [55N10]
defines: 6N7BC70CX0
uses: [M0Q5CFJ7ZH, 082GHNPJ53, 4P7GBWJ4RR]
sources:
  - url: https://en.wikipedia.org/wiki/Cohomology
---

## Definition

Let $X$ be a topological space, let $G$ be an [[abelian group|082GHNPJ53]], and let $C_\bullet(X)$ be the singular [[chain complex|WQ82C0M3QB]] of $X$ with integer coefficients.
The group of *singular $n$-cochains* is $C^n(X; G) = \Hom(C_n(X), G)$, that is, the group of all functions from singular $n$-simplices of $X$ to $G$.
The *coboundary* $\delta \colon C^n(X; G) \to C^{n+1}(X; G)$ is $\delta \varphi = \varphi \circ \partial_{n+1}$.
Then $\delta \circ \delta = 0$.
The *singular cohomology* group $H^n(X; G)$ is $\ker(\delta \colon C^n \to C^{n+1}) / \im(\delta \colon C^{n-1} \to C^n)$.
For a subspace $A \subseteq X$, the relative group $H^n(X, A; G)$ is defined in the same way from $\Hom(C_n(X, A), G)$.
These are the cochains that vanish on all simplices in $A$.

## Remarks

A continuous map $f \colon X \to Y$ induces $f^* \colon H^n(Y; G) \to H^n(X; G)$, so $H^n(-; G)$ is a contravariant functor; compare the [[Hom functor|VJXS8AK67E]].
Evaluation $\langle \varphi, c \rangle = \varphi(c)$ of a cochain on a chain gives the *Kronecker pairing* $H^n(X; G) \times H_n(X) \to G$.
The [[universal coefficient theorem|GTA8ZFGZ3N]] gives a split exact sequence $0 \to \operatorname{Ext}(H_{n-1}(X), G) \to H^n(X; G) \to \Hom(H_n(X), G) \to 0$, with [[Ext|4P7GBWJ4RR]] the Ext functor and $H_n$ [[singular homology|M0Q5CFJ7ZH]].
When $G = \Z$ one writes $H^n(X)$.

Example: a $0$-cochain $\varphi$ is a function from points of $X$ to $G$, and $(\delta \varphi)(\sigma) = \varphi(\sigma(1)) - \varphi(\sigma(0))$ for a path $\sigma$.
So $\varphi$ is a cocycle exactly when it is constant on each path component.
Hence $H^0(X; G)$ is the group of functions from the set of path components of $X$ to $G$.

Non-example: on $X = [0, 1]$ the $0$-cochain $\varphi(x) = x$ with $G = \R$ is not a cocycle, because $\delta\varphi$ takes the value $1$ on the path $t \mapsto t$.
