---
tag: Z3AF4DBYQ3
kind: statement
role: theorem
name: von Neumann's theory of almost periodic functions on groups
msc: ["43A60", "22D10"]
uses: [92700QAB5Y, N9WKQ0MSEK, 74BPYJNZTM, FX3NEFYFFN, G852FHZ3W1, EVHCE5VR6Y]
about: [N9WKQ0MSEK]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
---

## Statement

Let $G$ be a [[topological group|92700QAB5Y]], and let $AP(G)$ be the space of [[almost periodic functions|N9WKQ0MSEK]] on $G$, with the uniform norm.

1. There are a [[compact group|EVHCE5VR6Y]] $bG$ and a continuous homomorphism $\beta \colon G \to bG$ with dense image with this property.
The map $f \mapsto f \circ \beta$ is an isometric isomorphism of algebras from $C(bG)$ onto $AP(G)$.
2. Every $f \in AP(G)$ is a uniform limit on $G$ of finite linear combinations of functions $x \mapsto \ip{\pi(x) u}{v}$.
Here $\pi$ is a continuous [[irreducible|FX3NEFYFFN]] [[unitary representation|74BPYJNZTM]] of $G$ on a finite-dimensional space $V$, and $u, v \in V$.

## Remarks

The group $bG$ is the [[Bohr compactification|G852FHZ3W1]] of $G$.
One builds it from the action of $G$ on $AP(G)$.
Another way is to take the closure of the image of $G$ in the product of the unitary groups of its finite-dimensional unitary representations.
Part 2 follows from part 1 and the [[Peter–Weyl theorem|6VC9QE39XH]] for $bG$.
Matrix coefficients of irreducible representations of $bG$ are dense in $C(bG)$, and they pull back to matrix coefficients of $G$.
For $G = \R$, the irreducible finite-dimensional unitary representations are the characters $x \mapsto e^{i\lambda x}$, and part 2 is Bohr's approximation theorem by trigonometric polynomials with real frequencies.
For $G = \mathrm{SL}(2, \R)$, every finite-dimensional unitary representation is trivial, so $bG$ is a point and the only almost periodic functions are constants.

## Explanations

### L1 human

Von Neumann extended Bohr's theory of almost periodic functions from the real line to any group.
The key result is that such functions are built, up to small errors, from the simplest symmetric functions on the group: entries of matrices of finite-dimensional unitary representations.
Equivalently, almost periodic functions on $G$ are just the continuous functions on a compact group attached to $G$.

### L2 human

The theory reduces almost periodic functions on $G$ to harmonic analysis on the compact group $bG$.
With the [[invariant mean|3986F5K9J3]], each $f \in AP(G)$ has a Fourier series indexed by the finite-dimensional irreducible unitary representations of $G$, and this series determines $f$.
A group is called maximally almost periodic when its almost periodic functions separate points, that is, when $\beta$ is injective; abelian locally compact groups and compact groups are examples.
At the other end, minimally almost periodic groups such as $\mathrm{SL}(2, \R)$ have only constant almost periodic functions.
