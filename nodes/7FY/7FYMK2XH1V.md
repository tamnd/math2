---
tag: 7FYMK2XH1V
kind: definition
name: Radical extension
msc: [12F10, 12F05]
defines: V74WMGQQ9D
uses: [0WQ1A8SHTZ, 0P6SBR7YM2]
sources:
  - url: https://en.wikipedia.org/wiki/Radical_extension
---

## Definition

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]].
It is a *radical extension* if there are elements $\alpha_1, \dots, \alpha_m \in L$ and positive integers $n_1, \dots, n_m$ such that:

1. $L = K(\alpha_1, \dots, \alpha_m)$;
2. $\alpha_1^{n_1} \in K$;
3. $\alpha_i^{n_i} \in K(\alpha_1, \dots, \alpha_{i-1})$ for each $i$ with $2 \le i \le m$.

Equivalently, there is a tower $K = K_0 \subseteq K_1 \subseteq \dots \subseteq K_m = L$ in which each $K_i = K_{i-1}(\alpha_i)$ is a [[simple extension|0P6SBR7YM2]] with $\alpha_i^{n_i} \in K_{i-1}$.

## Remarks

Example: $L = \Q(\sqrt{2}, \sqrt[3]{1 + \sqrt{2}})$ is radical over $\Q$, with $\alpha_1 = \sqrt{2}$, $n_1 = 2$, $\alpha_2 = \sqrt[3]{1 + \sqrt{2}}$, $n_2 = 3$, and $\alpha_2^3 = 1 + \sqrt{2} \in \Q(\alpha_1)$.
Non-example: let $\theta = \cos(2\pi/7)$, a root of the irreducible cubic $8x^3 + 4x^2 - 4x - 1$.
The field $\Q(\theta)$ is real, and its three conjugates $\cos(2\pi k/7)$, $k = 1, 2, 3$, are real, so by the [[casus irreducibilis|MJ864PBRRJ]] $\theta$ lies in no radical extension of $\Q$ contained in $\R$.
In particular $\Q(\theta)/\Q$ is not radical, although $\Q(\theta)$ lies inside the radical extension $\Q(\zeta_7)$, with $\zeta_7 = e^{2\pi i/7}$.
A radical extension is finite, but it need not be normal or separable: $\Q(\sqrt[3]{2})/\Q$ is radical and not normal.
