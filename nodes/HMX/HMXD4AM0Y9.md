---
tag: HMXD4AM0Y9
kind: example
name: The additive group of the integers is not model complete
aliases: [integers-additive-group-not-model-complete]
msc: ["03C10", "20K01"]
topics: [1A9JSC5YG8]
audience: grad
not_instance_of:
  - target: YR6HCMABTE
    note: the even integers form a substructure of the integers that is isomorphic to it, but 2 is divisible by 2 in the integers and not in the even integers
uses: [ERVV6RWNNX, 676H7EGTKJ, 8WZF9SBP39, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
    locator: Non-examples
  - book: isbn:9780387987606
---

## Example

Let $L = \set{+, -, 0}$ be the signature of [[abelian groups|082GHNPJ53]], and let $T = \operatorname{Th}(\Z, +, -, 0)$.
We show that $T$ is not [[model complete|ERVV6RWNNX]].
Let $2\Z$ be the set of even integers.

1. The set $2\Z$ contains $0$ and is closed under $+$ and $-$. So $2\Z$ is a [[substructure|676H7EGTKJ]] of $\Z$.
2. The map $n \mapsto 2n$ is a bijection from $\Z$ to $2\Z$, and $2(m + n) = 2m + 2n$, $2(-n) = -2n$, $2 \cdot 0 = 0$. So it is an isomorphism of $L$-structures.
3. Isomorphic structures satisfy the same sentences, so $2\Z \models T$.
4. Let $\varphi(x)$ be $\exists y \, (y + y = x)$. In $\Z$, $\varphi(2)$ holds with $y = 1$.
5. In $2\Z$, a witness $y$ would satisfy $2y = 2$, so $y = 1$, which is not even. So $\varphi(2)$ fails in $2\Z$.
6. So $2\Z$ is a substructure of $\Z$ and a model of $T$, but not an [[elementary substructure|8WZF9SBP39]].

So $T$ is not model complete.

## Remarks

The example shows that an inclusion of models can fail to be elementary even when the two models are isomorphic.
The formula $\varphi$ is existential, and its negation is not equivalent to an existential formula modulo $T$.

When the signature changes, the result changes in this way.

- With the constant $1$ added, $2\Z$ is no longer a substructure, since it does not contain $1$.
- With $1$ and $<$ added, the theory of $\Z$ becomes model complete. [[Presburger arithmetic|4W0E9G7PPV]] has quantifier elimination after adding the predicates $D_n$, and both $D_n(x)$ and $\neg D_n(x)$ are existential: $\neg D_n(x)$ says $\exists y \, \bigvee_{0 < r < n} (ny + r = x)$.
- In the theory of nontrivial divisible torsion-free abelian groups, the formula $\varphi$ is equivalent to $x = x$, and the theory has [[quantifier elimination|BFK4T1WK38]].

## Explanations

### L1 human

The even numbers, with addition, look exactly like all the whole numbers: double every number and the sums still match.
So the even numbers sit inside the whole numbers as a copy of them.
But the two systems disagree about the number $2$.
Among all whole numbers, $2$ is "something plus itself", namely $1 + 1$.
Among the even numbers, $2$ is not of this form, since $1$ is missing.

### L2 human

We check the claim of step 5 with a list of candidates.

1. The even numbers near $2$ are $0$, $2$ and $4$.
2. Their doubles are $0$, $4$ and $8$, and none of them is $2$.
3. For an even $y$, the double $2y$ is a multiple of $4$, and $2$ is not.
4. So no even $y$ satisfies $y + y = 2$.

The typical use of the example is as the first non-example of model completeness, where the failure comes from divisibility.
A trap is to think that an inclusion $M \subseteq N$ of isomorphic models must be elementary: the isomorphism and the inclusion are different maps.
