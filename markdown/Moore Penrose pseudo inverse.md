<ndtag category="Proof" tag="Linear-Algebra" createdate="2022-12-11" editdate="2022-12-11"></ndtag>
<h3>Definition</h3>
<!--  -->
A matrix $A^g$ is pseudo inverse of $A$ if:
(i) $AA^gA=A$, (ii) $A^gAA^g=A^g$, (iii) $(AA^g)^*=AA^g$ and (iv) $(A^gA)^*=A^gA$
<h3>Properties</h3>
<h4>Existence and uniqueness</h4>
<h5>Existence</h5>
<h6>Proof</h6>
<!--  -->
Let $A=U\Sigma V^*$ be an SVD, then $A^g=V\Sigma^gU^*$ will be the pseudoinverse, where $\Sigma^g$ takes the reciprocal of $\Sigma$.
<h5>Uniqueness<h5>
<h6>Proof</h6>
<!--  -->
Suppose $A$ has two pseudoinverses $B$ and $C$, then $AB=AC$, because 
$$\begin{aligned}AB&=ACAB=(AC)^*(AB)^*=C^*(ABA)^*\\
&=C^*A^*=(AC)^*=AC\end{aligned}$$
Similarly, we have $BA=CA$, then $B=BAB=BAC=CAC=C$.
<h4>Linear equations</h4>
<h5>Theorem 1</h5> 
A solution to $Ax=b$ exists if and only if $AA^gb=b$.
<h6>Proof</h6>
The if part is easy to show.
To show the only if part, if a solution $z$ exists, then we have $Az=b$. Therefore $Az=AA^g(Az)=AA^gb$.
<h5>Theorem 2</h5>
The complete set of solutions to $Ax=b$ is give by $z=A^gb+(I-A^gA)w$ as $w$ varies all possible values.
<h6>Proof</h6>
<!-- -->
It is easy to show $z$ is a solution.If we show $(I-A^gA)w$ gives every vector in kernel space of $A$, we will have all solutions.
Suppose $k$ is a vector in the kernel space of $A$, we have $(I-A^gA)k=(k-A^gAk)=k$, so every vector in the kernel space of $A$ can be written in the form $(I-A^gA)w$.
<h4>Ordinary least squares (OLS)</h4>
<h5>Theorem 1</h5> 
$\| Ax-b\|$ is a minimum if and only if $x=A^gb+(I-A^gA)w$ for arbitrary $w\in \mathbb{R}^n$
<h6>Proof</h6>
Observe that $Ax-b=(Ax-AA^gb)-(I-AA^g)b$, then we show $(Ax-AA^gb)$ and $(I-AA^g)b$ are orthogonal:
$$\begin{aligned}
&{}(Ax-AA^gb)^T(I-AA^g)b\\
=&(AA^g(Ax-b))^T(I-AA^g)b\qquad\mbox{(i)} \\
=&(Ax-b)^TAA^g(I-AA^g)b\qquad\mbox{(iii)}\\
=&(Ax-b)^TA(A^g-A^gAA^g)b\qquad\mbox{(ii)}\\
=&0
\end{aligned}$$
Then we have 
$$\begin{aligned}\|Ax-b\|^2&=\|Ax-AA^gb\|^2+\|(I-AA^g)b\|^2\\
&\geq\|(I-AA^g)b\|^2\end{aligned}$$
and the lower bound is attained if and only if $Ax=AA^gb$, according to linear equation property's theorem 2, this occurs for 
$$x=A^g(AA^g)b+(I-A^gA)w=A^gb+(I-A^gA)w$$
<h5>Theorem 2</h5> 
$x=A^gb$ is the unique vector of smallest euclidean norm minimizing $\|Ax-b\|$.
<h6>Proof</h6>
$$\begin{aligned}
&{}(A^gb)^T(I-A^gA)w\\
=&(A^gAA^gb)^T(I-A^gA)w\qquad\mbox{(ii)} \\
=&(A^gb)^TA^gA(I-A^gA)w\qquad\mbox{(iv)}\\
=&(A^gb)^TA^g(A-A^gA)w\qquad\mbox{(i)}\\
=&0
\end{aligned}$$
Then we have $\|x\|^2\geq \|A^gb\|^2+\|(I-A^gA)w\|^2\geq \|A^gb\|^2$.
<h3>References</h3>
<!--  -->
* https://www.isical.ac.in/~arnabc/isivm2/pseudo.html
* https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
* https://doi.org/10.2307/3617665
* https://doi.org/10.2307/3617890