---
tag: J3JV10S9YX
kind: definition
name: Gowers norm
msc: [11B30, 05D10]
defines: ZBFZGA1J5G
uses: [082GHNPJ53, 0FTH2E9TAS, 0V2WP9B1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Gowers_norm
---

## Definition

Let $G$ be a finite [[abelian group|082GHNPJ53]], let $f \colon G \to \C$ be a function, and let $k \ge 1$ be an integer.
For $\omega = (\omega_1, \dots, \omega_k) \in \set{0, 1}^k$ and $h = (h_1, \dots, h_k) \in G^k$, write $\omega \cdot h = \omega_1 h_1 + \dots + \omega_k h_k$ and $\abs{\omega} = \omega_1 + \dots + \omega_k$.
Let $\mathcal{C}$ be [[complex conjugation|0FTH2E9TAS]], so $\mathcal{C}^m z$ is $z$ for even $m$ and $\bar z$ for odd $m$.
The *Gowers $U^k$ norm* of $f$ is the nonnegative real number $\norm{f}_{U^k}$ with
$$\norm{f}_{U^k}^{2^k} = \frac{1}{\abs{G}^{k+1}} \sum_{x \in G} \sum_{h \in G^k} \prod_{\omega \in \set{0,1}^k} \mathcal{C}^{\abs{\omega}} f(x + \omega \cdot h).$$

## Remarks

The sum on the right is a nonnegative real number, so the root is defined.
For $k \ge 2$ the map $f \mapsto \norm{f}_{U^k}$ is a [[norm|0V2WP9B1MF]] on the space of functions $G \to \C$.
For $k = 2$, with the Fourier transform $\hat f(\chi) = \abs{G}^{-1} \sum_x f(x) \overline{\chi(x)}$, one has $\norm{f}_{U^2}^4 = \sum_\chi \abs{\hat f(\chi)}^4$.
For a character $\chi$ of $G$, each product $\chi(x) \overline{\chi(x + h_1)} \, \overline{\chi(x + h_2)} \, \chi(x + h_1 + h_2)$ equals $1$, so $\norm{\chi}_{U^2} = 1$.
For $k = 1$ the formula gives $\norm{f}_{U^1} = \abs{\abs{G}^{-1} \sum_x f(x)}$, which is only a seminorm.
A nontrivial character $\chi$ has $\norm{\chi}_{U^1} = 0$ but $\chi \ne 0$, so $U^1$ fails positive definiteness.
The norms increase with $k$: $\norm{f}_{U^k} \le \norm{f}_{U^{k+1}}$.
