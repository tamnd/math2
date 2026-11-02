---
tag: VT2DVEEVRH
kind: definition
name: Polish space
msc: ["54E50", "54H05", "03E15"]
defines: 584GXXY73M
uses: [0CQHFPGJ45, 0Z2P41SVDP, 0BY52JW6NK, 0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Polish_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
The space $X$ is *Polish* if:

1. $X$ is [[separable|0Z2P41SVDP]]: it has a countable dense subset.
2. $X$ is completely metrizable: there is a [[metric|0VKD1TP7F3]] $d$ on $X$ that induces the topology of $X$ and makes $(X, d)$ a [[complete metric space|0BY52JW6NK]].

## Remarks

The real line $\R$ is Polish: the rationals are dense, and the usual metric is complete.
The open interval $(0, 1)$ is Polish, because the metric $d(x, y) = \abs{\tan(\pi x - \pi/2) - \tan(\pi y - \pi/2)}$ induces its topology and is complete.
The rationals $\Q$ are a non-example: they are separable and metrizable, but no complete metric induces their topology.
Indeed, by the Baire category theorem a nonempty complete metric space is not a countable union of nowhere dense sets, while $\Q$ is the countable union of its points.
An uncountable discrete space is another non-example: it is completely metrizable but not separable.
A subset of a Polish space is Polish in the subspace topology if and only if it is a $G_\delta$ set.
