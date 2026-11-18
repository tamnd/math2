---
tag: VK1RP97KKY
kind: example
name: A finite countermodel for axiom 4 in K by filtration
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [3NT8RCA6HE, 6ZZSHAKG5F]
uses: [3NT8RCA6HE, 6ZZSHAKG5F, T99DK51S0W, JS8W7PA6JK, NGHWZ9Y7ZV, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Take the [[Kripke model|NGHWZ9Y7ZV]] $\mathfrak{M}$ with $W = \N$, $R = \set{(n, n + 1) : n \in \N}$ and $V(p) = \set{1}$.
Take $\Sigma = \set{p, \square p, \square\square p, \square p \to \square\square p}$, which is closed under subformulas.
We turn the failure of axiom $\mathrm{4}$ at $0$ into a finite countermodel, as in the proof of the [[finite model property|3NT8RCA6HE]] of [[K|JS8W7PA6JK]].

1. $p$ is true only at $1$, by the choice of $V$.
2. $\square p$ is true at $n$ exactly when $n + 1 = 1$, so only at $0$.
3. $\square\square p$ is true at $n$ exactly when $\square p$ is true at $n + 1$, which never happens, since $n + 1 \neq 0$.
4. So $\square p \to \square\square p$ is false at $0$ and true at every $n \geq 1$.
5. The values of $(p, \square p, \square\square p, \square p \to \square\square p)$ are $(0, 1, 0, 0)$ at $0$, $(1, 0, 0, 1)$ at $1$, and $(0, 0, 0, 1)$ at each $n \geq 2$.
6. So the classes of agreement on $\Sigma$ are $[0] = \set{0}$, $[1] = \set{1}$ and $[2] = \set{n : n \geq 2}$.
7. The smallest [[filtration|6ZZSHAKG5F]] takes the images of the arrows: $[0] \to [1]$, $[1] \to [2]$ and $[2] \to [2]$.
8. Check $\square p$: $[0]$ sees only $[1]$, where $p$ is true, so $\square p$ is true at $[0]$. $[1]$ and $[2]$ see only $[2]$, where $p$ is false.
9. Check $\square\square p$: it is false at $[0]$, since $\square p$ is false at $[1]$, and false at $[1]$ and $[2]$, since $\square p$ is false at $[2]$.
10. These values match step 5, as the [[filtration theorem|T99DK51S0W]] says.
11. So $\square p \to \square\square p$ fails at $[0]$ in a model with 3 worlds, below the bound $2^{|\Sigma|} = 16$.

## Remarks

The example shows the filtration method on a concrete formula: an infinite countermodel becomes a finite one.
By [[common modal axiom schemata|FDFQFWPM4X]], axiom $\mathrm{4}$ fails on frames that are not transitive, and the finite frame here is not transitive: $[0] \to [1] \to [2]$ without $[0] \to [2]$.
The loop at $[2]$ is new: $\mathfrak{M}$ has no loops, but the class $[2]$ absorbs the whole tail.
If we take $V(p) = \set{0}$ instead, then $\square p$ is false everywhere, axiom $\mathrm{4}$ holds everywhere, and the method gives no countermodel.
The bound $2^{|\Sigma|}$ is crude: here only 3 of the 16 possible value patterns occur.

## Explanations

### L1 human

Picture days $0, 1, 2, \dots$, with rain only on day $1$.
On day $0$, "it rains tomorrow" is true, but "it rains in two days" is false.
That is the failure we want to keep.
Days $2, 3, 4, \dots$ all look alike for our questions, so we merge them into one day that leads to itself.
The result has 3 days, and the failure on day $0$ is still there.

### L2 human

1. Take the 3-world model with $0 \to 1 \to 2 \to 2$ and $p$ true only at $1$.
2. At $1$, $\square p$ is false, since $2$ lacks $p$.
3. At $0$, $\square p$ is true, since the only successor $1$ has $p$.
4. At $0$, $\square\square p$ is false, since the only successor $1$ makes $\square p$ false. So $\mathsf{K} \nvdash \square p \to \square\square p$.

The typical use of this example is to see each step of the proof that $\mathsf{K}$ has the finite model property.
A trap: the classes are formed by agreement on all of $\Sigma$, so $0$ and $n \geq 2$ fall into different classes, although both lack $p$.
