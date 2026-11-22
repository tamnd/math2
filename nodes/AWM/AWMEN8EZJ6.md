---
tag: AWMEN8EZJ6
kind: example
name: A complex quadratic form has no definiteness type
msc: [15A63]
topics: [6TSCEW8QMK]
audience: ug1
not_instance_of:
  - target: 01RBSSGMY5
    note: z^2 takes the values 1, -1 and i, so no sign condition applies to it
uses: [01RBSSGMY5, 0HZNE5QZDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
---

## Example

Let $Q(z) = z^2$ on the complex line $\mathbb{C}$, a [[quadratic form|0HZNE5QZDJ]] over $\mathbb{C}$.
We show that none of [[the five types|01RBSSGMY5]] applies to it.

1. At $z = 1$ the value is $Q(1) = 1$, which is positive.
2. At $z = i$ the value is $Q(i) = i^2 = -1$, which is negative.
3. At $z = e^{i\pi/4}$ the value is $Q(e^{i\pi/4}) = e^{i\pi/2} = i$, which is not a real number.
4. Each type is a sign condition on all the values of $Q$, and the value $i$ has no sign. So $Q$ is neither definite, nor semidefinite, nor indefinite in the real sense.

## Remarks

Steps 1 and 2 show a general reason.
If $Q(v) = c$, then $Q(iv) = i^2 c = -c$, so every complex quadratic form that takes a nonzero value also takes its negative.
So no nonzero complex quadratic form can be definite or semidefinite, and the types are a real notion only.

On complex spaces, definiteness belongs to [[Hermitian forms|48P4A1CX85]], whose values $h(v, v)$ are real.
The simplest one is $\lvert z \rvert^2 = \bar{z} z$, which is positive definite on $\mathbb{C}$.
If we write $z = x + iy$, the real part of $z^2$ is $x^2 - y^2$, a real form on $\mathbb{R}^2$ that is indefinite, and $\lvert z \rvert^2 = x^2 + y^2$ is positive definite.

## Explanations

### L1 human

Over the complex numbers, a quadratic form can take values that are not real numbers.
A number such as $i$ is neither positive nor negative, so words such as "positive" do not apply.
For complex vectors, the quantity that measures size is $\lvert z \rvert^2$, not $z^2$.

### L2 human

Watch out when you read about "positive definite complex matrices".
Those matrices are Hermitian, and the form is $\bar{x}^{\mathsf{T}} A x$, not $x^{\mathsf{T}} A x$.
For example, the identity matrix of size $2$ gives $\lvert z_1 \rvert^2 + \lvert z_2 \rvert^2$, which is positive at every nonzero vector, while $z_1^2 + z_2^2$ is $0$ at the nonzero vector $(1, i)$.
