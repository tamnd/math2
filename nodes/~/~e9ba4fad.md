---
tag: ~e9ba4fad
kind: definition
name: Galois group
msc: [12F10]
defines: ~220aa8df
uses: [~05511c4e, ~41b74bde, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_group
    locator: Definition
---

## Definition

Let $L/K$ be a [[field extension|~05511c4e]].
An automorphism of $L/K$ is a ring isomorphism $\sigma \colon L \to L$ with $\sigma(c) = c$ for every $c \in K$.
These automorphisms form a [[group|G5S1M9]] $\operatorname{Aut}(L/K)$ under composition.
If $L/K$ is a [[Galois extension|~aaec2530]], this group is the Galois group of $L/K$, written $\operatorname{Gal}(L/K)$.

## Remarks

Some authors call $\operatorname{Aut}(L/K)$ the Galois group for every extension $L/K$.
The group $\operatorname{Gal}(\mathbb{C}/\mathbb{R})$ has two elements: the identity and complex conjugation.
The group $\operatorname{Aut}(\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q})$ is trivial, because an automorphism must send $\sqrt[3]{2}$ to a real cube root of $2$.
For a finite extension, $|\operatorname{Aut}(L/K)| \le [L : K]$, by the [[bound on the order|~f531c8fd]].

## Explanations

### L1 human

The Galois group collects the symmetries of a bigger field that leave the smaller field unchanged.
Each symmetry permutes the roots of every polynomial over the smaller field.
