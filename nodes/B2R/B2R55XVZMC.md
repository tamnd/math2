---
tag: B2R55XVZMC
kind: example
name: Flat coherence spaces and their negations
msc: ["03F52", "68Q55"]
topics: [98QF5J4W16]
audience: research
instance_of: [WSGZ5HGK1X]
uses: [6RQPAH8SBK]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_space
    locator: Examples
  - book: isbn:9780521371810
    note: Girard, Lafont and Taylor, Proofs and Types
---

## Example

For a set $X$, the *flat* coherence space on $X$ has web $X$, and two tokens cohere only if they are equal.
Its cliques are $\emptyset$ and the singletons $\set{x}$, so a point is "no answer yet" or one answer $x$.
The Wikipedia article on coherent spaces calls it the discrete coherence space on $X$.

1. $\mathbf{Bool}$ is the flat space on $\set{t, f}$, with cliques $\emptyset$, $\set{t}$, $\set{f}$.
2. $\mathbf{Nat}$ is the flat space on $\mathbb{N}$, with cliques $\emptyset$ and $\set{n}$ for $n \in \mathbb{N}$.
3. The linear negation $\mathbf{Bool}^{\perp}$ has $t \frown f$, so its cliques are all four subsets of $\set{t, f}$.
4. A clique of $\mathbf{Bool}$ and a clique of $\mathbf{Bool}^{\perp}$ meet in at most one token: for example $\set{t} \cap \set{t, f} = \set{t}$.
5. $\mathbf{Bool} \mathbin{\&} \mathbf{Bool}$ has web $\set{t_1, f_1, t_2, f_2}$, where $t_1 \frown t_2$, $t_1 \frown f_2$, $f_1 \frown t_2$ and $f_1 \frown f_2$, but $t_1$ and $f_1$ do not cohere, nor $t_2$ and $f_2$.
6. Its maximal cliques are $\set{t_1, t_2}$, $\set{t_1, f_2}$, $\set{f_1, t_2}$ and $\set{f_1, f_2}$, the four pairs of booleans.
7. $\mathbf{Bool} \oplus \mathbf{Bool}$ has the same web with no coherence between distinct tokens, so it is the flat space on four tokens.

## Remarks

The cliques of $\mathbf{Bool} \mathbin{\&} \mathbf{Bool}$ are the partial pairs, such as $\set{t_1}$, "first component true, second unknown".
In $\mathbf{Bool} \oplus \mathbf{Bool}$ a point is a tagged boolean: it says from which side it comes.
So $\mathbin{\&}$ is a product and $\oplus$ is a sum, which matches their sequent rules.

## Explanations

### L1 human

A flat space is a question with a list of possible answers.
At first we know no answer, and then we know one answer.
Two different answers can never both hold, so they are not coherent.

### L2 human

We count the cliques of the flat space $\mathbf{Bool}$ and of $\mathbf{Bool} \mathbin{\&} \mathbf{Bool}$.

1. $\mathbf{Bool}$ has $3$ cliques: $\emptyset$, $\set{t}$, $\set{f}$.
2. A clique of $\mathbf{Bool} \mathbin{\&} \mathbf{Bool}$ is a pair of a clique of each part, since tokens from different parts cohere.
3. So it has $3 \cdot 3 = 9$ cliques.
4. $\mathbf{Bool} \oplus \mathbf{Bool}$ has $5$ cliques: $\emptyset$ and the four singletons.

The typical use of flat spaces is to interpret base types such as booleans and natural numbers.
A trap: the web of $\mathbf{Bool}^{\perp}$ is the same as that of $\mathbf{Bool}$, but its points are different.
