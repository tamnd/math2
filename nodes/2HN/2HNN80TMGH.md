---
tag: 2HNN80TMGH
kind: definition
name: Wavelet packet decomposition
msc: [42C40, 65T60, 94A12]
defines: 2QKRBPS8B9
uses: [PDVYQAW887, P3H4MMC4ZH]
sources:
  - url: https://en.wikipedia.org/wiki/Wavelet_packet_decomposition
---

## Definition

Let $(h_n)$ and $(g_n)$ be the real low-pass and high-pass filters of an orthonormal wavelet, with $g_n = (-1)^n h_{1-n}$, as in the [[fast wavelet transform|PDVYQAW887]].
For a sequence $c = (c_m)_{m \in \Z}$ define the sequences $Hc$ and $Gc$ by
$$(Hc)_k = \sum_m h_{m-2k} \, c_m, \qquad (Gc)_k = \sum_m g_{m-2k} \, c_m.$$
Let $x$ be a sequence and let $J \ge 1$ be an integer.
The *wavelet packet decomposition* of $x$ to depth $J$ is the family of sequences $w_{j,p}$, for $0 \le j \le J$ and $0 \le p < 2^j$, defined by

1. $w_{0,0} = x$;
2. $w_{j+1,2p} = H w_{j,p}$ and $w_{j+1,2p+1} = G w_{j,p}$ for $0 \le j < J$.

The sequences $w_{j,p}$ are the nodes of a full binary tree, in which $w_{j,p}$ has children $w_{j+1,2p}$ and $w_{j+1,2p+1}$.

## Remarks

The [[discrete wavelet transform|P3H4MMC4ZH]] keeps only the nodes $w_{j,0}$ and $w_{j,1}$, that is, it splits only the low-pass branch again.

Each step $c \mapsto (Hc, Gc)$ is an orthogonal transform of $\ell^2(\Z)$, by the orthonormality of the filters.
So for every admissible subtree, in which each node is either a leaf or has both children, the leaves together determine $x$ and preserve its energy.
For a finite signal of length $N = 2^J$ with periodic extension, every level contains $N$ coefficients in total.

Example: with the Haar filters and $x = (1, 1, 1, 1)$, level $1$ gives $w_{1,0} = (\sqrt{2}, \sqrt{2})$ and $w_{1,1} = (0, 0)$.
Level $2$ gives $w_{2,0} = (2)$, $w_{2,1} = (0)$, $w_{2,2} = (0)$ and $w_{2,3} = (0)$.
The energy $4$ of $x$ is kept in each level.

Non-example: if only $H$ is applied at a node and $G$ is dropped, the leaves no longer determine the signal.
With the Haar filters, $(1, -1)$ and $(0, 0)$ both have $H$-output $(0)$.

## Explanations

### L1 human

At every node of the tree, the current list of numbers is split into a smooth half and a detail half.
Unlike the plain wavelet transform, the detail halves are split again too.
