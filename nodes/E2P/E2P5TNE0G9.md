---
tag: E2P5TNE0G9
kind: statement
role: theorem
name: The equation AB − BA = I has no solution in characteristic 0
msc: ["15A15", "15A27"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [0XC1RDBY7A, 8G3X8MPG7E]
uses: [0Y4NF1DRKD, 0GJWQZCPZM, 6NHZRCKJNW]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a product
  - url: https://en.wikipedia.org/wiki/Canonical_commutation_relation
    locator: lead section
---

## Statement

Let $F$ be a field of characteristic $0$ and let $n \ge 1$.
Then there are no $n \times n$ matrices $A$ and $B$ over $F$ with $AB - BA = I_n$.

## Remarks

### Why each hypothesis is needed

- The characteristic must be $0$, or at least must not divide $n$. Over $\mathbb{F}_2$, [[this example|KZD8TFB85C]] gives $2 \times 2$ matrices with $AB - BA = I$.
- Over $\mathbb{F}_p$ there are $p \times p$ solutions for every prime $p$: on $\mathbb{F}_p[x]/(x^p)$ with the basis $1, x, \dots, x^{p-1}$, take $D = d/dx$ and $X$ = multiplication by $x$.
- Then $DX - XD = I$, because $D(x \cdot x^{p-1}) - x D(x^{p-1}) = 0 - (p-1) x^{p-1} = x^{p-1}$ in characteristic $p$, and the other basis vectors are checked by the product rule.
- The proof shows more: over any field, $AB - BA = cI_n$ needs $nc = 0$.

### Consequences

- In characteristic $0$, the identity is not a commutator of two matrices.
- The same holds for $cI$ with $c \neq 0$.

### Generalizations

- No bounded operators on a nonzero Hilbert space satisfy $AB - BA = I$ (a theorem of Wintner and Wielandt). So the [[canonical commutation relation|HKP9E7N7AB]] needs unbounded operators.
- A matrix over a field is a commutator $AB - BA$ if and only if its trace is $0$ (a theorem of Shoda for characteristic $0$, extended by Albert and Muckenhoupt).

## Explanations

### L1 human

The matrix $AB - BA$ measures how far $A$ and $B$ are from commuting.
Over the real or complex numbers it can never be the identity matrix.
The reason is that its diagonal entries always add up to $0$, while those of $I_n$ add up to $n$.

### L2 human

The trace is a linear form that vanishes on every commutator $AB - BA$.
It does not vanish on $I_n$ in characteristic $0$.
In quantum mechanics this is why position and momentum cannot be finite matrices.
