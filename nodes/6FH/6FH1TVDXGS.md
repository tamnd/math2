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

Is this argument valid?
Try to decide before you read the answer.

> Every integer divisible by $4$ is even.
> The integer $6$ is not divisible by $4$.
> So $6$ is not even.

It is not valid, and the conclusion is even false.
We find the error in four steps.

1. Both premises are true. If $n = 4k$, then $n = 2(2k)$ is even, and $6 = 4 \cdot 1 + 2$ leaves remainder $2$ on division by $4$.
2. The conclusion is false, since $6 = 2 \cdot 3$.
3. A valid inference never leads from true premises to a false conclusion, so the argument is invalid.
4. Its form is "if $P$ then $Q$; not $P$; so not $Q$", which [[denies the antecedent|J7KFCFQRBT]]. It would need the [[inverse|VB7B8766D2]] "if $n$ is not divisible by $4$, then $n$ is not even", and $6$ is a counterexample to the inverse.

The correct argument with the same first premise denies the consequent instead.
From "$7$ is not even" it concludes "$7$ is not divisible by $4$", and that is [[modus tollens|QWTTHZ9C6T]], a valid form.

## Remarks

A [[conditional|FA6YZGR2SS]] says nothing about the cases where its hypothesis is false.
The first premise talks about multiples of $4$, and $6$ is not one of them, so the premise is silent about $6$.
With $7$ in place of $6$, the same invalid form reaches the true conclusion "$7$ is not even", but only by luck.
A correct conclusion does not make an argument valid; validity is about the form, and $6$ shows that the form can fail.

## Explanations

### L1 human

"If it is a dog, then it has four legs" is true.
"This is not a dog" is true for a cat.
But "so it does not have four legs" is false for the cat.
The "if" sentence tells us about dogs and nothing about animals that are not dogs.

### L2 human

We test the inverse of a true theorem.
The theorem says that if a real function $f$ is differentiable at $c$, then $f$ is continuous at $c$.
Its inverse says that if $f$ is not differentiable at $c$, then $f$ is not continuous at $c$.
Take $f(x) = |x|$ and $c = 0$.
The difference quotient $\frac{|h|}{h}$ is $1$ for $h > 0$ and $-1$ for $h < 0$, so it has no limit, and $f$ is not differentiable at $0$.
But $|h| \to 0$ as $h \to 0$, so $f$ is continuous at $0$, and the inverse is false.

The typical use of this check is to read a theorem as a statement about the objects that satisfy its hypothesis, and only about them.
Watch out for using a theorem to rule out a property in exactly the case where its hypothesis fails.
