Matice
======

Matice je množina prvků uspořádaných do struktury řádků a sloupců, kde každý prvek má své pevně stanovené místo odvislé od jeho účelu zanesení do matice.

Maticí typu :math:`(m, n)` nazýváme schéma

.. math::
    :label: matice_schema
    :nowrap:

    \begin{math}
    \mathbf{A} =
    \left(
    \begin{array}{cccc}
    a_{11}, & a_{12}, & \ldots , & a_{1 n} \\
    a_{21}, & a_{22}, & \ldots , & a_{2 n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m 1}, & a_{m 2}, & \ldots , & a_{m n}
    \end{array}
    \right)
    \end{math}

Matice :math:`\mathbf{A}` s :math:`m` řádky a :math:`n` sloupci se při :math:`m \neq n` nazývá *obdélníková matice typu* :math:`(m, n)` a lze ji značit jako :math:`\mathbf{A}_{(m,n)}`, zatímco při :math:`m = n` se matice nazývá *čtvercová matice n-tého řádu* a lze ji značit jako :math:`\mathbf{A}_{n}`.

Řádkový a Sloupcový vektor
--------------------------

*Řádkovým vektorem matice* :math:`\mathbf{A}_{(m,n)}` nazýváme každý vektor

.. math:: \mathbf{a}_{i} = (a_{i 1}, a_{i 2}, \ldots, a_{i n}), \qquad i \in \{ 1, 2, \ldots, m \}

*Sloupcovým vektorem matice* :math:`\mathbf{A}_{(m,n)}` nazýváme každý vektor

.. math::
    :nowrap:

    \begin{math}
    \mathbf{a}_{k}^{T} = \left(
    \begin{array}{c}
    a_{1 k} \\
    a_{2 k} \\
    \vdots \\
    a_{m k}
    \end{array}
    \right)
    \qquad k \in \{ 1, 2, \ldots, n \}
    \end{math}

Sčítání a odečítání
-------------------

Násobení
--------

Matici lze násobit tzv. *skalárem*, což je číslo, nímž se vynásobí každý prvek matice zvlášť, nebo lze matici násobit vektorem, nebo lze matici násobit jinou maticí, pokud je pro matice :math:`\mathbf{A}_{(m,n)}` a :math:`\mathbf{B}_{(o,p)}` splněna podmínka :math:`n = o` a výsledkem je pak matice :math:`\mathbf{C}_{(m,p)}` pro jejíž prvky platí

.. math:: c_{i k} = \mathbf{a}_{i} \mathbf{b}_{k}^{T} = \sum_{j=1}^{n} a_{i j} b_{j k} \qquad \text{pro} \qquad \forall i \in \mathrm{\mathbf{U}}_m \land \forall k \in \mathrm{\mathbf{U}}_p