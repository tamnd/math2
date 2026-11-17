---
tag: QWAM86B7NF
kind: example
name: Comparing cardinalities with a Henkin quantifier
msc: ["03C80", "03B16"]
topics: [MDHDYV8QZW]
audience: research
instance_of: [KMNVEGS34N]
uses: [KMNVEGS34N, 09NWETVTNY, 0A9V6RKQG6, 0HGVCWQGY3]
sources:
  - url: https://en.wikipedia.org/wiki/Branching_quantifier
    locator: Definition and properties
---

## Example

Let the vocabulary have two unary relation symbols $P$ and $R$.
The [[branching quantifier|KMNVEGS34N]] sentence is
$$\sigma := \begin{pmatrix} \forall x_1 & \exists y_1 \\ \forall x_2 & \exists y_2 \end{pmatrix} \Bigl( \bigl( (P(x_1) \land P(x_2)) \to (x_1 = x_2 \leftrightarrow y_1 = y_2) \bigr) \land \bigl( P(x_1) \to R(y_1) \bigr) \Bigr).$$
We show that a structure $\mathcal{M}$ satisfies $\sigma$ if and only if there is an [[injective|09NWETVTNY]] map from $P^{\mathcal{M}}$ to $R^{\mathcal{M}}$, that is, $|P^{\mathcal{M}}| \leq |R^{\mathcal{M}}|$.

1. By the meaning of the Henkin quantifier, $\mathcal{M} \models \sigma$ if and only if there are $f, g : M \to M$ such that, for all $a_1, a_2 \in M$, the two conjuncts hold with $y_1 = f(a_1)$ and $y_2 = g(a_2)$.
2. Suppose that $f$ and $g$ exist, and let $a \in P^{\mathcal{M}}$. With $a_1 = a_2 = a$, the first conjunct gives $f(a) = g(a)$. So $f$ and $g$ agree on $P^{\mathcal{M}}$.
3. For $a_1, a_2 \in P^{\mathcal{M}}$, the first conjunct and step 2 give $a_1 = a_2 \leftrightarrow f(a_1) = f(a_2)$. So $f$ is injective on $P^{\mathcal{M}}$.
4. The second conjunct gives $f(a) \in R^{\mathcal{M}}$ for every $a \in P^{\mathcal{M}}$. So the restriction of $f$ is an injective map from $P^{\mathcal{M}}$ to $R^{\mathcal{M}}$.
5. Conversely, let $h : P^{\mathcal{M}} \to R^{\mathcal{M}}$ be injective. Define $f = g$ by $f(a) = h(a)$ for $a \in P^{\mathcal{M}}$ and $f(a) = a$ for the other elements.
6. If $a_1$ or $a_2$ is outside $P^{\mathcal{M}}$, the first conjunct holds because its hypothesis is false. If both lie in $P^{\mathcal{M}}$, it holds because $h$ is injective.
7. The second conjunct holds because $h$ takes values in $R^{\mathcal{M}}$. So $\mathcal{M} \models \sigma$.

Two instances on the domain $\set{1, 2, 3, 4, 5}$ follow.

- With $P = \set{1, 2}$ and $R = \set{3, 4, 5}$, the map $h(1) = 3$, $h(2) = 4$ is injective, so $\sigma$ is true.
- With $P = \set{1, 2, 3}$ and $R = \set{4, 5}$, no map from three elements to two elements is injective, by the [[pigeonhole principle|0HGVCWQGY3]], so $\sigma$ is false.

## Remarks

The example shows that the Henkin quantifier can compare the sizes of two definable sets.
Let $\sigma'$ be $\sigma$ with $P$ and $R$ exchanged.
Then $\sigma \land \sigma'$ says $|P| = |R|$, by the [[Schröder-Bernstein theorem|0A9V6RKQG6]], and $\sigma \land \neg \sigma'$ says $|P| < |R|$.
The first of these is the Härtig quantifier, so it is definable in first-order logic with the Henkin quantifier.

First-order logic cannot express $\sigma$, even on finite structures.
Call two structures $k$-similar when each of the four sets $P \cap R$, $P \setminus R$, $R \setminus P$ and $M \setminus (P \cup R)$ has the same size in both, or at least $k$ elements in both.
An Ehrenfeucht-Fraïssé game shows that $k$-similar structures satisfy the same first-order sentences of quantifier rank $k$.
Take disjoint $P$ and $R$ in both structures, with $|P| = k + 1$, $|R| = k$ in the first and $|P| = |R| = k$ in the second, and $k$ further elements in each.
These two structures are $k$-similar.
Then $\sigma$ is false in the first structure and true in the second.

The sentence also works for infinite sets.
With $M = \mathbb{N}$, $P$ the even numbers and $R = \mathbb{N}$, the identity on $P$ is a witness.
With $P = \mathbb{N}$ and $R$ the even numbers, the map $n \mapsto 2n$ is a witness, so both sizes are equal.

## Explanations

### L1 human

We want to say "there are at most as many red points as blue points" without counting.
The sentence asks for a rule that gives each red point its own blue partner, with no two red points sharing a partner.
Two players apply the rule separately, and the game checks that they always agree and never repeat a partner.
With $2$ red points and $3$ blue points such a rule exists.
With $3$ red points and $2$ blue points it does not, since two red points would share a blue partner.

### L2 human

We check $\sigma$ on $M = \set{1, 2, 3, 4}$ with $P = \set{1, 2}$ and $R = \set{2, 3}$, where the two sets overlap.

1. The map $h(1) = 3$, $h(2) = 2$ is injective from $P$ to $R$.
2. Put $f = g$ with $f(1) = 3$, $f(2) = 2$, $f(3) = 3$, $f(4) = 4$.
3. For $a_1 = 1$, $a_2 = 2$: both lie in $P$, $a_1 \neq a_2$, and $f(1) = 3 \neq 2 = g(2)$, so the first conjunct holds.
4. For $a_1 = 1$, $a_2 = 3$: $P(3)$ is false, so the first conjunct holds. Here $f(1) = g(3) = 3$, which shows why the conjunct must be restricted to $P$.
5. The second conjunct holds since $f(1) = 3$ and $f(2) = 2$ lie in $R$.

The typical use is to transfer a second-order statement about injections into one quantifier prefix, by the Skolem reading.
A trap is step 4: without the hypothesis $P(x_1) \land P(x_2)$, the function $f$ would have to be injective on all of $M$, and the sentence would say something else.
