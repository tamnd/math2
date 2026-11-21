---
tag: 1KSQ1F0DSG
kind: example
name: Linear orders that are not well-ordered
aliases: [non-well-ordered-linear-orders, ill-founded-linear-orders-pc-class]
msc: ["03C52", "06A05"]
topics: [JYJHB4YBAH]
audience: grad
instance_of: [YEC1Q3A490]
uses: [YEC1Q3A490, 0FRXBVVR03, AGYBSTD7BG, J64Y3JC0RE, MEC3ZMC4F1, E2CBFNAVZY]
sources:
  - book: isbn:9780521587136
---

## Example

Let $L = \set{<}$, and let $\mathcal{K}$ be the class of [[linear orders|0FRXBVVR03]] that are not well-ordered.
Then $\mathcal{K}$ is a basic [[pseudo-elementary class|YEC1Q3A490]], but it is not an [[elementary class|MEC3ZMC4F1]].

1. Let $L^+ = \set{<, P}$ with $P$ unary, and let $\sigma$ be the conjunction of the linear order axioms with
   $$\exists x \, P(x) \wedge \forall x \, \bigl(P(x) \to \exists y \, (P(y) \wedge y < x)\bigr).$$
2. If $(A, <, P) \models \sigma$, then $P$ is a nonempty subset of $A$ with no least element, so $(A, <)$ is not well-ordered.
3. If $(A, <)$ is a linear order that is not well-ordered, some nonempty subset $S$ has no least element, and $(A, <, S) \models \sigma$.
4. So $\mathcal{K}$ is the class of reducts to $L$ of the models of $\sigma$.
5. Let $U$ be a nonprincipal [[ultrafilter|J64Y3JC0RE]] on $\mathbb{N}$ and let $\mathcal{M} = (\mathbb{N}, <)^{\mathbb{N}} / U$.
6. The classes of the functions $n \mapsto \max(n - k, 0)$, for $k = 0, 1, 2, \ldots$, form a strictly decreasing sequence in $\mathcal{M}$, so $\mathcal{M} \in \mathcal{K}$.
7. By [[Łoś's theorem|AGYBSTD7BG]], $\mathcal{M}$ and $(\mathbb{N}, <)$ satisfy the same $L$-sentences, and $(\mathbb{N}, <) \notin \mathcal{K}$.
8. So no set of $L$-sentences has exactly the members of $\mathcal{K}$ as models.

## Remarks

The complement of $\mathcal{K}$ among linear orders, the class of well-orders, is not even $\mathrm{PC}$.
If it were, then by the separation form of [[Craig's interpolation theorem|E2CBFNAVZY]] the class $\mathcal{K}$ would be basic elementary, contradicting step 8.
So the pseudo-elementary classes are not closed under complements.

## Explanations

### L1 human

A list in order is "well-ordered" if every part of it has a first element.
Saying that this fails needs a hidden subset with no first element.
If we are allowed to name that subset, the failure is easy to write down.
Without the name, no list of rules can capture it.

### L2 human

Take the order $\omega + \mathbb{Z}$, a copy of $\mathbb{N}$ followed by a copy of $\mathbb{Z}$.
Choosing $P$ to be the copy of $\mathbb{Z}$ makes $(\omega + \mathbb{Z}, <, P)$ a model of $\sigma$, so $\omega + \mathbb{Z}$ lies in $\mathcal{K}$.
A trap is to choose $P$ to be all of $\omega + \mathbb{Z}$: the whole order has the least element $0$, so this choice fails the second conjunct.
