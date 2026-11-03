---
tag: DMS75X11WN
kind: definition
name: Conditional mutual information
msc: [94A17]
defines: PW6PXZ2WV4
uses: [0X2J0VY6DN, 0DR81R1F2B, 0ZN9EZTEM6, 0THJ7416DX, A83CYGDXFG, F3ZNDD6GG7]
sources:
  - url: https://en.wikipedia.org/wiki/Conditional_mutual_information
---

## Definition

Let $X$, $Y$ and $Z$ be [[discrete random variables|0X2J0VY6DN]] on a common probability space, with values in countable sets $\mathcal{X}$, $\mathcal{Y}$ and $\mathcal{Z}$.
Let $p(x, y, z)$ be their [[joint mass function|0DR81R1F2B]], and let $p(x, z)$, $p(y, z)$ and $p(z)$ be the marginal mass functions.
The *conditional mutual information* of $X$ and $Y$ given $Z$ is
$$I(X; Y \mid Z) = \sum_{x, y, z \,:\, p(x, y, z) > 0} p(x, y, z) \log \frac{p(z) \, p(x, y, z)}{p(x, z) \, p(y, z)} \in [0, \infty].$$

## Remarks

Grouping the terms by $z$ gives $I(X; Y \mid Z) = \sum_{z : p(z) > 0} p(z) \, I(X; Y \mid Z = z)$, where $I(X; Y \mid Z = z)$ is the [[mutual information|A83CYGDXFG]] of $X$ and $Y$ under the [[conditional law|0ZN9EZTEM6]] given $Z = z$.
So $I(X; Y \mid Z) \ge 0$, with equality exactly when $X$ and $Y$ are [[conditionally independent|0THJ7416DX]] given $Z$.
When the entropies are finite, $I(X; Y \mid Z) = H(X \mid Z) - H(X \mid Y, Z)$, with the [[conditional entropy|F3ZNDD6GG7]].
The chain rule $I(X; Y, Z) = I(X; Z) + I(X; Y \mid Z)$ holds.

Example: let $X$ and $Y$ be independent fair bits and $Z = X + Y \bmod 2$.
Given $Z = z$, the pair $(X, Y)$ is $(0, z)$ or $(1, 1 - z)$ with probability $\frac12$ each, so $Y$ determines $X$ and $I(X; Y \mid Z = z) = 1$ bit.
Hence $I(X; Y \mid Z) = 1$ bit, although $I(X; Y) = 0$.

Non-example: if $Z$ has a density, then $p(z) = 0$ for every $z$, so the formula does not apply.
Conditioning on such a variable needs the measure-theoretic form with conditional laws.
If $Z$ is constant, then $I(X; Y \mid Z) = I(X; Y)$.

## Explanations

### L1 human

Conditional mutual information is mutual information computed inside each slice $Z = z$ and then averaged over the slices.
