---
tag: X1NA9ZDY4Y
kind: definition
name: Chevalley basis
msc: ["17B20", "17B45"]
defines: 2JTTJ3XHH4
uses: [EY9DN7QAX1, BB098JPWGA, KZ7RZC8XC4, AVVV93CASN, CSBM217V1N, XV6Q01FVAS, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Chevalley_basis
---

## Definition

Let $\mathfrak{g}$ be a finite-dimensional [[semisimple Lie algebra|EY9DN7QAX1]] over $\C$ with a [[Cartan subalgebra|BB098JPWGA]] $\mathfrak{h}$.
Let $\Phi$ be its [[root system|AVVV93CASN]], let $\mathfrak{g}_\alpha$ be the root space ([[weight space|KZ7RZC8XC4]]) of $\alpha \in \Phi$, and let $\set{\alpha_1, \dots, \alpha_l}$ be a base of [[simple roots|CSBM217V1N]].
For $\alpha \in \Phi$, let $h_\alpha \in \mathfrak{h}$ be its [[coroot|XV6Q01FVAS]]: the element of $[\mathfrak{g}_\alpha, \mathfrak{g}_{-\alpha}]$ with $\alpha(h_\alpha) = 2$.
A *Chevalley basis* of $\mathfrak{g}$ is a [[basis|0KCQ9Y3QKA]] $\set{h_1, \dots, h_l} \cup \set{x_\alpha : \alpha \in \Phi}$ such that:

1. $h_i = h_{\alpha_i}$ for $1 \le i \le l$, and $x_\alpha \in \mathfrak{g}_\alpha$ for each $\alpha \in \Phi$;
2. $[x_\alpha, x_{-\alpha}] = h_\alpha$ for each $\alpha \in \Phi$;
3. if $\alpha, \beta, \alpha + \beta \in \Phi$, then $[x_\alpha, x_\beta] = \pm (r + 1) x_{\alpha + \beta}$, where $r$ is the largest integer with $\beta - r\alpha \in \Phi$.

## Remarks

From these rules, $[h_i, h_j] = 0$, $[h_i, x_\alpha] = \alpha(h_i) x_\alpha$ with $\alpha(h_i) \in \Z$, each $h_\alpha$ is an integer combination of the $h_i$, and $[x_\alpha, x_\beta] = 0$ if $\alpha + \beta \notin \Phi \cup \set{0}$.
So all structure constants are integers.
Example: in $\mathfrak{sl}_2(\C)$, the basis $h = \operatorname{diag}(1, -1)$, $x_\alpha = E_{12}$, $x_{-\alpha} = E_{21}$ is a Chevalley basis, since $[E_{12}, E_{21}] = h$ and $\alpha(h) = 2$; clause 3 is empty.
Non-example: the basis $h, 2E_{12}, E_{21}$ fails clause 2, since $[2E_{12}, E_{21}] = 2h \ne h_\alpha$.
In $\mathfrak{sl}_n(\C)$, the matrix units $E_{ij}$, $i \ne j$, with $h_i = E_{ii} - E_{i+1, i+1}$ form a Chevalley basis.
By a theorem of Chevalley, every complex semisimple Lie algebra has a Chevalley basis.
The $\Z$-span of a Chevalley basis is a Lie ring, from which the [[Chevalley groups|YPCH4Q0V34]] over any field are built.

## Explanations

### L1 human

A Chevalley basis is a basis of a semisimple Lie algebra, made of coroots and root vectors, in which every bracket has integer coefficients.
The sign rule $\pm (r+1)$ fixes the size of each coefficient; only the signs depend on choices.
