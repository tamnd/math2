---
tag: SJ5EESEWFR
kind: example
name: Symmetry is expressible in the guarded fragment
aliases: [guarded-frame-properties]
msc: ["03B25", "03B10"]
topics: [E4AVTNWE9E]
audience: grad
instance_of: [Y7YS1C3GAE]
uses: [Y7YS1C3GAE, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Guarded_logic
    locator: lead section
---

## Example

"If Anna is a friend of Ben, then Ben is a friend of Anna" only looks at pairs that are already friends, so it should be guarded.
We show that symmetry, reflexivity and seriality of a binary relation $R$ are all expressed by sentences of the [[guarded fragment|Y7YS1C3GAE]].
The three sentences are these:
$$\sigma_{\mathrm{sym}} = \forall x \, \forall y \, (R(x, y) \to R(y, x)),$$
$$\sigma_{\mathrm{ref}} = \forall x \, (x = x \to R(x, x)),$$
$$\sigma_{\mathrm{ser}} = \forall x \, (x = x \to \exists y \, (R(x, y) \wedge y = y)).$$

1. Symmetry.
   The block $\forall x \, \forall y$ quantifies $x$ and $y$ at once, with the guard $R(x, y)$.
   The guard is atomic and contains both quantified variables.
   The body $R(y, x)$ is atomic, and its free variables $x$ and $y$ occur in the guard.
2. Reflexivity.
   The quantifier $\forall x$ has the equality guard $x = x$, which contains $x$.
   The body $R(x, x)$ is atomic, with the free variable $x$ only.
3. Seriality, inner part.
   The formula $\exists y \, (R(x, y) \wedge y = y)$ has the guard $R(x, y)$, which contains $y$.
   Its body $y = y$ has the free variable $y$, which the guard contains.
4. Seriality, outer part.
   The inner formula has the free variable $x$ only.
   The outer quantifier $\forall x$ has the guard $x = x$, which contains $x$.

So $\sigma_{\mathrm{sym}}$, $\sigma_{\mathrm{ref}}$ and $\sigma_{\mathrm{ser}}$ are guarded sentences.
The usual forms $\forall x \, R(x, x)$ and $\forall x \, \exists y \, R(x, y)$ are logically equivalent to $\sigma_{\mathrm{ref}}$ and $\sigma_{\mathrm{ser}}$, because $x = x$ and $y = y$ are always true.

## Remarks

The example shows that symmetry, reflexivity and seriality are guarded frame properties.
So satisfiability of a modal formula on symmetric, reflexive or serial frames reduces to satisfiability of one guarded sentence: the translation of the formula together with the frame property.
The decidability of the guarded fragment then decides these modal logics, which are usually called $\mathsf{B}$, $\mathsf{T}$ and $\mathsf{D}$.

Change the relation to a ternary $S$, and symmetry in the first two places stays guarded.
The sentence $\forall x \, \forall y \, \forall z \, (S(x, y, z) \to S(y, x, z))$ has the guard $S(x, y, z)$, which contains all three variables.
Change the property to transitivity, and the answer flips: transitivity needs three variables in one clause with only binary atoms, and it is [[not guarded|F7EJ2VVKBE]].

## Explanations

### L1 human

"If Anna is a friend of Ben, then Ben is a friend of Anna" talks about a pair of people that is already linked by friendship.
The link "Anna is a friend of Ben" is the guard, so the statement only looks at pairs of friends.
That is why the property "friendship goes both ways" belongs to the guarded fragment.

### L2 human

Can a symmetric relation have a point with no successor while some other point has one?
We write the question as one sentence:
$$\sigma_{\mathrm{sym}} \wedge \exists x \, \exists y \, R(x, y) \wedge \exists x \, \forall y \, \neg R(x, y).$$
In guarded form, the second conjunct is $\exists x \, \exists y \, (R(x, y) \wedge x = x)$, and the third is $\exists x \, (x = x \wedge \forall y \, (R(x, y) \to \neg (y = y)))$.
Now try the model with elements $a, b, c$ and $R = \{ (a, b), (b, a) \}$.
The relation is symmetric, $a$ has the successor $b$, and $c$ has no successor.
Check: all three conjuncts hold, so the sentence is satisfiable, and the model is finite, as the finite model property of the guarded fragment predicts.

The typical use is to add frame conditions to a modal translation and stay inside a decidable fragment.
Watch out: not every universal sentence is guarded, since the guard must cover all free variables of the body.
