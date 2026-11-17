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

Let $L = \set{f, P}$ with a unary function symbol $f$ and a unary relation symbol $P$, and no constant symbols.
We show that $L$ has no closed terms.

1. By the definition of terms, every term is a variable, a constant symbol, or $f(t)$ for a term $t$.
2. We show by induction on terms that every term of $L$ contains a variable.
3. A variable contains itself. There are no constant symbols.
4. If $t$ contains a variable, then $f(t)$ contains the same variable.
5. So no term of $L$ is closed, and the set of closed terms is empty.

A structure must have a nonempty domain, so the empty set of closed terms cannot be the domain of a structure.
The condition that fails is the existence of a constant symbol.
The [[definition of the Herbrand universe|JKP0XNXRPB]] repairs this by adding a new constant $c_0$.
Then $H(L \cup \set{c_0}) = \set{c_0, f(c_0), f(f(c_0)), \ldots}$.

## Remarks

The example explains the convention on constants in the definition of the Herbrand universe.
The added constant is harmless for satisfiability: a set $\Sigma$ of $L$-sentences has a model if and only if it has a model as a set of $L \cup \set{c_0}$-sentences, because $c_0$ can be interpreted by any element.
The set of all terms of $L$, with variables, is also not the Herbrand universe: the term $f(x)$ has a variable.

## Explanations

### L1 human

If a language has no names at all, only a way $f$ to turn one thing into another, then it cannot name anything without a variable.
So we give it one name to start with, and then $f$ produces the rest.

### L2 human

We check that adding $c_0$ does not change the satisfiability of $\forall x \, (P(x) \to P(f(x)))$.

1. The structure $(\N, f(n) = n + 1, P = \N)$ is a model in the signature $L$.
2. Interpret $c_0$ as $0$. The sentence does not mention $c_0$, so it stays true, by the coincidence lemma.

The typical use is in clause-form theorem proving, where a constant is added when the input clauses have none.
A trap is to add the constant only to the universe and not to the signature; then $c_0$ is not a term of the language.
