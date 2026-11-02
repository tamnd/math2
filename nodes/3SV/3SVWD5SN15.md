---
tag: 3SVWD5SN15
kind: definition
name: Exponential of a bounded operator
msc: [47A60, 47D06]
defines: KX3QRA3CEP
uses: [06GZ956657, 03TM135G0N, 06EKW1AKXF, 082MGNWNA8, 020M04FN1H, CPAD5W1CGW]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_exponential
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] over $\R$ or $\C$, and let $T \colon X \to X$ be a [[continuous linear map|03TM135G0N]].
Write $T^0 = I$, the identity map of $X$.
The *exponential* of $T$ is the bounded operator
$$e^T = \exp(T) = \sum_{n=0}^{\infty} \frac{T^n}{n!},$$
where the series converges in [[operator norm|06EKW1AKXF]].

## Remarks

The series converges because $\norm{T^n / n!} \le \norm{T}^n / n!$, and the numbers $\norm{T}^n / n!$ have the finite sum $e^{\norm{T}}$; see [[absolutely convergent series in a Banach space converge|082MGNWNA8]].
This also gives $\norm{e^T} \le e^{\norm{T}}$.

Example: let $D$ be the diagonal operator $D(x_n) = (\lambda_n x_n)$ on $\ell^2$, with $(\lambda_n)$ a bounded sequence of complex numbers.
Then $D^k(x_n) = (\lambda_n^k x_n)$, so summing coordinatewise gives $e^D(x_n) = (e^{\lambda_n} x_n)$.

For $X = \C^n$, the definition gives the [[matrix exponential|020M04FN1H]].
If $ST = TS$, then $e^{S + T} = e^S e^T$; in particular $e^T$ is [[invertible|CPAD5W1CGW]] with inverse $e^{-T}$.
The identity $e^{S+T} = e^S e^T$ can fail when $S$ and $T$ do not commute, already for $2 \times 2$ matrices.
The map $t \mapsto e^{tT}$ from $\R$ to bounded operators is differentiable in operator norm, with derivative $T e^{tT}$.
