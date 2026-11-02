---
tag: 4AG8ZWK2BB
kind: definition
name: Ringed space
msc: [14A15, 54B40]
defines: KNDXDE7K8M
uses: [0CQHFPGJ45, TB6TM6R4MD, 0310REJJY8, JTAKAPTT8H, MZ02BKPHJA, HV6YBS0YDH, 4M94FZH9Y8, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Ringed_space
---

## Definition

A *ringed space* is a pair $(X, \mathcal O_X)$ where $X$ is a [[topological space|0CQHFPGJ45]] and $\mathcal O_X$ is a [[sheaf|TB6TM6R4MD]] of [[commutative rings|0310REJJY8]] on $X$.
The sheaf $\mathcal O_X$ is called the *structure sheaf*.
A *morphism of ringed spaces* $(f, f^\#) \colon (X, \mathcal O_X) \to (Y, \mathcal O_Y)$ consists of two parts.
The first is a [[continuous map|0VGFHTM75Y]] $f \colon X \to Y$.
The second is a ring homomorphism $f^\#_V \colon \mathcal O_Y(V) \to \mathcal O_X(f^{-1}(V))$ for each open set $V \subseteq Y$, compatible with restriction to smaller open sets.

## Remarks

Example: let $X$ be a topological space and let $\mathcal O_X(U)$ be the ring of continuous functions $U \to \R$; then $(X, \mathcal O_X)$ is a ringed space.
The [[stalk|JTAKAPTT8H]] at each point $x$ is a [[local ring|MZ02BKPHJA]], whose maximal ideal consists of the germs that vanish at $x$.

Example: an [[algebraic variety|HV6YBS0YDH]] $X$ over $k$, with $\mathcal O_X(U)$ the ring of [[regular functions|4M94FZH9Y8]] on $U$, is a ringed space.

Example: any topological space $X$ with the sheaf of locally constant functions to a commutative ring $A$ is a ringed space.

Non-example: let $\mathcal B(U)$ be the ring of bounded continuous functions on an open set $U \subseteq \R$.
Then $(\R, \mathcal B)$ is not a ringed space, because $\mathcal B$ is not a sheaf: the sections $x \mapsto x$ on the intervals $(-m, m)$ do not glue.

A ringed space whose stalks are all local rings is a locally ringed space; schemes and varieties are of this kind.
