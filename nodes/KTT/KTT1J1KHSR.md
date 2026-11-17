---
tag: KTT1J1KHSR
kind: example
name: A resolution refutation with a Skolem function
msc: ["03B10", "03B35"]
topics: [TTCRX3NFNY]
audience: grad
instance_of: [DEB3CF4Z2D]
uses: [DEB3CF4Z2D, GCPQGMJYEV, B37TYWXS74, RJJ9D0WF53, T3SXVH3ZZC]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in first-order logic
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: lead section
---

## Example

We prove by [[first-order resolution|DEB3CF4Z2D]] that
$$\forall x\,\exists y\, R(x,y),\quad \forall x\,\forall y\,(R(x,y) \to R(y,x)) \ \models\ \forall x\,\exists y\, R(y,x).$$
In words: if every element is related to something, and the relation $R$ is symmetric, then every element has something related to it.

1. Negate the goal. The sentence $\neg\forall x\,\exists y\, R(y,x)$ is equivalent to $\exists x\,\forall y\, \neg R(y,x)$.
2. Skolemize the first premise. The quantifier $\exists y$ follows $\forall x$, so $y$ is replaced by $f(x)$ with a new unary function symbol $f$. The result is $\forall x\, R(x, f(x))$; see [[Skolem normal form|GCPQGMJYEV]].
3. Skolemize the negated goal. The quantifier $\exists x$ comes first, so $x$ is replaced by a new constant $c$. The result is $\forall y\, \neg R(y, c)$.
4. Both new sentences are [[equisatisfiable|B37TYWXS74]] with the old ones, and the second premise has no existential quantifier.
5. The [[clauses|T3SXVH3ZZC]], with variables renamed apart, are $C_1 = \{R(x_1, f(x_1))\}$, $C_2 = \{\neg R(x_2, y_2), R(y_2, x_2)\}$ and $C_3 = \{\neg R(y_3, c)\}$.
6. Resolve $C_1$ with $C_2$ on $R(x_1, f(x_1))$ and $\neg R(x_2, y_2)$. The [[unification|RJJ9D0WF53]] starts with the equations $x_1 = x_2$ and $f(x_1) = y_2$.
7. The equation $x_1 = x_2$ gives the binding $x_2 \mapsto x_1$. The equation $f(x_1) = y_2$ gives $y_2 \mapsto f(x_1)$, since $y_2$ does not occur in $f(x_1)$.
8. The mgu is $\sigma_1 = \{x_2 \mapsto x_1, y_2 \mapsto f(x_1)\}$. Check: $R(x_2, y_2)\sigma_1 = R(x_1, f(x_1))$.
9. The resolvent is $\{R(y_2, x_2)\}\sigma_1 = \{R(f(x_1), x_1)\}$; call it $C_4$.
10. Resolve $C_4$ with $C_3$ on $R(f(x_1), x_1)$ and $\neg R(y_3, c)$. The equations are $f(x_1) = y_3$ and $x_1 = c$.
11. The first equation gives $y_3 \mapsto f(x_1)$. The second gives $x_1 \mapsto c$, and applying it to the first binding gives $y_3 \mapsto f(c)$.
12. The mgu is $\sigma_2 = \{x_1 \mapsto c, y_3 \mapsto f(c)\}$. Check: $R(f(x_1), x_1)\sigma_2 = R(f(c), c) = R(y_3, c)\sigma_2$.
13. The resolvent is $(\varnothing \cup \varnothing)\sigma_2 = \square$.

So the clause set is unsatisfiable, and the conclusion follows from the premises.

## Remarks

The mgus record the proof in the ordinary sense.
The witness for the goal at the element $c$ is $y = f(c)$: the premise gives $R(c, f(c))$, and symmetry turns it into $R(f(c), c)$.
The term $f(c)$ was not chosen by hand; unification found it in step 11.

Without the symmetry premise the set $\{C_1, C_3\}$ has no refutation.
The unification of $R(x_1, f(x_1))$ with $R(y_3, c)$ gives $y_3 \mapsto x_1$ and then the equation $f(x_1) = c$, which fails because $f$ and $c$ are different symbols.
The set is satisfiable: in $\mathbb{N}$ with $R(m, n)$ meaning $n = m + 1$, $f(m) = m + 1$ and $c = 0$, both clauses hold, since no $m$ has $m + 1 = 0$.

The Skolem symbols must be new and different for each sentence.
If the Skolem constant $c$ of step 3 were taken equal to a symbol already in use, the clause set could change its satisfiability.

## Explanations

### L1 human

Suppose that every person has a friend, and that friendship goes both ways.
Then every person is also the friend of someone.
The proof by resolution gives names to the unknown objects: "the friend of $x$" becomes $f(x)$.
To refute "some person $c$ is nobody's friend", the method looks for a match and finds the person $f(c)$, the friend of $c$.
Since friendship goes both ways, $c$ is the friend of $f(c)$, and this is the clash.

### L2 human

The two Skolem steps follow one rule: an existential variable becomes a function of the universal variables to its left.

1. In $\forall x\,\exists y\, R(x,y)$ one universal variable precedes $\exists y$, so $y$ becomes $f(x)$.
2. In $\exists x\,\forall y\, \neg R(y,x)$ no universal variable precedes $\exists x$, so $x$ becomes a constant $c$.
3. Unification then matches $x_1$ with $c$ and fills $y_3$ with $f(c)$.

The typical use of Skolem functions is this: they turn the search for witnesses into the computation of mgus.
A trap is to Skolemize the goal $\forall x\,\exists y\, R(y,x)$ itself instead of its negation.
The result $\forall x\, R(g(x), x)$ is stronger than the goal and is not equivalent to it.
