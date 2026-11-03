---
tag: 83FVPGE7Q5
kind: concept
name: Monad in functional programming
msc: [68N18, 18C15]
uses: [FF6XXA6D1A]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(functional_programming)
same_as:
  wikidata: Q1579914
  wikipedia: Monad (functional programming)
---

## Summary

In functional programming, a monad is a type constructor $M$ with two operations, $\mathsf{return} : A \to M\, A$ and $\mathsf{bind} : M\, A \to (A \to M\, B) \to M\, B$, that satisfy three laws.
A value of type $M\, A$ is read as a computation that produces a value of type $A$, possibly with an effect.
Typical effects are failure, state, input and output, and nondeterminism.
Eugenio Moggi used [[monads|FF6XXA6D1A]] of category theory to structure the semantics of effects.
Philip Wadler brought them into programming, where they are central to Haskell.
The laws are the laws of a Kleisli triple, an equivalent form of a monad on the category of types and functions.

## Explanations

### L1 human

Many computations do more than return a value: they may fail, print something, or read a state.
A monad packages a value together with such an effect, and gives a standard way to chain these packaged steps.
$\mathsf{return}$ wraps a plain value with no effect, and $\mathsf{bind}$ runs one step and feeds its result into the next.
For the "maybe" monad, a step either gives a value or fails, and $\mathsf{bind}$ stops the whole chain at the first failure.
