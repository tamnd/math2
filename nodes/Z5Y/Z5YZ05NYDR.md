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

Let $\sigma = \set{+, \cdot, -, 0, 1, <}$ be the signature of [[ordered fields|0P3VCBDEE2]].
Let $\sigma_{\mathbb{R}} = \sigma \cup \set{c_r : r \in \mathbb{R}}$, with one new constant symbol $c_r$ for each real number $r$.
We check that $\sigma_{\mathbb{R}}$ is a signature and use it to find an infinitesimal.

1. Each $c_r$ has arity $0$, and the symbols of $\sigma$ keep their arities. So $\sigma_{\mathbb{R}}$ is a [[signature|WDVVEYD6AT]].
2. It has as many symbols as $\mathbb{R}$ has elements, so it is uncountable.
3. The ordered field $\mathbb{R}$ is a $\sigma_{\mathbb{R}}$-structure when $c_r$ is interpreted as $r$.
4. In it the sentence $c_2 \cdot c_3 = c_6$ is true, and $c_2 \cdot c_3 = c_5$ is false. For $r \neq s$ the sentence $\neg (c_r = c_s)$ is true.
5. Let $T$ be the set of all $\sigma_{\mathbb{R}}$-sentences true in $\mathbb{R}$. Add one more constant $d$, and let $\Sigma = T \cup \set{0 < d} \cup \set{d < c_r : r > 0}$.
6. A finite subset of $\Sigma$ mentions only finitely many sentences $d < c_r$, say for $r_1, \dots, r_k > 0$. Interpret $d$ in $\mathbb{R}$ as half the least of $r_1, \dots, r_k$, or as $1$ when $k = 0$. Then $\mathbb{R}$ satisfies the finite subset.
7. By the [[compactness theorem|1NR3HAWG9D]], $\Sigma$ has a model $\mathcal{M}$.
8. The field and order axioms are in $T$, so $\mathcal{M}$ is an ordered field. By step 4, the map $r \mapsto c_r^{\mathcal{M}}$ is one-to-one, and it preserves the operations and the order.
9. In $\mathcal{M}$ the element $d$ is positive and below every positive real. So $d$ is an infinitesimal.

So a large signature lets first-order sentences name every real number, and compactness then gives a non-Archimedean extension of $\mathbb{R}$.

## Remarks

The set $T$ is the elementary diagram of $\mathbb{R}$, and its models are the elementary extensions of $\mathbb{R}$.
Step 4 shows that every model of $T$ has at least $2^{\aleph_0}$ elements.
So $T$ has no countable model, and the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]] gives only models of size at most $\max(\abs{\sigma_{\mathbb{R}}}, \aleph_0) = 2^{\aleph_0}$.
This construction is the start of Robinson's nonstandard analysis.

## Explanations

### L1 human

A signature may have as many symbols as one likes.
Here there is one name $c_r$ for each real number $r$, such as $c_2$ and $c_{\pi}$.
Then the sentence $c_2 \cdot c_3 = c_6$ says "$2$ times $3$ is $6$".
With one name for each number, sentences can talk about each real number separately.

### L2 human

We check the step 6 for one finite set of sentences.

1. Take the sentences $0 < d$, $d < c_{1/2}$ and $d < c_{1/10}$, and finitely many sentences of $T$.
2. The least of $1/2$ and $1/10$ is $1/10$, so interpret $d$ as $1/20$.
3. Then $0 < 1/20$, $1/20 < 1/2$ and $1/20 < 1/10$ hold in $\mathbb{R}$.
4. The sentences of $T$ hold in $\mathbb{R}$ by the definition of $T$, and $d$ does not occur in them.

The typical use of constants for elements is the method of diagrams in model theory.
A trap: no single real number works for all $r > 0$ at once, so $\mathbb{R}$ itself is not a model of $\Sigma$.
