Přímka, Polopřímka, Úsečka
==========================

Jedná se o jednorozměrný objekt v prostoru definovaný nejméně dvěma body.

Průsečník dvou přímek
---------------------

Jsou dány dvě parametrické přímky :

.. math::
	:label: primka_prusecnik_dve_parametricke_primky
	:nowrap:
	
	\begin{eqnarray*}
	\mathbf{p} & = & \mathbf{r} + \lambda \mathbf{a} \\
	\mathbf{q} & = & \mathbf{s} + \xi \mathbf{b}
	\end{eqnarray*}

jejichž společný bod zjistíme vypočítáním parametrů :math:`\lambda` a :math:`\xi` :

.. math::
	:label: primka_prusecnik_rovnice_pro_vypocet_parametru
	:nowrap:
	
	\begin{eqnarray*}
	\lambda & = & \frac{x_{\mathbf{b}} (y_{\mathbf{s}} - y_{\mathbf{r}}) + y_{\mathbf{b}} (x_{\mathbf{r}} - x_{\mathbf{s}})}{x_{\mathbf{b}} y_{\mathbf{a}} - x_{\mathbf{a}} y_{\mathbf{b}}} \\
	\xi & = & \frac{x_{\mathbf{a}} (y_{\mathbf{s}} - y_{\mathbf{r}}) + y_{\mathbf{a}} (x_{\mathbf{r}} - x_{\mathbf{s}})}{x_{\mathbf{b}} y_{\mathbf{a}} - x_{\mathbf{a}} y_{\mathbf{b}}}
	\end{eqnarray*}

kde :

.. math::
	x_{\mathbf{b}} y_{\mathbf{a}} - x_{\mathbf{a}} y_{\mathbf{b}} \neq 0

vycházíme přitom z rozepsání parametrických rovnic :eq:`primka_prusecnik_dve_parametricke_primky` pro přímky :math:`\mathbf{p}` a :math:`\mathbf{q}` pro jednotlivé souřadnice v prostoru :

.. math::
	:nowrap:
	
	\begin{eqnarray*}
	x_{\mathbf{p}} & = & x_{\mathbf{r}} + \lambda x_{\mathbf{a}} \\
	y_{\mathbf{p}} & = & y_{\mathbf{r}} + \lambda y_{\mathbf{a}} \\
	z_{\mathbf{p}} & = & z_{\mathbf{r}} + \lambda z_{\mathbf{a}} \\
	x_{\mathbf{q}} & = & x_{\mathbf{s}} + \xi x_{\mathbf{b}} \\
	y_{\mathbf{q}} & = & y_{\mathbf{s}} + \xi y_{\mathbf{b}} \\
	z_{\mathbf{q}} & = & z_{\mathbf{s}} + \xi z_{\mathbf{b}}
	\end{eqnarray*}

a jelikož hledáme průsečník, volíme předpoklad rovnosti pro společný bod :

.. math::
	x_{\mathbf{p}} = x_{\mathbf{q}} \land y_{\mathbf{p}} = y_{\mathbf{q}} \land z_{\mathbf{p}} = z_{\mathbf{q}}

a takto spojíme části rovnic pro :math:`[x,y,z]`, po čemž následuje eliminace jednoho z parametrů :math:`\lambda` nebo :math:`\xi` respektive výpočet pro parametr :math:`\xi` nebo :math:`\lambda`.
