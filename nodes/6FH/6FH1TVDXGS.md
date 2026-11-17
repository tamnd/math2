---
tag: 6FH1TVDXGS
kind: example
name: Denying the antecedent is not a valid deduction
msc: ["00A35", "97E30"]
topics: [T6QQ749DM5]
audience: school
instance_of: [J7KFCFQRBT]
uses: [J7KFCFQRBT, FA6YZGR2SS, VB7B8766D2]
sources:
  - url: https://en.wikipedia.org/wiki/Denying_the_antecedent
    locator: lead section
---

## Example

Consider the argument with two premises and a conclusion:

- Premise 1: if an integer $n$ is divisible by $4$, then $n$ is even.
- Premise 2: the integer $6$ is not divisible by $4$.
- Conclusion: so $6$ is not even.

We check whether the argument is valid.

1. Premise 1 is true. If $n = 4k$ for an integer $k$, then $n = 2(2k)$, so $n$ is even.
2. Premise 2 is true, because $6 = 4 \cdot 1 + 2$ leaves the remainder $2$ on division by $4$.
3. The conclusion is false, because $6 = 2 \cdot 3$ is even.
4. A valid inference never leads from true premises to a false conclusion. So the argument is not valid.
5. The form of the argument is "if $P$ then $Q$; not $P$; so not $Q$". This form [[denies the antecedent|J7KFCFQRBT]].
6. The form needs the [[inverse|VB7B8766D2]] "if $n$ is not divisible by $4$, then $n$ is not even". The number $6$ is a counterexample to the inverse.

## Remarks

The example shows that a conditional says nothing about the cases where its hypothesis is false.
Premise 1 is a statement about multiples of $4$, and $6$ is not one of them.
With $n = 7$ in place of $6$, the same form gives the true conclusion "$7$ is not even", but only by chance: the argument is still invalid.
The valid form with the same premise 1 is [[modus tollens|QWTTHZ9C6T]]: from "$n$ is not even", conclude "$n$ is not divisible by $4$".

## Explanations

### L1 human

"If it is a dog, then it has four legs" is true.
"This is not a dog" can be true too, for a cat.
But "so it does not have four legs" is false for the cat.
The "if" sentence tells us about dogs only, and it tells us nothing about animals that are not dogs.

### L2 human

We test the inverse of a true theorem.

1. The theorem: if a real function $f$ is differentiable at $c$, then $f$ is continuous at $c$.
2. Its inverse: if $f$ is not differentiable at $c$, then $f$ is not continuous at $c$.
3. Take $f(x) = |x|$ and $c = 0$. The difference quotient $\frac{|h|}{h}$ is $1$ for $h > 0$ and $-1$ for $h < 0$, so it has no limit, and $f$ is not differentiable at $0$.
4. But $|h| \to 0$ as $h \to 0$, so $f$ is continuous at $0$.
5. So the inverse is false, and the inference "not differentiable, so not continuous" denies the antecedent.

The typical use of this check is to read a theorem as a statement about the objects that satisfy its hypothesis, and only about them.
A trap is to use a theorem to rule out a property in the case where its hypothesis fails.
