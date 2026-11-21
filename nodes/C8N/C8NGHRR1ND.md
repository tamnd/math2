---
tag: C8NGHRR1ND
kind: example
name: The affine group of a field defines the field
aliases: [affine-group-defines-its-field, field-in-the-affine-group-of-the-line]
msc: ["03C07", "03C60", "20A15"]
topics: [SZRM3N6BXW]
audience: grad
instance_of: [7R0SJPH37J]
uses: [C5BWHPHAGA, G6GMSEZDB1, TJ9G1SBBJP, 0DEBXAJ5SA, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Morley_rank
    locator: Examples
---

## Example

Let $K$ be a [[field|04C5ZBG1WT]].
Let $G$ be the [[affine group|G6GMSEZDB1]] of the line over $K$: the set of pairs $(a, b)$ with $a \in K^\times$ and $b \in K$, where $(a, b)$ stands for the map $x \mapsto a x + b$.
Composition of maps gives the product $(a, b)(c, d) = (a c, a d + b)$, the identity $e = (1, 0)$ and the inverse $(a, b)^{-1} = (a^{-1}, -a^{-1} b)$.
We regard $G$ as a pure group, in the signature $\set{\cdot}$.
We show that the field $K$ is $1$-dimensionally definable in $G$ with the parameter $t = (1, 1)$.

### Two computations

1. Conjugation. For $g = (c, d)$ we have $g (1, b) = (c, c b + d)$, and then $g (1, b) g^{-1} = (c, c b + d)(c^{-1}, -c^{-1} d) = (1, c b)$.
2. [[Centralizer|TJ9G1SBBJP]] of $t$. We have $(c, d)\, t = (c, c + d)$ and $t \,(c, d) = (c, d + 1)$. These are equal exactly when $c = 1$.

### The interpretation

- Domain: $\partial(x)$ is $x \cdot t = t \cdot x$. By computation 2, the domain is the group $A = \set{(1, b) : b \in K}$ of translations.
- Equality: $\varepsilon$ is equality, and the coordinate map is $f(1, b) = b$, a bijection from $A$ onto $K$.
- Addition: $\varphi_+(x, y, z)$ is $z = x \cdot y$. Indeed $(1, b)(1, b') = (1, b + b')$.
- Zero and one: $\varphi_0(x)$ is $x \cdot x = x$, which holds only at $e = (1, 0)$, and $\varphi_1(x)$ is $x = t$.
- Multiplication: $\varphi_\times(x, y, z)$ is $(x = e \wedge z = e) \vee \exists g \, (g t g^{-1} = x \wedge g y g^{-1} = z)$.

### The check for multiplication

1. Let $x = (1, b)$ and $y = (1, b')$ in $A$.
2. If $b = 0$, then $x = e$. No conjugate of $t$ is $e$, by computation 1, so $\varphi_\times$ holds exactly when $z = e = (1, 0 \cdot b')$.
3. If $b \neq 0$, then $g = (c, d)$ satisfies $g t g^{-1} = x$ exactly when $c = b$, by computation 1 with $b = 1$.
4. For each such $g$, computation 1 gives $g y g^{-1} = (1, b b')$, whatever $d$ is. So $\varphi_\times$ holds exactly when $z = (1, b b')$.

So $f(z) = f(x) f(y)$ exactly when $\varphi_\times(x, y, z)$ holds, and $K$ is definable in $G$ over $\set{t}$.

## Remarks

The parameter is needed for this interpretation: every $(1, b)$ with $b \neq 0$ is a [[conjugate|0DEBXAJ5SA]] of $t$, so no element of $A \setminus \set{e}$ is definable without parameters.
A different choice of $t$ gives an isomorphic copy of $K$, rescaled by the conjugation of computation 1.

The group $G$ is also definable in $K$, as the set $K^\times \times K$ with the product formula above.
The two interpretations make $G$ and $K$ bi-interpretable with parameters; see [[this example|SK131CVMFY]].
When $K$ is algebraically closed, this shows that $G$ has Morley rank $2$.
Zilber's field theorem says that this example is typical: an infinite connected solvable group of finite Morley rank that is not nilpotent interprets an algebraically closed field.

## Explanations

### L1 human

The maps $x \mapsto a x + b$ of a line form a group under composition.
Inside this group sit the shifts $x \mapsto x + b$, and composing two shifts adds the amounts.
Conjugating a shift by a stretch $x \mapsto c x$ multiplies its amount by $c$.
So the group remembers both addition and multiplication of the numbers.
For example, conjugating the shift by $1$ with the stretch by $3$ gives the shift by $3$.

### L2 human

We compute one product in $K = \Q$ through the group.

1. Take $x = (1, 2)$ and $y = (1, 5)$, so $f(x) = 2$ and $f(y) = 5$.
2. The element $g = (2, 7)$ satisfies $g t g^{-1} = (1, 2 \cdot 1) = x$, by computation 1.
3. Then $g y g^{-1} = (1, 2 \cdot 5) = (1, 10)$, so $\varphi_\times(x, y, z)$ holds for $z = (1, 10)$.
4. And $f(z) = 10 = 2 \cdot 5$.

The typical use is to find a field inside a group, which is the first step in the analysis of groups of finite Morley rank.
A trap is to use the centralizer of an arbitrary element as the domain: for $K = \Q$, the centralizer of $(2, 0)$ is the group of stretches $\set{(c, 0)}$, which carries only the multiplicative group of $K$.
