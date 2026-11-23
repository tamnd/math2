---
tag: 9WVJK3DWAN
kind: example
name: The order of the natural numbers is not a logical notion
msc: ["03A05", "03C80"]
topics: [H8QZY0RZXZ]
audience: ug2
uses: [05RWFKVTJ7]
not_instance_of:
  - target: 2QQ7Q5SKP8
    note: "The relation < on the natural numbers is moved by the permutation that swaps 0 and 1, so it fails the permutation invariance criterion for logical notions."
sources:
  - url: https://en.wikipedia.org/wiki/Logical_constant
    locator: lead section
---

## Example

Let $D = \mathbb{N} = \{0, 1, 2, \ldots\}$, and let $L = \{(a, b) \in \mathbb{N} \times \mathbb{N} : a < b\}$ be the usual strict order.
By Tarski's criterion, $L$ is a logical notion only if $\pi[L] = L$ for every [[permutation|05RWFKVTJ7]] $\pi$ of $\mathbb{N}$.
We show that this condition fails.

1. Let $\sigma$ be the map with $\sigma(0) = 1$, $\sigma(1) = 0$ and $\sigma(n) = n$ for $n \geq 2$.
2. $\sigma \circ \sigma$ is the identity map, so $\sigma$ is its own inverse and a permutation of $\mathbb{N}$.
3. The pair $(0, 1)$ is in $L$, because $0 < 1$.
4. Its image is $(\sigma(0), \sigma(1)) = (1, 0)$, so $(1, 0) \in \sigma[L]$.
5. The pair $(1, 0)$ is not in $L$, because $1 < 0$ is false.
6. So $\sigma[L] \neq L$, and $L$ is not permutation invariant.

So $<$ is a non-logical symbol, and the sentence $0 < 1$ is true in $\mathbb{N}$ but is not a logical truth.

## Remarks

A relation that treats some objects differently from others is not logical, and this is how the criterion separates logic from arithmetic.
The same permutation shows that $\leq$, $>$ and the successor relation $\{(n, n + 1) : n \in \mathbb{N}\}$ are not logical.
The argument needs only two elements that the relation treats differently, so it works for every strict linear order on a domain with at least two elements.

On a one-element domain the strict order is empty, and the empty relation is invariant.
So invariance depends on the domain, and a symbol is logical only when its meaning is invariant on every domain.
The property "is a strict linear order", a property of relations, is permutation invariant, because a permutation maps a linear order to a linear order.

## Explanations

### L1 human

Take the numbers $0, 1, 2$ and the relation "is smaller than".
Now relabel them: call $0$ by the name of $1$, and $1$ by the name of $0$.
The fact "$0$ is smaller than $1$" turns into "$1$ is smaller than $0$", which is false.
So "is smaller than" depends on which object is which.
Logic does not look at which object is which, so "is smaller than" is not a word of logic.

### L2 human

We check one more permutation, to see that the failure is not special to $\sigma$.

1. Let $\tau(n) = n + 1$ for even $n$ and $\tau(n) = n - 1$ for odd $n$, so $\tau$ swaps $0$ with $1$, $2$ with $3$, and so on.
2. $\tau \circ \tau$ is the identity map, so $\tau$ is a permutation.
3. The pair $(2, 3)$ is in $L$, and its image $(3, 2)$ is not.
4. So $\tau[L] \neq L$ as well.
5. Some permutations fix $L$, such as the identity map, but invariance asks for all of them, so one failure is enough.

The same test shows that symbols of a mathematical theory, such as $<$, $+$ or $\in$, are non-logical, so their axioms belong to a theory and not to logic.
The trap is to think that $<$ is logical because its meaning is "fixed" in arithmetic: the theory fixes it, not logic.
