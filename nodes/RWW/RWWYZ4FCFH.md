---
tag: RWWYZ4FCFH
kind: proof
name: Proof of the polar form of a complex number
msc: [30A99]
proves: 0BRXFNQ5JV
uses: [0SQSQP748R, 0ZZRSX91QR, 0KW2X0TFBX, 04R3CY41VJ, 0WB57D9488]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_number
    locator: Polar form
---

## Proof

1. Let $z \neq 0$, let $r = |z|$ be its [[modulus|0KW2X0TFBX]] and let $\theta = \operatorname{Arg} z$.
2. By the [[principal value of the argument|0SQSQP748R]], $\theta$ is an [[argument|0ZZRSX91QR]] of $z$.
3. By the definition of an argument, $z = r (\cos \theta + i \sin \theta)$.
4. The number $\theta$ is real. For real arguments, the power series of $\cos$ and $\sin$ are the real [[sine and cosine|0WB57D9488]].
So [[Euler's formula|04R3CY41VJ]] with $z = \theta$ gives $e^{i \theta} = \cos \theta + i \sin \theta$.
5. Combining steps 3 and 4, $z = r (\cos \theta + i \sin \theta) = r e^{i \theta}$.

## Idea

The first equality is just the meaning of the word argument, once we know that the principal argument is an argument.
The second equality rewrites $\cos \theta + i \sin \theta$ with Euler's formula.
