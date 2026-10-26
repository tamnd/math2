---
tag: 0YKDJBV26S
kind: definition
name: Essential singularity
msc: [30D30]
defines: 0B8837S5T3
uses: [0TYB3HM9KE, 0P18JC72RE, 0WPQYW8MTE]
sources:
  - url: https://en.wikipedia.org/wiki/Essential_singularity
    locator: Formal description
  - url: https://en.wikipedia.org/wiki/Essential_singularity
    locator: Alternative descriptions
---

## Definition

Let $c$ be an [[isolated singularity|0TYB3HM9KE]] of $f$.
The singularity $c$ is essential if it is neither a [[removable singularity|0P18JC72RE]] nor a [[pole|0WPQYW8MTE]] of $f$.

## Remarks

The singularity $c$ is essential if and only if the [[principal part|0NDV5R6Z6X]] of $f$ at $c$ has infinitely many nonzero terms.
Equivalently, $f(z)$ has no limit in $\mathbb{C}$ as $z \to c$, and $|f(z)|$ does not tend to $\infty$.
The standard example is [[exp(1/z) at 0|0NB31CC4SN]]. The function $\sin(1/z)$ also has an essential singularity at $0$.
Near an essential singularity, $f$ comes close to each complex value, by the [[Casorati–Weierstrass theorem|02HHNPC8ED]].

## Explanations

### L1 human

An essential singularity is a bad point that is neither a removable hole nor a point where the function simply goes to infinity.
Near such a point, the function behaves wildly: along different paths it can go to $0$, to infinity, or to any other value.
