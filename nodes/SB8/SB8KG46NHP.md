---
tag: SB8KG46NHP
kind: concept
name: Quasiconformal mapping
msc: [30C62, 30C65]
specializes: [0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Quasiconformal_mapping
same_as:
  wikidata: Q380576
  wikipedia: Quasiconformal mapping
---

## Summary

A quasiconformal mapping is an orientation-preserving [[homeomorphism|0QT00PB5G2]] between plane domains that distorts infinitesimal circles into ellipses of bounded eccentricity.
The bound $K \ge 1$ on the ratio of the axes is the maximal dilatation, and $1$-quasiconformal maps are exactly the [[conformal maps|0YYT36R4YD]].
Quasiconformal maps are much more flexible than conformal maps, yet they keep many of their compactness and boundary properties.
They are a basic tool in Teichmüller theory, complex dynamics and the theory of Kleinian groups.

## Explanations

### L1 human

A conformal map sends tiny circles to tiny circles.
A quasiconformal map is allowed to squash tiny circles into tiny ellipses, as long as the ellipses never get too thin.
The number $K$ measures the worst ratio of the long axis to the short axis.
For example, the stretch $(x, y) \mapsto (2x, y)$ of the plane turns every circle into an ellipse with axis ratio $2$, so it is $2$-quasiconformal.
Such maps can bend shapes in ways that conformal maps cannot, which makes them easy to build by hand.
