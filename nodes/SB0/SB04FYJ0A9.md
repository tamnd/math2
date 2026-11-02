---
tag: SB04FYJ0A9
kind: definition
name: Injective tensor product
msc: [46B28, 46M05]
defines: RQXC5D3M1Y
uses: [06GZ956657, 0BF2DE2SYK, 4A82S5FVRT, 685ZV73JJ8]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_tensor_product
---

## Definition

Let $X$ and $Y$ be [[Banach spaces|06GZ956657]] over $\mathbb{K} = \R$ or $\C$, with [[continuous duals|4A82S5FVRT]] $X^*$ and $Y^*$.
Let $X \otimes Y$ be their algebraic [[tensor product|0BF2DE2SYK]].
For $u = \sum_{i=1}^n x_i \otimes y_i$ in $X \otimes Y$, let
$$\varepsilon(u) = \sup \Big\{ \Big| \sum_{i=1}^n f(x_i) \, g(y_i) \Big| : f \in X^*, \ g \in Y^*, \ \norm{f} \le 1, \ \norm{g} \le 1 \Big\}.$$
This number does not depend on the representation of $u$, and $\varepsilon$ is a norm on $X \otimes Y$, the *injective norm*.
The *injective tensor product* $X \check{\otimes}_\varepsilon Y$ is the completion of $X \otimes Y$ for $\varepsilon$.

## Remarks

The norm is a cross norm: $\varepsilon(x \otimes y) = \norm{x} \, \norm{y}$, by the Hahn–Banach theorem.
It is at most the [[projective norm|685ZV73JJ8]] $\pi$.
The bounds on $f$ and $g$ are needed: without them, scaling $f$ makes the supremum infinite for every $u \ne 0$.

Example: let $X = Y = \R^2$ with the Euclidean norm and $u = e_1 \otimes e_1 + e_2 \otimes e_2$.
Then $\varepsilon(u) = \sup \abs{\ip{f}{g}} = 1$, over unit vectors $f, g$.
The projective norm of $u$ is $2$, so the two norms differ.

For compact Hausdorff spaces $K$ and $L$, the map $f \otimes g \mapsto ((s, t) \mapsto f(s) g(t))$ extends to an isometry of $C(K) \check{\otimes}_\varepsilon C(L)$ onto $C(K \times L)$.
More generally, $C(K) \check{\otimes}_\varepsilon X$ is the space of continuous functions from $K$ to $X$ with the sup norm.
