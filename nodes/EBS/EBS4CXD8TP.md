---
tag: EBS4CXD8TP
kind: example
name: Π¹₁-CA0 proves that the set of indices of computable well-orderings exists
msc: ["03B30", "03D60"]
topics: [BY8AAFN7C5]
audience: grad
instance_of: [T21WETAHN5]
uses: [VPGQM418AG, 01CGSJ0GNQ, WHAP0K600D, NS1HWGTD8E, PPGD5KW8JC, J0Z2GNJZ2W]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Π11 comprehension Π11-CA0
---

## Example

For an index $e$, let $R_e = \{ (i, j) : \Phi_e((i, j)) = 1 \}$, and let $\mathrm{field}(R_e) = \{ i : (i, i) \in R_e \}$.
Let $\varphi(e)$ be the conjunction of three conditions.

- (a) $\Phi_e$ is total with values in $\{ 0, 1 \}$, so $R_e$ is a [[computable set|PPGD5KW8JC]] of pairs.
- (b) $R_e$ is a linear order on its field, with $(i, j) \in R_e$ read as $i \le j$.
- (c) For every set $F$, if $F$ is the graph of a function $f \colon \mathbb{N} \to \mathrm{field}(R_e)$, then there is a $k$ with $(f(k), f(k + 1)) \in R_e$.

Condition (c) says that there is no descending sequence $f(0) > f(1) > \cdots$ in $R_e$.
So $\varphi(e)$ says that $R_e$ is a computable [[well-ordering|01CGSJ0GNQ]].
We check that [[Π¹₁-CA0|VPGQM418AG]] proves that $W = \{ e : \varphi(e) \}$ exists, and that $W$ is far from arithmetical.

### The set exists

1. Conditions (a) and (b) use only quantifiers over numbers and the relation "$\Phi_e(x)$ halts with output $y$", which is $\Sigma^0_1$.
   So (a) and (b) together are arithmetical.
2. Condition (c) has the form $\forall F\, \psi(e, F)$ with $\psi$ arithmetical.
3. So $\varphi(e)$ is equivalent to $\forall F\, \big((a) \wedge (b) \wedge \psi(e, F)\big)$, which is a $\Pi^1_1$ formula.
4. By $\Pi^1_1$ comprehension, there is a set $W$ with $\forall e\, (e \in W \leftrightarrow \varphi(e))$.

### The set is not hyperarithmetical

5. In the full model $(\mathbb{N}, \mathcal{P}(\mathbb{N}))$, the set $W$ is the true set of indices of computable well-orderings.
6. This set is many-one equivalent to [[Kleene's O|WHAP0K600D]], a standard fact of hyperarithmetical theory that we cite without proof.
7. Kleene's O is not [[hyperarithmetical|NS1HWGTD8E]].
   So $W$ is not hyperarithmetical, and in particular it is not arithmetical.

## Remarks

The same method, with a set parameter $X$ in $\Phi^X_e$, shows that $\Pi^1_1\text{-}\mathsf{CA}_0$ proves that the hyperjump of $X$ exists for every $X$.
By step 7, the true set $W$ is not in the $\omega$-model of the [[arithmetical sets|9KPCZ6NA32]].

The domain of $f$ in condition (c) must be the field of $R_e$.
If $f$ could take values outside the field, a constant function at such a value would violate (c) for every $e$ with a field smaller than $\mathbb{N}$.

Watch out: a countable linear order with no descending sequence in a model may still have a descending sequence outside the model.
So in a model that is not a [[β-model|J0Z2GNJZ2W]], the set given by step 4 can differ from the true set.

## Explanations

### L1 human

The property "this computable order is a well-ordering" refers to all infinite sequences.
$\Pi^1_1$ comprehension still collects the indices with this property into one set.
For example, an index for the usual order on $\mathbb{N}$ is in the set, and an index for the order of the integers is not.

### L2 human

The true set $W$ is a complete $\Pi^1_1$ set, so every $\Pi^1_1$ set of numbers is many-one reducible to it.
So in the full model, every set that $\Pi^1_1$ comprehension gives without parameters is computable from $W$.
Each hyperarithmetical set is computable from $W$ as well, and $W$ itself is not hyperarithmetical.
For comparison, the sets of [[hyperarithmetical theory|NS1HWGTD8E]] are the intersection of all $\omega$-models of [[ATR0|MKB74TX3Z8]].
