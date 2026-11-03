---
tag: BK3091CPGF
kind: object
name: Classifying space BGL
msc: [19D06, 55R35]
uses: [0FCHE902D7, G8R9561PXT, WA796ZCNRX, TG6WHHR7CF, RV0MKJ3CQ6, CFAG3VRXEA, XFGZFM8PC6]
instance_of: [WA796ZCNRX]
sources:
  - url: https://en.wikipedia.org/wiki/Classifying_space
---

## Description

Let $R$ be a ring with identity.
For $n \ge 1$, let $GL_n(R)$ be the [[general linear group|0FCHE902D7]] of invertible $n \times n$ matrices over $R$.
Embed $GL_n(R)$ in $GL_{n+1}(R)$ by $g \mapsto \begin{pmatrix} g & 0 \\ 0 & 1 \end{pmatrix}$, and let $GL(R) = \bigcup_{n \ge 1} GL_n(R)$ be the [[stable general linear group|G8R9561PXT]], viewed as a discrete group.
The space $BGL(R)$ is a [[classifying space|WA796ZCNRX]] of $GL(R)$: a connected CW complex with $\pi_1(BGL(R)) = GL(R)$ and $\pi_k(BGL(R)) = 0$ for all $k \ge 2$.

Check: the [[geometric realization|TG6WHHR7CF]] of the [[nerve|RV0MKJ3CQ6]] of $GL(R)$, seen as a category with one object, has exactly these homotopy groups.
Since $GL(R)$ is the union of the $GL_n(R)$, one can take $BGL(R) = \bigcup_n BGL_n(R)$.

## Remarks

The homology of $BGL(R)$ is the [[group homology|CFAG3VRXEA]] of $GL(R)$, and it is the colimit of the homology of the groups $GL_n(R)$.
In degree $1$, $H_1(BGL(R); \Z) = GL(R)/[GL(R), GL(R)] = K_1(R)$.
The space $BGL(R)$ itself has no higher homotopy groups.
Quillen's [[plus construction|XFGZFM8PC6]] with respect to the commutator subgroup turns it into $BGL(R)^+$, which has the same homology and whose homotopy groups are the K-groups $K_n(R)$ for $n \ge 1$.
For $R = \C$ the group $GL(\C)$ is taken here with the discrete topology, so $BGL(\C)$ is not the space $BU$ of topology.

## Explanations

### L1 human

$BGL(R)$ is a space built so that its loops, up to deformation, are exactly the invertible matrices over $R$, and nothing else happens in higher dimensions.
It turns the algebra of matrices into the shape of a space.
Its homology records the homology of the matrix groups, but its homotopy groups are too simple to be interesting.
After the plus construction, the homotopy groups become the algebraic K-groups of $R$.
