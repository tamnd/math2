---
tag: XXYWTYDN37
kind: definition
name: Monad in functional programming
msc: [68N18, 18C15]
defines: 83FVPGE7Q5
uses: [FF6XXA6D1A, AVVQEG0MRJ]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(functional_programming)
---

## Definition

Work in a typed functional language, with a [[type system|AVVQEG0MRJ]] that has function types and type constructors.
A *monad* consists of a type constructor $M$, which sends each type $A$ to a type $M\, A$, and two polymorphic functions.
They are
$$\mathsf{return} : A \to M\, A, \qquad (\gg\!=) : M\, A \to (A \to M\, B) \to M\, B.$$
The following laws must hold for all $a : A$, $m : M\, A$, $f : A \to M\, B$ and $g : B \to M\, C$.

1. Left identity: $\mathsf{return}\ a \gg\!= f = f\, a$.
2. Right identity: $m \gg\!= \mathsf{return} = m$.
3. Associativity: $(m \gg\!= f) \gg\!= g = m \gg\!= (\lambda x.\, f\, x \gg\!= g)$.

## Remarks

Example: the option monad has $M\, A = \mathsf{Maybe}\, A$, whose values are $\mathsf{Nothing}$ and $\mathsf{Just}\ a$ for $a : A$.
Set $\mathsf{return}\ a = \mathsf{Just}\ a$, $\mathsf{Nothing} \gg\!= f = \mathsf{Nothing}$ and $\mathsf{Just}\ a \gg\!= f = f\, a$.
Law 1 is the second clause of $\gg\!=$.
Law 2 holds in both cases: $\mathsf{Nothing} \gg\!= \mathsf{return} = \mathsf{Nothing}$, and $\mathsf{Just}\ a \gg\!= \mathsf{return} = \mathsf{Just}\ a$.
For law 3, both sides are $\mathsf{Nothing}$ when $m = \mathsf{Nothing}$, and both equal $f\, a \gg\!= g$ when $m = \mathsf{Just}\ a$.

Non-example: on lists, take $\mathsf{return}\ a = [a, a]$ and let $m \gg\!= f$ concatenate the lists $f\, x$ for the entries $x$ of $m$.
Law 2 fails: $[1] \gg\!= \mathsf{return} = [1, 1] \ne [1]$.
With $\mathsf{return}\ a = [a]$ instead, the same $\gg\!=$ gives the list monad, which models nondeterminism.

Every monad gives a functor by $\mathsf{fmap}\, h\, m = m \gg\!= (\mathsf{return} \circ h)$, and a multiplication $\mathsf{join} : M\,(M\, A) \to M\, A$ by $\mathsf{join}\, n = n \gg\!= \mathrm{id}$.
With these, $\mathsf{return}$ and $\mathsf{join}$ are the unit and multiplication of a [[monad|FF6XXA6D1A]] in the sense of category theory, and the three laws become its unit and associativity laws.
Haskell writes $\gg\!=$ as `>>=` and provides the do-notation for chains of binds.
