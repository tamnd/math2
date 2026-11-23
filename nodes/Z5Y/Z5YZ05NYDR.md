---
tag: Z5YZ05NYDR
kind: example
name: A signature with a constant for each real number
msc: ["03C07", "03H05"]
topics: [PSRDJXRW53]
audience: grad
instance_of: [WDVVEYD6AT]
uses: [WDVVEYD6AT, 0P3VCBDEE2, 1NR3HAWG9D, 484M0TZ1S7, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Signature_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: lead section
---

## Example

A signature may be uncountable, and a signature with a name for every real number lets first-order sentences talk about each real number one at a time.
Let $\sigma = \{ +, \cdot, -, 0, 1, < \}$ be the signature of [[ordered fields|0P3VCBDEE2]], and let
$$\sigma_{\mathbb{R}} = \sigma \cup \{ c_r : r \in \mathbb{R} \},$$
with one new constant symbol $c_r$ for each real number $r$.
We check that $\sigma_{\mathbb{R}}$ is a signature, and then use it to build an ordered field with an infinitesimal.

1. Each $c_r$ has arity $0$, and the symbols of $\sigma$ keep their arities, so $\sigma_{\mathbb{R}}$ is a [[signature|WDVVEYD6AT]].
2. It has one symbol for each real number, so it is uncountable.
3. The ordered field $\mathbb{R}$ is a $\sigma_{\mathbb{R}}$-[[structure|983GZBQYT4]] when $c_r$ is read as $r$.
4. In it the sentence $c_2 \cdot c_3 = c_6$ is true and $c_2 \cdot c_3 = c_5$ is false, and for $r \neq s$ the sentence $\neg (c_r = c_s)$ is true.
5. Let $T$ be the set of all $\sigma_{\mathbb{R}}$-sentences true in $\mathbb{R}$.
   Add one more constant $d$, and let $\Sigma = T \cup \{ 0 < d \} \cup \{ d < c_r : r > 0 \}$.
6. A finite subset of $\Sigma$ contains only finitely many sentences $d < c_r$, say for $r_1, \dots, r_k > 0$.
   Read $d$ in $\mathbb{R}$ as half the least of $r_1, \dots, r_k$, or as $1$ when $k = 0$; then $\mathbb{R}$ satisfies the finite subset.
7. By the [[compactness theorem|1NR3HAWG9D]], $\Sigma$ has a model $\mathcal{M}$.
8. The ordered field axioms are in $T$, so $\mathcal{M}$ is an ordered field.
   The sentences $\neg (c_r = c_s)$, $c_r + c_s = c_{r+s}$, $c_r \cdot c_s = c_{rs}$ and $c_r < c_s$ for $r < s$ are in $T$, so $r \mapsto c_r^{\mathcal{M}}$ embeds $\mathbb{R}$ into $\mathcal{M}$.
9. In $\mathcal{M}$ the element $d$ is positive and below every positive real, so $d$ is an infinitesimal.

So a large signature lets sentences name every real number, and compactness then gives a non-Archimedean ordered field that contains $\mathbb{R}$.

## Remarks

The set $T$ is the elementary diagram of $\mathbb{R}$, and its models are, up to isomorphism, the elementary extensions of $\mathbb{R}$.
By step 4 every model of $T$ has at least $2^{\aleph_0}$ elements, so $T$ has no countable model.
This does not contradict the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]], since that theorem only promises models of size $\max(|\sigma_{\mathbb{R}}|, \aleph_0) = 2^{\aleph_0}$.
If we keep only countably many constants, say $c_q$ for $q \in \mathbb{Q}$, the countable models come back.
This construction is the starting point of Robinson's nonstandard analysis.

## Explanations

### L1 human

A signature may have as many symbols as you like.
Here there is one name $c_r$ for each real number $r$, such as $c_2$ and $c_{\pi}$.
Then the sentence $c_2 \cdot c_3 = c_6$ says "$2$ times $3$ is $6$".
With one name for each number, sentences can talk about each real number separately.

### L2 human

We check step 6 for one finite set of sentences.
Take $0 < d$, $d < c_{1/2}$ and $d < c_{1/10}$, together with finitely many sentences of $T$.
The least of $\tfrac{1}{2}$ and $\tfrac{1}{10}$ is $\tfrac{1}{10}$, so read $d$ as $\tfrac{1}{20}$.
Then all three new sentences hold in $\mathbb{R}$:
$$0 < \tfrac{1}{20}, \qquad \tfrac{1}{20} < \tfrac{1}{2}, \qquad \tfrac{1}{20} < \tfrac{1}{10}.$$
The sentences of $T$ hold in $\mathbb{R}$ by the definition of $T$, and $d$ does not occur in them.
The typical use of constants for elements is the method of diagrams in model theory.
Watch out: no single real number lies below every positive real and above $0$, so $\mathbb{R}$ itself is not a model of $\Sigma$.
