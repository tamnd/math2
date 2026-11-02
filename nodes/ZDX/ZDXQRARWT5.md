---
tag: ZDXQRARWT5
kind: definition
name: Colombeau algebra
msc: [46F30]
defines: XGQT4WEVGG
uses: [0V33BNKZ9S, 0R6EWFKRCF, 02BH3MCBQB, 096Z9MP2ME, 0076HWHGHQ, Q0C1H111EN]
sources:
  - url: https://en.wikipedia.org/wiki/Colombeau_algebra
---

## Definition

Let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]], and let $C^\infty(\Omega)$ be the algebra of [[smooth functions|0V33BNKZ9S]] on $\Omega$.
Let $\mathcal{E}(\Omega)$ be the algebra of families $(u_\varepsilon)_{\varepsilon \in (0,1]}$ in $C^\infty(\Omega)$, with pointwise operations.
For a [[compact set|0R6EWFKRCF]] $K \subseteq \Omega$ and a multi-index $\alpha$, let $p_{K,\alpha}(u) = \sup_{x \in K} \abs{\partial^\alpha u(x)}$.

1. A family $(u_\varepsilon)$ is *moderate* if for each $K$ and $\alpha$ there is $N \ge 0$ with $p_{K,\alpha}(u_\varepsilon) = O(\varepsilon^{-N})$ as $\varepsilon \to 0$.
2. A family $(u_\varepsilon)$ is *negligible* if for each $K$, $\alpha$ and $m \ge 0$, $p_{K,\alpha}(u_\varepsilon) = O(\varepsilon^{m})$ as $\varepsilon \to 0$.

The moderate families form a subalgebra $\mathcal{E}_M(\Omega)$, and the negligible families form an [[ideal|096Z9MP2ME]] $\mathcal{N}(\Omega)$ of it.
The *special Colombeau algebra* on $\Omega$ is the [[quotient algebra|0076HWHGHQ]] $\mathcal{G}(\Omega) = \mathcal{E}_M(\Omega) / \mathcal{N}(\Omega)$.

## Remarks

$\mathcal{G}(\Omega)$ is a commutative associative algebra, and the partial derivatives $\partial_j$, applied to each $u_\varepsilon$, pass to the quotient and satisfy the Leibniz rule.
A smooth function $f$ embeds as the class of the constant family $u_\varepsilon = f$, and this embedding keeps products.
On $\R^n$, distributions embed by convolution with a rescaled mollifier $\rho_\varepsilon(x) = \varepsilon^{-n} \rho(x / \varepsilon)$, where $\rho$ is a Schwartz function with $\int \rho = 1$ and all higher moments $0$.
This embedding depends on the choice of $\rho$, and the moment condition makes it agree with the embedding of smooth functions.
The [[Schwartz impossibility theorem|Q0C1H111EN]] shows that the product of continuous functions cannot also be kept; in $\mathcal{G}$ it is kept only up to association.

Example: on $\R$, let $\rho$ be smooth with compact support and $\int \rho = 1$, and let $u_\varepsilon(x) = \varepsilon^{-1} \rho(x / \varepsilon)$.
Then $\sup \abs{\partial^\alpha u_\varepsilon} = \varepsilon^{-1-\alpha} \sup \abs{\rho^{(\alpha)}}$, so the family is moderate.
Its class is associated with the delta: $\int u_\varepsilon \varphi \to \varphi(0)$ for every test function $\varphi$.
Its square is the class of $(u_\varepsilon^2)$.

Non-example: the constant family $u_\varepsilon = e^{1/\varepsilon}$ is not moderate, since $e^{1/\varepsilon}$ grows faster than every power $\varepsilon^{-N}$.
So it defines no element of $\mathcal{G}(\R)$.
