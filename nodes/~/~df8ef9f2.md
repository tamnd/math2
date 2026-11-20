---
tag: ~df8ef9f2
kind: proof
name: Proof of Vaught's never-two theorem by naming a non-isolated type
msc: ["03C15", "03C35"]
topics: [6XEXRME4C1]
audience: grad
proves: ~ea319e25
uses: [1513J40TKA, ~2528b92a, ~24829d6c, ~ddda0a28, ~166b8a9e, ~fbef995e, 484M0TZ1S7]
methods: [0J0XBKG64S]
sources:
  - book: isbn:9780387987606
  - book: isbn:9780521587136
---

## Proof

Let $T$ be complete with infinite models in a countable signature $L$.
Suppose that $T$ has exactly two countable models up to isomorphism.
We derive a contradiction.

### The two models are the prime and the saturated model

1. Each complete type of $T$ is realized in some countable model, by compactness and the [[Löwenheim-Skolem theorem|484M0TZ1S7]]. Each countable model realizes countably many types. With finitely many countable models, $T$ is [[small|~166b8a9e]].
2. By [[this theorem|~24829d6c]] $T$ has a prime model $M_0$, and by [[this theorem|~2528b92a]] a countable saturated model $M_s$.
3. $T$ is not $\aleph_0$-categorical, so by the [[Ryll-Nardzewski theorem|1513J40TKA]] some complete $n$-type $p$ is not isolated.
4. $M_s$ realizes every type, so it realizes $p$. $M_0$ is [[atomic|~fbef995e]], so it omits $p$. So $M_0 \not\cong M_s$, and these are the two countable models.

### Naming a realization of p

1. Let $\bar a$ in $M_s$ realize $p$. Let $T' = \operatorname{Th}(M_s, \bar a)$ in the signature $L$ with $n$ new constants $\bar c$.
2. $T'$ is small. A type of $T'$ in variables $\bar y$ is fixed by the type of $T$ in $\bar x \bar y$ that it gives with $\bar c$ replaced by $\bar x$.
3. So $T'$ has a prime model $(N, \bar b)$. Here $N$ is a countable model of $T$, and $\bar b$ realizes $p$ in $N$. So $N \not\cong M_0$, and $N \cong M_s$.
4. $N$ is saturated, so $(N, \bar b)$ is saturated: a type over a finite set together with $\bar b$ is a type over a finite subset of $N$.
5. So $(N, \bar b)$ is atomic and realizes every type of $T'$. Every type of $T'$ is isolated, and $T'$ is $\aleph_0$-categorical by the Ryll-Nardzewski theorem.

### The contradiction

1. Let $q(\bar y)$ be a complete $k$-type of $T$. $M_s$ realizes $q$ by some $\bar d$, and $\operatorname{tp}^{(M_s, \bar a)}(\bar d)$ is a type of $T'$ that restricts to $q$.
2. So restriction maps $S_k(T')$ onto $S_k(T)$. By step 5 above, $S_k(T')$ is finite, so $S_k(T)$ is finite for every $k$.
3. By the Ryll-Nardzewski theorem, $T$ is $\aleph_0$-categorical, which contradicts step 3 of the first part.

## Idea

Finitely many countable models force smallness, so the prime model and the saturated model exist and differ.
Name a tuple that realizes a non-isolated type.
The prime model of the new theory is a model of $T$ that is not prime, so it must be the saturated one.
But then the new theory has a model that is prime and saturated at once, so it is $\aleph_0$-categorical, and this passes back to $T$.

## Variants

The same steps show that the countable saturated model of a small theory that is not $\aleph_0$-categorical is never prime over a finite tuple.
Ehrenfeucht's example shows that the third model produced here can be new: it is the model in which the constants have a least upper bound.
