Unicode vs. TeX symboly
=======================

.. role:: boldit
    :class: boldit

Matematický zápis proměnných (matematické alfanumerické symboly)
----------------------------------------------------------------

Tučná
^^^^^

Poznámka k Python vs. Unicode [#unicode10000support]_.

============== ============== ==================
Znak           Unicode (U+)   TeX
============== ============== ==================
**A**          1D400          :math:`\mathbf{A}`
:math:`\vdots` :math:`\vdots` :math:`\vdots`
**Z**          1D419          :math:`\mathbf{Z}`
:math:`\ldots` :math:`\ldots` :math:`\ldots`
**a**          1D41A          :math:`\mathbf{a}`
:math:`\vdots` :math:`\vdots` :math:`\vdots`
**z**          1D433          :math:`\mathbf{z}`
============== ============== ==================

Lomená
^^^^^^

Poznámka k Python vs. Unicode [#unicode10000support]_.

============== ============== ==============
Znak           Unicode (U+)   TeX
============== ============== ==============
*A*            1D434          :math:`A`
:math:`\vdots` :math:`\vdots` :math:`\vdots`
*Z*            1D44D          :math:`Z`
:math:`\ldots` :math:`\ldots` :math:`\ldots`
*a*            1D44E          :math:`a`
:math:`\vdots` :math:`\vdots` :math:`\vdots`
*g*            1D454          :math:`g`
[#planckh]_    [#planckh]_    [#planckh]_
*i*            1D456          :math:`i`
:math:`\vdots` :math:`\vdots` :math:`\vdots`
*z*            1D467          :math:`z`
============== ============== ==============

Tučná lomená
^^^^^^^^^^^^

Poznámka k Python vs. Unicode [#unicode10000support]_.

============== ============== ======================
Znak           Unicode (U+)   TeX
============== ============== ======================
:boldit:`A`    1D468          :math:`\boldsymbol{A}`
:math:`\vdots` :math:`\vdots` :math:`\vdots`
:boldit:`Z`    1D481          :math:`\boldsymbol{Z}`
:math:`\ldots` :math:`\ldots` :math:`\ldots`
:boldit:`a`    1D482          :math:`\boldsymbol{a}`
:math:`\vdots` :math:`\vdots` :math:`\vdots`
:boldit:`z`    1D49B          :math:`\boldsymbol{z}`
============== ============== ======================

.. rubric:: Poznámky pod čarou

.. [#unicode10000support] V systému jazyka Python nejsou znaky vyšší rovny hexadecimální hodnotě ``0x10000`` podporovány a proto pro jejich reprezentaci a zobrazení v odpovídající formě je třeba ustanovit nový soubor s písmem a hodnotami nastavenými tak, aby odpovídaly unikódovému číslu daného znaku, avšak bez prefixu ``1`` (tedy např. pro U+1D44E -> U+D44E, kde se vyskytují *Hangul Syllables* (*Hangulské Slabiky*)).

.. [#planckh] Rezervováno pro Planck(ovu) konstantu :math:`h`. Tato není v symbolech Unicode umístěna v matematických alfanumerických znacích, ale v tabulce *Letterlike Symbols* (*Písmenům podobné symboly*). (U+210E)