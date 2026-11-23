---
tag: KGN4PW4YEF
kind: example
name: Atomic sentences of arithmetic
msc: ["03B10", "03F30"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [MCZRXR3SVB]
uses: [MCZRXR3SVB, BP6WW7H5CC, 6D3WA7N2W4, DKFGQTRYZE, 0QFT7Z76N5, 3K1AKGXF8A]
sources:
  - url: https://en.wikipedia.org/wiki/Atomic_formula
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: lead section
---

## Example

An atomic sentence of arithmetic is a claim about two closed terms, so you can decide it by computing.
Let $\sigma = \{ 0, S, +, \cdot, < \}$ be the signature of arithmetic, with arities $0, 1, 2, 2, 2$, where $<$ is a relation symbol.
Consider the strings
$$\alpha: \ S(0) + S(0) = S(S(0)), \qquad \beta: \ S(S(0)) < S(0) \cdot S(S(0)).$$
We check that $\alpha$ and $\beta$ are atomic [[sentences|DKFGQTRYZE]] and decide their truth in $\mathbb{N}$.

1. The strings $0$, $S(0)$ and $S(S(0))$ are closed [[terms|6D3WA7N2W4]], and so are $S(0) + S(0)$ and $S(0) \cdot S(S(0))$.
2. The string $\alpha$ is $t_1 = t_2$ for two terms, so it is [[atomic|MCZRXR3SVB]] by form 1 of the [[definition|BP6WW7H5CC]].
3. The string $\beta$ is $<(t_1, t_2)$ written infix, so it is atomic by form 2.
4. Neither string contains a variable, so neither has a free variable, and both are sentences.
5. In $\mathbb{N}$, $S(0) + S(0)$ has the value $1 + 1 = 2$, and $S(S(0))$ has the value $2$, so $\alpha$ is true.
6. In $\mathbb{N}$, $S(S(0))$ has the value $2$, and $S(0) \cdot S(S(0))$ has the value $1 \cdot 2 = 2$.
   Since $2 < 2$ is false, $\beta$ is false.

So the truth of an atomic sentence in $\mathbb{N}$ is decided by computing the values of two closed terms.

## Remarks

Every atomic sentence of $\sigma$ is decided in $\mathbb{N}$ by a finite computation, since closed terms have computable values.
The proof side agrees: [[Robinson arithmetic|3K1AKGXF8A]], in the signature without $<$, proves every true equation between closed terms and refutes every false one, and so it decides every Boolean combination of them as well.
Hard questions in arithmetic need quantifiers, such as $\forall x \, \exists y \, (x < y \land \cdots)$, and with unbounded quantifiers truth is no longer computable.

If we change one numeral in $\beta$, the answer changes.
The sentence $S(0) < S(0) \cdot S(S(0))$ compares $1$ with $2$, so it is true.

## Explanations

### L1 human

The sentence "$1 + 1 = 2$" is atomic: it compares two expressions without variables.
To decide whether it is true, you compute both sides.
The sentence "$2 < 1 \cdot 2$" is also atomic, and it is false, because $1 \cdot 2 = 2$.

### L2 human

We decide the atomic sentence
$$S(S(0)) \cdot (S(0) + S(S(0))) = S(S(S(S(S(S(0))))))$$
in $\mathbb{N}$ by computing both sides from the leaves up.
On the left, $S(0)$ has the value $1$ and $S(S(0))$ has the value $2$.
Then $S(0) + S(S(0))$ has the value $1 + 2 = 3$, and the product has the value $2 \cdot 3 = 6$.
On the right, six copies of $S$ around $0$ give the value $6$.
So the sentence is true in $\mathbb{N}$.
The typical use of atomic sentences is in the diagram of a structure, the list of basic facts about its named elements.
Watch out: an atomic sentence can be true in one structure and false in another.
The sentence $S(0) + S(0) = 0$ says $2 = 0$ in $\mathbb{N}$, so it is false there.
In $\mathbb{Z}/2\mathbb{Z}$, with $S$ read as adding $1$, it says $1 + 1 = 0$, so it is true there.
