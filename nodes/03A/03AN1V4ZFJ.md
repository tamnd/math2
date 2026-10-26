---
tag: 03AN1V4ZFJ
kind: definition
name: Norm on the Gaussian integers
msc: [11R11]
defines: 0WBRJXXDPZ
uses: [0K5W69AC0J]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_integer
    locator: Basic definitions
---

## Definition

The norm on the [[Gaussian integers|0K5W69AC0J]] is the map $N \colon \mathbb{Z}[i] \to \mathbb{N}$,
$$N(a + b i) = a^2 + b^2 = (a + b i)(a - b i).$$

## Remarks

The norm is multiplicative: $N(z w) = N(z) N(w)$ for all $z, w \in \mathbb{Z}[i]$. This follows from $|z w| = |z| |w|$ in $\mathbb{C}$.
$N(z) = 0$ if and only if $z = 0$.
The norm is a Euclidean function on $\mathbb{Z}[i]$.
For example, $N(2 + i) = 5$ and $N(1 + i) = 2$.

## Explanations

### L1 human

The norm is the squared distance from $0$ to the point $a + b i$ in the complex plane.
Because it is multiplicative, it turns questions about factoring Gaussian integers into questions about factoring integers.
