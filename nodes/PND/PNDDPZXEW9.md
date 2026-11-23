---
tag: PNDDPZXEW9
kind: example
name: Skolemizing alternating quantifiers
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [GCPQGMJYEV]
uses: [GCPQGMJYEV, EZ8NCHN7SJ, Q5H7C57VNH]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: Examples
---

## Example

Let $R$ be a relation symbol of arity $4$, and let
$$\varphi = \forall x \, \exists y \, \forall z \, \exists w \, R(x, y, z, w).$$
We compute the [[Skolem normal form|GCPQGMJYEV]] of $\varphi$ by the [[Skolemization step|EZ8NCHN7SJ]], and test it in a structure.

1. The sentence $\varphi$ is prenex, its prefix variables are distinct, and its matrix $R(x, y, z, w)$ is quantifier-free.
2. The leftmost $\exists y$ has one universal variable $x$ before it.
   So $y$ becomes $f(x)$ for a new unary symbol $f$, and we get
   $$\varphi_1 = \forall x \, \forall z \, \exists w \, R(x, f(x), z, w).$$
3. The next $\exists w$ has the universal variables $x$ and $z$ before it.
   So $w$ becomes $g(x, z)$ for a new binary symbol $g$.
4. The result is
   $$\varphi^S = \forall x \, \forall z \, R\big( x, f(x), z, g(x, z) \big).$$
   It has only universal quantifiers, so it is in Skolem normal form.
5. Test it in $\mathbb{N}$ with $R(x, y, z, w)$ read as "$x < y$ and $z < w$".
   Then $\varphi$ is true, with $y = x + 1$ and $w = z + 1$.
6. The expansion with $f(x) = x + 1$ and $g(x, z) = z + 1$ satisfies $\varphi^S$, as part 2 of the [[Skolem normal form theorem|Q5H7C57VNH]] says.

So $\varphi^S$ uses two Skolem symbols, one for each existential quantifier.

## Remarks

The function $f$ has the argument $x$ only, because $y$ is chosen before $z$ is known.
A symbol $f(x, z)$ would let $y$ depend on $z$, and the result would be the Skolem form of the weaker sentence $\forall x \, \forall z \, \exists y \, \exists w \, R(x, y, z, w)$.
In the test structure $g$ does not need its argument $x$, but the Skolemization step always uses all universal variables to the left.

## Explanations

### L1 human

The sentence says: "for every $x$ there is a $y$, and then for every $z$ there is a $w$, such that $R$ holds".
The first choice $y$ may depend only on $x$.
The second choice $w$ may depend on $x$ and on $z$.
Skolem functions record these choices as $f(x)$ and $g(x, z)$.

### L2 human

We check the claim of the remark with a structure where the order matters.
Let the domain be $\{ 0, 1 \}$, and let $R(x, y, z, w)$ mean $y = z$.
The sentence $\forall x \, \forall z \, \exists y \, \exists w \, R(x, y, z, w)$ is true, since we can take $y = z$.
The sentence $\varphi$ is false: for given $x$ and $y$, the value $z = 1 - y$ makes $y = z$ false.
So a Skolem function $f(x, z)$ would describe the weaker sentence, not $\varphi$.
The typical use of this example is to read off the dependence of each witness from the prefix.
Watch out: $f$ and $g$ must be different new symbols, even when both happen to be read as successor functions.
