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
2. The map $\sigma$ is a permutation of $\mathbb{N}$, because $\sigma \circ \sigma$ is the identity map, so $\sigma$ is its own inverse.
3. The pair $(0, 1)$ is in $L$, because $0 < 1$.
4. The image of this pair is $(\sigma(0), \sigma(1)) = (1, 0)$, so $(1, 0) \in \sigma[L]$.
5. The pair $(1, 0)$ is not in $L$, because $1 < 0$ is false.
6. So $\sigma[L] \neq L$, and $L$ is not permutation invariant.

So the symbol $<$ is a non-logical symbol, and the sentence $0 < 1$ is true in $\mathbb{N}$ but it is not a logical truth.

## Remarks

The example shows how the criterion separates logic from arithmetic: a relation that prefers some objects to others is not logical.
The same permutation shows that $\leq$, $>$ and the successor relation $\{(n, n + 1)\}$ are not logical.
The argument needs only two elements that the relation treats differently, so it works on every domain with at least two elements and every strict linear order on it.
On a domain with exactly one element, $L$ is empty, and the empty relation is invariant; this shows that invariance depends on the domain, and a symbol is logical only when its meaning is invariant on every domain.
In contrast, the property "$L$ is a strict linear order" is a property of relations, and it is permutation invariant: a permutation maps a linear order to a linear order.

## Explanations

### L1 human

Take the numbers $0, 1, 2$ and the relation "is smaller than".
Now give the numbers new labels: call $0$ by the name of $1$ and $1$ by the name of $0$.
The fact "$0$ is smaller than $1$" turns into "$1$ is smaller than $0$", which is false.
So "is smaller than" depends on which object is which.
Logic does not look at which object is which, so "is smaller than" is not a word of logic.

### L2 human

We check one more permutation, to see that the failure is not special to $\sigma$.

1. Let $\tau(n) = n + 1$ for even $n$ and $\tau(n) = n - 1$ for odd $n$, so $\tau$ swaps $0$ with $1$, $2$ with $3$, and so on.
2. The map $\tau$ is a permutation, because $\tau \circ \tau$ is the identity map.
3. The pair $(2, 3)$ is in $L$, and its image $(3, 2)$ is not in $L$.
4. So $\tau[L] \neq L$ as well.
5. Some permutations do fix $L$: the identity map is one. Invariance asks for all permutations, so one failure is enough.

The typical use is to show that a symbol of a mathematical theory, such as $<$, $+$ or $\in$, is non-logical, so that its axioms are part of a theory and not of logic.
A trap is to think that $<$ is logical because its meaning is "fixed" in arithmetic: the meaning is fixed by the theory, not by logic.
