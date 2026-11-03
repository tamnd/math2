---
tag: XZZ00Y5S7R
kind: definition
name: Bode plot
msc: [93C80, 93C05]
defines: EMVW7N54FE
uses: [BMY8QZSD9H, 86JKV3TRFD, 04DXAFN2ES, 070PFSYJJR]
sources:
  - url: https://en.wikipedia.org/wiki/Bode_plot
---

## Definition

Let $G$ be the [[transfer function|86JKV3TRFD]] of a single-input single-output linear time-invariant system, with [[frequency response|BMY8QZSD9H]] $\omega \mapsto G(i\omega)$ defined for $\omega > 0$.
The *Bode plot* of $G$ is the pair of graphs:

1. the *magnitude plot*, the graph of $20 \log_{10} \abs{G(i\omega)}$ (the gain in decibels) against $\log_{10} \omega$;
2. the *phase plot*, the graph of a continuous choice of the [[argument|070PFSYJJR]] $\arg G(i\omega)$ against $\log_{10} \omega$.

## Remarks

Because $\log_{10} \abs{G_1 G_2} = \log_{10} \abs{G_1} + \log_{10} \abs{G_2}$ and $\arg (G_1 G_2) = \arg G_1 + \arg G_2$, the Bode plot of a product is the sum of the Bode plots of the factors.

Example: for $G(s) = 1/(s + 1)$, the magnitude is $-10 \log_{10}(1 + \omega^2)$ decibels.
It is close to $0$ for $\omega \ll 1$, equals about $-3$ decibels at $\omega = 1$, and is close to $-20 \log_{10} \omega$ for $\omega \gg 1$.
The phase is $-\arctan \omega$, which goes from $0$ to $-90$ degrees.
These straight-line approximations are the asymptotes of the plot.

Non-example: the graph of $\abs{G(i\omega)}$ against $\omega$ on linear axes carries the same data but is not a Bode plot, since its axes are not logarithmic.
