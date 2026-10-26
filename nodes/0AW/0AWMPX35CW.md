---
tag: 0AWMPX35CW
kind: statement
role: theorem
name: K[x]/(f) is a field iff f is irreducible
msc: ["12E05"]
uses: [095ZHQ7WCJ, 0WD3SE7S1X, 0DQG39K2NH, 00X2A9G9W3]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_polynomial
    locator: Field extension
---

## Statement

Let $K$ be a [[field|0QA8CHH8MG]] and let $f \in K[x]$.
Then the [[quotient ring|0VFW4Y69BT]] $K[x]/(f)$ is a field if and only if $f$ is [[irreducible|00X2A9G9W3]] over $K$.

## Remarks

The proof: $K[x]$ is a [[principal ideal domain|0RZYDVZ475]]. So $(f)$ is maximal if and only if $f$ is irreducible, by the [[theorem on PIDs|095ZHQ7WCJ]]. Then [[$R/M$ is a field iff $M$ is maximal|0WD3SE7S1X]].
For example, $\mathbb{R}[x]/(x^2 + 1) \cong \mathbb{C}$ and $\mathbb{Q}[x]/(x^2 - 2) \cong \mathbb{Q}(\sqrt{2})$.
The field $\mathbb{F}_2[x]/(x^2 + x + 1)$ has $4$ elements.
If $f$ is irreducible of degree $n$, then $K[x]/(f)$ is an extension of $K$ of degree $n$.
The class of $x$ in $K[x]/(f)$ is a root of $f$.

## Explanations

### L1 human

You can build new fields from polynomials.
Take an irreducible polynomial $f$ and declare $f(x) = 0$.
The result is a field in which $f$ has a root, as the complex numbers come from $x^2 + 1 = 0$.
