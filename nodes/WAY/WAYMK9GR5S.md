---
tag: WAYMK9GR5S
kind: statement
role: proposition
name: Zero and self-adjoint operators detected by the quadratic form
msc: ["15A04", "47B15"]
topics: [3YM9EK6VMB]
audience: ug1
about: [0NEGN5CRSC]
uses: [0ST8QF9T3T, 0MB8HQW495, 0PTF1PTJK0]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Real-valuedness of quadratic forms
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.4
---

## Statement

On a complex space, the numbers $\ip{Tv}{v}$ determine the operator $T$, and they are all real exactly when $T$ is self-adjoint.
On a real space, they determine $T$ only among the self-adjoint operators.
Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to V$ be a linear [[operator|0PTF1PTJK0]].

1. Let $\mathbb{K} = \mathbb{C}$. If $\ip{Tv}{v} = 0$ for all $v \in V$, then $T = 0$.
2. Let $\mathbb{K} = \mathbb{C}$. Then $T$ is [[self-adjoint|0MB8HQW495]] if and only if $\ip{Tv}{v}$ is a real number for every $v \in V$.
3. Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. If $T$ is self-adjoint and $\ip{Tv}{v} = 0$ for all $v \in V$, then $T = 0$.

## Remarks

### Why each hypothesis is needed

Parts 1 and 2 need complex scalars.
On $\mathbb{R}^2$ with the dot product, [[the rotation by a right angle|VMHPYDZERM]] $R(x, y) = (-y, x)$ gives
$$\ip{R(x, y)}{(x, y)} = -yx + xy = 0$$
for every vector, but $R \ne 0$.
So part 1 fails over $\mathbb{R}$, and part 2 fails too, since every value is the real number $0$ while $R^* = -R \ne R$.

Part 3 needs the self-adjoint hypothesis over $\mathbb{R}$, by the same rotation.
Over $\mathbb{C}$ the hypothesis is not needed, because part 1 already covers every operator.

### What it gives you

The main use of part 1 is to prove an identity between operators by checking the quadratic forms.
If $\ip{Sv}{v} = \ip{Tv}{v}$ for all $v$ in a complex space, then part 1 applied to $S - T$ gives $S = T$.
Over $\mathbb{R}$ the same conclusion holds when $S$ and $T$ are both self-adjoint, by part 3.

For example, the criterion for [[normal operators|EMW3QTE3H9]] says that $T$ is normal exactly when $\norm{Tv} = \norm{T^* v}$ for all $v$.
Its proof writes $\norm{Tv}^2 - \norm{T^* v}^2 = \ip{(T^* T - T T^*) v}{v}$ and applies part 3 to the self-adjoint operator $T^* T - T T^*$.

Part 2 says that a complex matrix $A$ has $x^* A x$ real for every $x \in \mathbb{C}^n$ exactly when $A$ is [[Hermitian|0EKZCX4K3P]].
Take $A = \begin{pmatrix} 2 & 1 + i \\ 1 - i & 0 \end{pmatrix}$ and $x = (a, b)$:
$$x^* A x = 2 \abs{a}^2 + (1 + i) \overline{a} b + (1 - i) a \overline{b}.$$
The last two terms are complex conjugates of each other, so their sum is real, as part 2 predicts.

### The converse

Each part is an equivalence or has an easy converse.
The zero operator has $\ip{0v}{v} = 0$ for every $v$.
A self-adjoint operator has real values, because conjugate symmetry and $T^* = T$ give
$$\overline{\ip{Tv}{v}} = \ip{v}{Tv} = \ip{Tv}{v}.$$
This direction of part 2 holds over $\mathbb{R}$ as well, where it says nothing new.

### Generalizations

The three parts hold for bounded operators on a complex or real Hilbert space, with the same proof.
Part 1 is a case of polarization: a sesquilinear form on a complex space is determined by its values on the diagonal.
A real bilinear form is determined by its diagonal only when it is symmetric, and that is why part 3 needs self-adjointness.

## Explanations

### L1 human

The number $\ip{Tv}{v}$ measures how much $T$ moves $v$ along its own direction.
Over the complex numbers, these numbers for all $v$ determine $T$ completely.
Over the real numbers they do not.
A quarter turn of the plane moves each arrow to a perpendicular arrow, so all these numbers are $0$, but the quarter turn is not the zero map.

### L2 human

Here is a typical use: decide whether $A = \begin{pmatrix} 1 & i \\ 0 & 1 \end{pmatrix}$ is Hermitian by its quadratic form.
For $x = (a, b)$ in $\mathbb{C}^2$,
$$x^* A x = \abs{a}^2 + i \overline{a} b + \abs{b}^2.$$
At $x = (1, 1)$ the value is $2 + i$, which is not real, so part 2 says that $A$ is not Hermitian.
Check: $A^* = \begin{pmatrix} 1 & 0 \\ -i & 1 \end{pmatrix} \ne A$.
One test vector with a non-real value settles the question, while a proof of self-adjointness by this route needs all vectors.
Watch out: over $\mathbb{R}$ a real matrix always gives real values, so the test says nothing there.

### L3 human

The statement is a form of polarization.
A real bilinear form splits into a symmetric part and an alternating part, and the quadratic form sees only the symmetric part.
A complex sesquilinear form loses nothing, because the values on $u \pm w$ and $u \pm iw$ recover it.
The numerical range $\{\ip{Tv}{v} : \norm{v} = 1\}$ refines part 2: on a complex space it lies in $\mathbb{R}$ exactly when $T$ is self-adjoint.
In quantum mechanics, $\ip{Tv}{v}$ is the expected value of an observable in the state $v$, and part 2 says that the real expected values belong to the self-adjoint operators.
