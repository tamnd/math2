---
tag: ENSESQT9XB
kind: example
name: 2023 is not a perfect square by modus tollens
msc: ["03B05", "11A07"]
topics: [PM1AYWABA7]
audience: school
instance_of: [32AQPJQQAM]
uses: [32AQPJQQAM, HCGCPW8ZFE]
sources:
  - url: https://en.wikipedia.org/wiki/Modus_tollens
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Square_number
    locator: lead section
---

## Example

When a square number is divided by $4$, the remainder is $0$ or $1$, and $2023$ leaves remainder $3$, so $2023$ is not a square.
The argument has premise 1, "for every integer $n$, if $n$ is a [[perfect square|HCGCPW8ZFE]], then $n \equiv 0$ or $n \equiv 1 \pmod 4$", premise 2, "$2023 \not\equiv 0$ and $2023 \not\equiv 1 \pmod 4$", and the conclusion "$2023$ is not a perfect square".
We check that the premises are true and that the argument is an instance of [[modus tollens|32AQPJQQAM]].

1. Let $n = m^2$ for an integer $m$.
   If $m = 2k$, then $n = 4k^2 \equiv 0 \pmod 4$.
2. If $m = 2k + 1$, then $n = 4(k^2 + k) + 1 \equiv 1 \pmod 4$.
   Every integer $m$ is even or odd, so steps 1 and 2 prove premise 1.
3. Premise 2 is true, because $2023 = 4 \cdot 505 + 3$.
4. Premise 1 with $n = 2023$ gives $\varphi \to \psi$, where $\varphi$ is "$2023$ is a perfect square" and $\psi$ is "$2023 \equiv 0$ or $1 \pmod 4$".
5. Premise 2 is $\neg \psi$, so modus tollens gives $\neg \varphi$: $2023$ is not a perfect square.

Check: $44^2 = 1936 < 2023 < 2025 = 45^2$, so $2023$ lies strictly between two consecutive squares.

## Remarks

### What the example shows

Modus tollens typically uses a property that every square has and that the number lacks.
The same argument shows that no integer of the form $4k + 2$ or $4k + 3$ is a square, for example $10$, $11$ or $2022$.
The argument gives nothing for numbers congruent to $0$ or $1$ modulo $4$: $5 \equiv 1 \pmod 4$ is not a square, and $9 \equiv 1 \pmod 4$ is a square.

### Watch out

Concluding "$5$ is a square" from "$5 \equiv 1 \pmod 4$" would be [[affirming the consequent|J7KFCFQRBT]].
Passing a necessary test proves nothing.

### Try it

Show that $2^{100} + 2$ is not a perfect square.
Modulo $3$ the test gives nothing, since every square is $0$ or $1$ modulo $3$ and $2^{100} + 2 \equiv 1 + 2 \equiv 0 \pmod 3$.
Modulo $4$ it works: $2^{100} + 2 = 4 \cdot 2^{98} + 2 \equiv 2 \pmod 4$, so modus tollens with premise 1 gives the answer.

## Explanations

### L1 human

When a square number is divided by $4$, the remainder is always $0$ or $1$.
For example, $36 = 4 \cdot 9$ leaves $0$, and $49 = 4 \cdot 12 + 1$ leaves $1$.
The number $2023$ leaves remainder $3$.
So $2023$ cannot be a square, and we know this without trying any square roots.

### L2 human

To show that a number is not a square, choose a modulus in which the number lacks the property of squares.
For $2^{100} + 2$, the modulus $3$ fails: squares are $0$ or $1$ modulo $3$, because $(3k)^2 \equiv 0$ and $(3k \pm 1)^2 = 9k^2 \pm 6k + 1 \equiv 1$.
Since $2^{100} = (2^2)^{50} \equiv 1 \pmod 3$, the number $2^{100} + 2$ is $0$ modulo $3$, and the test is passed, which proves nothing.
The modulus $4$ succeeds, because $2^{100} + 2 \equiv 2 \pmod 4$, and modus tollens finishes the proof.
