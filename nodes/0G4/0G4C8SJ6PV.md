---
tag: 0G4C8SJ6PV
kind: statement
role: theorem
name: Automorphism group of a cyclic group
msc: [20F28]
uses: [0CWXCWP0Y0, 0B85Q41RP6, 0VVPQNVM8S, 08FHNR8Z5D]
sources:
  - url: https://en.wikipedia.org/wiki/Automorphism_group
    locator: Examples
---

## Statement

Let $n$ be a positive integer and let $G$ be a [[cyclic group|0KVGH0J5B3]] of order $n$.
For each integer $a$ with $\gcd(a, n) = 1$, the map $\sigma_a \colon x \mapsto x^a$ is an automorphism of $G$.
The map $a \bmod n \mapsto \sigma_a$ is an [[isomorphism|08MG7H8JW5]] from the [[group of units|0FJ90Y9926]] $(\mathbb{Z}/n\mathbb{Z})^\times$ to $\operatorname{Aut}(G)$.

## Remarks

An automorphism of $G = \langle g \rangle$ is determined by the image of $g$, and this image must be a generator $g^a$ with $\gcd(a, n) = 1$.
Thus $|\operatorname{Aut}(G)| = \varphi(n)$, where $\varphi$ is Euler's totient function.
For the infinite cyclic group, $\operatorname{Aut}(\mathbb{Z}) \cong \{1, -1\}$.

## Explanations

### L1 human

An automorphism of a cyclic group must send a generator to a generator.
Each choice of a generator gives exactly one automorphism.
For $\mathbb{Z}/5\mathbb{Z}$, the generators are $1, 2, 3, 4$, so there are four automorphisms, given by multiplication by $1, 2, 3, 4$.
