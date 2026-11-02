---
tag: D1TK8AHMCM
kind: definition
name: Moments and orthogonal polynomials
msc: [44A60, 42C05]
defines: GSY904FM0A
uses: [01XAHPADBA, PQ1D8FQB3E, 00KDZRW4C0, 07YQ1C78G0, A18HPFPC4D]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_polynomials
---

## Definition

Let $(m_n)_{n \ge 0}$ be a sequence of real numbers.
For $n \ge 0$ let $\Delta_n = \det (m_{i+j})_{i,j=0}^{n}$ be the [[determinant|00KDZRW4C0]] of its $(n+1) \times (n+1)$ [[Hankel matrix|PQ1D8FQB3E]], and put $\Delta_{-1} = 1$.
Assume that $\Delta_n > 0$ for all $n \ge 0$.
The *moment functional* of $(m_n)$ is the [[linear form|07YQ1C78G0]] $L$ on the real polynomials $\R[x]$ with $L(x^n) = m_n$ for all $n \ge 0$.
The *monic orthogonal polynomials* of $(m_n)$ are the polynomials $P_0 = 1$ and, for $n \ge 1$,
$$P_n(x) = \frac{1}{\Delta_{n-1}} \det \begin{pmatrix} m_0 & m_1 & \cdots & m_n \\ m_1 & m_2 & \cdots & m_{n+1} \\ \vdots & \vdots & & \vdots \\ m_{n-1} & m_n & \cdots & m_{2n-1} \\ 1 & x & \cdots & x^n \end{pmatrix}.$$
Each $P_n$ is monic of degree $n$, and $L(P_m P_n) = 0$ for $m \ne n$.

## Remarks

Orthogonality holds because, for $k < n$, applying $L$ to $x^k P_n$ replaces the last row by $(m_k, \ldots, m_{n+k})$, which equals row $k$, so the determinant vanishes.
The leading coefficient is $1$ since the cofactor of $x^n$ is $\Delta_{n-1}$.
Also $L(P_n^2) = \Delta_n / \Delta_{n-1} > 0$.
Let $(m_n)$ be the moment sequence of a positive Borel measure $\mu$ on $\R$ with infinite support and all moments finite.
Then $\Delta_n > 0$ for all $n$, and the $P_n$ are the monic [[orthogonal polynomials|A18HPFPC4D]] of $\mu$ in $L^2(\mu)$.

Example: for Lebesgue measure on $[-1, 1]$ one has $m_0 = 2$, $m_1 = 0$, $m_2 = \tfrac23$ and $\Delta_0 = 2$, $\Delta_1 = \tfrac43$.
The formula gives $P_1(x) = \tfrac12 \det \begin{pmatrix} 2 & 0 \\ 1 & x \end{pmatrix} = x$ and
$P_2(x) = \tfrac34 \left( \tfrac43 x^2 - \tfrac49 \right) = x^2 - \tfrac13$, the monic Legendre polynomials.

Non-example: the moments of the Dirac measure at $0$ are $m_0 = 1$ and $m_n = 0$ for $n \ge 1$.
Then $\Delta_1 = \det \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = 0$, so the condition $\Delta_n > 0$ fails.
Indeed $L(x^2) = 0$, and no monic polynomial of degree $1$ is orthogonal to $1$ with nonzero norm.

## Explanations

### L1 human

All the information needed to build orthogonal polynomials sits in the moments.
The determinant formula turns a list of moments directly into the polynomials, one degree at a time.
