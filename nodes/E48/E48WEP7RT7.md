---
tag: E48WEP7RT7
kind: definition
name: Relay channel
msc: [94A40, 94A24, 94A05]
defines: TYQ7V5EVH1
uses: [B9C5RBFATB, J7MZ2XQP9M, A83CYGDXFG]
sources:
  - url: https://en.wikipedia.org/wiki/Relay_channel
---

## Definition

A *discrete memoryless relay channel* consists of finite sets $\mathcal X$, $\mathcal X_1$, $\mathcal Y$, $\mathcal Y_1$ and a conditional probability distribution $p(y, y_1 \mid x, x_1)$ on $\mathcal Y \times \mathcal Y_1$ for each $(x, x_1) \in \mathcal X \times \mathcal X_1$.
Here $x$ is the sender's input, $x_1$ is the relay's input, $y_1$ is the relay's output and $y$ is the receiver's output.
Over $n$ uses the channel acts independently at each time.

A code with $M$ messages and block length $n$ consists of:

1. an encoder that maps each message $w \in \set{1, \dots, M}$ to a sequence $x^n(w) \in \mathcal X^n$;
2. relay functions $f_1, \dots, f_n$, where the relay sends $x_{1i} = f_i(y_{11}, \dots, y_{1,i-1})$ at time $i$, so it uses only what it has received before time $i$;
3. a decoder that maps each $y^n \in \mathcal Y^n$ to an estimate $\hat w \in \set{1, \dots, M}$.

Let the message $W$ be uniform.
A rate $R$ is *achievable* if there are codes with $M \ge 2^{nR}$ whose error probability $P(\hat W \ne W)$ tends to $0$ as $n \to \infty$.
The *capacity* of the relay channel is the supremum of the achievable rates.

## Remarks

Example: let all four alphabets be $\set{0, 1}$, and let $Y_1 = X$ and $Y = X_1$ with probability $1$.
The relay hears the sender perfectly, and the receiver hears only the relay.
The relay strategy $x_{1i} = y_{1,i-1}$ for $i \ge 2$ satisfies clause 2, and it delivers $n - 1$ of the $n$ sent bits without error, so every rate $R < 1$ is achievable.
No rate above $1$ is achievable, because the receiver sees one bit per use; so the capacity is $1$.
The Gaussian relay channel, with $Y_1 = X + Z_1$ and $Y = X + X_1 + Z$ for independent Gaussian noises, is the analogue with real alphabets and power constraints.

Non-example: if the relay were allowed to send $x_{1i} = f_i(y_{11}, \dots, y_{1i})$, using the output of the current time, clause 2 would fail.
That model, sometimes called a relay without delay, is a different channel model.

The capacity $C$ satisfies the cut-set bound, in terms of [[mutual information|A83CYGDXFG]],
$$C \le \max_{p(x, x_1)} \min\set{I(X, X_1; Y), \; I(X; Y, Y_1 \mid X_1)}.$$
Cover and El Gamal showed that equality holds when the channel is physically degraded, that is, when $X \to (X_1, Y_1) \to Y$ is a Markov chain.
