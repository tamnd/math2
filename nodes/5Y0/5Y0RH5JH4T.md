---
tag: 5Y0RH5JH4T
kind: example
name: A signature without constant symbols has no closed terms
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
not_instance_of:
  - target: NFW38QJ3A7
    note: the set of closed terms of a signature without constants is empty, so it cannot serve as a Herbrand universe until a constant is added
uses: [JKP0XNXRPB, 6D3WA7N2W4, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Example

Let $L = \{ f, P \}$, with a unary function symbol $f$, a unary relation symbol $P$, and no constant symbols.
Try to write down a term without variables: $f(\ )$ needs an argument, and the only arguments on offer are variables or other terms of the form $f(\ldots)$.
We show that this search always fails, so $L$ has no closed [[terms|6D3WA7N2W4]].

1. By the definition of terms, every term of $L$ is a variable or $f(t)$ for a term $t$, since $L$ has no constant symbols.
2. We show by induction on terms that every term of $L$ contains a variable.
3. A variable contains itself.
4. If $t$ contains a variable, then $f(t)$ contains the same variable.
5. So no term of $L$ is closed, and the set of closed terms is empty.

A [[structure|983GZBQYT4]] must have a nonempty domain, so the empty set of closed terms cannot be the domain of a Herbrand structure.
The condition that fails is the existence of a constant symbol.
The [[definition of the Herbrand universe|JKP0XNXRPB]] repairs this by adding a new constant $c_0$, and then
$$H(L \cup \{ c_0 \}) = \{ c_0, \ f(c_0), \ f(f(c_0)), \ \ldots \}.$$

## Remarks

The example explains the convention on constants in the definition of the Herbrand universe.
The added constant does no harm to satisfiability.
If a set $\Sigma$ of $L$-sentences has a model $\mathcal{M}$, we can read $c_0$ as any element of $M$, and $\Sigma$ stays true, because no sentence of $\Sigma$ mentions $c_0$.
The converse is immediate: forget the meaning of $c_0$.

The set of all terms of $L$, with variables, is not a Herbrand universe either.
The term $f(x)$ contains the variable $x$, so it names nothing until $x$ gets a value.

## Explanations

### L1 human

Suppose a language has no names at all, only a way $f$ to turn one thing into another.
Then it cannot name anything without first having a thing to start from.
So we give it one name $c_0$ to start with, and then $f$ produces $f(c_0)$, $f(f(c_0))$ and the rest.

### L2 human

We check that adding $c_0$ does not change the satisfiability of $\forall x \, (P(x) \to P(f(x)))$.
In the signature $L$, the structure with domain $\mathbb{N}$, $f(n) = n + 1$ and $P$ true of every number is a model, since every implication has a true conclusion.
Now read $c_0$ as $0$.
The sentence does not mention $c_0$, so it stays true, by the [[coincidence lemma|FM580NZ9W6]].
The typical use is in clause-form theorem proving, where a constant is added when the input clauses have none.
Watch out: add $c_0$ to the signature, not only to the universe, because otherwise $c_0$ is not a term of the language.
